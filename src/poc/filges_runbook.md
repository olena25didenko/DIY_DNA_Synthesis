# FILGES REAL-DATA RUNBOOK (IDT vs Sigma, column phosphoramidite)

Goal: take the 18 downloaded FASTQs to a real IDT-vs-Sigma classification with
leave-one-batch-out validation. Run in **WSL/Linux/Mac** (the bioinformatics
tools don't run natively in Windows PowerShell).

Files you already have:
- `download_filges_subset.sh`  — fetches the 18 runs
- `filges_labels.csv`          — Run -> manufacturer/batch/replicate
- `filges_reference.fasta`     — the designed oligo (use `variant1`)
- `call_errors.py`             — BAM -> error-events table (VERIFIED)
- `extract_features.py`        — events -> 16-feature grid
- `run_poc.py` / `synth_forensics.py` — the classifier

Which steps are verified vs standard:
- ✅ VERIFIED here: `call_errors.py` (tested on a synthetic alignment).
- 🔧 STANDARD but not tested in-sandbox: trimming, UMI consensus, alignment
  (ordinary tools; the one thing to check is the UMI pattern — see step 3).

---

## 1. Tools (one-time, via conda/mamba in WSL)
```bash
conda create -n filges -c bioconda -c conda-forge \
    fastp bwa samtools umi_tools fgbio python=3.11 pysam pandas scikit-learn numpy matplotlib -y
conda activate filges
```
(Alternative to umi_tools+fgbio: the Ståhlberg lab's purpose-built
**UMIErrorCorrect** — `pip install umierrorcorrect` — designed for exactly this
SiMSen-Seq data; it does UMI grouping + consensus + reference mapping in one.)

## 2. Download
```bash
sh download_filges_subset.sh          # 18 x ~40 MB
```

## 3. Check the UMI/read layout FIRST (don't skip)
```bash
zcat SRR14416340.fastq.gz | head -8
```
From the supplement the universal forward primer is
`...CGATCT [12-nt UMI] ATGGGAAAGAGTGTCC [target]`. Confirm where the 12-nt UMI
sits in the actual read; adjust the `--bc-pattern` below to match. This is the
step most likely to need tweaking on real data.

## 4. Per-sample: trim -> extract UMI -> align -> consensus -> call errors
Run this loop over the 18 SRR ids (use `filges_labels.csv` for the batch label):
```bash
REF=filges_reference.fasta
bwa index $REF
while IFS=, read -r RUN MANU _rest; do
  [ "$RUN" = "Run" ] && continue                      # skip header
  # 3a. quality/adapter trim
  fastp -i ${RUN}.fastq.gz -o ${RUN}.trim.fastq.gz -w 4 -j /dev/null -h /dev/null
  # 3b. move the 12-nt UMI into the read name (ADJUST bc-pattern to step 3)
  umi_tools extract --bc-pattern=NNNNNNNNNNNN \
      -I ${RUN}.trim.fastq.gz -S ${RUN}.umi.fastq.gz
  # 3c. align to the designed oligo
  bwa mem -t4 $REF ${RUN}.umi.fastq.gz | samtools sort -o ${RUN}.sorted.bam
  samtools index ${RUN}.sorted.bam
  # 3d. UMI consensus (removes sequencing error; keeps synthesis error)
  fgbio GroupReadsByUmi -i ${RUN}.sorted.bam -o ${RUN}.grouped.bam -s adjacency -t RX
  fgbio CallMolecularConsensusReads -i ${RUN}.grouped.bam -o ${RUN}.cons.unmapped.bam -M 3
  samtools fastq ${RUN}.cons.unmapped.bam | bwa mem -t4 $REF - \
      | samtools sort -o ${RUN}.cons.bam ; samtools index ${RUN}.cons.bam
  # 3e. call errors (VERIFIED script) -> one events CSV per run
  python call_errors.py ${RUN}.cons.bam $REF ${RUN} -o errors_${RUN}.csv --region variant1
done < filges_labels.csv
```
> If you use **UMIErrorCorrect** instead, run it per FASTQ against `$REF`; it
> outputs consensus + a mapped BAM you can feed straight to `call_errors.py`.

## 5. Combine events -> feature grid -> classify (leave-one-BATCH-out)
```python
import pandas as pd, glob
from extract_features import build_real_dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut, cross_val_predict

lab = pd.read_csv("filges_labels.csv")
meta = {r.Run: (r.manufacturer_short, r.batch) for r in lab.itertuples()}

events = pd.concat([pd.read_csv(f) for f in glob.glob("errors_SRR*.csv")], ignore_index=True)
# denominators from call_errors.py stdout (the AGGREGATE lines), or recompute:
aligned_bases = events.groupby("batch_id").size()*0  # fill from AGGREGATE lines
n_molecules   = {b: events[events.batch_id==b].molecule_id.nunique() for b in events.batch_id.unique()}
batch_method  = {b: meta[b][0] for b in events.batch_id.unique()}   # IDT / Sigma
# (paste aligned_bases from the AGGREGATE stdout lines into a dict)

X, y, groups_run = build_real_dataset(events, aligned_bases, n_molecules, batch_method)
# group for CV = synthesis BATCH (1/2/3), so we leave a whole batch out:
batch_of_run = {b: meta[b][1] for b in events.batch_id.unique()}
groups = [batch_of_run[b] for b in groups_run]   # align order to build_real_dataset output

clf = RandomForestClassifier(n_estimators=400, min_samples_leaf=2, random_state=0)
pred = cross_val_predict(clf, X, y, groups=groups, cv=LeaveOneGroupOut(), method="predict")
acc = (pred == y).mean()
print("IDT-vs-Sigma leave-one-batch-out accuracy:", round(acc*100,1), "%  (chance 50%)")
```

## 6. Read the result honestly
- **>50%** and stable across the 3 held-out batches → a real, batch-generalising
  manufacturer signal in the error phenotype. That's a genuine finding.
- **~50%** → no manufacturer signal survives batch effects at this purity/variant.
  Also a finding (and consistent with "batch effect can exceed manufacturer",
  Filges' own conclusion).
- Always run the **label-shuffle** control (shuffle `y`, expect ~chance).

## Known messy-data snags to expect
- UMI pattern mismatch (step 3) — the #1 thing to fix.
- Low consensus depth on some runs (drop runs with too few consensus molecules).
- Primer-region errors are under-measured (primers select against them) — if
  results look odd, restrict error-calling to the insert region (positions
  ~18-80 of `variant1`) rather than the full oligo.
