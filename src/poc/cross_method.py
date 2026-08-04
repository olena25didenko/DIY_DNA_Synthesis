"""
cross_method.py
===============
Compare synthesis-method error phenotypes across studies (e.g. Filges column
vs Lietard photolithographic) from the per-batch error-events CSVs produced by
call_errors.py.

DESIGN PRINCIPLE (read this): with only one study per method, "method" is
perfectly confounded with "study/platform". A classification accuracy here does
NOT prove chemistry discrimination -- it could be learning the platform. So this
script LEADS with the honest, defensible output -- the descriptive phenotype
contrast (does column show G->A while photolithographic shows G->T? does the
error-class balance differ?) -- and reports any classifier accuracy only with a
loud confound warning. This matches Chapter 4's "profiles differ in kind, not a
benchmark accuracy" framing.

INPUTS (in --dir): errors_<batch>.csv (+ errors_<batch>.agg.csv) from call_errors.py.
Method/study per batch come from a --manifest CSV (batch_id,method,study) or,
by default, are inferred from the id prefix: SRR*->column_phosphoramidite/filges,
ERR*->photolithographic/lietard (override with the manifest).

USAGE:
    python cross_method.py --dir .            # infer from prefixes
    python cross_method.py --dir . --manifest manifest.csv
"""
import argparse, glob, os, sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_features import build_real_dataset  # noqa

try:
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except Exception:
    HAVE_MPL = False


def infer(batch_id):
    if batch_id.startswith("SRR"):
        return "column_phosphoramidite", "filges"
    if batch_id.startswith("ERR"):
        return "photolithographic", "lietard"
    return "unknown", "unknown"


def load(dir_, manifest):
    ev_files = sorted(glob.glob(os.path.join(dir_, "errors_*.csv")))
    ev_files = [f for f in ev_files if not f.endswith(".agg.csv")]
    if not ev_files:
        sys.exit(f"No errors_*.csv found in {dir_}. Run call_errors.py first.")
    events = pd.concat([pd.read_csv(f) for f in ev_files], ignore_index=True)

    aligned_bases, n_molecules = {}, {}
    for f in glob.glob(os.path.join(dir_, "errors_*.agg.csv")):
        a = pd.read_csv(f)
        for r in a.itertuples():
            aligned_bases[r.batch_id] = int(r.aligned_bases)
            n_molecules[r.batch_id] = int(r.n_molecules)

    method_map, study_map = {}, {}
    if manifest:
        m = pd.read_csv(manifest)
        for r in m.itertuples():
            method_map[r.batch_id] = r.method
            study_map[r.batch_id] = getattr(r, "study", "NA")
    for b in events.batch_id.unique():
        if b not in method_map:
            method_map[b], study_map[b] = infer(b)
        # fall back for missing denominators (approximate)
        n_molecules.setdefault(b, events[events.batch_id == b].molecule_id.nunique())
        aligned_bases.setdefault(b, max(n_molecules[b] * 60, 1))  # rough; prefer the sidecar
    return events, aligned_bases, n_molecules, method_map, study_map


