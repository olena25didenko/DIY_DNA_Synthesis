#!/usr/bin/env bash
# ============================================================================
# lietard_acquire.sh - Lietard et al. 2021 (NAR 49:6687), ENA PRJEB43002.
# PHOTOLITHOGRAPHIC / light-directed array. 3 runs (paired-end MiSeq 2x150):
#   ERR5265254 normal | ERR5265252 cap-protected | ERR5265253 increased-space
# 19,794 designed 67-mers (data/lietard_reference_panel.fa.gz).
#
# 2x150 fully overlaps the 67-mer -> BBMerge overlap-consensus (removes seq
# error; no UMI here so this matters) -> map to the panel -> call_errors.py.
# CAVEAT: no UMI => class-level only (photolith vs column). The class signal
# (deletion 4.65% vs substitution 0.97%; G->T not G->A) is >>MiSeq floor.
# Deps (synth2): bbmap, bwa, samtools, pysam, pandas.
# Run from src/poc/acquisition/.  smoke: RUNS="ERR5265254" bash lietard_acquire.sh
# ============================================================================
set -uo pipefail
PANEL_GZ=../../../data/lietard_reference_panel.fa.gz
CALLER=../call_errors.py
OUT=lietard_out; mkdir -p "$OUT"; AGG="$OUT/lietard_aggregates.tsv"; : > "$AGG"
REF="$OUT/panel.fa"
[ -s "$REF" ] || zcat "$PANEL_GZ" > "$REF"
samtools faidx "$REF" 2>/dev/null; bwa index "$REF" 2>/dev/null

# run -> (ENA subdir, condition)
sub_of(){ case "$1" in ERR5265252) echo 002;; ERR5265253) echo 003;; ERR5265254) echo 004;; esac; }
cond_of(){ case "$1" in ERR5265252) echo capped;; ERR5265253) echo space;; ERR5265254) echo normal;; esac; }

RUNS="${RUNS:-ERR5265254 ERR5265252 ERR5265253}"
DIAG=1
for RUN in $RUNS; do
  c=$(cond_of "$RUN"); sd=$(sub_of "$RUN")
  echo "==== $RUN ($c) ===="
  for r in 1 2; do
    F="$OUT/${RUN}_$r.fastq.gz"
    if [ ! -s "$F" ]; then
      wget -q --tries=4 --waitretry=6 --read-timeout=120 -O "$F" \
        "https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR526/$sd/$RUN/${RUN}_$r.fastq.gz" || rm -f "$F"
    fi
  done
  if [ ! -s "$OUT/${RUN}_1.fastq.gz" ]; then
    echo "  wget failed -> SRA fallback"; fasterq-dump --split-files -e 4 -O "$OUT" "$RUN" 2>/dev/null && gzip -f "$OUT/${RUN}"_*.fastq
  fi
  [ -s "$OUT/${RUN}_1.fastq.gz" ] || { echo "  download failed $RUN (skip)"; continue; }

  # adapter trim -> overlap-merge (pfilter=1) -> Q30/no-N
  bbduk.sh in1="$OUT/${RUN}_1.fastq.gz" in2="$OUT/${RUN}_2.fastq.gz" \
           out1="$OUT/$RUN.a1.fq" out2="$OUT/$RUN.a2.fq" ref=adapters ktrim=r k=23 mink=11 hdist=1 tpe tbo 2>/dev/null
  bbmerge.sh in1="$OUT/$RUN.a1.fq" in2="$OUT/$RUN.a2.fq" out="$OUT/$RUN.merged.fq" pfilter=1 2>"$OUT/$RUN.bbmerge.log"
  bbduk.sh in="$OUT/$RUN.merged.fq" out="$OUT/$RUN.clean.fq" maxns=0 minavgquality=30 2>/dev/null

  # length-filter merged reads to a 67-mer product window (drops BBMerge
  # concatemer/adapter-readthrough artifacts that align as huge insertions)
  awk -v lo="${MINLEN:-45}" -v hi="${MAXLEN:-75}" 'BEGIN{OFS="\n"}
     {h=$0; getline s; getline p; getline q; L=length(s); if(L>=lo && L<=hi) print h,s,p,q}' \
     "$OUT/$RUN.clean.fq" > "$OUT/$RUN.lenfilt.fq"
  bwa mem -k 15 -T 25 "$REF" "$OUT/$RUN.lenfilt.fq" 2>/dev/null | samtools sort -o "$OUT/$RUN.bam"
  samtools index "$OUT/$RUN.bam"
  if [ "$DIAG" = "1" ]; then
    echo "  merged: $(( $(wc -l < "$OUT/$RUN.clean.fq")/4 ))  len-filtered: $(( $(wc -l < "$OUT/$RUN.lenfilt.fq")/4 ))  mapped(q>=30): $(samtools view -c -q30 "$OUT/$RUN.bam")"
    DIAG=0
  fi

  python "$CALLER" "$OUT/$RUN.bam" "$REF" "lietard_$c" -o "$OUT/errors_$RUN.csv" --min-mapq 30 \
    | awk -F'\t' -v run="$RUN" -v c="$c" '/^AGGREGATE/{print run"\t"c"\t"$3"\t"$4}' >> "$AGG"
  # drop 5'-flank artifact insertions (recorded at position -1; untrimmed leading
  # constant sequence, not synthesis error). Internal insertions are kept.
  awk -F, 'NR==1 || !($5=="ins" && ($3+0)<0)' "$OUT/errors_$RUN.csv" > "$OUT/errors_$RUN.csv.tmp" \
    && mv "$OUT/errors_$RUN.csv.tmp" "$OUT/errors_$RUN.csv"
done
echo; echo "Done. events: $OUT/errors_ERR*.csv ; aggregates(run,cond,aligned_bases,n_mol): $AGG"
echo "Next: python validate_lietard.py"
