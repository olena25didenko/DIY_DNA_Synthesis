"""Chapter 3 (Cost & Accessibility Trajectories) figures, standardized.
Single source of truth for the OpenIDS trajectory numbers -> table + figures tie out."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from figstyle import (apply_style, caption, METHOD_COLORS, CONDITIONAL, HATCH,
                      INK, MUTED, GRID)

apply_style()
import os as _os
OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "figures")
_os.makedirs(OUT, exist_ok=True)

ANCHOR = 19.9  # Kim et al. 2024 BOM, $K
RATES = {"conservative": 0.05, "base": 0.08, "optimistic": 0.15}
YEARS = np.arange(2024, 2031)

def traj(rate):
    return ANCHOR * (1 - rate) ** (YEARS - 2024)

curves = {k: traj(r) for k, r in RATES.items()}

# print the exact table values used in the markdown
print("OpenIDS trajectory ($K), anchor $19.9K (2024):")
print("year   " + "  ".join(str(y) for y in YEARS))
for k in ["conservative", "base", "optimistic"]:
    print(f"{k:12s} " + " ".join(f"{v:5.1f}" for v in curves[k]))

def crossing(rate, target):
    # year cost first drops below target
    t = np.log(target / ANCHOR) / np.log(1 - rate)
    return 2024 + t
print("\nThreshold crossings (year):")
for k, r in RATES.items():
    print(f"  {k:12s} <$15K ~{crossing(r,15):.1f}   <$10K ~{crossing(r,10):.1f}")

# ---------------------------------------------------------------- Fig 3.1
fig, ax = plt.subplots(figsize=(9.6, 5.6))
fig.subplots_adjust(top=0.80, bottom=0.12, left=0.10, right=0.82)
c = METHOD_COLORS["OpenIDS"]
ax.fill_between(YEARS, curves["optimistic"], curves["conservative"],
                color=c, alpha=0.12, label="scenario range")
ax.plot(YEARS, curves["base"], "-o", color=c, lw=2.4, label="base case (~8%/yr)")
ax.plot(YEARS, curves["conservative"], "--", color="#c78a1e", lw=1.8, marker="^",
        markersize=5, label="conservative (~5%/yr)")
ax.plot(YEARS, curves["optimistic"], "--", color="#2c7a7b", lw=1.8, marker="v",
        markersize=5, label="optimistic (~15%/yr)")
ax.axhline(15, color="#94a3b8", ls=":", lw=1.2)
ax.axhline(10, color="#d1604a", ls=":", lw=1.2)
ax.text(2024.05, 15.25, "$15K  well-funded-lab threshold", fontsize=8.5, color=MUTED)
ax.text(2024.05, 10.25, "$10K  commodity-instrument threshold", fontsize=8.5, color="#b0553f")
ax.scatter([2024], [ANCHOR], s=70, color=c, zorder=6, edgecolor="white")
ax.text(2024, ANCHOR+0.5, "published $19.9K\n(Kim et al. 2024)", fontsize=8.5, va="bottom")
for yr, val in [(2026, curves["base"][2]), (2028, curves["base"][4]), (2030, curves["base"][6])]:
    ax.annotate(f"${val:.1f}K", (yr, val), textcoords="offset points",
                xytext=(6, -12), fontsize=9, fontweight="bold", color=c)
ax.set_xticks(YEARS); ax.set_ylim(6, 21); ax.set_xlabel("Year")
ax.set_ylabel("OpenIDS capital cost (USD, $K)")
ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0))
caption(fig, "3.1", "OpenIDS cost trajectory - three annual-decline scenarios (conditional)",
        source="Source: Chapter 3, Sec. 4.1. HIGH-confidence anchor ($19.9K, 2024); projections CONDITIONAL on "
               "sustained community iteration. Scenario rates (~5/8/15%/yr) are deliberately below the ~12-18%/yr "
               "commercial-synthesis analog. MEDIUM confidence at best.")
fig.savefig(f"{OUT}/fig3_1_openids.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 3.2 electrochemical TRL
fig, ax = plt.subplots(figsize=(10.4, 5.4))
fig.subplots_adjust(top=0.80, bottom=0.12, left=0.08, right=0.97)
ax.axhspan(2.6, 4, color="#fbeeea", alpha=0.5, zorder=0)
ax.text(2035.5, 3.3, "cost UNDEFINED\n(no benchtop exists)", fontsize=8.5, color="#b0553f", ha="right")
# anchor
ax.scatter([2021], [3], s=80, color="#4a5568", zorder=6)
ax.text(2021, 2.78, "Xu et al. 2021\nproof-of-concept (TRL 3)", fontsize=8, va="top")
ax.axvline(2026.0, color="#94a3b8", ls=":", lw=1.2)
ax.text(2026.1, 6.7, "Oct 2026\nframework revision (paused)", fontsize=8, color=MUTED)
ec = METHOD_COLORS["Electrochemical"]
# accelerated
ax.plot([2026, 2027, 2028], [3, 4, 5], "--", color="#2c7a7b", marker="D", lw=1.8)
ax.text(2028.1, 5.0, "accelerated: TRL4 ~2027 ($8-12K), TRL5 ~2028", fontsize=8.5, color="#2c7a7b")
# continued
ax.plot([2026, 2028.5, 2030], [3, 4, 4], "--", color=ec, marker="D", lw=1.8)
ax.text(2030.1, 4.0, "continued: TRL4 ~2028-30 ($10-15K)", fontsize=8.5, color=ec)
# stalled
ax.plot([2026, 2032], [3, 3], "--", color="#d1604a", marker="x", lw=1.8)
ax.text(2032.1, 3.0, "stalled: TRL3 indefinitely - no cost projection", fontsize=8.5, color="#b0553f")
ax.set_xlim(2020.5, 2036.5); ax.set_ylim(2.5, 7.3)
ax.set_yticks([3,4,5,6,7]); ax.set_xlabel("Year")
ax.set_ylabel("Technology Readiness Level")
caption(fig, "3.2", "Electrochemical maturation - cost is TRL-gated (conditional paths)",
        source="Source: Chapter 3, Sec. 4.2. Anchor: Xu et al. 2021 (Sci. Adv. eabk0100), TRL 3. Cost estimates are "
               "LOW-confidence and only defensible at TRL >= 4 - below that, no benchtop exists to measure. "
               "TRL-advance timings assume ~2-3 yr per level; all paths conditional on R&D.")
fig.savefig(f"{OUT}/fig3_2_electrochem.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 3.3 2030 matrix
rows3 = ["OpenIDS", "Electrochemical", "Enzymatic benchtop"]
cols3 = ["R&D accelerates", "R&D continues", "R&D stalls"]
# OpenIDS: accelerate=optimistic, continue=base, stall=conservative
o = curves
cells = [
    [f"${o['optimistic'][6]:.1f}K", f"${o['base'][6]:.1f}K", f"${o['conservative'][6]:.1f}K"],
    ["$8-12K*", "$10-15K*", "TRL 3 - undefined"],
    ["~$112K", "~$190K", "~$298K"],
]
# color by band: <15K green, 15-30K amber, >30K red, undefined grey
def cell_color(txt):
    if "undefined" in txt: return "#c9ced6"
    import re
    nums = [float(x) for x in re.findall(r"([\d.]+)", txt)]
    v = min(nums) if nums else 99
    if v < 15: return "#bfe0c7"
    if v < 30: return "#f2e0a8"
    return "#efc0b4"

fig, ax = plt.subplots(figsize=(9.6, 4.6))
fig.subplots_adjust(top=0.78, bottom=0.14, left=0.20, right=0.97)
for r in range(3):
    for cc in range(3):
        ax.add_patch(plt.Rectangle((cc, r), 1, 1, facecolor=cell_color(cells[r][cc]),
                     edgecolor="white", linewidth=3))
        ax.text(cc+0.5, r+0.5, cells[r][cc], ha="center", va="center",
                fontweight="bold", fontsize=11, color=INK)
ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.invert_yaxis()
ax.set_xticks(np.arange(3)+0.5); ax.set_xticklabels(cols3, fontsize=10, fontweight="bold")
ax.xaxis.tick_top()
ax.set_yticks(np.arange(3)+0.5); ax.set_yticklabels(rows3, fontsize=10)
ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
leg = [Patch(facecolor="#bfe0c7", label="<$15K (accessible)"),
       Patch(facecolor="#f2e0a8", label="$15-30K"),
       Patch(facecolor="#efc0b4", label=">$30K (constrained)"),
       Patch(facecolor="#c9ced6", label="undefined (TRL 3)")]
ax.legend(handles=leg, loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=4, fontsize=8.5)
caption(fig, "3.3", "2030 capital cost by R&D scenario",
        source="Source: Chapter 3, Sec. 5.1. *Electrochemical cost valid only IF the required TRL advance occurs; "
               "undefined at TRL 3. OpenIDS spans its 3 scenarios (accelerate=~15%/yr ... stall=~5%/yr). "
               "Enzymatic follows commercial (IFP 2024), not DIY.")
fig.savefig(f"{OUT}/fig3_3_matrix.png", bbox_inches="tight"); plt.close(fig)
print("\nChapter 3 figures written.")
