# DIY and benchtop DNA synthesis: a biosecurity assessment and a calibrated route-exclusion method

**Author:** Olena Didenko  
**Preprint:** pending IBBIS infohazard review  
**Zenodo deposit (draft):** https://doi.org/10.5281/zenodo.22014124

---

## What this repository contains

Code and data supporting the synthesis-route attribution analysis in the paper.

The paper assesses eight synthesis routes across technical and governance dimensions, evaluates whether input controls and jurisdictional mandates are durable, and develops a method for inferring synthesis process from the error signature of sequenced product — attribution after the fact rather than prevention at the point of order.

This repository holds the proof-of-concept implementation of that attribution method and the reference data required to reproduce it.

---

## Repository structure

```
data/               Reference sequences and metadata for the four co-processed datasets
figures/            Article figures (PNG)
src/
  poc/              Attribution analysis: error calling, feature extraction, classifier training,
                    leave-one-run-out validation, calibration, and reference atlas build
  figstyle.py       Shared figure style module
  gen_fig1_7.py     Cost-per-base trajectory figure
requirements.txt    Python dependencies
```

---

## Datasets

The four co-processed datasets are public:

| Dataset | Accession | Synthesis process |
|---------|-----------|-------------------|
| Filges et al. | PRJNA727098 | Column (commercial) |
| Masaki et al. | DRA013805 | Photolithographic |
| Lietard et al. | PRJEB43002 | Electrochemical array |
| Gimpel et al. | PRJEB65931 | Inkjet array |

Acquisition scripts for each are in `src/poc/acquisition/`. The Filges dataset is large; `data/download_filges_subset.sh` downloads only the subset used in the paper.

An external held-out check used the Yeom SHIFT dataset, provided directly by the authors. It is not publicly available and is not redistributed here.

---

## Reproducing the attribution results

See `src/poc/README.md` for the full runbook.

The short version:

```bash
pip install -r requirements.txt

# 1. Acquire raw reads (or use pre-built atlas)
bash src/poc/acquisition/<dataset>_acquire.sh

# 2. Call errors against reference
python src/poc/call_errors.py

# 3. Extract 16-feature error vector per run
python src/poc/extract_features.py

# 4. Build reference atlas
python src/poc/build_reference_atlas.py

# 5. Run leave-one-run-out classifier
python src/poc/train_multiclass_real.py

# 6. Calibration analysis
python src/poc/calibration_lr.py
```

Pre-built outputs (reference atlas, classifier results, calibration results) are in `src/poc/reference_library/`.

---

## Status

The Zenodo deposit and this repository are in draft/private status pending IBBIS infohazard review. The record will be made public once IBBIS clears the manuscript.

---

## Citation

Didenko, O. (2026). Do-it-yourself and benchtop DNA synthesis: a biosecurity assessment and a calibrated route-exclusion method. Zenodo. https://doi.org/10.5281/zenodo.22014124
