"""Chapter 2 (Regime-Conditional Control Assessment) figures, standardized."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
from figstyle import apply_style, caption, INK, MUTED, GRID

apply_style()
import os as _os
OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "figures")
_os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- Fig 2.3 Sensitivity
# impact on conclusions if the assumption moved (0=robust ... 1=decisive)
rows = [
    ("S. 3741 enacted & OSTP revision\nimplemented as projected", 0.95,
     "the entire R1 conclusion depends on this"),
    ("DIY systems classified as regulated\n'benchtop synthesizers'", 0.78,
     "decides whether OpenIDS is constrained under R1"),
    ("Electrochemical advances TRL 3->5\nby ~2028", 0.72,
     "would reshape the DIY landscape - but conditional"),
    ("Reagent (phosphoramidite) price\nfalls ~50%", 0.27,
     "rank order roughly unchanged"),
    ("On-device screening adds\n$5-10K per device", 0.20,
     "<10% of instrument price - minimal effect"),
    ("CORE FINDING: supply-chain\nrestriction is not durable", 0.13,
     "survives worst-case - very low sensitivity"),
]
def zone_color(v):
    if v < 0.40:  return "#3f9b5c"   # robust  (green)
    if v < 0.70:  return "#e0b23c"   # watch   (amber)
    return "#d1604a"                 # decisive(red)

fig, ax = plt.subplots(figsize=(11.0, 5.6))
fig.subplots_adjust(top=0.78, bottom=0.13, left=0.28, right=0.97)
# zones
ax.axvspan(0, 0.40, color="#eaf3ee", zorder=0)
ax.axvspan(0.40, 0.70, color="#fdf6e9", zorder=0)
ax.axvspan(0.70, 1.0, color="#fbeeea", zorder=0)
ax.text(0.20, len(rows)-0.25, "robust",  ha="center", fontsize=10, color="#3f9b5c", fontweight="bold")
ax.text(0.55, len(rows)-0.25, "watch",   ha="center", fontsize=10, color="#c78a1e", fontweight="bold")
ax.text(0.85, len(rows)-0.25, "decisive",ha="center", fontsize=10, color="#c0492f", fontweight="bold")

labels = [r[0] for r in rows]
vals   = [r[1] for r in rows]
notes  = [r[2] for r in rows]
ypos = list(range(len(rows)))[::-1]
for y, v, n in zip(ypos, vals, notes):
    ax.barh(y, v, color=zone_color(v), edgecolor="white", height=0.55, zorder=3)
    ax.text(v+0.015, y, n, va="center", ha="left", fontsize=8.5, style="italic", color=MUTED)
ax.set_yticks(ypos); ax.set_yticklabels(labels, fontsize=9)
ax.set_xlim(0, 1.0); ax.set_xticks([0.2,0.55,0.85])
ax.set_xticklabels(["low","medium","high"])
ax.set_xlabel("Impact on the chapter's conclusions if the assumption moved")
ax.set_ylim(-0.6, len(rows)-0.05)
caption(fig, "2.3", "Sensitivity: which assumptions could change the conclusions?",
        source="Source: corrected Chapter 2, Sec. 3.2 / Sec. 5. The high-impact items are projections not yet "
               "realized (R1 implementation; electrochemical maturation; DIY classification). The core finding "
               "(supply-chain restriction is not durable) is the most robust - it survives worst-case bounds.")
fig.savefig(f"{OUT}/fig2_3_sensitivity.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 2.6 Durability ladder
tiers = [
    ("TIER 1 - durable - recommended primary controls", "#3f9b5c", [
        "On-device screening  -  firmware-level, hard to defeat on regulated devices",
        "Mandatory provider screening  -  50-nt window, funding/procurement + Commerce enforcement",
        "Functional SOC detection  -  resists AI-designed evasion (Wittmann et al. 2025)"]),
    ("TIER 2 - durable but limited", "#3a7ca5", [
        "Record retention  -  enables attribution, but post-hoc (does not prevent synthesis)"]),
    ("TIER 3 - weak / emerging", "#e0b23c", [
        "International coordination  -  IBBIS Common Mechanism, IGSC, ISO 20688-2 - broad reach, incomplete"]),
    ("TIER 4 - NOT durable (do not rely on as a primary lever)", "#d1604a", [
        "Supply-chain restriction  -  inputs substitutable / commodity - no chokepoint"]),
]
fig, ax = plt.subplots(figsize=(11.0, 6.0))
fig.subplots_adjust(top=0.80, bottom=0.06, left=0.10, right=0.97)
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")

heights = [2.7, 1.5, 1.5, 1.5]
gap = 0.35
y = 9.2
for (title, color, items), h in zip(tiers, heights):
    box = FancyBboxPatch((0.9, y-h), 8.8, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                         facecolor=color, alpha=0.13, edgecolor=color, linewidth=1.6)
    ax.add_patch(box)
    ax.add_patch(plt.Rectangle((0.9, y-h), 0.14, h, facecolor=color, edgecolor="none"))
    ax.text(1.25, y-0.32, title, fontsize=11, fontweight="bold", color=color, va="top")
    for i, it in enumerate(items):
        ax.text(1.45, y-0.72-0.42*i, "\u2022 "+it, fontsize=9.2, color=INK, va="top")
    y -= (h + gap)

# "more durable" arrow up the left margin
ax.annotate("", xy=(0.45, 9.2), xytext=(0.45, 1.0),
            arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.6))
ax.text(0.30, 5.0, "more durable", rotation=90, va="center", ha="center",
        fontsize=9, color=MUTED)
caption(fig, "2.6", "Control durability ladder (single resolved tiering)",
        source="Source: corrected Chapter 2, Sec. 4.1 / Sec. 6, reconciled into one scheme "
               "(Tier 1 = most durable / recommended primary ... Tier 4 = not durable). R1 controls are projected.")
fig.savefig(f"{OUT}/fig2_6_ladder.png", bbox_inches="tight"); plt.close(fig)

print("Chapter 2 figures written.")
