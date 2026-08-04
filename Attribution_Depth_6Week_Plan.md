# Six-Week Plan — Deepening the Synthesis-Route Attribution Core

**Goal:** turn the attribution framework from a *specification with a proof-of-concept* into a *calibrated, published methods contribution* (target: a short bioRxiv methods preprint + a clean, citable repository), using **already-deposited public data only**. The collaborator-OpenIDS experiment and IBBIS infohazard review are deliberately parked for now.

**Why this workstream:** it is the project's single most novel and defensible contribution — no published method fingerprints the synthesis chemistry from the error phenotype — and it is the output most likely to outlive the fellowship.

---

## Week-by-week

**Week 1 — Calibration & likelihood ratios (✅ started, first result in hand).**
Convert the classifier's outputs into calibrated evidence. *Done:* out-of-fold calibration on the 65-run atlas — 4-class balanced accuracy 1.00 with max-confidence **ECE 0.053**; the exclusion contrast (commercial column vs not) is well-calibrated (**ECE 0.048**) and well-powered — true-column runs give a median likelihood ratio ≈ **48×** (inclusion), non-column runs ≈ **0.047×** (exclusion), with **100% exclusion power** (every non-column run yields LR < 1 against "commercial column"). New Figure 4.8 produced. *Remaining this week:* expand the atlas with two more deposited datasets (Antkowiak 2020 photolithographic, figshare; Erlich & Zielinski 2017 Twist deposition, ENA PRJEB19305/07) to fatten the non-column classes and enable cross-dataset tests.

**Week 2 — Put the enzymatic class on real data.** Enzymatic (TdT) is currently the one *simulated* class. Attempt Lee et al. 2019 (SRA SRP185459, Nanopore) for a class-level enzymatic deletion/insertion signature; it is no-UMI/high-raw-error, so treat as class-level only and document honestly if it is too noisy. Deliverable: either a real enzymatic atlas row, or a clearly-reported data gap and a recommendation.

**Week 3 — Attribution-resolution index + deamination deconvolution.** (a) Compute ARI ≈ log₂(N_total / N_class) per route, with N_class from the manufacturer-landscape population (array ≈ few firms → high resolving power; column ≈ dozens + installed base → near zero) — turning "value scales inversely with population" into a table of numbers. (b) Subtract the C→T/T→C deamination-damage signature (COSMIC SBS / NMF mutational-signature methods) from the substitution spectra and re-test whether a clean synthesis-specific substitution signal survives — hardening the G→A vs G→T discriminator against a documented confounder.

**Week 4 — Adversarial-laundering degradation + generalization.** (a) Quantify how the likelihood ratio decays toward 1 under (i) the position-local dG-substitution suppression already reproduced and (ii) simulated assembly/error-correction that erases the oligo-level signal — an LR→1 degradation curve that makes the honest scope limit quantitative. (b) Leave-one-*dataset*-out generalization (not just leave-one-run-out) to show the signal transfers across independent studies, not just across runs within one study.

**Week 5 — Consolidate, integrate, verify.** Fold the calibrated numbers and Figure 4.8 into Chapter 4 (§4.3/§4.7); assemble the final figure set and results tables; run a verification pass (re-run end-to-end from raw scripts; sanity-check every number; a label-shuffle control on any new task). Consider a subagent verification of the key claims.

**Week 6 — Preprint + repository, with buffer.** Draft a short bioRxiv methods preprint (framed around exclusion and calibration, not identification); finalise the repository (README, atlas, acquisition and analysis scripts, environment file) so the forensics are reproducible and citable; keep buffer for slippage from the enzymatic (Week 2) risk.

---

## Dependencies, risks, and parked items

- **No external dependency** for Weeks 1, 3–6 — all public deposited data. **Week 2 (enzymatic) is the main risk** (Nanopore/no-UMI noise); mitigation is to report a class-level result or a documented gap.
- **Parked (your call):** the collaborator-OpenIDS product-read experiment and the IBBIS infohazard route. These would convert the *predicted* OpenIDS capping-omission discriminator into a *measured* one — the highest-value single experiment — but have long lead times; revisit if you want to start the request later.
- **Secondary, not in this plan but worth a day each:** the manufacturer-landscape census (own the "8 of 34" claim) and the 2–3 expert interviews (Grass/Gimpel would directly strengthen this chapter).

## Deliverables at the end of six weeks

A calibrated attribution instrument (ECE-reported, likelihood-ratio output, exclusion-first) validated across independent datasets and against a documented laundering attack; an updated Chapter 4 with the calibrated numbers and new figures; a runnable, citable repository; and a short methods preprint ready for bioRxiv.
