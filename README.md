# Synthesis Screening TRI Project

DIY DNA synthesis under governance transitions — four corrected chapters, a
standardized figure set, and a working proof-of-concept for synthesis-method
attribution. Everything here is detection/attribution and governance analysis:
no synthesis, no evasion guidance.

## What's in here
```
Chapter1_TRI.md                 Regime-conditional Technology Readiness Index
Chapter2_ControlAssessment.md   Control-point robustness & policy durability
Chapter3_CostTrajectories.md    Cost/accessibility forecasts (with uncertainty)
Chapter4_ForensicFramework.md   Synthesis-method attribution + the PoC
figures/                        All 15 figures (PNG), one shared style
requirements.txt                Python packages
src/
  figstyle.py                   Shared figure style (fixed palette + captions)
  gen_ch1_figs.py .. gen_ch4    Reproduce each chapter's figures
  poc/
    synth_forensics.py          Phenotypes + simulator + features + LR/tiers
    run_poc.py                  Run the demo (classify, calibrate, exclude, Fig 4.6)
    extract_features.py         Scaffold for REAL sequencing data
    README.md                   PoC overview
    RUNBOOK.md                  Full step-by-step: demo + real data
```

## Read the chapters
Open any `ChapterX_*.md` in VS Code and press **Ctrl+Shift+V** (Cmd+Shift+V on Mac)
for the Markdown preview. Figures render inline because the paths are relative.

## Run the proof-of-concept in VS Code

1. **Open the folder.** VS Code → File → Open Folder → select this project folder.
2. **Install the Python extension** (Extensions panel, search "Python", by Microsoft).
   If you don't have Python itself, get it from https://www.python.org/downloads/
   and tick **"Add python.exe to PATH"** during install.
3. **Pick the interpreter.** Ctrl+Shift+P → "Python: Select Interpreter" → choose
   your Python 3.
4. **Open a terminal.** Terminal → New Terminal.
5. **Install the packages** (from the project root):
   ```
   python -m pip install -r requirements.txt
   ```
   (On Windows, if `python` isn't found, use `py` instead: `py -m pip install -r requirements.txt`.)
6. **Run the demo:**
   ```
   python src/poc/run_poc.py
   ```
   or open `src/poc/run_poc.py` in the editor and click the ▶ Run button (top-right).
   It prints the metrics and writes `src/poc/figures/fig4_6_poc.png`.

### What the demo shows
Leave-batch-out classification of four synthesis-method classes, calibration (ECE),
an exclusion (rules-out-commercial) likelihood ratio, a DIY-vs-commercial noise
sweep, and a label-shuffle control. The input error profiles are **simulated from
published per-method values** (Masaki/Filges/Lietard/Palluk); the pipeline is real
and runs unchanged on real data. See `src/poc/RUNBOOK.md` for how to swap in real
deposited sequencing data (Filges SRA PRJNA727098, Masaki DDBJ DRA013805, etc.).

### Regenerate the figures (optional)
Each `src/gen_chN_figs.py` writes that chapter's PNGs to a local `figures/` folder
next to the script. Run e.g. `python src/gen_ch1_figs.py` (needs `src/figstyle.py`
alongside, which it is).

## Notes
- Detection/attribution and governance analysis only.
- The OpenIDS DIY error phenotype is a *prediction* (suppressed G→A + elevated n−1
  deletions from capping omission), to be tested against real OpenIDS product data.
- Report calibrated likelihood ratios and ranges, not point calls.
