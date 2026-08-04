#!/usr/bin/env python3
"""
build_masaki_dataset.py — glue between the Masaki acquisition arm and the PoC.

Reads   masaki_out/errors_DRR*.csv   (per-run events from ../call_errors.py)
        masaki_out/masaki_aggregates.tsv   (batch_id, aligned_bases, n_molecules)
        ../../../data/masaki_runs_meta.tsv (per-run condition map)
Produces the exact  X, y, groups  that run_poc.py's classifier consumes, via
../extract_features.build_real_dataset  — no change to the base PoC.

Two label modes:
  --label capping   (default) : within-Masaki task. Restricts to the capping-
        experiment background (activator=BTT, oxidizer=I2, deblock=TCA) so the
        ONLY varying axis is the capping chemistry, then asks whether the 16-D
        error-profile vector recovers it. Classes:
        Ac2O / Ac2O_lut / Pac2O / da7G / a8da7G. This is the measured version of
        "capping omission leaves a G->A fingerprint".
  --label method    : labels every run 'column_phosphoramidite' (one class) —
        degenerate alone; use it only when concatenating with the Lietard/Gimpel
        arms for the cross-chemistry (class-level) classifier.

  --classify : also run the SAME RandomForest + GroupKFold (leave-run-out) block
        as run_poc.py, print accuracy vs chance, a confusion table, and the
        label-shuffle control (must collapse to chance = no leakage).

Split is by RUN (groups=batch_id), never by read — matching the RUNBOOK rule.
Run from: src/poc/acquisition/
"""
import os, sys, glob, argparse
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))          # to import extract_features
from extract_features import build_real_dataset, FEATURE_NAMES

OUT  = os.path.join(HERE, "masaki_out")
DATA = os.path.join(HERE, "..", "..", "..", "data")

def load_events():
    files = sorted(glob.glob(os.path.join(OUT, "errors_DRR*.csv")))
    if not files:
        sys.exit(f"No events found in {OUT}. Run masaki_acquire.sh first.")
    ev = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
    need = {"batch_id","molecule_id","position","oligo_len","error_type","ref_base","alt_base"}
    miss = need - set(ev.columns)
    if miss: sys.exit(f"events missing columns {miss}; got {list(ev.columns)}")
    print(f"[events] {len(files)} runs, {len(ev):,} error rows")
    return ev

def load_meta_agg():
    meta = pd.read_csv(os.path.join(DATA, "masaki_runs_meta.tsv"), sep="\t")
    agg  = pd.read_csv(os.path.join(OUT, "masaki_aggregates.tsv"), sep="\t",
                       names=["batch_id","aligned_bases","n_molecules"])
    return meta, agg

def capping_label(row):
    if row["noncanonical"] == "7-deaza-dG":        return "da7G"
    if row["noncanonical"] == "8-aza-7-deaza-dG":  return "a8da7G"
    if row["capping"] == "Ac2O_standard":          return "Ac2O"
    if row["capping"] == "Ac2O_lutidine":          return "Ac2O_lut"
    if row["capping"] == "Pac2O":                  return "Pac2O"
    return "other"

def capping_label3(row):
    """Group by capping MECHANISM family (the chemically meaningful split)."""
    if row["noncanonical"] in ("7-deaza-dG", "8-aza-7-deaza-dG"): return "dG_analog"
    if row["capping"] in ("Ac2O_standard", "Ac2O_lutidine"):     return "Ac2O"
    if row["capping"] == "Pac2O":                                return "Pac2O"
    return "other"

def capping_labelbin(row):
    """Binary: standard capping vs reactive-capping family (incl. dG-laundered)."""
    lab = capping_label3(row)
    if lab == "other": return "other"
    return "Ac2O_standard_cap" if lab == "Ac2O" else "reactive_cap"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", choices=["capping","capping3","capping_bin","method"], default="capping")
    ap.add_argument("--classify", action="store_true")
    ap.add_argument("-o", "--out", default=os.path.join(OUT, "masaki_dataset.npz"))
    a = ap.parse_args()

    events = load_events()
    meta, agg = load_meta_agg()

    if a.label in ("capping", "capping3", "capping_bin"):
        bg = ((meta.activator=="BTT") & (meta.oxidizer=="I2") & (meta.deblock=="TCA"))
        meta = meta[bg].copy()
        fn = {"capping": capping_label, "capping3": capping_label3,
              "capping_bin": capping_labelbin}[a.label]
        meta["label"] = meta.apply(fn, axis=1)
        meta = meta[meta.label != "other"]
        print(f"[label={a.label}] restricted to BTT/I2/TCA background: {len(meta)} runs")
    else:
        meta = meta.copy(); meta["label"] = meta["method_class"]

    keep = set(meta.batch_id)
    events = events[events.batch_id.isin(keep)]
    aligned_bases = dict(zip(agg.batch_id, agg.aligned_bases))
    n_molecules   = dict(zip(agg.batch_id, agg.n_molecules))
    batch_method  = dict(zip(meta.batch_id, meta.label))

    X, y, groups = build_real_dataset(events, aligned_bases, n_molecules, batch_method)
    if len(X) == 0:
        sys.exit("No batches built — check that errors_*.csv cover the selected runs.")
    print(f"[dataset] X={X.shape}  classes={dict(zip(*np.unique(y, return_counts=True)))}")
    np.savez(a.out, X=X, y=y, groups=groups, feature_names=np.array(FEATURE_NAMES))
    print(f"[saved] {a.out}  (X, y, groups, feature_names)")

    if a.classify:
        classify(X, y, groups)

def classify(X, y, groups):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import GroupKFold, cross_val_predict
    n_groups  = len(np.unique(groups))
    n_classes = len(np.unique(y))
    n_splits  = min(5, n_groups)
    if n_groups < 2 or n_classes < 2:
        print(f"[classify] need >=2 groups and >=2 classes (have {n_groups} groups, "
              f"{n_classes} classes). Run the full 34 first."); return
    clf = RandomForestClassifier(n_estimators=400, min_samples_leaf=2, random_state=0)
    pred = cross_val_predict(clf, X, y, groups=groups, cv=GroupKFold(n_splits=n_splits))
    acc  = (pred == y).mean()
    print(f"\n=== leave-run-out classification ({n_classes} classes, {n_groups} runs) ===")
    print(f"  accuracy = {acc:.3f}   (chance = {1/n_classes:.3f})")
    labels = sorted(np.unique(y))
    cm = pd.DataFrame(0, index=labels, columns=labels)
    for t, p in zip(y, pred): cm.loc[t, p] += 1
    print("  confusion (rows=true, cols=pred):"); print(cm.to_string())
    # label-shuffle control: must fall to ~chance
    rng = np.random.default_rng(0)
    ys  = rng.permutation(y)
    ps  = cross_val_predict(clf, X, ys, groups=groups, cv=GroupKFold(n_splits=n_splits))
    print(f"  label-shuffle control accuracy = {(ps==ys).mean():.3f}  "
          f"(must be ~chance {1/n_classes:.3f}; higher => leakage)")

if __name__ == "__main__":
    main()
