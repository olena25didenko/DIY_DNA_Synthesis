"""
call_errors.py
==============
Stage C4 of the pipeline: turn a BAM of aligned reads into the per-molecule
error-events table that extract_features.py consumes.

INPUT  : a BAM of **UMI-consensus** reads aligned to the designed reference
         (one read = one source molecule; sequencing error already removed by
         UMI consensus). Plus the reference FASTA and a batch label.
OUTPUT : a CSV with one row per error event, columns exactly as expected by
         extract_features.py:
             batch_id, molecule_id, position, oligo_len, error_type,
             ref_base, alt_base
plus a per-batch summary line (aligned bases, #molecules) you feed into
extract_features.build_real_dataset() as `aligned_bases` / `n_molecules`.

IMPORTANT: run this on CONSENSUS reads, not raw reads. On raw reads every
sequencing error becomes a false "synthesis error". For Filges (SiMSen-Seq)
generate the consensus first with UMIErrorCorrect or umi_tools; see RUNBOOK.

Detection rule (per read, via pysam get_aligned_pairs):
    ref pos present, query pos absent  -> deletion
    query pos present, ref pos absent  -> insertion
    both present, bases differ         -> substitution (ref_base->alt_base)
Consecutive indels are emitted as individual single-base events (so the
truncation-ladder / n-1,n-2 features in extract_features can count them).
"""
import argparse, csv, sys
import pysam


def call_events(bam_path, ref_path, batch_id, out_csv,
                min_mapq=0, region=None):
    ref = pysam.FastaFile(ref_path)
    refnames = ref.references
    refseqs = {r: ref.fetch(r).upper() for r in refnames}

    rows = []
    aligned_bases = 0
    molecules = set()

    with pysam.AlignmentFile(bam_path, "rb") as bam:
        for read in bam.fetch(region=region) if region else bam.fetch(until_eof=True):
            if read.is_unmapped or read.mapping_quality < min_mapq:
                continue
            rname = bam.get_reference_name(read.reference_id)
            rseq = refseqs.get(rname)
            if rseq is None:
                continue
            qseq = read.query_sequence
            if qseq is None:
                continue
            mol = read.query_name
            molecules.add(mol)
            oligo_len = len(rseq)

            pairs = read.get_aligned_pairs()  # list of (qpos, rpos)
            for qpos, rpos in pairs:
                if rpos is not None and qpos is None:
                    rb = rseq[rpos] if rpos < len(rseq) else "N"
                    rows.append([batch_id, mol, rpos, oligo_len, "del", rb, "-"])
                elif qpos is not None and rpos is None:
                    ab = qseq[qpos]
                    rows.append([batch_id, mol, -1, oligo_len, "ins", "-", ab])
                elif rpos is not None and qpos is not None:
                    aligned_bases += 1
                    rb = rseq[rpos] if rpos < len(rseq) else "N"
                    ab = qseq[qpos]
                    if rb != ab and rb in "ACGT" and ab in "ACGT":
                        rows.append([batch_id, mol, rpos, oligo_len, "sub", rb, ab])

    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["batch_id", "molecule_id", "position", "oligo_len",
                    "error_type", "ref_base", "alt_base"])
        w.writerows(rows)

    n_mol = len(molecules)
    n_del = sum(1 for r in rows if r[4] == "del")
    n_ins = sum(1 for r in rows if r[4] == "ins")
    n_sub = sum(1 for r in rows if r[4] == "sub")
    print(f"[{batch_id}] molecules={n_mol}  aligned_bases={aligned_bases}  "
          f"events: del={n_del} ins={n_ins} sub={n_sub}  -> {out_csv}")
    # emit the two denominators extract_features needs
    print(f"AGGREGATE\t{batch_id}\t{aligned_bases}\t{n_mol}")
    return dict(batch_id=batch_id, aligned_bases=aligned_bases, n_molecules=n_mol,
                events=len(rows))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Call synthesis errors from a consensus BAM.")
    ap.add_argument("bam", help="indexed BAM of UMI-consensus reads")
    ap.add_argument("ref", help="reference FASTA (e.g. filges_reference.fasta)")
    ap.add_argument("batch_id", help="label for this batch/run, e.g. IDT_b1")
    ap.add_argument("-o", "--out", default=None, help="output CSV")
    ap.add_argument("--min-mapq", type=int, default=0)
    ap.add_argument("--region", default=None, help="e.g. variant1 to restrict to one reference")
    a = ap.parse_args()
    call_events(a.bam, a.ref, a.batch_id, a.out or f"errors_{a.batch_id}.csv",
                min_mapq=a.min_mapq, region=a.region)
