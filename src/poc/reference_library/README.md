# Synthesis-route error-signature reference library

A single labelled table of DNA-synthesis error signatures, co-processed from four
independently deposited public datasets through one pipeline with shared
denominators, one consensus definition, and one 16-feature extraction. This is
the artifact Chapter 4's downstream results (cross-chemistry attribution,
calibration, likelihood ratios) depend on.

## What's here

| File | What it is |
|---|---|
| `reference_atlas.csv` | 65 runs × (7 metadata + 16 feature) columns. One row per sequencing run. |
| `DATA_DICTIONARY.md` | Every column defined. |
| `PROVENANCE.csv` | Per-study repository, accession, run IDs, chemistry, run count. |
| `multiclass_results.txt` | Leave-group-out attribution results run on the atlas. |
| `calibration_lr_results.txt` | Calibration (ECE) and exclusion likelihood ratios run on the atlas. |

## Composition (65 runs, 4 chemistry classes)

| route_class | study | n | chemistry |
|---|---|---|---|
| column_phosphoramidite | masaki | 34 | column phosphoramidite, capping-chemistry panel |
| column_phosphoramidite | filges | 24 | column phosphoramidite, 4 vendors |
| photolithographic | lietard | 3 | light-directed (NPPOC) array |
| array_electrochem | gimpel | 2 | electrochemical array (GenScript/CustomArray) |
| array_deposition | gimpel | 2 | material-deposition array (Twist) |

Enzymatic (TdT) is not in the atlas. It's the one class still cited from
published per-step tables (Palluk et al. 2018), not reprocessed from raw reads,
because no suitable UMI-tagged enzymatic product dataset is deposited. Adding it
is the open extension (see the six-week plan, Week 2).

## The shared pipeline (why these runs are comparable)

Each dataset was acquired and reprocessed separately (raw reads → trim → UMI/duplex
consensus → reference-anchored alignment → per-event error call), producing one
`errors_<run>.csv` per run plus a per-study aggregate file of denominators.
`build_reference_atlas.py` then folds all four into the atlas using identical rules:

- **Denominator.** Every per-base rate uses `aligned_bases` (total consensus bases
  aligned for that run) as the denominator. `n_molecules` is the consensus-molecule
  count. Both come from each study's aggregate file, so no rate mixes definitions.
- **Consensus.** `umi_clean` records whether the run had UMI/duplex consensus
  (masaki, filges = True) or not (gimpel, lietard = data-storage pools, no UMI =
  False). For the no-UMI classes, absolute substitution rates carry a shared
  PCR/sequencing confound and the heavily-deleted tail is undercounted, so those
  rows support **class-level** deletion-rate comparison, not absolute-rate claims.
  This is why the headline result is framed as class separation, not per-base
  precision.
- **Features.** The same 16-feature vector is extracted for every run by
  `extract_features._batch_features` (definitions in `DATA_DICTIONARY.md`). No
  per-study feature engineering.

## Rebuild from scratch

Needs only the per-run error CSVs and aggregate files already under
`src/poc/acquisition/` (no raw reads, no network):

```bash
cd src/poc
python3 build_reference_atlas.py        # writes reference_library/reference_atlas.csv
python3 multiclass_attribution.py       # leave-group-out attribution
python3 calibration_lr.py               # ECE + exclusion LR + fig4_8
```

The builder is idempotent: it appends and skips run IDs already in the atlas. To
force a clean rebuild, write to a new output directory (set `OUT`) rather than
deleting the committed file.

## Reproduction check (2026-08-04)

Rebuilt fresh from the on-disk error CSVs and compared to the committed atlas:
65 runs, identical labels, **maximum absolute feature difference 0.0** (bit-for-bit).
Downstream reproduced on the rebuild: cross-chemistry attribution balanced
accuracy 1.000 (leave-one-run-out, 4 classes, chance 0.25); calibration
max-confidence ECE 0.053; commercial-column exclusion 100% of non-column runs
give LR < 1 (median LR ≈ 48× inclusion, ≈ 0.047× exclusion).

## Honest limits

- Two of the four classes (array_electrochem, array_deposition) have n = 2 runs
  each; the perfect cross-chemistry separation rests on order-of-magnitude
  deletion-rate gaps, not on large per-class samples. Widening these classes with
  further deposited pools (Antkowiak 2020, Erlich & Zielinski 2017) is the next
  step.
- Within-column vendor attribution is hard under honest leave-one-lot-out and is
  reported as a limitation, not a result (`multiclass_results.txt`, Task B).
- No reference DNA is synthesised here. Every row is deposited public product-read
  data reprocessed for detection/attribution only.
