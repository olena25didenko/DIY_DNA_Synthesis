# RUNBOOK — Synthesis-Method Attribution Pipeline

Two parts: **(A)** run the demo (works offline, anywhere), and **(B)** get the real
sequencing data and turn it into a measured classifier. This is a detection/
attribution workflow on published error-profiling data — it involves no synthesis.

---

## PART A — Run the demo (5 minutes, no internet needed)

The demo runs on error profiles simulated from published per-method values, so it
works anywhere — including a laptop with no network.

**1. Get the code.** Everything is in `src/poc/`:
```
synth_forensics.py    # phenotypes + simulator + features + LR/tiers
run_poc.py            # driver: classify, calibrate, exclude, label-shuffle, Fig 4.6
extract_features.py   # scaffold for REAL data (Part C)
README.md
```

**2. Install dependencies** (once):
```bash
python3 -m venv venv && source venv/bin/activate
pip install numpy scikit-learn scipy matplotlib pandas
```

**3. Run it:**
```bash
cd src/poc
python run_poc.py
```

**4. What you'll see** — printed metrics and `fig4_6_poc.png`:
- leave-batch-out accuracy (4 classes) and chance baseline
- calibration ECE
- exclusion: % of non-commercial batches giving LR>1 vs commercial, median LR, tier
- DIY-vs-commercial binary accuracy across a batch-noise sweep
- label-shuffle control accuracy (must fall to ~chance)

**5. Modify it.** In `run_poc.py`, edit `METHODS`, `n_batches`, `n_molecules`. In
`synth_forensics.py`, the `PHENOTYPES` dict holds the per-method parameters (with
the published source on each line). `openids_diy` is the *predicted* DIY class
(suppressed G→A + elevated n−1 deletions from capping omission).

> The demo tests that the *method* behaves correctly. It is NOT evidence about
> nature — the three measured classes are known to differ in kind (Masaki/Filges/
> Lietard/Palluk). Real performance needs Part B.

---

## PART B — Get the real sequences

**This part needs internet + the SRA/ENA/DDBJ tools and won't run in a locked-down
sandbox — use your laptop or HPC.** These are public product-sequence deposits from
the error-profiling papers.

> **Concrete, runnable scripts now live in `acquisition/`** — they implement Parts
> B–C for each dataset and feed your existing `call_errors.py`. The Masaki arm is
> fully complete (reference + 34-run condition map provided). Start there:
> `cd acquisition && bash masaki_acquire.sh && python validate_masaki.py`.

### B1. Accessions (verified)

| Method class | Paper | Archive | Accession | Notes |
|---|---|---|---|---|
| Column phosphoramidite (multi-manufacturer, UMI) | Filges et al. 2021, *Clin Chem* | NCBI SRA | **PRJNA727098** | UMI (SiMSen-Seq); ideal — batch/manufacturer labels |
| Column phosphoramidite (G→A / capping) | Masaki et al. 2022, *Sci Rep* | DDBJ DRA | **DRA013805** | **COMPLETE — see `acquisition/masaki_acquire.sh`.** 34 runs DRR357663–696; reference `data/masaki_reference.fasta` (Fig 2, 48-mer insert); condition map `data/masaki_runs_meta.tsv`. **NOT UMI — uses BBMerge overlap-consensus** (see C2). |
| Photolithographic (light-directed) | Lietard et al. 2021, *NAR* 49:6687 | ENA | **PRJEB43002** | Illumina MiSeq 2×150; no UMI → class-level only; panel in `data/lietard_reference_panel.fa.gz`. `acquisition/cross_chemistry_acquire.sh` |
| Array deposition vs electrochemical | Gimpel et al. 2023 (dt4dds), *Nat Commun* | ENA | **PRJEB65931** | Twist vs CustomArray/GenScript, identical prep; no UMI → class-level. Designs: Zenodo 10.5281/zenodo.8329037 |
| Enzymatic (TdT) | Palluk 2018 (supplement); Lee 2019 (SRA **SRP185459**) | — | gap | **No clean UMI enzymatic dataset exists.** Lee is Nanopore/no-UMI; Palluk = per-step tables only. Reportable gap / collaborator ask. |

### B2. Finding an accession when it isn't listed above
Open the paper → **"Data availability"** section (usually just before References) →
it names the archive + accession. If none is listed, search the archive by the
paper: ENA (`https://www.ebi.ac.uk/ena/browser/text-search?query=<title>`) or NCBI
SRA (`https://www.ncbi.nlm.nih.gov/sra/?term=<title or author>`). Palluk's
per-step error rates live in the **supplementary tables** — usable directly as a
low-resolution reference profile even without raw reads.

