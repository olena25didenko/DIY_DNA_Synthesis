# HOW TO RUN — start here

There are **two modes**, and they have different requirements. Read this first.

| Mode | What it does | Where it runs | Files needed |
|---|---|---|---|
| **A. Simulation demo** | proves the classifier + validation works, on simulated data | **VS Code on Windows** (plain Python) | `src/poc/*.py`, `requirements.txt` |
| **B. Real pipeline** | real sequencing reads → real result | **WSL (Linux) inside VS Code** | the `data/` files + `src/poc/*.py` + bioinformatics tools |

You already ran Mode A successfully. Mode B is the new part and it needs **WSL**,
because the tools (bowtie2, samtools, fastp…) don't exist on Windows.

---

## MODE A — simulation demo (Windows, 5 min)

1. Unzip this project, e.g. to `C:\ERA\synthesis-screening-project`.
2. **VS Code → File → Open Folder** → pick that folder.
3. Install the Python extension (if prompted). Ctrl+Shift+P → **Python: Select Interpreter** → your Python 3.
4. **Terminal → New Terminal**, then:
   ```
   python -m pip install -r requirements.txt
   python src\poc\run_poc.py
   ```
   (If `python` isn't found, use `py`. It prints metrics and writes `src\poc\figures\fig4_6_poc.png`.)

That's the whole simulation. Everything below is Mode B.

---

## MODE B — real sequencing pipeline (WSL)

### B0. Install WSL (one-time, ~10 min)
1. Open **PowerShell as Administrator** and run:
   ```
   wsl --install
   ```
   Restart when asked. On reboot, Ubuntu opens and asks you to make a username/password.
2. In VS Code, install the **"WSL"** extension (by Microsoft).
3. Reopen the project inside WSL: Ctrl+Shift+P → **WSL: Open Folder in WSL…**
   (or, from a WSL terminal, `cd` to the project and type `code .`).
   The bottom-left of VS Code should now say **"WSL: Ubuntu"**.

> From here on, use the **WSL terminal** in VS Code (Terminal → New Terminal →
> pick the **Ubuntu** profile if there's a dropdown). Not PowerShell.

### B1. Put the project in the Linux filesystem (faster + avoids path issues)
In the WSL terminal:
```bash
cp -r /mnt/c/ERA/synthesis-screening-project ~/project
cd ~/project
```
(adjust the `/mnt/c/...` path to wherever you unzipped it — your `C:\` is `/mnt/c/`.)

### B2. Install the bioinformatics tools (one-time)
```bash
# install miniconda if you don't have it:
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b && ~/miniconda3/bin/conda init bash
# reopen the terminal, then:
conda create -n dna -c bioconda -c conda-forge \
    fastp cutadapt bowtie2 bwa samtools umi_tools fgbio \
    python=3.11 pysam pandas scikit-learn numpy matplotlib -y
conda activate dna
```

### B3. Run the Filges test first (the clean, ready one)
Everything is in `data/`. From `~/project/data`:
```bash
cd ~/project/data
sh download_filges_subset.sh          # 18 files, ~700 MB
```
Then follow **`../src/poc/filges_runbook.md`** step by step (trim → UMI consensus →
align → call errors → classify). The scripts are at `../src/poc/`, so calls look like:
```bash
python ../src/poc/call_errors.py <sample>.cons.bam filges_reference.fasta <label> -o errors_<label>.csv
```
Result: an IDT-vs-Sigma leave-one-batch-out accuracy — your first real number.

### B4. Then Lietard + cross-method (photolithographic)
Download the 3 Lietard files (use the ENA script you got for PRJEB43002), then
follow **`../src/poc/lietard_runbook.md`** (paired-end → Bowtie2 to
`lietard_reference_panel.fa.gz` → call errors). Same `call_errors.py`.
The cross-method comparison and its caveats are at the bottom of that runbook.

---

## What's in this bundle

```
HOW_TO_RUN.md            <- you are here
README.md                project overview + VS Code notes
requirements.txt         Python packages for Mode A
Chapter1..4 .md          the four corrected chapters
figures/                 all 15 standardized figures
data/                    <- everything for the REAL pipeline (Mode B)
  download_filges_subset.sh   18 Filges FASTQ URLs
  filges_labels.csv           SRR -> manufacturer/batch/replicate
  filges_reference.fasta      Filges designed oligo (variant1)
  lietard_reference_panel.fa.gz   19,794 Lietard designed sequences
src/
  figstyle.py            shared figure style
  gen_ch*_figs.py        regenerate chapter figures
  poc/
    synth_forensics.py   phenotypes + simulator + features + LR/tiers
    run_poc.py           the Mode A demo
    extract_features.py  error-events table -> feature grid
    call_errors.py       BAM -> error-events table (VERIFIED)
    filges_runbook.md    Filges real-data steps
    lietard_runbook.md   Lietard real-data steps + cross-method
    RUNBOOK.md           general real-data notes
    README.md            poc overview
```

## Troubleshooting (the things that already bit us)
- **`python` not recognized (Windows):** use `py`, or the full path to python.exe.
  Always install and run with the *same* interpreter (`python -m pip install …`).
- **`&&` errors / `source … activate` fails (Windows PowerShell):** those are
  Linux syntax. In Mode A you don't need them; in Mode B you're in WSL where they work.
- **`ModuleNotFoundError` in Mode A:** you're in the wrong folder or wrong
  interpreter — `cd` to the project root and re-select the interpreter.
- **bioinformatics tool "command not found":** you're in PowerShell, not the WSL
  terminal, or you forgot `conda activate dna`.
- **UMI pattern mismatch (Filges):** check an actual read (`zcat file.fastq.gz | head`)
  and adjust — see filges_runbook step 3.
```
