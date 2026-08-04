"""
Shared figure style for the Synthesis Screening TRI project.
Import this in every chapter's figure script so the whole set is visually coherent.

Conventions
-----------
- One fixed colour per synthesis method, used identically in every figure.
- Conditional-future methods (TRL 3-4: Electrochemical, DropSynth) are drawn
  with a hatch overlay wherever they appear as bars/markers.
- Every figure carries a baked-in caption block:
      Figure X.Y  <Title>            (bold, top)
      <one-line subtitle>            (optional, top)
      Source: ...                    (small, grey italic, bottom)
- Palette continues the colours used in the original drafts (OpenIDS blue,
  electrochemical orange, enzymatic teal/light-blue, DropSynth gold, commercial grey).
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

# ---- fixed method palette -------------------------------------------------
METHOD_COLORS = {
    "OpenIDS":              "#2b6cb0",  # blue
    "MAS 2.0":              "#805ad5",  # violet  (open photolithographic)
    "Electrochemical":      "#dd6b20",  # orange  (conditional-future)
    "Enzymatic (service)":  "#2c7a7b",  # teal
    "Enzymatic (benchtop)": "#4299e1",  # light blue
    "DropSynth":            "#d69e2e",  # gold    (conditional-future)
    "Commercial":           "#718096",  # grey
}

# methods whose numbers are conditional-future (TRL 3-4) -> hatch them
CONDITIONAL = {"Electrochemical", "DropSynth"}
HATCH = "////"

# confidence colours (used by heatmaps / tags)
CONF_COLORS = {"H": "#3f9b5c", "M": "#e0b23c", "L": "#d1604a", "n/a": "#c9ced6"}

INK   = "#1a202c"   # near-black text
MUTED = "#6b7280"   # grey captions / source lines
GRID  = "#e2e8f0"


def apply_style():
    mpl.rcParams.update({
        "figure.dpi": 160,
        "savefig.dpi": 160,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.edgecolor": "#cbd5e0",
        "axes.linewidth": 0.9,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "axes.labelcolor": INK,
        "text.color": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "legend.frameon": False,
        "legend.fontsize": 9.5,
    })


def caption(fig, number, title, subtitle=None, source=None,
            top=0.99, left=0.06):
    """Baked-in standardized caption block."""
    fig.text(left, top, f"Figure {number}   {title}",
             ha="left", va="top", fontsize=13.5, fontweight="bold", color=INK)
    if subtitle:
        fig.text(left, top - 0.045, subtitle,
                 ha="left", va="top", fontsize=10.5, color=MUTED)
    if source:
        fig.text(left, 0.015, source, ha="left", va="bottom",
                 fontsize=7.8, color=MUTED, style="italic", wrap=True)


def method_bar_style(ax, methods, values, orientation="v", err=None):
    """Draw bars with fixed colours + hatch for conditional-future methods."""
    colors = [METHOD_COLORS[m] for m in methods]
    if orientation == "v":
        bars = ax.bar(range(len(methods)), values, color=colors,
                      edgecolor="white", linewidth=1.2,
                      yerr=err, capsize=4,
                      error_kw=dict(ecolor="#4a5568", elinewidth=1.1))
    else:
        bars = ax.barh(range(len(methods)), values, color=colors,
                       edgecolor="white", linewidth=1.2,
                       xerr=err, capsize=4,
                       error_kw=dict(ecolor="#4a5568", elinewidth=1.1))
    for b, m in zip(bars, methods):
        if m in CONDITIONAL:
            b.set_hatch(HATCH)
            b.set_edgecolor("white")
    return bars