### B3. Download the reads
NCBI SRA (Filges) — SRA Toolkit:
```bash
# install sra-tools (conda: conda install -c bioconda sra-tools)
prefetch PRJNA727098                         # or individual SRR ids
fasterq-dump --split-files SRRXXXXXXX -O fastq/
```
ENA mirror (often the fastest — direct FASTQ, no toolkit):
```bash
# browse https://www.ebi.ac.uk/ena/browser/view/PRJNA727098  -> "Generated FASTQ" column
wget <ena_fastq_ftp_url>
```
DDBJ DRA (Masaki):
```bash
# browse https://ddbj.nig.ac.jp/resource/sra-submission/DRA013805
# fetch FASTQ from the DRA/DRR ftp links listed there
```

### B4. Get the DESIGNED reference sequences
Error-calling is relative to the intended oligo, so you need the *designed*
sequences (not a genome). These are in each paper's **supplementary files** (the
oligo/library design tables). Save them as a FASTA of reference targets.

---

## PART C — Reads → error table → feature vectors

The goal: one **feature vector per synthesis batch**, matching `FEATURE_NAMES`.

**C1. QC / adapter trim**
```bash
fastp -i R1.fastq -I R2.fastq -o R1.trim.fastq -O R2.trim.fastq
```

**C2. Consensus (separates synthesis error from sequencing error).**
*Filges is UMI (SiMSen-Seq)* — use `fgbio` or `UMI-tools`. **Masaki is NOT UMI** —
it uses **BBMerge perfect-overlap paired-end merge (`pfilter=1`) + Q≥40 / no-N**;
this is implemented faithfully in `acquisition/masaki_acquire.sh`. (Getting this
wrong — treating Masaki as UMI — will not reproduce its published rates.) fgbio
route for the UMI case:
```bash
# fgbio route (schematic):
fgbio ExtractUmisFromBam ...           # pull the UMI
fgbio GroupReadsByUmi --strategy=adjacency ...
fgbio CallMolecularConsensusReads --min-reads 3 -o consensus.bam
```
Consensus collapses each source molecule to one high-fidelity read → true
synthesis errors are shared across a UMI family, sequencing errors are not.

**C3. Align consensus reads to the designed reference**
```bash
minimap2 -a designed_refs.fasta consensus.fastq | samtools sort -o aln.bam
samtools index aln.bam
```

**C4. Call per-molecule errors vs the designed reference.** Walk each alignment's
CIGAR/MD and emit one row per event (`del`/`ins`/`sub`, position, ref/alt base).
Produce the events table with the columns documented at the top of
`extract_features.py`. (A short pysam script does this; the exact form depends on
your data, which is why it's left as the adapter you fill in.)

**C5. Build the feature matrix**
```python
from extract_features import load_events, build_real_dataset
events = load_events("consensus_errors.parquet")
# from study metadata:
aligned_bases = {...}   # batch_id -> total consensus bases
n_molecules   = {...}   # batch_id -> #consensus molecules
batch_method  = {...}   # batch_id -> 'column_phosphoramidite' | 'photolithographic' | ...
X, y, groups = build_real_dataset(events, aligned_bases, n_molecules, batch_method)
```

**Split by batch, never by read** — Filges shows batch effects can exceed
purification effects, so a read-level split would learn the batch, not the method.

---

## PART D — Run the classifier on real data

Reuse the exact classifier block from `run_poc.py`, but feed it your real
`X, y, groups`:
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupKFold, cross_val_predict
proba = cross_val_predict(
    RandomForestClassifier(n_estimators=400, min_samples_leaf=2, random_state=0),
    X, y, groups=groups, cv=GroupKFold(n_splits=7), method="predict_proba")
# accuracy, ECE, LR(not-commercial), tiers, and the label-shuffle control
# are computed exactly as in run_poc.py.
```
Now the accuracy / ECE / likelihood ratios are **measurements**, not a demo.

**Sanity checks before you believe any number:**
1. Label-shuffle collapses to chance (no leakage).
2. Leave-one-*manufacturer*-out still works (signal is method-level, not lot-level).
3. Start with **exclusion** (rules-out-commercial, Tier 3) — the most defensible
   output, per Crook et al. 2022 (X99/X95).

---

## Guardrails
- Detection/attribution only — no synthesis, ever. Use deposited or
  collaborator-provided data; do not synthesise reference material yourself.
- DIY-class labelled data is scarce; treat the OpenIDS phenotype as a *prediction*
  until you have real OpenIDS product data.
- Report ranges and calibrated LRs, not point calls; laundering (assembly,
  error-correction, non-canonical dG) degrades the signal — state it.
