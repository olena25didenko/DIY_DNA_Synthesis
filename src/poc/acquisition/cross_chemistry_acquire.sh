#!/usr/bin/env bash
# ============================================================================
# cross_chemistry_acquire.sh — the ARRAY and ELECTROCHEMICAL arms, feeding YOUR
# existing src/poc/call_errors.py.
#   Lietard 2021  ENA PRJEB43002  -> photolithographic array
#   Gimpel  2023  ENA PRJEB65931  -> Twist deposition vs CustomArray/GenScript e-chem
#
# CAVEAT (state it in the paper): neither is UMI-tagged, so synthesis error is
# entangled with sequencing error. Use for CLASS-LEVEL (between-chemistry)
# comparison only — valid because the class signal is order-of-magnitude larger
# than the sequencing floor. Do NOT make within-chemistry/per-vendor claims here.
# These are multiplexed libraries: bwa assigns each read to its design, then YOUR
# caller parses errors per read (no UMI consensus available).
# Run from: src/poc/acquisition/
# ============================================================================
set -euo pipefail
CALLER=../call_errors.py
OUT=xchem_out; mkdir -p "$OUT"; AGG="$OUT/xchem_aggregates.tsv"; : > "$AGG"
# deps: bwa, samtools, sra-tools/wget, pysam

# ---- Lietard (photolithographic array) : you already have the panel ----
LIET_REF="$OUT/lietard_panel.fa"
gunzip -c ../../../data/lietard_reference_panel.fa.gz > "$LIET_REF"   # pysam needs plain/bgzipped fasta
samtools faidx "$LIET_REF"; bwa index "$LIET_REF" 2>/dev/null || true
# runs: https://www.ebi.ac.uk/ena/browser/view/PRJEB43002  -> put run ids in lietard_runs.txt
while read -r RUN; do
  [ -z "$RUN" ] && continue
  fasterq-dump --split-files -O "$OUT" "$RUN" || true
  bwa mem "$LIET_REF" "$OUT/${RUN}_1.fastq" "$OUT/${RUN}_2.fastq" 2>/dev/null \
    | samtools sort -o "$OUT/${RUN}.bam"; samtools index "$OUT/${RUN}.bam"
  python "$CALLER" "$OUT/${RUN}.bam" "$LIET_REF" "lietard_${RUN}" -o "$OUT/errors_lietard_${RUN}.csv" \
    | awk -F'\t' '/^AGGREGATE/{print "array_photolith\t"$2"\t"$3"\t"$4}' >> "$AGG"
done < lietard_runs.txt

# ---- Gimpel dt4dds (Twist deposition vs electrochemical) ----
GIMP_REF="$OUT/dt4dds_designs.fa"    # <<FROM ZENODO 10.5281/zenodo.8329037>>: design FASTA
if [ -f "$GIMP_REF" ]; then
  samtools faidx "$GIMP_REF"; bwa index "$GIMP_REF" 2>/dev/null || true
  # runs file: "ERRxxxxxx  twist|customarray|genscript"  (label from the study metadata)
  while read -r RUN PLAT; do
    [ -z "$RUN" ] && continue
    fasterq-dump --split-files -O "$OUT" "$RUN" || true
    bwa mem "$GIMP_REF" "$OUT/${RUN}_1.fastq" "$OUT/${RUN}_2.fastq" 2>/dev/null \
      | samtools sort -o "$OUT/${RUN}.bam"; samtools index "$OUT/${RUN}.bam"
    ROUTE=$([ "$PLAT" = twist ] && echo array_deposition || echo array_electrochem)
    python "$CALLER" "$OUT/${RUN}.bam" "$GIMP_REF" "gimpel_${PLAT}_${RUN}" -o "$OUT/errors_gimpel_${RUN}.csv" \
      | awk -F'\t' -v r="$ROUTE" '/^AGGREGATE/{print r"\t"$2"\t"$3"\t"$4}' >> "$AGG"
  done < gimpel_runs.txt
else
  echo "[skip Gimpel] fetch design FASTA from Zenodo 10.5281/zenodo.8329037 -> $GIMP_REF"
fi
echo "Done. events: $OUT/errors_*.csv ; route+denominators: $AGG"
