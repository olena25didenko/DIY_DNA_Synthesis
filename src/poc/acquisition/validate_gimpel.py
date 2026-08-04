#!/usr/bin/env python3
"""
validate_gimpel.py - Gimpel et al. 2023 (Nat Commun 14:6026) electrochemical vs
material-deposition, GCall pool. Reprocessed (overlap-merge, mapq>=30) events.

  Paper: electrochemical (Genscript/CustomArray) mean deletion 1.35%/nt with a
  5'-ward positional gradient; material deposition (Twist) 0.06%/nt, flat. Both:
  substitutions dominated by PCR/sequencing (no UMI here) - a SHARED confound
  that does not discriminate; the DELETION rate is the class signal.
  Caveat: our overlap-merge + MAPQ/length filters undercount the heavily-deleted
  electrochemical tail, so absolute del% is a lower bound; the class RATIO holds.
Run from src/poc/acquisition/ after gimpel_acquire.sh.
"""
import os, glob
import pandas as pd, numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(HERE,"gimpel_out")
agg=pd.read_csv(os.path.join(OUT,"gimpel_aggregates.tsv"),sep="\t",names=["run","cond","ab","nm"])
def load(cond):
    runs=agg[agg.cond==cond].run.tolist()
    ab=int(agg[agg.cond==cond].ab.sum())
    ev=pd.concat([pd.read_csv(os.path.join(OUT,f"errors_{r}.csv")) for r in runs],ignore_index=True)
    return ev[~((ev.error_type=="ins")&(ev.position<0))], ab
def gradient(ev):
    dels=ev[ev.error_type=="del"].copy(); dels["fr"]=dels.position/dels.oligo_len.clip(lower=1)
    h,_=np.histogram(dels.fr,bins=10,range=(0,1))
    payload=h[:9]                                   # exclude 3' constant-primer decile
    return payload.max()/max(payload[0],1), np.polyfit(range(9),payload/payload.sum(),1)[0]
print("=== Gimpel: electrochemical vs deposition (GCall pool) ===")
print("  %-12s %6s %8s %8s %8s %9s %12s"%("process","runs","del%","ins%","sub%","del/sub","5'grad(pk/1st)"))
dr={}
for cond,paper in [("electrochem","1.35"),("deposition","0.06")]:
    sel=agg[agg.cond==cond]
    if sel.empty: print("  %-12s (no runs yet)"%cond); continue
    ev,ab=load(cond)
    if ab<=0: print("  %-12s %6d  (0 reads mapped at MAPQ>=30 - wrong reference?)"%(cond,len(sel))); continue
    tc=ev.error_type.value_counts()
    d,i,s=tc.get("del",0),tc.get("ins",0),tc.get("sub",0); dr[cond]=100*d/ab
    pk,slope=gradient(ev)
    print("  %-12s %6d %8.3f %8.3f %8.3f %9.2f %12.2f  (paper del~%s%%)"%(cond,len(sel),100*d/ab,100*i/ab,100*s/ab,d/max(s,1),pk,paper))
if "electrochem" in dr and "deposition" in dr:
    print("\n  DELETION-RATE class ratio electrochem/deposition = %.1fx   (paper ~23x; our lower bound)"%(dr['electrochem']/max(dr['deposition'],1e-9)))
print("  PASS = electrochem deletions >> deposition deletions, and electrochem shows a 5'-ward gradient (pk/1st>1).")