def descriptive_contrast(events, method_map):
    """The honest headline: per-method error-class balance + substitution direction."""
    events = events.copy()
    events["method"] = events.batch_id.map(method_map)
    rows = []
    for method, g in events.groupby("method"):
        n = len(g)
        d = (g.error_type == "del").sum()
        i = (g.error_type == "ins").sum()
        s = (g.error_type == "sub").sum()
        subs = g[g.error_type == "sub"]
        def chan(rb, ab):
            return ((subs.ref_base == rb) & (subs.alt_base == ab)).sum() / max(len(subs), 1)
        rows.append(dict(method=method, n_events=n,
                         del_frac=d/n, ins_frac=i/n, sub_frac=s/n,
                         GtoA=chan("G", "A"), GtoT=chan("G", "T"),
                         dominant_sub=("G->A" if chan("G","A") >= chan("G","T") else "G->T")))
    return pd.DataFrame(rows).set_index("method")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".")
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--fig", default="cross_method_result.png")
    a = ap.parse_args()

    events, aligned_bases, n_molecules, method_map, study_map = load(a.dir, a.manifest)
    methods = sorted(set(method_map[b] for b in events.batch_id.unique()))
    studies = sorted(set(study_map[b] for b in events.batch_id.unique()))
    print(f"Loaded {events.batch_id.nunique()} batches | methods={methods} | studies={studies}\n")

    # ---- 1. DESCRIPTIVE CONTRAST (the defensible result) --------------------
    print("=" * 64)
    print("1. PHENOTYPE CONTRAST  (this is the honest, defensible result)")
    print("=" * 64)
    contrast = descriptive_contrast(events, method_map)
    with pd.option_context("display.float_format", lambda v: f"{v:.4f}"):
        print(contrast.to_string())
    print()
    if {"column_phosphoramidite", "photolithographic"} <= set(contrast.index):
        c = contrast.loc["column_phosphoramidite"]; p = contrast.loc["photolithographic"]
        print(f"  column   dominant substitution: {c['dominant_sub']}  (G->A={c['GtoA']:.3f}, G->T={c['GtoT']:.3f})")
        print(f"  photolith dominant substitution: {p['dominant_sub']}  (G->A={p['GtoA']:.3f}, G->T={p['GtoT']:.3f})")
        flip = c["dominant_sub"] != p["dominant_sub"]
        print(f"  => substitution direction {'FLIPS between methods (core signal present)' if flip else 'does NOT flip (signal weak here)'}")
    print()

    # ---- 2. CLASSIFIER (caveated) ------------------------------------------
    print("=" * 64)
    print("2. CLASSIFIER  (read the confound warning below)")
    print("=" * 64)
    X, y, groups_batch = build_real_dataset(events, aligned_bases, n_molecules, method_map)
    study_per_row = np.array([study_map[b] for b in groups_batch])
    method_per_study = {s: set(y[study_per_row == s]) for s in set(study_per_row)}
    confounded = all(len(v) == 1 for v in method_per_study.values()) and len(set(y)) > 1

    if confounded:
        print("  *** CONFOUND WARNING: each method comes from a single study. ***")
        print("  *** 'method' == 'study/platform' here, so any accuracy below   ***")
        print("  *** may reflect PLATFORM, not chemistry. Do NOT report it as a ***")
        print("  *** method-discrimination benchmark. The contrast in (1) is the ***")
        print("  *** real finding.                                              ***\n")

    if len(set(y)) > 1 and len(X) >= 4:
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import LeaveOneGroupOut, cross_val_predict
        # group by study when possible, else by batch, so runs aren't split
        groups = study_per_row if len(set(study_per_row)) > 1 else np.arange(len(y))
        try:
            pred = cross_val_predict(
                RandomForestClassifier(n_estimators=300, min_samples_leaf=1, random_state=0),
                X, y, groups=groups, cv=LeaveOneGroupOut(), method="predict")
            acc = (pred == y).mean()
            tag = "  (CONFOUNDED - illustrative only)" if confounded else ""
            print(f"  leave-group-out accuracy: {acc*100:.0f}%{tag}")
        except Exception as e:
            print(f"  (CV skipped: {e})")
        # label-shuffle control
        rng = np.random.default_rng(0)
        ys = rng.permutation(y)
        from sklearn.ensemble import RandomForestClassifier as RF
        from sklearn.model_selection import cross_val_score, KFold
        acc_s = cross_val_score(RF(n_estimators=200, random_state=0), X, ys,
                                cv=KFold(3, shuffle=True, random_state=0)).mean()
        print(f"  label-shuffle control: {acc_s*100:.0f}%  (should be ~chance {100/len(set(y)):.0f}%)")
    else:
        print("  Not enough distinct methods/batches for a classifier yet.")

    # ---- 3. figure ----------------------------------------------------------
    if HAVE_MPL and len(contrast):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        contrast[["del_frac", "ins_frac", "sub_frac"]].plot.bar(ax=ax1, rot=20)
        ax1.set_title("Error-class balance by method"); ax1.set_ylabel("fraction of events")
        contrast[["GtoA", "GtoT"]].plot.bar(ax=ax2, rot=20, color=["#2b6cb0", "#dd6b20"])
        ax2.set_title("Substitution direction (G->A vs G->T)"); ax2.set_ylabel("fraction of substitutions")
        fig.tight_layout(); fig.savefig(a.fig, dpi=150)
        print(f"\nFigure written: {a.fig}")

    print("\nHONEST SUMMARY: lead with the phenotype contrast (part 1). Report the")
    print("classifier only with the confound caveat until you have >1 study per method.")


if __name__ == "__main__":
    main()
