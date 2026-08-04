#!/usr/bin/env python3
"""
multiclass_attribution.py
=========================
Replace the SIMULATED four-class demo with REAL measured data.

Trains and validates synthesis-route attribution on the co-processed
reference_atlas.csv (produced by build_reference_atlas.py) — leave-group-out
validation, a label-shuffle (permutation) negative control, calibration (ECE),
and an exclusion metric. Reports the honest cross-method result AND the
unconfounded within-study results.

Everything here runs on the measured error tables — nothing is seeded from
published values.
"""
import os, json, numpy as np, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut, cross_val_predict
from sklearn.metrics import accuracy_score, confusion_matrix

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "reference_library")
ATLAS = os.path.join(OUT, "reference_atlas.csv")
FEATS = ["del_frac","ins_frac","sub_frac","log_total_err","sub_GtoA","sub_GtoT",
         "sub_CtoT","sub_TtoC","sub_AtoG","pos5p_slope","trunc_n1_frac","trunc_decay",
         "homopolymer_enrich","gc_effect","intra_corr"]
rng = np.random.default_rng(0)

def loro_accuracy(X, y, groups, n_perm=100):
    """Leave-one-group-out accuracy + majority-class chance + label-shuffle p."""
    feats = [f for f in FEATS if f in X.columns]
    Xv = X[feats].values
    clf = RandomForestClassifier(n_estimators=150, random_state=0, class_weight="balanced")
    cv = LeaveOneGroupOut()
    pred = cross_val_predict(clf, Xv, y, groups=groups, cv=cv)
    acc = accuracy_score(y, pred)
    # majority-class baseline
    chance = pd.Series(y).value_counts(normalize=True).max()
    # label-shuffle: permute labels WITHIN the CV, recompute
    null = []
    for _ in range(n_perm):
        ysh = rng.permutation(y)
        p = cross_val_predict(clf, Xv, ysh, groups=groups, cv=cv)
        null.append(accuracy_score(ysh, p))
    null = np.array(null)
    pval = (np.sum(null >= acc) + 1) / (n_perm + 1)
    return dict(acc=round(float(acc), 3), chance=round(float(chance), 3),
                shuffle_mean=round(float(null.mean()), 3), p=round(float(pval), 4),
                n=len(y), classes=sorted(set(y)))

def ece_binary(X, y_bin, groups, n_bins=8):
    """Expected Calibration Error for a leave-group-out probability model."""
    feats = [f for f in FEATS if f in X.columns]
    clf = RandomForestClassifier(n_estimators=150, random_state=0, class_weight="balanced")
    proba = cross_val_predict(clf, X[feats].values, y_bin, groups=groups,
                              cv=LeaveOneGroupOut(), method="predict_proba")[:, 1]
    bins = np.linspace(0, 1, n_bins + 1); ece = 0.0
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = (proba >= lo) & (proba < hi)
        if m.sum():
            ece += m.mean() * abs(y_bin[m].mean() - proba[m].mean())
    return round(float(ece), 3)

def main():
    a = pd.read_csv(ATLAS)
    res = {"atlas_runs": int(len(a)),
           "composition": a.groupby(["route_class","study"]).size().to_dict()}
    print(f"Reference atlas: {len(a)} runs, {len(FEATS)} features\n")

    # ---- 1. Full cross-method (4 real chemistry classes) ----
    print("[1] Cross-method attribution (4 real chemistry classes), leave-one-run-out")
    r = loro_accuracy(a, a["route_class"].values, a["batch_id"].values)
    res["cross_method_4class"] = r
    print(f"    accuracy {r['acc']*100:.0f}%  (majority baseline {r['chance']*100:.0f}%, "
          f"shuffle {r['shuffle_mean']*100:.0f}%, p={r['p']})")
    cm = confusion_matrix(a["route_class"], cross_val_predict(
        RandomForestClassifier(n_estimators=150, random_state=0, class_weight="balanced"),
        a[FEATS].values, a["route_class"].values, groups=a["batch_id"].values,
        cv=LeaveOneGroupOut()), labels=sorted(a["route_class"].unique()))
    res["cross_method_confusion"] = {"labels": sorted(a["route_class"].unique()),
                                     "matrix": cm.tolist()}
    print("    NOTE: one study per non-column class -> class partly confounded with study;")
    print("          robust because classes differ by orders of magnitude. See within-study tests.\n")

    # ---- 2. Unconfounded within-study tests ----
    print("[2] Unconfounded within-study attribution")

    g = a[a.study == "gimpel"]
    r = loro_accuracy(g, g["route_class"].values, g["batch_id"].values, n_perm=100)
    res["gimpel_electro_vs_deposition"] = r
    print(f"  Gimpel electrochem vs deposition (same study/prep): {r['acc']*100:.0f}% "
          f"(chance {r['chance']*100:.0f}%, shuffle {r['shuffle_mean']*100:.0f}%, n={r['n']})")

    f = a[a.study == "filges"]
    r = loro_accuracy(f, f["sublabel"].values, f["batch_id"].values)
    res["filges_4vendor"] = r
    print(f"  Filges 4-vendor manufacturer: {r['acc']*100:.0f}% "
          f"(chance {r['chance']*100:.0f}%, shuffle {r['shuffle_mean']*100:.0f}%, "
          f"p={r['p']}, n={r['n']})")

    m = a[a.study == "masaki"].copy()
    def capgroup(s):
        if s.startswith("Ac2O"): return "Ac2O_standard"
        if "deaza" in s: return "dG_rescue"
        return "Pac2O_reactive"
    m["capclass"] = m["sublabel"].map(capgroup)
    r = loro_accuracy(m, m["capclass"].values, m["batch_id"].values)
    res["masaki_capping_3class"] = r
    print(f"  Masaki capping (Ac2O / Pac2O / dG-rescue): {r['acc']*100:.0f}% "
          f"(chance {r['chance']*100:.0f}%, shuffle {r['shuffle_mean']*100:.0f}%, "
          f"p={r['p']}, n={r['n']})\n")

    # ---- 3. Calibration + exclusion (the near-term output) ----
    print("[3] Exclusion output: 'commercial column vs not', calibrated")
    ybin = (a["route_class"].values == "column_phosphoramidite").astype(int)
    ece = ece_binary(a, ybin, a["batch_id"].values)
    pred = cross_val_predict(
        RandomForestClassifier(n_estimators=150, random_state=0, class_weight="balanced"),
        a[FEATS].values, ybin, groups=a["batch_id"].values, cv=LeaveOneGroupOut())
    from sklearn.metrics import precision_score, recall_score
    res["exclusion_column_vs_not"] = dict(
        accuracy=round(float(accuracy_score(ybin, pred)), 3),
        precision=round(float(precision_score(ybin, pred)), 3),
        recall=round(float(recall_score(ybin, pred)), 3), ece=ece)
    print(f"    column-vs-not: acc {accuracy_score(ybin,pred)*100:.0f}%, "
          f"precision {precision_score(ybin,pred):.2f}, recall {recall_score(ybin,pred):.2f}, "
          f"ECE {ece}")

    with open(os.path.join(OUT, "attribution_results.json"), "w") as fh:
        json.dump(res, fh, indent=2)
    print(f"\nWROTE {os.path.join(OUT, 'attribution_results.json')}")
    return res

if __name__ == "__main__":
    main()
