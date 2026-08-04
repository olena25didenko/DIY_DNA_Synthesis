#!/usr/bin/env python3
"""
validate_masaki.py - independent check that reprocessed Masaki numbers reproduce
the paper's headline results (Masaki et al. 2022, Sci Rep 12:12095). Run after
masaki_acquire.sh.

  A. Capping drives G->A  (hold activator=BTT, oxidizer=I2, deblock=TCA):
       Pac2O ~1.3%  vs  Ac2O ~0.1%  (~13x). Non-canonical dG analogs, incorporated
       at a FEW G positions, suppress G->A ~10x (7-deaza) / ~50x (8-aza-7-deaza)
       AT THOSE POSITIONS. Suppression is position-local, so it must be read per
       substituted guanine - a whole-insert average dilutes it and hides it.
  B. Error is chemistry-determined, not readout-determined (hold Tet/Ac2O/I2/TCA):
       Q5 ~ Phusion ~ Ex Taq (no significant difference).

G->A whole-insert rate is reported PER GUANINE (paper-comparable): aligned_bases
counts all covered reference positions, so per-guanine rate = per-base rate x
(ref_len / #G). Insert = 12 G in 48 nt -> x4.
"""
import os, statistics as st
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "..", "data")

def load_insert(path):
    name, seq, cur = None, {}, []
    for ln in open(path):
        ln = ln.strip()
        if not ln: continue
        if ln.startswith(">"):
            if name: seq[name] = "".join(cur)
            name, cur = ln[1:].split()[0], []
        else:
            cur.append(ln.upper())
    if name: seq[name] = "".join(cur)
    return seq
REFS = load_insert(os.path.join(DATA, "masaki_reference.fasta"))
INSERT = REFS.get("C1_insert_48mer") or next(iter(REFS.values()))
REF_LEN, G_COUNT = len(INSERT), INSERT.count("G")
GNORM = REF_LEN / G_COUNT
GPOS = [i for i, b in enumerate(INSERT) if b == "G"]
print("[ref] insert length=%d  #G=%d  per-guanine multiplier=%.2f\n" % (REF_LEN, G_COUNT, GNORM))

META = pd.read_csv(os.path.join(DATA, "masaki_runs_meta.tsv"), sep="\t")
AGG  = pd.read_csv(os.path.join(HERE, "masaki_out", "masaki_aggregates.tsv"), sep="\t",
                   names=["batch_id", "aligned_bases", "n_molecules"])
meta = META.merge(AGG, on="batch_id", how="left").set_index("batch_id")

def _errfile(b): return os.path.join(HERE, "masaki_out", "errors_%s.csv" % b)

def rate_GtoA(batch):
    f = _errfile(batch)
    if not os.path.exists(f): return None
    ev = pd.read_csv(f)
    n = len(ev[(ev.error_type == "sub") & (ev.ref_base == "G") & (ev.alt_base == "A")])
    ab = meta.loc[batch, "aligned_bases"]
    if not ab or ab <= 0: return None
    return 100.0 * n / ab * GNORM

def total_err_per_kb(batch):
    f = _errfile(batch)
    if not os.path.exists(f): return None
    ev = pd.read_csv(f); ab = meta.loc[batch, "aligned_bases"]
    return 1000.0 * len(ev) / ab if ab and ab > 0 else None

def ga_by_position(runs):
    """Pooled per-position G->A rate (%) across runs. Analog sits at a few G's,
    so suppression is read position-by-position (a whole-insert avg hides it)."""
    counts = {p: 0 for p in GPOS}; cov = 0.0
    for r in runs:
        f = _errfile(r); ab = meta.loc[r, "aligned_bases"]
        if not os.path.exists(f) or not ab or ab <= 0: continue
        ev = pd.read_csv(f)
        ga = ev[(ev.error_type == "sub") & (ev.ref_base == "G") & (ev.alt_base == "A")]
        vc = ga.position.value_counts()
        for p in GPOS: counts[p] += int(vc.get(p, 0))
        cov += ab / REF_LEN
    if cov <= 0: return None
    return {p: 100.0 * counts[p] / cov for p in GPOS}

