# OpenIDS developer correspondence — Junhyeong Kim (김준형)

**Correspondent:** Junhyeong Kim, OpenIDS lead developer (first author, Kim, Kim & Bang 2024 Sci. Rep. and 2025 PLOS ONE). Project since discontinued (he graduated; his advisor left the position).
**Interlocutor:** Olena Didenko (ERA/IBBIS).
**Date:** July 2026 email thread. **Standing constraint:** analysis of published/deposited data only; no synthesis.

---

## Key findings

**The 15–30 nt ceiling is inkjet-specific, not a general DIY limit.** OpenIDS delivers phosphoramidite as picolitre inkjet droplets whose very high surface-area-to-volume ratio makes coupling extremely sensitive to trace atmospheric moisture, which is hard to exclude in a DIY setting. That was a deliberate trade-off for massive parallelism. Kim estimates a DIY build on conventional column phosphoramidite chemistry (the IDT/GenScript architecture) would have a far easier moisture problem and could synthesise arbitrary sequences of ~100 nt, then assemble those into longer molecules. No such column DIY instrument has been published.

**The binding barrier is lab infrastructure, not the build.** OpenIDS was designed so a non-specialist could build it in a few months; with today's AI-assisted CAD/circuit/code design, Kim judges a typical science or engineering researcher could build OpenIDS2 in weeks. The real bottleneck is the laboratory infrastructure to handle corrosive acids, organic solvents, and pressurised inert gases (N₂/Ar) safely: fume hood, solvent/acid handling, compressed gas.

**Capping was deliberately omitted in both versions, with double-coupling in its place.** Omitting capping cut two reagents plus the pumps, tubing, control code, and space to handle them. Instead they used double-coupling (retry the addition if the first coupling fails), which raises per-cycle efficiency (cf. Agilent patent US10072261B1). Kim expects builders to omit capping wherever coupling efficiency is high enough.

**No OpenIDS sequencing data exists, and none is coming from him.** Synthesis efficiency never reached a level that justified sequencing; products were assessed only by PAGE and HPLC. The project ended after his graduation. So the OpenIDS-specific test of the capping-omission phenotype is closed; confirming it would need a future independent build that deposits reads.

**DIY forensic signatures will be more diverse than commercial ones.** Commercial providers hold synthesis conditions standardised, giving consistent, attributable signatures (Kim thinks capping chemistry might even be identifiable by mass spectrometry). DIY builders vary reagents, protocol, capping, and reaction conditions freely, so DIY signatures should be a heterogeneous family, making positive DIY attribution harder. This supports framing the discriminator as evidence for excluding a standard commercial origin rather than for positively identifying an OpenIDS origin.

**No independent build has been formally published,** but all reproduction details are on GitHub, so silent reproductions are possible and Kim would have no way to know. "No independent build published" therefore understates possible unpublished builds.

**Cost: OpenIDS v1 = $19,900; OpenIDS2 ≈ $4,000 (2025), developer-confirmed.** v2 redesigned most components for in-house fabrication. Actual cost varies by country/supplier; international purchasing roughly doubled some component prices (e.g. the printhead).

---

## Chapter implications

- **Ch.1 §2.1 (OpenIDS):** already updated — inkjet-specific ceiling, facilities-not-fabrication barrier, capping/double-coupling, ~$4,000 v2.
- **Ch.4 §4.1(f) and executive summary:** already updated — double-coupling, no-data/discontinued, heterogeneous DIY signatures, exclusion-not-identification.
- **Ch.3 (cost):** the confirmed ~$4,000 v2 (2025) is a step-change that undercuts the $19.9K-anchored decline forecasts; capital is no longer the binding DIY constraint, fidelity/length is.
- **Ch.2 (control):** the open design can't be governed at the plans (public GitHub, silent builds); the reachable handles are wet-lab inputs (acids, solvents, gases, purchased reagents/oligos). A column DIY build reaching ~100 nt would move the residual-gap object.
- **IBBIS summary:** the 15–30 nt figure is inkjet-specific; column DIY could reach ~100 nt; barrier is infrastructure; v2 ≈ $4,000.

---

## Kim's substantive replies (verbatim excerpts)

**On length/fidelity:** "the coupling efficiency achieved by OpenIDS was lower than that of commercial DNA synthesizers, and we only demonstrated the synthesis of relatively short oligonucleotides, such as poly(T) of approximately 20–30 nt. The biggest reason for the low synthesis efficiency was moisture control. ... The inkjet-based approach used in OpenIDS delivers phosphoramidite as extremely small droplets in the picoliter range ... highly sensitive even to trace amounts of moisture ... if a DIY synthesizer were built using the conventional column-based phosphoramidite synthesis method used by companies such as IDT or GenScript, moisture control would be much easier. In my opinion, it should be possible to synthesize arbitrary DNA sequences of around 100 nt. Of course, it should also be possible to assemble these oligonucleotides into much longer DNA molecules."

**On the build vs the lab:** "even someone without professional training in software or hardware could build and operate it within a few months ... anyone with the technical background ... could build and operate OpenIDS2 within a few weeks. I think the greater bottleneck is not building the synthesizer itself, but rather obtaining the necessary laboratory infrastructure for safely handling corrosive acids, organic solvents, and pressurized inert gases such as nitrogen or argon."

**On forensics:** "Commercial DNA synthesis companies generally optimize their synthesis conditions and then do not change them significantly ... it may be possible to infer which company synthesized a DNA molecule ... In contrast, I think DIY synthesizers such as OpenIDS will be much more difficult to analyze ... Each user is free to modify the synthesis conditions, protocols, reagents, and optional processes such as capping ... I expect the synthesis signatures to become much more diverse, making forensic attribution much more difficult."

**On capping:** "By omitting the capping step, we could reduce not only the number of reagents required, but also the components needed to handle those reagents ... the double-coupling approach we used attempts the nucleotide addition again during a second coupling step if the first coupling fails ... Agilent holds a patent describing this type of technology: https://patents.google.com/patent/US10072261B1/en ... I would expect users to prefer omitting capping when possible."

**On sequencing data:** "Unfortunately, I do not currently have any sequencing data from OpenIDS or OpenIDS2 products that I can share. ... We were also unable to achieve a synthesis efficiency high enough to proceed with sequencing, so the synthesized products were evaluated only by PAGE and HPLC. Shortly after the publication of OpenIDS2, the research was discontinued as I graduated and my professor left his position."

**On independent builds:** "there has not yet been a formally published report of OpenIDS or OpenIDS2 being completely and independently reproduced outside our research group. ... all of the detailed information needed to reproduce the systems is publicly available on GitHub. Therefore, even if someone reproduced OpenIDS, there would be no need for them to contact me ... I may simply have no way of knowing about such builds."

**On cost:** "approximately USD 4,000 is the correct estimate [for OpenIDS2]. By redesigning most of the components so that they could be fabricated in-house, we were able to build OpenIDS2 at a substantially lower cost than OpenIDS1. ... when we actually purchased the printhead, we had to pay almost twice the manufacturer's listed price because of international purchasing services, shipping costs, and related expenses."
