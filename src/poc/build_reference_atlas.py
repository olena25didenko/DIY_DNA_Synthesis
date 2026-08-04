#!/usr/bin/env python3
"""
build_reference_atlas.py
========================
Co-process the four independently-reprocessed deposited datasets
(Masaki, Filges, Lietard, Gimpel) into ONE labelled error-signature reference
table with SHARED denominators, feature definitions, and consensus method.

Produces the single artifact Chapter 4's downstream results depend on:
    reference_library/reference_atlas.csv

Memory-safe: processes ONE run's error CSV at a time (never concatenates all
studies). Consumes only per-run error-event CSVs already produced on WSL and
the per-run denominators from each study's aggregate file. No raw reads, no
pysam, no synthesis -- deposited data only.
"""
import os, sys, glob
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_features import _batch_features, FEATURE_NAMES  # noqa

ACQ = os.path.join(HERE, "acquisition")
DATA = os.path.abspath(os.path.join(HERE, "..", "..", "data"))
OUT = os.path.join(HERE, "reference_library")
os.makedirs(OUT, exist_ok=True)

def load_denoms():
    ab, nm, gimpel_route = {}, {}, {}
    for line in open(f"{ACQ}/masaki_out/masaki_aggregates.tsv"):
        p = line.split()
        if len(p) >= 3: ab[p[0]] = int(p[1]); nm[p[0]] = int(p[2])
    for line in open(f"{ACQ}/filges_out/filges_aggregates.tsv"):
        p = line.split()
        if len(p) >= 3: ab[p[0]] = int(p[1]); nm[p[0]] = int(p[2])
    for line in open(f"{ACQ}/lietard_out/lietard_aggregates.tsv"):
        p = line.split()
        if len(p) >= 4: ab[p[0]] = int(p[2]); nm[p[0]] = int(p[3])
    for cl in glob.glob(f"{ACQ}/gimpel_out/*.callog"):
        run = os.path.basename(cl).split(".")[0]
        for line in open(cl):
            if line.startswith("AGGREGATE"):
                p = line.split("\t")
                ab[run] = int(p[2]); nm[run] = int(p[3])
                gimpel_route[run] = ("array_electrochem" if "electro" in p[1] else "array_deposition")
    return ab, nm, gimpel_route

def manifest_for(bid, gimpel_route, mrow, fvendor, lcond):
    if bid.startswith("DRR"):
        r = mrow.get(bid); cap = getattr(r, "capping", "?") if r is not None else "?"
        nc = getattr(r, "noncanonical", "canonical") if r is not None else "canonical"
        sub = cap if nc in ("canonical", "?", None) else f"{cap}/{nc}"
        return "column_phosphoramidite", "masaki", sub, True
    if bid.startswith("SRR"):
        return "column_phosphoramidite", "filges", fvendor.get(bid, "?"), True
    if bid in gimpel_route:
        return gimpel_route[bid], "gimpel", gimpel_route[bid].replace("array_", ""), False
    if bid.startswith("ERR"):
        return "photolithographic", "lietard", lcond.get(bid, "?"), False
    return "unknown", "unknown", "?", False

def run_files():
    for study, d in [("masaki","masaki_out"),("filges","filges_out"),
                     ("lietard","lietard_out"),("gimpel","gimpel_out")]:
        for f in sorted(glob.glob(f"{ACQ}/{d}/errors_*.csv")):
            # gimpel + lietard error CSVs are keyed by condition, not run id -> re-key from filename
            bid = (os.path.basename(f).replace("errors_","").replace(".csv","")
                   if study in ("gimpel", "lietard") else None)
            yield study, f, bid

def main():
    ab, nm, gimpel_route = load_denoms()
    mmeta = pd.read_csv(f"{DATA}/masaki_runs_meta.tsv", sep="\t")
    mrow = {r.batch_id: r for r in mmeta.itertuples()}
    fl = pd.read_csv(f"{DATA}/filges_labels.csv")
    fvendor = dict(zip(fl["Run"], fl["manufacturer_short"]))
    lcond = {}
    for line in open(f"{ACQ}/lietard_out/lietard_aggregates.tsv"):
        p = line.split()
        if len(p) >= 2: lcond[p[0]] = p[1]

    META = ["batch_id","route_class","study","sublabel","umi_clean","n_molecules","aligned_bases"]
    cols = META + list(FEATURE_NAMES)
    path = os.path.join(OUT, "reference_atlas.csv")
    done = set()
    if os.path.exists(path):
        done = set(pd.read_csv(path, usecols=["batch_id"])["batch_id"].astype(str))
    fh = open(path, "a")
    if not done:
        fh.write(",".join(cols) + "\n"); fh.flush()

    RD = {"position":"int32","oligo_len":"int32",
          "error_type":"category","ref_base":"category","alt_base":"category"}
    for study, f, gbid in run_files():
        # figure out batch id cheaply for gimpel (filename); else peek first data row
        if gbid is not None:
            bid = gbid
        else:
            bid = pd.read_csv(f, usecols=["batch_id"], nrows=1)["batch_id"].iloc[0]
        if str(bid) in done:
            print(f"  skip (done) {bid}", flush=True); continue
        ev = pd.read_csv(f, usecols=list(RD)+["molecule_id"], dtype=RD)
        ev["molecule_id"] = pd.factorize(ev["molecule_id"])[0].astype("int32")  # low-mem id
        vec = _batch_features(ev, ab.get(bid, 0), nm.get(bid, 0))
        del ev
        if vec is None:
            print(f"  SKIP {bid} (no features)", flush=True); continue
        rc, st, sub, umi = manifest_for(bid, gimpel_route, mrow, fvendor, lcond)
        row = [bid, rc, st, sub, umi, nm.get(bid,0), ab.get(bid,0)] + [f"{v:.6g}" for v in vec]
        fh.write(",".join(str(x) for x in row) + "\n"); fh.flush()
        print(f"  {st:9s} {bid:16s} {rc:22s} {sub}", flush=True)
    fh.close()

    atlas = pd.read_csv(path)
    print(f"\nWROTE {path}  ({atlas.shape[0]} runs x {len(FEATURE_NAMES)} features)")
    print("\nclass x study composition:\n", atlas.groupby(["route_class","study"]).size().to_string())
    print("\nsublabel composition:\n", atlas.groupby(["route_class","sublabel"]).size().to_string())

if __name__ == "__main__":
    main()