def suppression_report(pac_runs, analog_runs, label, target):
    pac = ga_by_position(pac_runs); ana = ga_by_position(analog_runs)
    if not pac or not ana:
        print("  %s: (need Pac2O + %s runs)" % (label, label)); return
    folds = {p: (pac[p] / ana[p] if ana[p] > 0 else float('inf')) for p in GPOS}
    sites = [p for p in GPOS if folds[p] > 3]
    if not sites:
        print("  %s: no position suppressed >3x (analog may be absent)" % label); return
    med = st.median(folds[p] for p in sites)
    detail = ", ".join("pos%d:%.0fx" % (p, folds[p]) for p in sites)
    print("  %s: substituted positions %s -> median %.0fx suppression (paper ~%dx)  [%s]"
          % (label, sites, med, target, detail))

def summarize(mask, fn, lab):
    vals = [v for v in (fn(b) for b in meta[mask].index) if v is not None]
    m = st.median(vals) if vals else float("nan")
    print("  %-34s median=%.4f   n=%d" % (lab, m, len(vals)))
    return m

print("=== EXPERIMENT A: capping -> G->A per guanine [%]  (BTT / I2 / TCA) ===")
bg = (meta.activator == "BTT") & (meta.oxidizer == "I2") & (meta.deblock == "TCA")
ac  = summarize(bg & (meta.capping == "Ac2O_standard") & (meta.noncanonical == "canonical"), rate_GtoA, "Ac2O_standard")
lut = summarize(bg & (meta.capping == "Ac2O_lutidine"), rate_GtoA, "Ac2O_lutidine")
pac = summarize(bg & (meta.capping == "Pac2O") & (meta.noncanonical == "canonical"), rate_GtoA, "Pac2O")
_   = summarize(bg & (meta.noncanonical == "7-deaza-dG"), rate_GtoA, "Pac2O + da7G (insert avg)")
_   = summarize(bg & (meta.noncanonical == "8-aza-7-deaza-dG"), rate_GtoA, "Pac2O + a8da7G (insert avg)")
ok = lambda x: x == x and x > 0
print()
if ok(ac) and ok(pac): print("  RATIO  Pac2O / Ac2O = %.1fx   (paper ~13x, i.e. 0.10 -> 1.33)" % (pac/ac))
print("  non-canonical dG rescue (measured at the substituted G positions):")
pac_runs = list(meta[bg & (meta.capping == "Pac2O") & (meta.noncanonical == "canonical")].index)
da7_runs = list(meta[bg & (meta.noncanonical == "7-deaza-dG")].index)
a8_runs  = list(meta[bg & (meta.noncanonical == "8-aza-7-deaza-dG")].index)
suppression_report(pac_runs, da7_runs, "da7G",   10)
suppression_report(pac_runs, a8_runs,  "a8da7G", 50)
print("  PASS = Pac2O >> Ac2O, and dG analogs suppress ~10x/~50x at their positions.\n")

print("=== EXPERIMENT B: readout-independence, total err/kb  (Tet / Ac2O / I2 / TCA) ===")
bgB = (meta.activator == "Tet") & (meta.capping == "Ac2O_standard") & \
      (meta.oxidizer == "I2") & (meta.deblock == "TCA")
polys = {p: summarize(bgB & (meta.polymerase == p), total_err_per_kb, p) for p in ["Q5", "Phusion", "ExTaq"]}
vals = [v for v in polys.values() if v == v]
if len(vals) >= 2:
    spread = max(vals) / min(vals) if min(vals) > 0 else float("inf")
    print("  spread (max/min) = %.2fx   (PASS if close to 1; paper: ~2.1/kb, no diff)" % spread)
