# LIETARD RUNBOOK (photolithographic) + cross-method note

Processes the 3 ENA runs (PRJEB43002) into error-events using the designed
panel we recovered from the a-slide/DNA_photolitography_seq repo. Run in WSL.

Files:
- `lietard_reference_panel.fa.gz`  — 19,794 designed 67-nt sequences (the reference)
- `call_errors.py`                 — works unchanged (multi-reference aware)
- `extract_features.py`            — events -> feature grid

Sample decode (from the repo README):
- ERR run with **index 2** = normal 2SZ (standard photolithographic)
- **index 4** = capped 2SZ
- **index 5** = 4SZ (increased cluster spacing)
(confirm which ERR id is which from the ENA `library_name`/`sample_title`.)

## 1. Tools
```bash
conda create -n lietard -c bioconda -c conda-forge \
    cutadapt bowtie2 samtools fastp python=3.11 pysam pandas -y
conda activate lietard
gunzip -k lietard_reference_panel.fa.gz          # -> lietard_reference_panel.fa
```

## 2. Build the Bowtie2 index (short reads to a big panel -> Bowtie2, not bwa)
```bash
bowtie2-build lietard_reference_panel.fa panel
```

## 3. Per sample: merge pairs -> trim -> align -> call errors
The insert is 67 nt and reads are 2x150, so the pairs fully overlap -> merge them
into one accurate read first (this is the paired-end analogue of UMI consensus:
the overlap corrects most sequencing error).
```bash
for ERR in ERR5265252 ERR5265253 ERR5265254; do
  # 3a. merge overlapping pairs (corrects sequencing error in the overlap)
  fastp -i ${ERR}_1.fastq.gz -I ${ERR}_2.fastq.gz --merge \
        --merged_out ${ERR}.merged.fastq.gz -j /dev/null -h /dev/null
  # 3b. trim residual adapter, min len 20 (as in the paper)
  cutadapt -m 20 -o ${ERR}.trim.fastq.gz ${ERR}.merged.fastq.gz > /dev/null
  # 3c. align to the panel
  bowtie2 -x panel -U ${ERR}.trim.fastq.gz --no-unal -p4 \
        | samtools sort -o ${ERR}.bam ; samtools index ${ERR}.bam
  # 3d. call errors (same verified script as Filges)
  python call_errors.py ${ERR}.bam lietard_reference_panel.fa ${ERR} -o errors_${ERR}.csv
done
```

## 4. Sanity check against the paper
Aggregate deletion / insertion / substitution fractions should land near the
paper's numbers (4SZ: ~5.0-5.5% deletion, ~0.16-0.23% insertion, ~0.55-0.60%
mismatch; Fig S5F). If they do, the pipeline is trustworthy. Deletion should
dominate, and the dominant substitution should be **G->T** (vs Filges' G->A) -
that direction difference is the core cross-method signal.

---

## Cross-method comparison: the one caveat that matters

Filges and Lietard are different experiments, so process them **the same way**
for a fair method-vs-method test:

- **Sequencing-error handling differs:** Filges uses UMIs (true consensus);
  Lietard has none (pair-merge only). For the cross-method run, treat both at the
  **merged/consensus-read level** (don't UMI-collapse Filges further) so the
  residual sequencing-error baseline is comparable.
- **Lean on SHAPE, not magnitude:** use error-class *ratios* and the
  substitution *direction* (G->A vs G->T), not absolute rates - the platforms and
  library designs differ too much for absolute rates to be comparable. This is
  exactly Chapter 4's "profile shape, not magnitude" rule.
- **Study = method confound:** with only two studies, a classifier can learn
  "which study" instead of "which chemistry." State this plainly; the honest
  claim is "the phenotypes differ in kind" (which the G->A vs G->T + spatial
  gradient shows), not a headline accuracy.

## Then classify (column vs photolithographic)
Concatenate `errors_*.csv` from both studies, build the feature grid with
`extract_features.build_real_dataset`, label each batch by method
(`column_phosphoramidite` vs `photolithographic`), and group by **study/run** for
CV so leakage is controlled. Report the confusion + a label-shuffle control.
```
