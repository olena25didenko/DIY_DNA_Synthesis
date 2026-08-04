"""
extract_features.py
===================
Turn REAL per-molecule error calls into the feature vector the classifier
expects (same layout as synth_forensics.FEATURE_NAMES). This is the piece that
replaces simulate_batch() once you have real data.

INPUT (one row per detected error event, after UMI/duplex consensus):
    a pandas DataFrame `events` with columns:
      batch_id     str    synthesis batch / run / manufacturer-lot (the split unit)
      molecule_id  str    consensus molecule (UMI family) id
      position     int    0-based position along the DESIGNED reference oligo
      oligo_len    int    length of the designed reference for this molecule
      error_type   str    'del' | 'ins' | 'sub'
      ref_base     str    A/C/G/T   (reference base at the event)
      alt_base     str    A/C/G/T/'-'  (observed base; '-' for deletion)
      ctx          str    optional: 'homopolymer' | 'gc' | 'other'
    plus a dict `aligned_bases[batch_id] -> total consensus bases aligned`
    (the denominator for per-base rates) and
    `n_molecules[batch_id] -> number of consensus molecules in the batch`.

OUTPUT: X (n_batches x 16), y (method label per batch), groups (batch id),
matching synth_forensics.FEATURE_NAMES exactly, so run_poc.py works unchanged.

You provide `batch_method[batch_id] -> method label` from the study metadata.

This is a SCAFFOLD: the exact column names depend on your upstream caller
(fgbio/UMI-tools consensus + a reference-anchored error caller). Adapt the
`load_events()` reader to your files; the feature math below is method-agnostic.
"""
import numpy as np
import pandas as pd
from synth_forensics import FEATURE_NAMES, SUB_CHANNELS

SUBSTITUTION_KEYS = {("G", "A"): "GtoA", ("G", "T"): "GtoT", ("C", "T"): "CtoT",
                     ("T", "C"): "TtoC", ("A", "G"): "AtoG"}


def _batch_features(ev, aligned_bases, n_molecules):
    """Compute the 16-D feature vector for one batch's error events."""
    n_ev = len(ev)
    if n_ev == 0 or aligned_bases <= 0:
        return None

    # (1) error-type spectrum + log total rate
    counts = ev["error_type"].value_counts()
    d, i, s = (counts.get("del", 0), counts.get("ins", 0), counts.get("sub", 0))
    tot = max(d + i + s, 1)
    total_rate = (d + i + s) / aligned_bases
    f_errtype = [d / tot, i / tot, s / tot, np.log10(max(total_rate, 1e-9))]

    # (2) substitution spectrum (directed), fraction of sub events per channel
    # vectorised (no iterrows): map (ref,alt) -> channel, then value_counts.
    subs = ev[ev["error_type"] == "sub"]
    _cm = {f"{a}>{b}": v for (a, b), v in SUBSTITUTION_KEYS.items()}
    key = (subs["ref_base"].astype(str) + ">" + subs["alt_base"].astype(str)).map(_cm)
    vc = key.value_counts()
    chan = {c: int(vc.get(c, 0)) for c in SUB_CHANNELS}
    ns = max(len(subs), 1)
    f_sub = [chan[c] / ns for c in SUB_CHANNELS]

    # (3) positional gradient: deletion rate vs normalised 5'->3' position
    dels = ev[ev["error_type"] == "del"].copy()
    if len(dels) > 20:
        dels["np"] = dels["position"] / dels["oligo_len"].clip(lower=1)
        hist, edges = np.histogram(dels["np"], bins=10, range=(0, 1))
        centers = (edges[:-1] + edges[1:]) / 2
        slope = np.polyfit(centers, hist / max(hist.sum(), 1), 1)[0]
    else:
        slope = 0.0
    f_pos = [slope]

    # (4) truncation ladder: per-molecule deletion count -> n-1 / n-2 structure
    per_mol_del = ev[ev["error_type"] == "del"].groupby("molecule_id").size()
    n1 = (per_mol_del == 1).sum()
    n2 = (per_mol_del == 2).sum()
    n1_frac = n1 / max(len(per_mol_del), 1)
    decay = n2 / max(n1, 1)
    f_trunc = [n1_frac, decay]

    # (5) context conditioning (needs ctx column; else neutral 1.0/0.0)
    if "ctx" in ev.columns:
        hp = (ev["ctx"] == "homopolymer").mean()
        gc = (ev["ctx"] == "gc").mean()
        homopolymer_enrich = hp / max((1 - hp), 1e-3)
        gc_effect = gc
    else:
        homopolymer_enrich, gc_effect = 1.0, 0.0
    f_ctx = [homopolymer_enrich, gc_effect]

    # (6) intra-molecule correlation: dispersion of errors-per-molecule
    per_mol = ev.groupby("molecule_id").size()
    mean = per_mol.mean() if len(per_mol) else 0.0
    var = per_mol.var(ddof=0) if len(per_mol) else 0.0
    intra_corr = (var - mean) / max(mean, 1e-3)   # >0 => over-dispersed (clustered)
    f_intra = [np.clip(intra_corr, -1, 5)]

    vec = f_errtype + f_sub + f_pos + f_trunc + f_ctx + f_intra
    assert len(vec) == len(FEATURE_NAMES)
    return np.array(vec, dtype=float)


def build_real_dataset(events, aligned_bases, n_molecules, batch_method):
    """events: DataFrame; aligned_bases/n_molecules/batch_method: dicts keyed by batch_id."""
    X, y, groups = [], [], []
    for bid, ev in events.groupby("batch_id"):
        vec = _batch_features(ev, aligned_bases.get(bid, 0), n_molecules.get(bid, 0))
        if vec is None:
            continue
        X.append(vec); y.append(batch_method[bid]); groups.append(bid)
    return np.array(X), np.array(y), np.array(groups)


def load_events(path):
    """Adapt to your consensus error-caller output (CSV/Parquet)."""
    return pd.read_parquet(path) if path.endswith(".parquet") else pd.read_csv(path)


if __name__ == "__main__":
    # Wire real data into the SAME classifier used in run_poc.py:
    #   events = load_events("consensus_errors.parquet")
    #   X, y, groups = build_real_dataset(events, aligned_bases, n_molecules, batch_method)
    #   ... then feed X, y, groups to the GroupKFold classifier block in run_poc.py.
    print("Scaffold. Fill load_events() + the four dicts from your study metadata, "
          "then reuse the classifier in run_poc.py. Split by batch, never by read.")
