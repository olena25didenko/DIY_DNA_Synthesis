"""
run_poc.py  --  end-to-end proof-of-concept for synthesis-method attribution.

Runs the pipeline on simulated-but-published-value-seeded error profiles and
reports the metrics that a real deployment would report:
  * leave-one-batch-out accuracy + confusion matrix  (leakage-aware)
  * calibration (ECE)
  * exclusion power: likelihood ratio for "rules-out-commercial"
  * four-tier evidentiary mapping
  * label-shuffle negative control (must collapse to chance)
Saves Figure 4.6.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # figstyle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from synth_forensics import (build_dataset, PHENOTYPES, FEATURE_NAMES, lr_to_tier)
try:
    from figstyle import apply_style, caption, INK, MUTED
except ImportError:  # flat-folder / standalone use: minimal fallbacks
    INK, MUTED = "#1a202c", "#6b7280"
    def apply_style():
        import matplotlib as mpl
        mpl.rcParams.update({"figure.dpi": 150, "savefig.dpi": 150,
                             "font.size": 11, "axes.grid": True,
                             "figure.facecolor": "white", "axes.facecolor": "white"})
    def caption(fig, number, title, subtitle=None, source=None):
        fig.text(0.06, 0.99, f"Figure {number}   {title}", ha="left", va="top",
                 fontsize=13, fontweight="bold", color=INK)
        if subtitle:
            fig.text(0.06, 0.955, subtitle, ha="left", va="top", fontsize=10, color=MUTED)
        if source:
            fig.text(0.06, 0.015, source, ha="left", va="bottom", fontsize=7.5,
                     color=MUTED, style="italic")

apply_style()
import os as _os
OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "figures")
_os.makedirs(OUT, exist_ok=True)

METHODS = ["column_phosphoramidite", "photolithographic", "enzymatic_tdt", "openids_diy"]
LABELS  = [PHENOTYPES[m]["label"] for m in METHODS]
SHORT   = ["Column\nphosphoramidite", "Photo-\nlithographic", "Enzymatic\n(TdT)", "OpenIDS DIY\n(predicted)"]

X, y, groups = build_dataset(METHODS, n_batches=14, n_molecules=1500, seed=7)
print(f"Dataset: {X.shape[0]} batches x {X.shape[1]} features, {len(METHODS)} method classes\n")

clf = RandomForestClassifier(n_estimators=400, min_samples_leaf=2, random_state=0)
cv = GroupKFold(n_splits=7)   # leave-batches-out: never split within a batch

# out-of-fold predictions (leakage-aware)
proba = cross_val_predict(clf, X, y, groups=groups, cv=cv, method="predict_proba")
classes = clf.fit(X, y).classes_
pred = classes[proba.argmax(1)]

acc = (pred == y).mean()
print(f"Leave-batch-out accuracy: {acc*100:.1f}%   (chance = {100/len(METHODS):.1f}%)")

# confusion matrix
idx = {m: i for i, m in enumerate(METHODS)}
cm = np.zeros((len(METHODS), len(METHODS)), int)
for t, p in zip(y, pred):
    cm[idx[t], idx[p]] += 1

# calibration (ECE) on max-prob
conf = proba.max(1)
correct = (pred == y).astype(float)
bins = np.linspace(0, 1, 11)
ece = 0.0
for b in range(10):
    m = (conf >= bins[b]) & (conf < bins[b+1])
    if m.sum():
        ece += m.mean() * abs(correct[m].mean() - conf[m].mean())
print(f"Calibration ECE: {ece:.3f}")

# exclusion power: LR that a sample is NOT commercial column
ci = idx["column_phosphoramidite"]
p_comm = proba[:, list(classes).index("column_phosphoramidite")]
lr_not_comm = (1 - p_comm) / np.clip(p_comm, 1e-6, None)   # equal-prior LR
noncomm = y != "column_phosphoramidite"
excl = (lr_not_comm[noncomm] > 1).mean()
print(f"Exclusion: {excl*100:.0f}% of non-commercial samples correctly give LR>1 vs commercial")
med_lr = np.median(lr_not_comm[noncomm])
print(f"  median LR(not-commercial) on non-commercial samples = {med_lr:.0f}  -> {lr_to_tier(med_lr)}")

# the DIY-vs-commercial discrimination (the forensic value-add) -- the HARD pair
di = list(classes).index("openids_diy")
diy_mask = y == "openids_diy"
p_diy_on_diy = proba[diy_mask, di].mean()
print(f"\nDIY-vs-commercial: mean P(OpenIDS-DIY | DIY sample) = {p_diy_on_diy:.2f}")
print("  (separation driven by SUPPRESSED G->A + elevated n-1 deletion, per capping omission)")

# binary DIY-vs-commercial accuracy + a noise sweep (realism)
def binary_diy_vs_commercial(cv_noise, n_batches=14, n_mol=1500):
    import synth_forensics as sf
    orig = sf.simulate_batch.__defaults__
    Xb, yb, gb = [], [], []
    gid = 0
    rng = np.random.default_rng(3)
    for m in ["column_phosphoramidite", "openids_diy"]:
        for _ in range(n_batches):
            br = np.random.default_rng(rng.integers(1e9))
            # rebuild a batch with custom jitter cv
            p = sf.PHENOTYPES[m]
            jit = lambda x: x * np.exp(br.normal(0, cv_noise))
            dr, ir, sr = jit(p["del_rate"]), jit(p["ins_rate"]), jit(p["sub_rate"])
            tot = dr + ir + sr
            spec = br.dirichlet(np.array([p["sub_spectrum"][c] for c in sf.SUB_CHANNELS]) * 120)
            en = 1/np.sqrt(n_mol)
            f = ([dr/tot, ir/tot, sr/tot, np.log10(tot)] + list(spec)
                 + [jit(p["pos5p_slope"]), jit(p["trunc_n1_frac"]), jit(p["trunc_decay"]),
                    jit(p["homopolymer_enrich"]), jit(p["gc_effect"]), jit(p["intra_corr"])])
            f = np.array(f) + br.normal(0, en*0.4, size=len(f))
            Xb.append(f); yb.append(m); gb.append(gid); gid += 1
    Xb, yb, gb = np.array(Xb), np.array(yb), np.array(gb)
    pr = cross_val_predict(RandomForestClassifier(n_estimators=300, min_samples_leaf=2, random_state=0),
                           Xb, yb, groups=gb, cv=GroupKFold(5), method="predict_proba")
    prd = np.array(["column_phosphoramidite", "openids_diy"])[pr.argmax(1)] \
        if list(sorted(set(yb)))[0] == "column_phosphoramidite" else None
    from sklearn.ensemble import RandomForestClassifier as RF
    m2 = RF(n_estimators=300, min_samples_leaf=2, random_state=0).fit(Xb, yb)
    prd = m2.classes_[pr.argmax(1)]
    return (prd == yb).mean()

noise_levels = [0.10, 0.18, 0.24, 0.32, 0.42, 0.55]
binary_acc = [binary_diy_vs_commercial(c) for c in noise_levels]
print("\nDIY-vs-commercial binary accuracy vs batch-noise CV:")
for c, a in zip(noise_levels, binary_acc):
    print(f"  CV={c:.2f} -> {a*100:.0f}%")

# label-shuffle negative control
rng = np.random.default_rng(1)
y_shuf = y.copy()
# shuffle at the batch level, preserving group structure
for g in np.unique(groups):
    pass
y_shuf = rng.permutation(y)
proba_s = cross_val_predict(clf, X, y_shuf, groups=groups, cv=cv, method="predict_proba")
pred_s = clf.classes_[proba_s.argmax(1)]
acc_s = (pred_s == y_shuf).mean()
print(f"\nLabel-shuffle control accuracy: {acc_s*100:.1f}%  (should be ~chance {100/len(METHODS):.0f}%)")

# ---- Figure 4.6 -----------------------------------------------------------
fig = plt.figure(figsize=(12.6, 4.8))
fig.subplots_adjust(top=0.80, bottom=0.16, left=0.06, right=0.985, wspace=0.42)

# (a) LDA 2-D separation
axA = fig.add_subplot(1, 3, 1)
lda = LinearDiscriminantAnalysis(n_components=2)
Z = lda.fit_transform(X, y)
palette = {"column_phosphoramidite": "#718096", "photolithographic": "#dd6b20",
           "enzymatic_tdt": "#2c7a7b", "openids_diy": "#2b6cb0"}
for m, s in zip(METHODS, SHORT):
    mask = y == m
    axA.scatter(Z[mask, 0], Z[mask, 1], s=45, color=palette[m], edgecolor="white",
                linewidth=0.8, label=s.replace("\n", " "))
axA.set_title("(a) Error-phenotype separation (LDA)", fontsize=11)
axA.set_xlabel("LD1"); axA.set_ylabel("LD2")
axA.legend(fontsize=7.3, loc="best")

# (b) noise sweep: DIY-vs-commercial binary accuracy vs batch noise
axB = fig.add_subplot(1, 3, 2)
axB.plot([c*100 for c in noise_levels], [a*100 for a in binary_acc], "-o",
         color="#2b6cb0", lw=2.2)
axB.axhline(50, color="#d1604a", ls="--", lw=1.2)
axB.text(11, 52, "chance (binary)", color="#b0553f", fontsize=8)
axB.set_ylim(45, 102)
axB.set_title("(b) DIY-vs-commercial: the hard pair", fontsize=11)
axB.set_xlabel("batch-to-batch noise (CV %)")
axB.set_ylabel("leave-batch-out accuracy (%)")

# (c) exclusion: LR distribution
axC = fig.add_subplot(1, 3, 3)
lrc = np.log10(np.clip(lr_not_comm, 1e-3, 1e6))
axC.hist(lrc[y == "column_phosphoramidite"], bins=20, color="#718096", alpha=0.7,
         label="true commercial")
axC.hist(lrc[noncomm], bins=20, color="#2b6cb0", alpha=0.65, label="true non-commercial")
axC.axvline(0, color="#d1604a", ls="--", lw=1.4)
axC.text(0.12, axC.get_ylim()[1]*0.9, "LR = 1", color="#b0553f", fontsize=8)
axC.set_title("(c) Exclusion: rules-out-commercial", fontsize=11)
axC.set_xlabel("log10 LR(not commercial)"); axC.set_ylabel("batches")
axC.legend(fontsize=7.8, loc="upper left")

caption(fig, "4.6", "Proof-of-concept: synthesis-method attribution from error phenotypes",
        source="Source: Chapter 4 PoC (synth_forensics). Input error profiles are SIMULATED from published "
               "per-method values (Masaki/Filges/Lietard/Palluk); the pipeline (features, leave-batch-out CV, "
               "calibration, LR/tiers, label-shuffle) is real. OpenIDS-DIY is a PREDICTED phenotype (capping omitted). "
               "Real reference deposits are the binding constraint, not this simulator.")
fig.savefig(f"{OUT}/fig4_6_poc.png", bbox_inches="tight"); plt.close(fig)
print("\nFigure 4.6 written.")
