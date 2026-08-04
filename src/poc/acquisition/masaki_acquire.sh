#!/usr/bin/env bash
# ============================================================================
# masaki_acquire.sh  —  DDBJ DRA013805 (Masaki et al. 2022, Sci Rep 12:12095)
# Downloads + processes column-phosphoramidite, capping-controlled reads and
# feeds them into YOUR existing src/poc/call_errors.py -> events CSVs.
#
# FAITHFUL to Masaki's Methods (this is the important bit):
#   Masaki do NOT use UMI-family consensus. Their synthesis-vs-sequencing
#   separation = BBMerge PERFECT-OVERLAP paired-end merge (pfilter=1) + drop any
#   read with an N or quality < 40. A base survives only if R1 and R2 agree,
#   which removes sequencing error. (The xGen UMI is in the adapter but the
#   published error-parsing is overlap-based.) Reproducing THIS is what makes
#   your numbers match their per-condition rates.
# Run from: src/poc/acquisition/
# ============================================================================
set -euo pipefail
REF=../../../data/masaki_reference.fasta      # provided (Fig 2): C1_insert_48mer + 85mer
META=../../../data/masaki_runs_meta.tsv       # provided: 34-run capping/polymerase map
CALLER=../call_errors.py                    # YOUR existing caller (BAM -> events CSV)
PHIX=phix.fa   # NC_001422 ; ECOLI=U00096.3 (fetch from NCBI or bbduk resources)
ECOLI=ecoli.fa
OUT=masaki_out; mkdir -p "$OUT"; AGG="$OUT/masaki_aggregates.tsv"; : > "$AGG"
# single-seq 48-mer reference for robust alignment/calling (keeps reads off the 85-mer record)
INSERT="$OUT/insert.fa"
samtools faidx "$REF" >/dev/null 2>&1 && samtools faidx "$REF" C1_insert_48mer > "$INSERT" 2>/dev/null || sed -n '1,2p' "$REF" > "$INSERT"
samtools faidx "$INSERT"; bwa index "$INSERT" 2>/dev/null

# deps: bbmap>=38.87 (bbduk.sh,bbmerge.sh), sra-tools, minimap2, samtools, pysam
# default = all 34 runs; smoke-test 2:  RUNS="357675 357681" bash masaki_acquire.sh
RUNS="${RUNS:-$(seq 357663 357696)}"
for n in $RUNS; do RUN="DRR$n"; sub=${RUN:0:6}
  # 1. download (ENA FTP; SRA-toolkit fallback)
  wget -q -P "$OUT" "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/${sub}/${RUN}/${RUN}_1.fastq.gz" \
                    "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/${sub}/${RUN}/${RUN}_2.fastq.gz" \
    || { prefetch "$RUN" && fasterq-dump --split-files -O "$OUT" "$RUN" && gzip "$OUT/${RUN}"_*.fastq; }

  # 2. adapter trim + PhiX/E.coli removal (BBDuk)
  bbduk.sh in1="$OUT/${RUN}_1.fastq.gz" in2="$OUT/${RUN}_2.fastq.gz" \
           out1="$OUT/${RUN}.a1.fq" out2="$OUT/${RUN}.a2.fq" ref=adapters ktrim=r k=23 mink=11 hdist=1 tpe tbo
  # contaminant removal is optional — alignment to C1 already drops non-matching
  # reads. Only run if you've provided phix.fa / ecoli.fa; otherwise pass through.
  refs=""; for r in "$PHIX" "$ECOLI"; do [ -f "$r" ] && refs="${refs:+$refs,}$r"; done
  if [ -n "$refs" ]; then
    bbduk.sh in1="$OUT/${RUN}.a1.fq" in2="$OUT/${RUN}.a2.fq" \
             out1="$OUT/${RUN}.c1.fq" out2="$OUT/${RUN}.c2.fq" ref="$refs" k=31 hdist=1
  else
    cp "$OUT/${RUN}.a1.fq" "$OUT/${RUN}.c1.fq"; cp "$OUT/${RUN}.a2.fq" "$OUT/${RUN}.c2.fq"
  fi

  # 3. perfect-overlap merge (the consensus step) + N/Q40 filter
  bbmerge.sh in1="$OUT/${RUN}.c1.fq" in2="$OUT/${RUN}.c2.fq" out="$OUT/${RUN}.merged.fq" pfilter=1
  bbduk.sh in="$OUT/${RUN}.merged.fq" out="$OUT/${RUN}.clean.fq" maxns=0 minavgquality=40

  # 4. align merged reads to the 48-mer insert -> sorted BAM (what your caller needs)
  bwa mem -k 15 -T 20 "$INSERT" "$OUT/${RUN}.clean.fq" 2>/dev/null | samtools sort -o "$OUT/${RUN}.bam"
  samtools index "$OUT/${RUN}.bam"

  # 5. YOUR caller -> events CSV (restrict to the synthesized 48-mer)
  python "$CALLER" "$OUT/${RUN}.bam" "$INSERT" "$RUN" -o "$OUT/errors_${RUN}.csv" \
    | tee -a "$OUT/masaki_call.log" | awk -F'\t' '/^AGGREGATE/{print $2"\t"$3"\t"$4}' >> "$AGG"
done

echo "Done. Per-run events: $OUT/errors_DRR*.csv ; denominators: $AGG"
echo "method labels + capping/polymerase per run: $META"
echo "Next: python validate_masaki.py   (checks capping->G->A and polymerase-independence)"
echo "Then feed events into extract_features.build_real_dataset + run_poc.py (see RUNBOOK Part D)."
