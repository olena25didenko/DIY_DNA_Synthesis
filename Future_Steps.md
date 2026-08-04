# Future Steps & Further Directions

**Project:** DNA Synthesis Screening Under Device Proliferation — Regime-Conditional Analysis (2026–2030)
**Prepared:** July 2026
**Standing constraint (applies to everything below):** detection and attribution only — no synthesis, ever. Any DIY-class or product-specific material must be collaborator-provided and infohazard-reviewed through IBBIS. No reference DNA is synthesised in-house.

---

## Where the project stands

The four chapters now form a coherent argument. Chapter 1 (regime-conditional TRI) maps seven synthesis routes onto a technology-readiness frame and isolates the TRL 3–6 DIY band as the object of interest. Chapter 2 (control assessment) shows the R0 status quo is porous and asks what residual DIY gap survives a mandatory-benchtop R1. Chapter 3 (cost trajectories) establishes that DIY accessibility is, on the evidence, a one-anchor story (OpenIDS at ~$19.9K with a hedged downward path) and that cheapness alone — DropSynth at ~$3.4K, MAS 2.0 as an open build — does not translate into screening-relevant capability. Chapter 4 (forensic framework) is the empirical core: four deposited datasets reprocessed from raw reads, each method's published error signature reproduced to within ±20%, and a working classifier that separates capping chemistry at 100% and four vendors at 75% (p<0.001).

The single most consequential fact about the project's current state is that Chapter 4's binding constraint — a co-processed, labelled reference library — is now within reach, because the acquisition and processing scripts for all four chemistries already exist and run.

---

## Immediate next steps (0–3 months)

1. **Build the co-processed reference library.** This is the binding constraint named throughout Chapter 4 and the highest-value next action. Reprocess every deposited dataset (Masaki, Filges, Lietard, Gimpel) through a *single* pipeline with shared denominators, feature definitions, and consensus method, then publish the result as a labelled error-signature reference set. Everything downstream — real multiclass attribution, calibrated likelihood ratios, exclusion metrics — is currently blocked on this one artifact.

2. **Replace the simulated four-class demo with real data.** The cross-method classifier (column / photolithographic / enzymatic / OpenIDS-DIY) still runs on profiles seeded from published values. Once the reference library exists, retrain and re-report it on measured error tables, with leave-group-out validation and a label-shuffle control.

3. **Lock down references and numbers across the whole thesis.** Apply the same verification pass to the IBBIS summary and the literature review that was applied to the chapters (OpenIDS2 is 2025 with no itemised public cost; the enzymatic 2030 forecast is the Institute for Progress report by Langenkamp; Yeom 2023 is a general synthesis-vs-sequencing profiler, not electrochemical-specific). This keeps every document internally consistent before external circulation.

## Near-term research directions (3–12 months)

4. **Test the one specified but unmeasured prediction.** OpenIDS omits the capping step, so its product should show a suppressed G→A signature and an elevated n−1 deletion ladder relative to capped commercial column synthesis. This is the project's cleanest DIY-vs-commercial discriminator and its only untested hypothesis. It requires collaborator-provided OpenIDS product reads (Kim et al. deposited none), routed through IBBIS infohazard review.

5. **Add position-resolved features to the classifier.** The Masaki reproduction showed the dG-laundering evasion is *position-local* — a position-agnostic aggregate G→A rate is fooled by it. A position-resolved feature is required to expose it, and building this now makes the adversarial-robustness claim in §4.6 concrete rather than asserted.

6. **Report calibration and exclusion power, not just accuracy.** Adopt the GEA field's discipline: expected calibration error (ECE) on every classifier, and an X99/X95-style exclusion metric. This directly supports the exclusion-first evidentiary framing, which the literature (Crook et al. 2022) shows is where attribution is strongest.

7. **Close the enzymatic gap when data allows.** The TdT signature (Palluk et al.) is currently cited from per-step supplementary tables, not reprocessed from raw reads. If a deposited enzymatic product dataset appears, reprocess it to make the fifth chemistry measured rather than published.

## Further directions (12+ months / more ambitious)

8. **Attribution of assembled constructs.** The method attributes unassembled oligo pools best; error-correction and assembly drive the likelihood ratio toward 1. A serious open question is how much signal survives assembly — an in-silico laundering study (no wet-lab synthesis) could map exactly where the signal dies.

9. **Combined multimodal attribution.** Genetic-engineering attribution identifies the *designer*; this project's method identifies the *instrument/chemistry*. Fusing the two into a single likelihood-ratio framework would be a genuinely new forensic capability.

10. **A public synthesis-method attribution benchmark.** The Genetic Engineering Attribution Challenge accelerated GEA. An analogous open benchmark, built on the reference library from step 1, could do the same here — and would establish this project as the reference point for the sub-field it defines.

11. **Feed the policy side.** Physical-signature and supply-chain forensics are named in Chapter 4 as capability gaps that belong in compartmented IBBIS working-group and agency work, not open research. The sequence-level method developed here is the open, publishable complement; positioning it explicitly as the detection leg that pairs with imperfect prevention strengthens the policy contribution of Chapters 1–2.

12. **Keep the cost and landscape model live.** Watch for the OpenIDS2 itemised cost (supplementary S1 table), array-benchtop entrants (e.g. LinkZill) eroding the "array = closed platform" assumption, and any DIY enzymatic movement. Chapter 3's forecasts are explicitly conditional; a light annual refresh keeps them honest.

---

## What could change the thesis

Three developments would each materially shift the argument and are worth monitoring:

- **A credible DIY device below gene-scale-capable cost outside the provider perimeter.** So far OpenIDS is the only sub-$25K self-run route to defined sequences, and it is short-oligo-limited. A working, longer-read DIY route would move the residual-gap conclusion.
- **Deposited OpenIDS (or other DIY) product reads.** These would convert the project's central prediction from hypothesis to measurement — the biggest single scientific upgrade available.
- **A mandatory on-device screening regime that resolves the DIY-classification question.** Chapter 2's whole R1 analysis turns on whether open-source/DIY instruments fall under a device mandate; a statutory answer either way collapses one of the main open uncertainties.

## A note on scope discipline

The project's credibility rests on staying strictly on the detection/attribution side of the line. Every step above is framed to consume product-sequence data, reproduce deposited results, or model publicly available cost data — none require synthesising reference material. The two places where new data is needed (OpenIDS product reads; a deposited enzymatic dataset) are explicitly gated on collaborator provision and IBBIS infohazard review. Maintaining that discipline is not a constraint on the work so much as the reason the work is publishable.
