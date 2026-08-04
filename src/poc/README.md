# Synthesis-Method Attribution — Proof-of-Concept Pipeline

Reference implementation for **Chapter 4**: attribute the *synthesis method* of a
DNA product from its **error phenotype** (the "detect" leg of delay/detect/defend).
This is a **detection/attribution** tool. It performs no synthesis and gives no
evasion guidance.

## What's here
- `synth_forensics.py` — library:
  - `PHENOTYPES` — per-method error parameters taken from the published primary
    studies (Masaki 2022, Filges 2021, Lietard 2021, Palluk 2018), plus a
    **predicted** OpenIDS-DIY phenotype (column chemistry with the capping step
    omitted → suppressed G→A + elevated insertions).
  - `simulate_batch()` — emits one error-profile feature vector per synthesis
    *batch*. In a real deployment this is replaced by feature extraction from a
    UMI-consensus error table; the vector layout is identical.
  - `build_dataset()`, `FEATURE_NAMES`, `lr_to_tier()`.
- `run_poc.py` — end-to-end driver: leave-batch-out classification, calibration
  (ECE), exclusion / likelihood-ratio output, four-tier mapping, a DIY-vs-commercial
  noise sweep, and a **label-shuffle negative control**. Writes `fig4_6_poc.png`.

## Real vs simulated
- **Real:** the pipeline (features, leakage-aware CV, calibration, LR/tiers,
  controls). Runs unchanged on real UMI-consensus error tables.
- **Simulated (demo only):** the input error profiles, drawn from the published
  per-method values above. The **binding constraint** for real use is a labelled
  reference library from deposited product-sequence data (DDBJ/SRA/ENA behind
  Masaki, Lietard, Filges) — not this simulator.

## Run
```
pip install numpy scikit-learn matplotlib scipy
python run_poc.py
```

## Next step (to make it real)
Replace `simulate_batch()` with a loader that computes the six-family feature
vector from UMI-consensus error tables of the public deposits, split **by batch**
(never by read). Then the reported accuracy/ECE/LR become measurements, not
demonstrations.
