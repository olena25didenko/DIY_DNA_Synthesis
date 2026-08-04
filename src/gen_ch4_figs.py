"""Chapter 4 (Forensic & Attribution Framework) figures, standardized."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
from figstyle import apply_style, caption, INK, MUTED

apply_style()
import os as _os
OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "figures")
_os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- Fig 4.5
fig, (axA, axB) = plt.subplots(1, 2, figsize=(12.4, 5.0))
fig.subplots_adjust(top=0.78, bottom=0.16, left=0.13, right=0.97, wspace=0.35)

# (a) error-class balance (del / ins / sub), published values
methods = ["Column\nphosphoramidite", "Photolithographic\n(light-directed)", "Enzymatic\n(TdT)"]
# fractions [del, ins, sub]
comp = np.array([
    [84, 4, 12],    # Filges del 0.176 / ins ~0.008 / sub 0.025  (%/nt)
    [75, 9, 16],    # Lietard del 4.65 / ins 0.58 / sub 0.97      (%/bp)
    [54, 42, 4],    # Palluk del 1.3 / ins 1.0 / sub <0.1         (%/step)
])
totals = ["total = 0.2%/nt", "total = 6.2%/bp", "total = 2.4%/step"]
colors3 = ["#2b6cb0", "#7fb3e0", "#dd6b20"]  # deletion / insertion / substitution
y = np.arange(len(methods))[::-1]
left = np.zeros(len(methods))
labels3 = ["deletion", "insertion", "substitution"]
for k in range(3):
    axA.barh(y, comp[:, k], left=left, color=colors3[k], edgecolor="white",
             height=0.55, label=labels3[k])
    for yi, (v, l) in enumerate(zip(comp[:, k], left)):
        if v >= 6:
            axA.text(l + v/2, y[yi], f"{v}%", ha="center", va="center",
                     color="white", fontsize=9, fontweight="bold")
    left += comp[:, k]
for yi, t in zip(y, totals):
    axA.text(102, yi, t, va="center", fontsize=8.5, color=MUTED)
axA.set_yticks(y); axA.set_yticklabels(methods, fontsize=9)
axA.set_xlim(0, 100); axA.set_xlabel("error-class composition (normalised, %)")
axA.set_title("(a) Error-class balance differs by method", fontsize=11)
axA.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=3, fontsize=8.5)

# (b) substitution DIRECTION -- the fine discriminator
labelsB = ["G→A\nphosphoramidite\n(capping-driven)", "G→T\nphotolithographic\n(coupling-order)",
           "no dominant\nsubstitution\n(enzymatic)"]
valsB = [0.11, 0.31, 0.05]
colB = ["#2b6cb0", "#dd6b20", "#2c7a7b"]
xb = np.arange(3)
axB.bar(xb, valsB, color=colB, edgecolor="white", width=0.6)
for i, v in enumerate(valsB):
    txt = "<0.1%" if i == 2 else f"{v:.2f}%"
    axB.text(i, v + 0.02, txt, ha="center", fontweight="bold", fontsize=10)
# annotate capping shift
axB.annotate("", xy=(0, 1.33), xytext=(0, 0.13),
             arrowprops=dict(arrowstyle="->", color="#2b6cb0", ls="--", lw=1.3))
axB.text(0.05, 1.33, "1.33%\n(Pac₂O capping)", fontsize=8, color="#2b6cb0", va="top")
axB.text(0.5, 1.46, "same base (G), opposite product → diagnostic", fontsize=8.5,
         style="italic", color=MUTED, ha="center")
axB.set_xticks(xb); axB.set_xticklabels(labelsB, fontsize=8.3)
axB.set_ylim(0, 1.6); axB.set_ylabel("substitution rate (%)")
axB.set_title("(b) Substitution direction is the fine discriminator", fontsize=11)

caption(fig, "4.5", "Measured error phenotypes discriminate synthesis method (sourced, not illustrative)",
        source="Sources: (a) phosphoramidite = Filges et al. 2021; photolithographic = Lietard et al. 2021; enzymatic = "
               "Palluk et al. 2018. (b) G→A = Masaki et al. 2022 (0.11%; 1.33% with Pac₂O); G→T = Lietard et al. 2021. "
               "Absolute rates are NOT directly comparable across studies (different lengths/chemistries/denominators) - "
               "the discriminative signal is the profile SHAPE, not the magnitude.")
fig.savefig(f"{OUT}/fig4_5_phenotypes.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 4.3 tiers
tiers = [
    ("Tier 1 — proves DIY method", "needs error + equipment + supply (equipment/supply not developed, sec.5)",
     "LR > 1000", "aspirational", "#d1604a"),
    ("Tier 2 — consistent with DIY", "error phenotype suggests DIY; method not pinned",
     "LR 10–1000", "near-term", "#e0b23c"),
    ("Tier 3 — rules out commercial", "exclusion — most defensible & publishable now (cf. Crook X99/X95)",
     "LR < 1 vs commercial", "realistic now", "#3f9b5c"),
    ("Tier 4 — uninformative", "error-corrected / assembled construct",
     "LR ≈ 1", "n/a", "#94a3b8"),
]
fig, ax = plt.subplots(figsize=(11.0, 5.2))
fig.subplots_adjust(top=0.82, bottom=0.05, left=0.04, right=0.97)
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
h = 2.0; gap = 0.28; yv = 9.3
for title, desc, lr, flag, color in tiers:
    ax.add_patch(FancyBboxPatch((0.4, yv-h), 9.2, h,
                 boxstyle="round,pad=0.02,rounding_size=0.10",
                 facecolor=color, alpha=0.12, edgecolor=color, linewidth=1.5))
    ax.add_patch(plt.Rectangle((0.4, yv-h), 0.12, h, facecolor=color))
    ax.text(0.75, yv-0.35, title, fontsize=12, fontweight="bold", color=INK, va="top")
    ax.text(0.75, yv-0.95, desc, fontsize=9.2, color=MUTED, va="top")
    ax.text(7.2, yv-0.55, lr, fontsize=11, fontweight="bold", color=color, va="center")
    # realism flag chip
    ax.add_patch(FancyBboxPatch((8.35, yv-h/2-0.28), 1.1, 0.56,
                 boxstyle="round,pad=0.02,rounding_size=0.14",
                 facecolor=color, edgecolor="none"))
    ax.text(8.9, yv-h/2, flag, fontsize=8.3, color="white", ha="center", va="center", fontweight="bold")
    yv -= (h + gap)
caption(fig, "4.3", "Attribution tiers by likelihood ratio — exclusion is the realistic near-term output",
        source="Source: Chapter 4, sec. 6 (LR tiers per ENFSI 2015; NRC 2014 evidence standards). Tier 1 relies on "
               "equipment/supply-chain forensics that are NOT developed (sec. 5) — aspirational. Tier 3 exclusion is the "
               "defensible near-term output, mirroring Crook et al. 2022 X99/X95.")
fig.savefig(f"{OUT}/fig4_3_tiers.png", bbox_inches="tight"); plt.close(fig)
print("Chapter 4 figures written.")
