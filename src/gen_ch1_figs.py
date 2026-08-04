"""Chapter 1 (Regime-Conditional TRI) figures, standardized."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, FancyArrow
from figstyle import (apply_style, caption, method_bar_style,
                      METHOD_COLORS, CONDITIONAL, CONF_COLORS, HATCH,
                      INK, MUTED, GRID)

apply_style()
import os as _os
OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "figures")
_os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- Fig 1.1 TRL
methods = ["OpenIDS", "MAS 2.0", "Electrochemical", "Enzymatic (service)",
           "Enzymatic (benchtop)", "DropSynth", "Commercial"]
trl = [5, 5, 3, 5, 5, 4, 9]
labels = ["5", "5", "3", "5", "5", "4", "9"]
short = ["OpenIDS\n(inkjet)", "MAS 2.0\n(photolith.)", "Electro-\nchemical", "Enzymatic\n(service)",
         "Enzymatic\n(benchtop)", "DropSynth", "Commercial\nbenchtop"]

fig, ax = plt.subplots(figsize=(8.4, 5.0))
fig.subplots_adjust(top=0.80, bottom=0.16, left=0.09, right=0.83)
# maturity bands
bands = [(1,3,"#eef4fb","Concept"),(3,5,"#eaf3ee","Demonstrated"),
         (5,7,"#eef6f0","Production"),(7,9,"#f3eefa","Commodity")]
for lo,hi,c,name in bands:
    ax.axhspan(lo,hi,color=c,zorder=0)
    ax.text(6.55,(lo+hi)/2,name,va="center",ha="left",fontsize=8.5,color=MUTED)
method_bar_style(ax, methods, trl)
for i,(v,l) in enumerate(zip(trl,labels)):
    ax.text(i, v+0.12, l, ha="center", va="bottom", fontweight="bold", fontsize=11)
ax.set_xticks(range(len(methods))); ax.set_xticklabels(short, fontsize=9)
ax.set_ylim(1,9); ax.set_ylabel("Technology Readiness Level (1-9)")
ax.set_xlim(-0.6, 6.5)
ax.legend(handles=[Patch(facecolor="#cbd5e0", hatch=HATCH, edgecolor="white",
          label="conditional-future (TRL 3-4): scenario, not present-tense")],
          loc="upper left", bbox_to_anchor=(0.0,1.02))
caption(fig,"1.1","Technology readiness by synthesis approach",
        subtitle="TRL = how close to a working, assembly-ready capability a non-expert could stand up. DIY zone of interest = TRL 3-6.",
        source="Source: corrected TRI, Sec. 2. TRL reconciled with the literature review (commercial = 9, enzymatic = 5). "
               "Electrochemical (TRL 3) and DropSynth (TRL 4) are conditional-future (hatched); MAS 2.0 (TRL 5) is an open-hardware photolithographic build.")
fig.savefig(f"{OUT}/fig1_1_trl.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.2 Capital
cap_methods = ["OpenIDS","MAS 2.0","Electrochemical","Enzymatic (benchtop)","DropSynth","Commercial"]
# MAS 2.0 corrected from ~$30K est to a SOURCED figure: instrument ~EUR150-170K (~$163-185K);
# whisker extends to the ~EUR300K (~$326K) fully-loaded build (Somoza/Helices interview, Jul 2026).
best = [19900, 175000, 12000, 292000, 3400, 120000]
lo   = [15000, 163000,  8000, 200000, 3000,  50000]
hi   = [25000, 326000, 20000, 298000, 4000, 200000]
cshort = ["OpenIDS","MAS 2.0","Electrochem.","Enz. bench","DropSynth","Commercial"]
fig, ax = plt.subplots(figsize=(8.4,5.0))
fig.subplots_adjust(top=0.80, bottom=0.13, left=0.12, right=0.96)
err = [np.array(best)-np.array(lo), np.array(hi)-np.array(best)]
method_bar_style(ax, cap_methods, best, err=err)
ax.set_yscale("log")
for i,v in enumerate(best):
    ax.text(i, hi[i]*1.06, f"${v/1000:.0f}K", ha="center", va="bottom", fontweight="bold")
ax.set_xticks(range(len(cap_methods))); ax.set_xticklabels(cshort, fontsize=9.5)
ax.set_ylabel("Capital cost (log scale, USD)")
ax.set_ylim(2500, 560000)
ax.set_yticks([3000,10000,20000,50000,100000,200000,300000])
ax.set_yticklabels(["$3K","$10K","$20K","$50K","$100K","$200K","$300K"])
caption(fig,"1.2","Capital cost by approach",
        subtitle="bars = best estimate; whiskers = stated range",
        source="Source: corrected TRI Sec. 2. MAS 2.0 now SOURCED (Somoza/Helices, Jul 2026): instrument ~$175K, "
               "whisker to ~$326K fully-loaded - far above the earlier ~$30K estimate. DropSynth 'capital' = ~$3.4K "
               "bead pool (consumable). Electrochemical = LOW-confidence est (TRL 3). Enzymatic (service) omitted: no capital.")
fig.savefig(f"{OUT}/fig1_2_capital.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.3 Expertise
ex_methods = ["MAS 2.0","DropSynth","Electrochemical","OpenIDS","Enzymatic (benchtop)",
              "Commercial","Enzymatic (service)"]
ex_vals = [8,8,7,6,5,2,2]
ex_short = ["MAS 2.0","DropSynth","Electrochem.","OpenIDS","Enz. bench","Commercial","Enz. service"]
fig, ax = plt.subplots(figsize=(8.4,4.8))
fig.subplots_adjust(top=0.83, bottom=0.13, left=0.20, right=0.95)
ax.axvspan(0,3,color="#eaf3ee",zorder=0); ax.axvspan(3,6,color="#fdf6e9",zorder=0)
ax.axvspan(6,10,color="#fbeeea",zorder=0)
method_bar_style(ax, ex_methods, ex_vals, orientation="h")
for i,v in enumerate(ex_vals):
    ax.text(v+0.15, i, f"{v}/10", va="center", ha="left", fontweight="bold")
ax.set_yticks(range(len(ex_methods))); ax.set_yticklabels(ex_short)
ax.invert_yaxis()
ax.set_xlim(0,10); ax.set_xlabel("Expertise required (1 = none, 10 = specialist)")
ax.text(1.5,-0.75,"low barrier",ha="center",fontsize=8.5,color=MUTED)
ax.text(4.5,-0.75,"moderate",ha="center",fontsize=8.5,color=MUTED)
ax.text(8,-0.75,"high barrier",ha="center",fontsize=8.5,color=MUTED)
caption(fig,"1.3","Expertise barrier to DIY use",
        source="Source: corrected TRI, Sec. 2. Hatched = conditional-future (TRL 3-4).")
fig.savefig(f"{OUT}/fig1_3_expertise.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.4 Trajectories
fig, (axA, axB) = plt.subplots(1,2, figsize=(11.2,5.0))
fig.subplots_adjust(top=0.80, bottom=0.14, left=0.08, right=0.97, wspace=0.28)
yrs = [2026, 2028]
traj = {
    "OpenIDS":              ([20,17],  [18,15], [22,18]),
    "MAS 2.0":              ([175,175],[163,163],[326,326]),  # DIY, but single 2026 anchor: flat, no OSS trajectory
    "Electrochemical":      ([12,9],   [10,8],  [15,10]),
    "Enzymatic (benchtop)": ([90,55],  [50,30], [100,60]),
    "Commercial":           ([110,90], [50,40], [180,120]),
}
for m,(mid,l,h) in traj.items():
    c = METHOD_COLORS[m]
    ls = "--" if m in CONDITIONAL else "-"
    axA.plot(yrs, mid, ls, color=c, lw=2.2, marker="o", label=m, zorder=3)
    axA.fill_between(yrs, l, h, color=c, alpha=0.13, zorder=1)
axA.set_yscale("log"); axA.set_xticks(yrs)
axA.set_yticks([10,20,50,100,200,300])
axA.set_yticklabels(["$10K","$20K","$50K","$100K","$200K","$300K"])
axA.set_ylim(7,420); axA.set_ylabel("Capital cost (log, USD)")
axA.set_title("(a) Capital-cost projections, 2026->2028", fontsize=11.5)
axA.legend(loc="lower left", fontsize=8.5)
axA.text(0.5,-0.16,"dashed = conditional on TRL advancement (electrochemical); MAS 2.0 flat = single 2026 anchor (no OSS trajectory)",
         transform=axA.transAxes, ha="center", fontsize=7.4, color=MUTED)

nyr = [2001,2007,2008,2010,2015,2019,2022]
ncost = [95e6,10e6,0.75e6,50e3,4e3,1e3,600]
axB.plot(nyr, ncost, "-o", color="#4a5568", lw=2, markersize=5)
axB.axvspan(2007.5,2009,color="#f6dfd6",alpha=0.6)
axB.text(2008.2, 3e7, "NGS\ninflection", fontsize=8, color="#b0553f")
axB.set_yscale("log"); axB.set_ylim(2e2,3e8)
axB.set_xlabel("Year"); axB.set_ylabel("Cost per genome (log, USD)")
axB.set_title("(b) DNA sequencing cost analog (NHGRI)", fontsize=11.5)
axB.text(0.5,-0.16,"Approximate milestones; NHGRI updates ceased 2022. Curve shape only.",
         transform=axB.transAxes, ha="center", fontsize=8, color=MUTED)
caption(fig,"1.4","Cost trajectories: conditional DIY/benchtop projections vs. the sequencing-cost analog",
        source="Source: corrected TRI Sec. 3. Panel (a) projections are CONDITIONAL on continued "
               "development and carry the TRL gate; use for shape, not point forecasts.")
fig.savefig(f"{OUT}/fig1_4_trajectories.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.5 Evasion R0->R1
ev_methods = ["OpenIDS","MAS 2.0","Electrochemical","Enzymatic (service)",
              "Enzymatic (benchtop)","DropSynth","Commercial"]
# High=1 Medium=2 Low=3 Very low=4  (right = more oversight / less evasion)
r0 = {"OpenIDS":2,"MAS 2.0":2,"Electrochemical":1,"Enzymatic (service)":3,
      "Enzymatic (benchtop)":2,"DropSynth":2,"Commercial":2}
r1 = {"OpenIDS":3,"MAS 2.0":3,"Electrochemical":2,"Enzymatic (service)":4,
      "Enzymatic (benchtop)":3,"DropSynth":3,"Commercial":3}
fig, ax = plt.subplots(figsize=(9.2,5.0))
fig.subplots_adjust(top=0.83, bottom=0.15, left=0.20, right=0.80)
for i,m in enumerate(ev_methods):
    c = METHOD_COLORS[m]
    y = len(ev_methods)-1-i
    ax.annotate("", xy=(r1[m],y), xytext=(r0[m],y),
                arrowprops=dict(arrowstyle="-|>", color=c, lw=2.4))
    ax.scatter([r0[m]],[y], s=90, color=c, zorder=5,
               edgecolor="white", linewidth=1.2,
               hatch=HATCH if m in CONDITIONAL else None)
star = " *" if m in CONDITIONAL else ""
labels5 = [m+(" *" if m in CONDITIONAL else "") for m in ev_methods]
ax.set_yticks(range(len(ev_methods)))
ax.set_yticklabels(list(reversed(labels5)))
ax.set_xlim(0.5,4.5); ax.set_xticks([1,2,3,4])
ax.set_xticklabels(["High","Medium","Low","Very low"])
ax.set_xlabel("Oversight-evasion potential  (left = more able to evade; right = more oversight)")
# High(1) on left ... Very low(4) on right; R0->R1 arrows point right = tightening
from matplotlib.lines import Line2D
leg = [Line2D([0],[0],marker="o",color="w",markerfacecolor="#6b7280",markersize=9,label="R0 (status quo, observed)"),
       Line2D([0],[0],marker=">",color="#6b7280",label="R1 (mandatory/on-device, projected)"),
       Patch(facecolor="#cbd5e0",hatch=HATCH,edgecolor="white",label="* conditional-future (TRL 3-4): scenario")]
ax.legend(handles=leg, loc="upper left", bbox_to_anchor=(1.01,1.0))
caption(fig,"1.5","Oversight tightens under R1  (dot = R0 -> arrow = R1)",
        source="Source: corrected TRI Sec. 4.1. The policy-relevant quantity is the R0->R1 shift, not the "
               "absolute level. R1 is projected, not observed.")
fig.savefig(f"{OUT}/fig1_5_evasion.png", bbox_inches="tight"); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.6 Confidence heatmap
rows = ["TRL","Capital","Per-seq","Expertise","Time-to-first","Max length","Yield","Evasion (R0/R1)"]
cols = ["OpenIDS","MAS 2.0","Electrochem.","Enz. service","Enz. bench","DropSynth","Commercial"]
grid = [
 ["H","M","M","H","H","M","H"],
 ["H","M","L","H","M","L","H"],
 ["M","L","L","M","M","L","H"],
 ["M","M","M","H","M","M","H"],
 ["M","L","L","M","M","L","H"],
 ["M","M","L","M","M","L","H"],
 ["H","M","L","n/a","H","M","H"],
 ["M","L","L","M","M","L","M"],
]
fig, ax = plt.subplots(figsize=(9.0,5.4))
fig.subplots_adjust(top=0.82, bottom=0.14, left=0.16, right=0.97)
for r in range(len(rows)):
    for c in range(len(cols)):
        v = grid[r][c]
        ax.add_patch(plt.Rectangle((c,r),1,1,facecolor=CONF_COLORS[v],
                     edgecolor="white",linewidth=2))
        txt = "-" if v=="n/a" else v
        ax.text(c+0.5,r+0.5,txt,ha="center",va="center",fontweight="bold",
                color="white" if v!="n/a" else "#6b7280", fontsize=11)
ax.set_xlim(0,len(cols)); ax.set_ylim(0,len(rows)); ax.invert_yaxis()
ax.set_xticks(np.arange(len(cols))+0.5); ax.set_xticklabels(cols, fontsize=9.5)
ax.set_yticks(np.arange(len(rows))+0.5); ax.set_yticklabels(rows, fontsize=9.5)
ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
leg = [Patch(facecolor=CONF_COLORS["H"],label="HIGH"),
       Patch(facecolor=CONF_COLORS["M"],label="MED"),
       Patch(facecolor=CONF_COLORS["L"],label="LOW"),
       Patch(facecolor=CONF_COLORS["n/a"],label="n/a")]
ax.legend(handles=leg, loc="upper center", bbox_to_anchor=(0.5,-0.10), ncol=4)
caption(fig,"1.6","Confidence in each estimate  (H / M / L; - = not applicable)",
        source="Source: corrected TRI Sec. 6. Electrochemical & DropSynth dominated by LOW confidence "
               "(TRL 3-4). Yield n/a for enzymatic (service): provider-side, not a customer property.")
fig.savefig(f"{OUT}/fig1_6_confidence.png", bbox_inches="tight"); plt.close(fig)

print("Chapter 1 figures written to", OUT)
import os
for f in sorted(os.listdir(OUT)):
    print("  ", f)
