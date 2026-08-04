#!/usr/bin/env bash
# ============================================================================
# gimpel_acquire.sh - Gimpel et al. 2023 (Nat Commun 14:6026), ENA PRJEB65931.
# ELECTROCHEMICAL (Genscript/CustomArray) vs material DEPOSITION (Twist), GCall
# pool (12,472 x 102-nt designs = data/gimpel_gcall_design.fasta). Unaged
# baselines, 2 replicates each.
#   electrochem: ERR12033803 ERR12033807   deposition: ERR12033805 ERR12033809
# 2x150 fully overlaps the 102-mer -> BBMerge overlap-consensus (no UMI ->
# class-level only; the electrochemical del rate ~1.35%/nt vs deposition
# ~0.06%/nt is >20x, far above the MiSeq floor). Run from src/poc/acquisition/.
# ============================================================================
set -uo pipefail
REF_GEN=../../../data/gimpel_gcall_design.fasta        # Genscript (electrochemical) GCall design
REF_TWI=../../../data/gimpel_twist_gcall_design.fasta  # Twist (deposition) GCall design
CALLER=../call_errors.py
OUT=gimpel_out; mkdir -p "$OUT"; AGG="$OUT/gimpel_aggregates.tsv"; : > "$AGG"
for R in "$REF_GEN" "$REF_TWI"; do [ -s "$R" ] && { samtools faidx "$R" 2>/dev/null; bwa index "$R" 2>/dev/null; }; done
declare -A COND=( [ERR12033803]=electrochem [ERR12033807]=electrochem [ERR12033805]=deposition [ERR12033809]=deposition )
declare -A SUB=(  [ERR12033803]=003 [ERR12033807]=007 [ERR12033805]=005 [ERR12033809]=009 )
RUNS="${RUNS:-ERR12033803 ERR12033807 ERR12033805 ERR12033809}"
DIAG=1
for RUN in $RUNS; do
  c=${COND[$RUN]}; sd=${SUB[$RUN]}
  REF=$([ "$c" = deposition ] && echo "$REF_TWI" || echo "$REF_GEN")
  echo "==== $RUN ($c) -> $(basename "$REF") ===="
  [ -s "$REF" ] || { echo "  MISSING reference $REF (skip)"; continue; }
  for r in 1 2; do
    F="$OUT/${RUN}_$r.fastq.gz"
    [ -s "$F" ] || wget -q --tries=4 --waitretry=6 --read-timeout=150 -O "$F" \
      "https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR120/$sd/$RUN/${RUN}_$r.fastq.gz" || rm -f "$F"
  done
  [ -s "$OUT/${RUN}_1.fastq.gz" ] || { echo "  download failed (skip)"; continue; }

  bbduk.sh in1="$OUT/${RUN}_1.fastq.gz" in2="$OUT/${RUN}_2.fastq.gz" \
           out1="$OUT/$RUN.a1.fq" out2="$OUT/$RUN.a2.fq" ref=adapters ktrim=r k=23 mink=11 hdist=1 tpe tbo 2>/dev/null
  bbmerge.sh in1="$OUT/$RUN.a1.fq" in2="$OUT/$RUN.a2.fq" out="$OUT/$RUN.merged.fq" pfilter=1 2>"$OUT/$RUN.bbmerge.log"
  bbduk.sh in="$OUT/$RUN.merged.fq" out="$OUT/$RUN.clean.fq" maxns=0 minavgquality=25 2>/dev/null
  awk -v lo="${MINLEN:-80}" -v hi="${MAXLEN:-118}" 'BEGIN{OFS="\n"}
     {h=$0;getline s;getline p;getline q;L=length(s); if(L>=lo&&L<=hi) print h,s,p,q}' \
     "$OUT/$RUN.clean.fq" > "$OUT/$RUN.lenfilt.fq"
  bwa mem -k 15 -T 25 "$REF" "$OUT/$RUN.lenfilt.fq" 2>/dev/null | samtools sort -o "$OUT/$RUN.bam"
  samtools index "$OUT/$RUN.bam"
  [ "$DIAG" = "1" ] && { echo "  merged:$(( $(wc -l <"$OUT/$RUN.clean.fq")/4 )) lenfilt:$(( $(wc -l <"$OUT/$RUN.lenfilt.fq")/4 )) mapped(q30):$(samtools view -c -q30 "$OUT/$RUN.bam")"; DIAG=0; }

  python "$CALLER" "$OUT/$RUN.bam" "$REF" "gimpel_$c" -o "$OUT/errors_$RUN.csv" --min-mapq 30 > "$OUT/$RUN.callog" 2>&1
  grep '^AGGREGATE' "$OUT/$RUN.callog" | awk -F'\t' -v run="$RUN" -v c="$c" '{print run"\t"c"\t"$3"\t"$4}' >> "$AGG"
  grep -q '^AGGREGATE' "$OUT/$RUN.callog" || { echo "  WARN: no AGGREGATE for $RUN; call_errors tail:"; tail -3 "$OUT/$RUN.callog"; }
  awk -F, 'NR==1 || !($5=="ins" && ($3+0)<0)' "$OUT/errors_$RUN.csv" > "$OUT/errors_$RUN.csv.tmp" \
    && mv "$OUT/errors_$RUN.csv.tmp" "$OUT/errors_$RUN.csv"
done
echo; echo "Done. events: $OUT/errors_ERR*.csv ; aggregates(run,cond,ab,nmol): $AGG"
echo "Next: python validate_gimpel.py"
