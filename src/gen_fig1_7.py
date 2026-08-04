"""Figure 1.7 - Cost per usable base vs synthesis volume (sourced methods only).
Rebuilt, with MAS 2.0 added as a capital-floor-only curve (same treatment as DNA Script)."""
import os
import numpy as np
import matplotlib.pyplot as plt
from figstyle import apply_style, caption, MUTED
apply_style()

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(OUT, exist_ok=True)

x = np.logspace(3, 8, 500)          # cumulative usable bases (1e3 -> 1e8)

# --- sourced curves -----------------------------------------------------------
openids   = 0.044 + 19900.0 / x     # consumable floor + capital amortization (Kim 2024)
dnascript = 292000.0 / x            # capital floor only (no per-base consumable published)
mas2      = 175000.0 / x            # capital floor only (Somoza/Helices 2026; ~EUR150-170K instrument)

fig, ax = plt.subplots(figsize=(9.6, 5.8))
fig.subplots_adjust(top=0.82, bottom=0.20, left=0.10, right=0.97)

# horizontal reference bands (verified assembled product)
ax.axhspan(0.13, 0.38, color="#cdeede", alpha=0.55, zorder=0)
ax.text(1.3e3, 0.20, "Ansa enzymatic clonal service  $0.13-0.38/bp", fontsize=8, color="#2f6f5e")
ax.axhspan(0.07, 0.10, color="#dfe3e8", alpha=0.8, zorder=0)
ax.text(1.3e3, 0.083, "Mail-order providers  $0.07-0.10/bp", fontsize=8, color="#4a5568")
ax.text(1.3e3, 0.058, "(flat, verified assembled product)", fontsize=7.5, color=MUTED)
ax.axhline(0.044, ls=":", color="#2b6cb0", lw=1.4, zorder=1)
ax.text(1.3e3, 0.047, "OpenIDS consumable floor  ~$0.044/base", fontsize=7.5, color="#2b6cb0")

# curves
ax.plot(x, openids,  "-",  color="#2b6cb0", lw=2.6, label="OpenIDS (raw short oligos)", zorder=4)
ax.plot(x, dnascript,"--", color="#63b3ed", lw=2.0, label="DNA Script SYNTAX - capital floor only", zorder=3)
ax.plot(x, mas2,     "--", color="#805ad5", lw=2.2, label="MAS 2.0 - capital floor only (~$175K)", zorder=3)

# crossover marker: OpenIDS undercuts providers above ~480k usable bases
xc, yc = 480000, 0.044 + 19900.0/480000
ax.scatter([xc], [yc], s=70, color="#c0392b", zorder=6)
ax.annotate("OpenIDS undercuts providers\nabove ~480k usable bases",
            xy=(xc, yc), xytext=(1.1e6, 0.35), fontsize=8, color="#c0392b",
            arrowprops=dict(arrowstyle="-|>", color="#c0392b", lw=1.3))

ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(1e3, 1e8); ax.set_ylim(1e-3, 1e2)
ax.set_xlabel("Cumulative usable bases synthesized  (proxy for order volume, log)")
ax.set_ylabel("Cost per usable base (USD, log)")
ax.set_yticks([1e-3,1e-2,0.1,1,10,100])
ax.set_yticklabels(["$0.001","$0.01","$0.10","$1","$10","$100"])
ax.legend(loc="upper right", fontsize=8.5, framealpha=0.95)

caption(fig, "1.7", "Cost per usable base vs synthesis volume (sourced methods only)",
        source="Two-part model: cost/usable base = consumable/base + capital / cumulative usable bases; yield-adjusted "
               "where a full-length fraction is known. SOURCED anchors only: OpenIDS (capital $19,900 + run cost $102.61, "
               "Kim 2024; ~55% full-length); DNA Script (capital $292K) and MAS 2.0 (instrument ~EUR150-170K / ~$175K, "
               "Somoza/Helices 2026) shown as CAPITAL FLOOR ONLY - no per-base consumable is published for either, so "
               "these are lower bounds, not full curves. MAS 2.0 output is library-grade, not per-strand-perfect. "
               "Provider/Ansa lines are flat, no capital.")
fig.savefig(f"{OUT}/fig1_7_costperbase.png", bbox_inches="tight", dpi=150)
plt.close(fig)
print("wrote", f"{OUT}/fig1_7_costperbase.png")
