# acquisition/ — real-data acquisition & processing (feeds the existing PoC)

These scripts are the concrete implementation of RUNBOOK Parts B–C. They download
the published deposits, produce consensus/aligned BAMs, and call **your existing
`../call_errors.py`** to emit the events CSVs that `../extract_features.py` and
`../run_poc.py` already consume. Nothing in the base PoC is changed.

## Files
| file | arm | notes |
|---|---|---|
| `masaki_acquire.sh` | column, capping-controlled (DDBJ **DRA013805**) | **BBMerge overlap-consensus** (NOT UMI — see below); complete: uses `data/masaki_reference.fasta` + `data/masaki_runs_meta.tsv` |
| `cross_chemistry_acquire.sh` | array (ENA **PRJEB43002**) + electrochemical (ENA **PRJEB65931**) | non-UMI → class-level only; uses `data/lietard_reference_panel.fa.gz` |
| `validate_masaki.py` | — | independent check: capping→G→A ordering + polymerase-independence |

## The one correction vs the old RUNBOOK
Masaki (DRA013805) is **not** UMI-consensus. Their synthesis-vs-sequencing
separation is **BBMerge perfect-overlap paired-end merge (`pfilter=1`) + Q≥40 /
no-N** — a base survives only if R1 and R2 agree exactly. `masaki_acquire.sh`
implements this faithfully; that's what makes your numbers match their published
per-condition rates. (Filges *is* UMI/SiMSen-Seq — that arm is unchanged.)

## Run order
```bash
cd src/poc/acquisition
bash masaki_acquire.sh                     # -> masaki_out/errors_DRR*.csv + masaki_aggregates.tsv
python validate_masaki.py                  # confirms Pac2O G->A ~13x Ac2O (per guanine); Q5~Phusion~ExTaq
python build_masaki_dataset.py --classify  # errors+agg+meta -> X,y,groups (.npz) + leave-run-out capping classifier
bash cross_chemistry_acquire.sh            # -> xchem_out/errors_*.csv  (edit lietard_runs.txt first)
```
`build_masaki_dataset.py` is the RUNBOOK Part D glue: it concatenates the
`errors_DRR*.csv`, reads denominators from `masaki_aggregates.tsv` and condition
labels from `data/masaki_runs_meta.tsv`, and calls
`extract_features.build_real_dataset` to emit `X, y, groups` (saved to
`masaki_out/masaki_dataset.npz`). `--label capping` (default) restricts to the
BTT/I2/TCA background and classifies the capping chemistry (Ac2O / Ac2O_lut /
Pac2O / da7G / a8da7G) leave-run-out — the measured version of the G->A
fingerprint. `--label method` labels all runs `column_phosphoramidite` for later
concatenation with the array/electrochemical arms. `--classify` also runs the
RandomForest+GroupKFold block from `run_poc.py` with a label-shuffle control.

## Scope reminders (unchanged)
- Class-level (column vs array vs electrochemical) is the robust result.
- Within-class (which vendor / DIY-vs-commercial) is not recoverable per-sequence.
- No clean enzymatic UMI dataset exists — a real, reportable gap.
- Detection/attribution only; deposited data only; no synthesis.
