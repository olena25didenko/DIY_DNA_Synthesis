#!/usr/bin/env bash
# ============================================================================
# filges_acquire.sh - Filges et al. 2021 (Clin Chem 67:1384), SRA PRJNA727098.
# Column phosphoramidite, UMI (SiMSen-Seq). IDT vs Sigma, 3 batches x 3 reps x
# 2 manufacturers = 18 runs, Desalted, variant 1.
# download(+retry/SRA fallback) -> UMIErrorCorrect (ul12,sl16) -> families>=MINFAM
# -> call_errors.py -> events CSV + aggregates.
# Deps (synth2): umierrorcorrect, bwa, samtools, sra-tools, pysam, pandas.
# Run from src/poc/acquisition/.  smoke: RUNS="SRR14416340 SRR14416386" bash filges_acquire.sh
# ============================================================================
set -uo pipefail
LABELS=../../../data/filges_labels.csv
REFALL=../../../data/filges_reference.fasta
CALLER=../call_errors.py
MINFAM="${MINFAM:-3}"
OUT=filges_out; mkdir -p "$OUT"; AGG="$OUT/filges_aggregates.tsv"; : > "$AGG"

REF="$OUT/variant1.fa"
samtools faidx "$REFALL" variant1 > "$REF" 2>/dev/null || sed -n '1,2p' "$REFALL" > "$REF"
samtools faidx "$REF"; bwa index "$REF" 2>/dev/null

RUNS="${RUNS:-$(tail -n +2 "$LABELS" | cut -d, -f1)}"
DIAG=1
for RUN in $RUNS; do
  echo "==== $RUN ===="
  F="$OUT/$RUN.fastq.gz"
  if [ ! -s "$F" ]; then
    url=$(grep "^$RUN," "$LABELS" | awk -F, '{print $NF}')
    wget -q --tries=4 --waitretry=6 --read-timeout=120 -O "$F" "https://$url" || rm -f "$F"
    if [ ! -s "$F" ]; then
      echo "  wget failed -> SRA toolkit fallback"; rm -f "$F"
      if fasterq-dump --split-spot -e 4 -O "$OUT" "$RUN" 2>/dev/null; then gzip -f "$OUT/$RUN.fastq" 2>/dev/null; fi
    fi
  fi
  [ -s "$F" ] || { echo "  download failed $RUN (skip)"; continue; }

  CB=$(ls "$OUT/$RUN/"*consensus_reads.bam 2>/dev/null | head -1)
  if [ -z "$CB" ]; then
    mkdir -p "$OUT/$RUN"
    run_umierrorcorrect.py -r1 "$F" -ul 12 -sl 16 -r "$REF" -o "$OUT/$RUN" \
      || { echo "  umierrorcorrect FAILED $RUN"; continue; }
    CB=$(ls "$OUT/$RUN/"*consensus_reads.bam 2>/dev/null | head -1)
  fi
  [ -z "$CB" ] && { echo "  no consensus_reads.bam"; continue; }

  CBF="$OUT/$RUN/${RUN}_cons_ge${MINFAM}.bam"
  samtools view -h "$CB" | awk -v m="$MINFAM" 'BEGIN{FS="\t"} /^@/{print;next}
     {c=$1; sub(/.*Count=/,"",c); sub(/[^0-9].*/,"",c); if(c+0>=m) print}' \
     | samtools view -b -o "$CBF" -
  samtools index "$CBF"
  [ "$DIAG" = "1" ] && { echo "  families>=$MINFAM: $(samtools view -c "$CBF")"; DIAG=0; }

  python "$CALLER" "$CBF" "$REF" "$RUN" -o "$OUT/errors_$RUN.csv" --region variant1 \
    | awk -F'\t' -v r="$RUN" '/^AGGREGATE/{print r"\t"$3"\t"$4}' >> "$AGG"
done
echo; echo "Done (families>=$MINFAM). runs with events: $(ls $OUT/errors_SRR*.csv 2>/dev/null | wc -l)/18"
echo "Next: python validate_filges.py"
