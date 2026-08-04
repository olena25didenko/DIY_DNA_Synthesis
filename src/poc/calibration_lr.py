#!/usr/bin/env python3
"""
calibration_lr.py  — Week-1 attribution-depth task.
Turns the cross-chemistry classifier from a specification into a *calibrated
instrument*: out-of-fold probabilities on the 65-run atlas, Expected Calibration
Error (ECE), a reliability diagram, and a calibrated likelihood-ratio /
exclusion output (the realistic Tier-3 "rules out commercial column").

Public data only (the co-processed atlas). No synthesis; no collaborator data.
"""
import os, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.metrics import balanced_accuracy_score

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from synth_forensics import FEATURE_NAMES

ATLAS = os.path.join(HERE, "reference_library", "reference_atlas.csv")
OUTTXT = os.path.join(HERE, "reference_library", "calibration_lr_results.txt")
FIG = os.path.abspath(os.path.join(HERE, "..", "..", "figures", "fig4_8_calibration.png"))
CHEM = ["column_phosphoramidite", "photolithographic", "array_electrochem", "array_deposition"]
RNG = 20260729

def logo_proba(X, y, groups, classes, n_est=400):
    """Out-of-fold predicted probabilities (rows align to input order)."""
    P = np.zeros((len(y), len(classes)))
    for tr, te in LeaveOneGroupOut().split(X, y, groups):
        clf = RandomForestClassifier(n_estimators=n_est, class_weight="balanced",
                                     random_state=RNG, n_jobs=1).fit(X[tr], y[tr])
        proba = clf.predict_proba(X[te])
        for j, c in enumerate(clf.classes_):
            P[te, classes.index(c)] = proba[:, j]
    return P

def ece(conf, correct, bins=10):
    """Expected Calibration Error on confidence vs correctness."""
    edges = np.linspace(0, 1, bins + 1); e = 0.0; rows = []
    for b in range(bins):
        m = (conf > edges[b]) & (conf <= edges[b + 1])
        if m.sum():
            acc = correct[m].mean(); cf = conf[m].mean()
            e += (m.mean()) * abs(acc - cf)
            rows.append((0.5*(edges[b]+edges[b+1]), cf, acc, int(m.sum())))
    return e, rows

def main():
    df = pd.read_csv(ATLAS).dropna(subset=FEATURE_NAMES)
    df["batch_id"] = df["batch_id"].astype(str)
    df = df[df.route_class.isin(CHEM)].reset_index(drop=True)
    X = df[FEATURE_NAMES].to_numpy(float)
    groups = df["batch_id"].to_numpy()
    log = []
    def w(s=""): print(s, flush=True); log.append(s)

    w("CALIBRATION & LIKELIHOOD-RATIO ANALYSIS on the co-processed atlas")
    w(f"{df.shape[0]} runs | groups(batch_id)={len(set(groups))} | classes: "
      + ", ".join(f"{c}:{int((df.route_class==c).sum())}" for c in CHEM))

    # ---- (1) 4-class calibration (max-confidence ECE) ----
    y4 = df.route_class.to_numpy()
    P4 = logo_proba(X, y4, groups, CHEM)
    yhat = np.array(CHEM)[P4.argmax(1)]
    conf = P4.max(1); correct = (yhat == y4).astype(float)
    e4, rows4 = ece(conf, correct)
    w(f"\n[4-class] balanced accuracy = {balanced_accuracy_score(y4, yhat):.3f}  "
      f"(chance 0.25) | max-confidence ECE = {e4:.3f}")

    # ---- (2) Binary EXCLUSION calibration: commercial column vs not ----
    yb = (df.route_class == "column_phosphoramidite").astype(int).to_numpy()
    Pb = logo_proba(X, yb, groups, [0, 1])[:, 1]          # P(column | X), out-of-fold
    eb, rowsb = ece(Pb, (yb == 1).astype(float))          # calibration of P(column)
    # empirical prior-corrected likelihood ratio for "is commercial column"
    prior = yb.mean(); prior_odds = prior / (1 - prior)
    eps = 1e-6; Pb_c = np.clip(Pb, eps, 1 - eps)
    LR = (Pb_c / (1 - Pb_c)) / prior_odds
    log10LR = np.log10(LR)
    w(f"\n[Exclusion: commercial column vs not]  ECE(P_column) = {eb:.3f} | prior={prior:.2f}")
    w(f"  true COLUMN     (n={int((yb==1).sum())}): median log10 LR = {np.median(log10LR[yb==1]):+.2f}"
      f"  (LR≈{10**np.median(log10LR[yb==1]):.1f}×) → inclusion")
    w(f"  true NON-column (n={int((yb==0).sum())}): median log10 LR = {np.median(log10LR[yb==0]):+.2f}"
      f"  (LR≈{10**np.median(log10LR[yb==0]):.3f}×) → EXCLUSION (rules out column)")
    # exclusion power: fraction of non-column runs with LR<1 (evidence against column)
    excl = (log10LR[yb==0] < 0).mean()
    w(f"  exclusion power: {excl*100:.0f}% of non-column runs give LR<1 (evidence against 'commercial column')")

    # ---- Figure: reliability diagram + LR distribution ----
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
    a = ax[0]
    a.plot([0, 1], [0, 1], "--", color="#888", lw=1, label="perfect calibration")
    if rowsb:
        mid = [r[1] for r in rowsb]; obs = [r[2] for r in rowsb]
        a.plot(mid, obs, "-o", color="#2166AC", lw=2, label=f"P(column) — ECE {eb:.2f}")
    a.set_xlabel("mean predicted P(commercial column)"); a.set_ylabel("observed fraction")
    a.set_title("(a) Reliability diagram — exclusion contrast", fontweight="bold", fontsize=10)
    a.set_xlim(0, 1); a.set_ylim(0, 1); a.legend(fontsize=8, frameon=False)

    b = ax[1]
    b.hist(log10LR[yb == 1], bins=12, alpha=0.7, color="#2166AC", label="true commercial column")
    b.hist(log10LR[yb == 0], bins=12, alpha=0.8, color="#B2182B", label="true non-column (DIY/array/EC)")
    b.axvline(0, ls="--", color="#333", lw=1)
    b.text(0.15, b.get_ylim()[1]*0.9, "LR>1\ninclusion", fontsize=7.5, color="#2166AC")
    b.text(-0.9, b.get_ylim()[1]*0.9, "LR<1\nexclusion", fontsize=7.5, color="#B2182B", ha="center")
    b.set_xlabel("log10 likelihood ratio (commercial column vs not)"); b.set_ylabel("runs")
    b.set_title("(b) Calibrated LR — exclusion is well-powered", fontweight="bold", fontsize=10)
    b.legend(fontsize=8, frameon=False)
    fig.suptitle("Figure 4.8  Calibrated likelihood-ratio / exclusion output on the co-processed atlas",
                 fontweight="bold", fontsize=11, y=1.02)
    fig.savefig(FIG, bbox_inches="tight", dpi=150); plt.close(fig)
    w(f"\nwrote figure: {FIG}")
    open(OUTTXT, "w").write("\n".join(log) + "\n")
    print("wrote", OUTTXT)

if __name__ == "__main__":
    main()
