#!/usr/bin/env python3
"""
validate_lietard.py - reproduce Lietard et al. 2021 (NAR 49:6687) photolithographic
signatures from the reprocessed (overlap-merged, mapq>=30) events.

  Lietard headline (67-mer library): DELETION-DOMINATED (del 4.65%, ins 0.58%,
  sub 0.97% per bp); dominant substitution is G->T (not column's G->A), 0.31-0.32%
  uncapped falling to 0.07% with capping. Position/array-dependent (spatial).
Run from src/poc/acquisition/ after lietard_acquire.sh.
"""
import os, glob, sys
import pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "lietard_out")
AGG = {}
for l in open(os.path.join(OUT, "lietard_aggregates.tsv")):
    p = l.split(); AGG[p[0]] = (p[1], int(p[2]), int(p[3]))   # run -> (cond, aligned_bases, n_mol)

def load(run):
    ev = pd.read_csv(os.path.join(OUT, f"errors_{run}.csv"))
    return ev[~((ev.error_type == "ins") & (ev.position < 0))]   # defensive flank drop

def rate(ev, ab, **sel):
    m = pd.Series(True, index=ev.index)
    for k, v in sel.items(): m &= (ev[k] == v)
    return 100.0 * int(m.sum()) / ab

print("=== EXPERIMENT: photolithographic error profile (per bp) ===")
print("  %-10s %8s %8s %8s %9s %8s %8s %9s" %
      ("cond","del%","ins%","sub%","del/sub","G->T%","G->A%","GT/GA"))
GT = {}
for run, (cond, ab, nm) in AGG.items():
    ev = load(run)
    d = rate(ev, ab, error_type="del"); i = rate(ev, ab, error_type="ins"); s = rate(ev, ab, error_type="sub")
    gt = rate(ev, ab, error_type="sub", ref_base="G", alt_base="T")
    ga = rate(ev, ab, error_type="sub", ref_base="G", alt_base="A")
    GT[cond] = gt
    print("  %-10s %8.3f %8.3f %8.3f %9.1f %8.3f %8.3f %9.1f"
          % (cond, d, i, s, d/max(s,1e-9), gt, ga, gt/max(ga,1e-9)))
print("  Lietard:   del=4.65   ins=0.58   sub=0.97   (G->T dominant; G->T >> G->A)\n")

print("=== capping -> G->T (Lietard: 0.31% uncapped -> 0.07% capped) ===")
if "normal" in GT and "capped" in GT:
    print("  normal(uncapped) G->T = %.3f%%   capped G->T = %.3f%%   fold = %.1fx  (paper ~4.5x)"
          % (GT["normal"], GT["capped"], GT["normal"]/max(GT["capped"],1e-9)))
else:
    print("  (need both 'normal' and 'capped' runs)")
print("  PASS = deletion-dominated, G->T >> G->A, and capping lowers G->T.")
