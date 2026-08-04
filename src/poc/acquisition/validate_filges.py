#!/usr/bin/env python3
"""
validate_filges.py - Filges (Clin Chem 67:1384) signatures + manufacturer
attribution across up to 4 manufacturers (IDT, Sigma, Eurofins, BioSearch),
all desalted variant 1. UMI consensus families >= MINFAM (set when acquiring).

  Classifier A (rigorous): IDT vs Sigma, leave-one-BATCH-out (3 batches each).
  Classifier B (separability): all manufacturers, leave-one-RUN-out multiclass.
     NB EF/BS have a single batch each, so B is a replicate-level separability
     check, not a batch-generalisation test - stated explicitly.
Run from src/poc/acquisition/ after filges_acquire.sh.
"""
import os, sys, glob
import numpy as np, pandas as pd
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,".."))
from extract_features import build_real_dataset, FEATURE_NAMES
OUT=os.path.join(HERE,"filges_out")
LAB=pd.read_csv(os.path.join(HERE,"..","..","..","data","filges_labels.csv"))
manu_of=dict(zip(LAB.Run,LAB.manufacturer_short)); batch_of=dict(zip(LAB.Run,LAB.batch.astype(str)))
AGG=pd.read_csv(os.path.join(OUT,"filges_aggregates.tsv"),sep="\t",names=["batch_id","aligned_bases","n_molecules"])
aligned_bases=dict(zip(AGG.batch_id,AGG.aligned_bases)); n_molecules=dict(zip(AGG.batch_id,AGG.n_molecules))
files=sorted(glob.glob(os.path.join(OUT,"errors_SRR*.csv")))
if not files: sys.exit("No errors_SRR*.csv - run filges_acquire.sh first.")
events=pd.concat((pd.read_csv(f) for f in files),ignore_index=True)
runs=sorted(events.batch_id.unique())
print("[loaded] %d runs, %d error rows\n"%(len(runs),len(events)))

# ---- 1. per-manufacturer profile ----
print("=== Filges profile (per manufacturer, pooled; families as acquired) ===")
print("  %-10s %5s %8s %8s %8s %9s %8s %8s"%("manu","runs","del%","ins%","sub%","del/sub","5'del%","intact%"))
order=["IDT","Sigma","Eurofins","BioSearch"]
for manu in [m for m in order if m in set(manu_of.get(r) for r in runs)]:
    mruns=[r for r in runs if manu_of.get(r)==manu]
    ev=events[events.batch_id.isin(mruns)]
    ab=sum(aligned_bases.get(r,0) for r in mruns); nm=sum(n_molecules.get(r,0) for r in mruns)
    tc=ev.error_type.value_counts(); d,i,s=tc.get("del",0),tc.get("ins",0),tc.get("sub",0)
    dels=ev[ev.error_type=="del"]; five=100*(dels.position<50).mean() if len(dels) else float("nan")
    intact=100*(1-ev.molecule_id.nunique()/max(nm,1))
    print("  %-10s %5d %8.3f %8.3f %8.3f %9.1f %8.0f %8.1f"%(manu,len(mruns),100*d/ab,100*i/ab,100*s/ab,d/max(s,1),five,intact))
print("  (Filges: deletion-dominated; substitution ~0.008-0.025%/nt at families>=10)\n")

def run_clf(X,y,groups,chance,title,shuffle=True):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import LeaveOneGroupOut, cross_val_predict
    clf=RandomForestClassifier(n_estimators=400,min_samples_leaf=2,random_state=0)
    pred=cross_val_predict(clf,X,y,groups=groups,cv=LeaveOneGroupOut())
    acc=(pred==y).mean()
    print("%s\n  accuracy = %.3f   (chance = %.3f)"%(title,acc,chance))
    labs=sorted(np.unique(y)); cm=pd.DataFrame(0,index=labs,columns=labs)
    for t,p in zip(y,pred): cm.loc[t,p]+=1
    print("  confusion (rows=true, cols=pred):"); print(cm.to_string())
    if shuffle:
        accs=[]
        for seed in range(50):
            rng=np.random.default_rng(seed); ys=rng.permutation(y)
            ps=cross_val_predict(clf,X,ys,groups=groups,cv=LeaveOneGroupOut())
            accs.append((ps==ys).mean())
        accs=np.array(accs); pval=(accs>=acc).mean()
        print("  label-shuffle (50 perms): mean=%.3f  max=%.3f  permutation p=%.3f"%(accs.mean(),accs.max(),pval))
    print()

# ---- 2A. IDT vs Sigma, leave-one-BATCH-out (rigorous) ----
sub=[r for r in runs if manu_of.get(r) in ("IDT","Sigma")]
ev2=events[events.batch_id.isin(sub)]
X,y,gr=build_real_dataset(ev2,aligned_bases,n_molecules,{r:manu_of[r] for r in sub})
run_clf(X,y,np.array([batch_of[g] for g in gr]),0.5,
        "=== 2A. IDT vs Sigma - leave-one-BATCH-out (rigorous, batch-generalising) ===")

# ---- 2B. all manufacturers, leave-one-RUN-out (separability) ----
manus=set(manu_of.get(r) for r in runs)
if len(manus)>=3:
    X,y,gr=build_real_dataset(events,aligned_bases,n_molecules,{r:manu_of[r] for r in runs})
    run_clf(X,y,gr,1.0/len(manus),
            "=== 2B. %d-manufacturer - leave-one-RUN-out (separability; EF/BS single-batch) ==="%len(manus))
