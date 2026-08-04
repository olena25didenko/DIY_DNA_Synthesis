# DNA Synthesis Screening Under Device Proliferation

### A Regime-Conditional Technical Review: Readiness, Reach, Control Robustness, and Forensic Attribution, 2026–2030

**Author:** Olena Didenko · AIxBio Summer Fellowship 2026 · Mentor: Rassin Lababidi (IBBIS)

**Status:** Technical review consolidating the project's four analytical chapters, the literature review, the supply-chain assessments, and a July 2026 developer interview. All figures are the verified/corrected values used across the project; where a figure is an estimate, a projection, or vendor-supplied, it is labelled as such.

---

## Executive summary

DNA synthesis screening is not being defeated by clever evasion. It is being deliberately strengthened — made mandatory and pushed onto the synthesis device itself — at the same moment that do-it-yourself (DIY) and benchtop synthesis capability is proliferating and, increasingly, concentrating in jurisdictions a United States mandate cannot reach. This review characterises the resulting control architecture as a function of the policy regime, and asks not whether screening works but where control remains robust, where it erodes, and where policy must shift to keep pace through 2030.

Four findings anchor the analysis. First, on a disciplined reading of *usable length at high fidelity* rather than advertised maximum, the genuinely DIY-reproducible de-novo synthesizers are narrow, academic, and short-oligo: OpenIDS (open-source inkjet, ~$19,900, TRL 5, usable ~15–30 nt) and MAS 2.0 (open photolithographic, TRL 5, library-grade) — and MAS 2.0, on a newly sourced figure, is a ~€150–170K instrument (~€200–300K fully built), not a cheap garage device. Second, supply-chain restriction is not a durable control point under either the status-quo (R0) or the projected mandatory/on-device (R1) regime; this holds structurally and survives worst-case testing. Third, the most consequential result is about *reach*: a US mandate directly binds only 8 of 34 inventoried benchtop manufacturers, with the newest, highest-throughput capacity concentrating outside its reach — so international harmonisation is load-bearing, not optional. Fourth, because prevention is imperfect by design, the project specifies and now *demonstrates* a post-hoc forensic capability: reprocessing four deposited sequencing datasets reproduces published per-method error signatures to within ~±20%, and a co-processed reference atlas separates four synthesis chemistries at 100% balanced accuracy under leakage-safe validation, while within-chemistry vendor attribution remains hard.

The policy implication is a layered, mandatory, regime-conditional architecture: on-device screening for compliant new devices, mandatory provider screening with functional sequence-of-concern (SOC) detection, record retention, forensic attribution as a backstop for the devices and residual DIY routes those levers cannot reach, and international coordination to raise the jurisdictional ceiling. Every R1 claim is doubly conditional — on the paused OSTP framework revision being issued substantially as projected, and on S. 3741 (or an equivalent) being enacted.

## 1. Scope and the regime framework

This review is scoped to the **synthesis step only**. Sequence acquisition, oligo assembly into genetic constructs, pathogen rescue, and deployment are out of scope — a boundary that is principled rather than convenient, because the binding constraint on turning DIY oligos into a functional agent sits downstream of synthesis (Section 5). Synthesis technologies are characterised at the existence level: what has been demonstrated, and at what maturity.

Two governance regimes frame the analysis, and are kept explicitly separate because conflating them was an error in earlier drafts. **R0 is the observed status quo as of October 2026:** the OSTP Framework for Nucleic Acid Synthesis Screening (April 2024) has been paused by Executive Order 14292 (signed 5 May 2025) and directed to be revised or replaced, with no revised framework published as of July 2026; the International Gene Synthesis Consortium (IGSC) Harmonized Screening Protocol v3.0 (September 2024) operates voluntarily; there is no on-device screening requirement for benchtop manufacturers and no bulk-reagent monitoring mandate. **R1 is a projected mandatory/on-device regime** assembled from two distinct instruments that must not be merged: the OSTP framework revision, which supplies the technical specification (a tightened 50-nucleotide screening window, functional SOC definitions, six-frame translation, and manufacturer/on-device expectations, scheduled for 13 October 2026 but paused); and S. 3741, the Biosecurity Modernization and Innovation Act of 2026 (introduced 29 January 2026 by Senators Cotton and Klobuchar), which supplies a mandate mechanism via Commerce regulation plus a biotechnology governance sandbox at NIST, but does not itself specify the 50-nt window, functional SOCs, or an on-device mandate. R1 is therefore a composite projection, doubly conditional on the framework revision issuing as expected and on S. 3741 (or an equivalent) being enacted. The analytically interesting object under R1 is the **residual DIY gap** — the synthesis capability that remains outside the perimeter once commercial providers and benchtop manufacturers are screened.

**Table 1. The two governance regimes at a glance.**

| Dimension | R0 (status quo, Oct 2026) | R1 (projected mandatory / on-device) |
|---|---|---|
| Provider screening | Voluntary (IGSC v3.0) | Mandatory (Commerce reg. and/or funding conditions) |
| Screening window | 200 nt (paused before 50-nt tightening) | 50 nt |
| SOC definition | Homology-based | Functional SOC + six-frame translation |
| On-device screening | None required | Manufacturer / on-device expectation |
| Reagent monitoring | None | None (deliberate — inputs are commodity) |
| Legal instrument | OSTP framework (paused, EO 14292) | OSTP framework revision + S. 3741 (composite) |
| Status | Observed | Projected; doubly conditional (framework issued + S. 3741 enacted) |

## 2. Regime-conditional Technology Readiness Index

The Technology Readiness Index (TRI) scores seven synthesis approaches across nine technical and governance dimensions, weighted toward the TRL 3–6 band where capability meets accessibility. Two disciplines give it rigour. **Capability is scored by usable length at high fidelity, not advertised maximum.** At 98% per-step coupling a 30-mer is full-length only ~55% of the time and a 50-mer under 40%; OpenIDS2 measured ~96.1% per step and only ~56% full-length for a 15-mer — so OpenIDS's usable high-fidelity length is ~15–30 nt and its output is not directly assembly-ready. And **every input carries lower/best/upper bounds and a HIGH/MEDIUM/LOW confidence tag**, with a worst-case survival test on the qualitative conclusions.

**OpenIDS (inkjet, TRL 5)** is the reference DIY route: an open-source, 3D-printed synthesizer built from off-the-shelf components (Kim, Kim & Bang, 2024), capital ~$19,900 (HIGH confidence), ~$1–5 per sequence at scale, usable ~15–30 nt. A forensically relevant build detail — the published protocol omits the capping step — makes its error phenotype predictable and distinguishable from capped commercial column synthesis (Section 6). **MAS 2.0 (open photolithographic, TRL 5)** uses photolabile amidites (NPPOC/BzNPPOC) and a digital micromirror device to pattern 365 nm UV, with library-grade (error-prone) output. Its capital cost, previously estimated at "tens of $K," is now sourced: a July 2026 interview with a co-founder of Helices Biological Photolithography GmbH (the Vienna company that sells the instrument) gives optics alone at ~€150,000 and a realistic end-to-end build at ~€200,000–300,000; the instrument figure for like-for-like comparison is ~€150–170K. No independent (non-origin-lab) build exists yet, and optical alignment is the binding barrier — MAS 2.0 is a lab, not a garage, capability. **Electrochemical synthesis (TRL 3)** remains a single data-storage proof-of-concept (Xu et al., 2021) with no independent or DIY build; all present-day accessibility claims are conditional-future, and cost is undefined at this maturity. **Enzymatic synthesis** appears in two forms: a service model (TdT-based, e.g. Ansa Biotechnologies; no customer capital; provider is the controllable chokepoint) and a benchtop instrument (DNA Script SYNTAX, ~€250–280K / ~$270–303K vendor quote, corroborated by the Institute for Progress's 2024 figure of $292,000), which is purchasable but not independently reproducible — it runs on proprietary reagent cartridges under licensing. The only off-the-shelf DIY enzymatic route (commercial TdT + dNTPs + apyrase; Lee et al., 2019) makes stochastic homopolymers for data storage, not defined sequence. **DropSynth (TRL 4)** is an assembly method, not a de-novo synthesizer: it compartmentalises microarray-derived oligos by bulk vortex emulsification (no microfluidic chip, no cleanroom) and stitches them into genes, at ~$3,400 for the barcoded-bead pool; crucially it inherits the screening perimeter through its commercial oligo-pool input. **Commercial benchtop phosphoramidite instruments (TRL 9)** — e.g. Kilobaser (~$35,500), MerMade-class (~$120K+) — are the mature baseline; the Institute for Progress separately models a hypothetical 5-kb-capable benchtop in 2030 with a cost distribution peaking near ~$190,000 (25th–75th percentile ~$112,000–$298,000), a forecast for a future device, not a shipping price.

The at-a-glance summary (**Table 2**):

| Approach | TRL | DIY or buy | Capital | Usable length @ fidelity | Evasion R0→R1 |
|---|---|---|---|---|---|
| OpenIDS / OpenIDS2 (inkjet) | 5 | DIY build | ~$19.9K (v1) | ~15–30 nt | Medium → Low |
| MAS 2.0 (photolithographic) | 5 | DIY build | ~€150–170K instr. (~€200–300K loaded) | library-grade | Medium → Low |
| DropSynth (emulsion assembly) | 4 | DIY assembly | ~$3.4K bead pool | gene-length via assembly | Medium → Low |
| Electrochemical | 3 | no DIY build | undefined (~$10–12K est.) | 13–17 nt (demo only) | High* → Medium* |
| Enzymatic — SYNTAX (benchtop) | 5 | buy | ~$270–303K | 80–120 nt | Medium → Low |
| Enzymatic — Church (DIY) | ~3 | DIY off-the-shelf | low | data-storage only | — |
| Commercial benchtop (column) | 9 | buy | ~$60K (~$15–150K) | ~100–150+ nt | Medium → Low |
| Commercial provider (mail-order) | 9 | buy (service) | none | genes/genomes | Medium → Low |

*Electrochemical values are conditional-future (TRL 3). The evasion column reports the R0→R1 direction, not an absolute level.

## 3. Cost and accessibility trajectories

Cost projections are stated as conditional annual-decline scenarios with explicit TRL gating, not mechanical learning-curve fits — because DIY cumulative build volume is unknown and Wright's-law transfer would be false precision (Nagy et al., 2013; Lafond et al., 2018). Only OpenIDS has both a real cost anchor and a plausible trajectory: modelled from its $19,900 build at ~5/8/15% per year, the base case runs ~$16.8K (2026) → ~$12.1K (2030), crossing <$15K around 2027 and <$10K only ~2028 (optimistic) / ~2032 (base). The load-bearing conclusion is structural, not a point forecast: because commercial cost-per-base has plateaued (~$0.07/bp), the DIY accessibility barrier is **capital cost, not per-base cost** — and even where OpenIDS undercuts providers at high volume (above ~480,000 usable bases), it yields raw short oligos, not the assembled, verified, screened product a provider delivers.

Electrochemical cost is undefined at TRL 3 and is modelled as maturation-first; the enzymatic benchtop is commercial-only (~$270–303K now, ~$190K IFP 2030 mode). MAS 2.0, following the July 2026 interview, now has a sourced capital anchor (~€150–170K instrument) but is deliberately given no trajectory: a single anchor with no open-source decline series would be false precision, and its capital sits near the commercial-benchtop tier rather than the OpenIDS DIY tier. The honest overall picture is that DIY-synthesis accessibility is, for now, a story about one system (OpenIDS) with a real anchor and a conditional downward path, one conditional-future technology (electrochemical), and a set of higher-capital lab or commercial builds — all conditional on sustained R&D that DIY synthesis, lacking a large competitive market, is not guaranteed to sustain.

**Table 3. Cost anchors and conditional trajectories (all figures labelled by basis and confidence).**

| Approach | 2026 | 2030 (base / scenario) | Basis · confidence |
|---|---|---|---|
| OpenIDS (inkjet) | ~$16.8K (base) | ~$12.1K base; ~$7.5K opt / ~$14.6K cons | Kim 2024 anchor $19.9K · MED projection |
| Electrochemical | undefined (TRL 3) | undefined unless TRL 4 (~2028–30) | no anchor · LOW, TRL-gated |
| Enzymatic benchtop | ~$270–303K | ~$190K (IFP 2030 mode; IQR $112–298K) | vendor quote + IFP 2024 · commercial-only |
| MAS 2.0 (photolithographic) | ~€150–170K instrument | no trajectory (single anchor) | Somoza/Helices 2026 · sourced anchor |
| Commercial benchtop | ~$15–150K (best ~$60K) | ~$15–120K (slow decline) | device tier varies · MED |

## 4. Manufacturer landscape, jurisdictional reach, and the secondary market

The commercial benchtop landscape is the layer where abstract chemistry becomes shippable product. Drawing on the 34-firm inventory compiled within the ERA/IBBIS working group, the review contributes not a fresh census but an accessibility-and-reach scoring. The single most consequential result is about reach, not manufacturing capacity: of the 34 inventoried benchtop manufacturers, only **8 are US-headquartered** (directly bound by a US mandate), 12 are in allied jurisdictions (reachable via harmonisation, not US rule alone), and 14 sit outside both. Five of the nine firms founded since 2019 are outside US jurisdiction — including the highest-throughput array-based class — and roughly 35% predate 2010, a legacy installed base that cannot be retrofitted with know-your-customer checks, secure boot, or on-device screening. A US mandate therefore directly reaches under a quarter of known manufacturers, and the newest, most capable capacity is concentrating precisely where it does not.

Capability is common; capability combined with unreachability is rare. Devices reaching 120–150 nt exist in several jurisdictions — France (DNA Script SYNTAX, 120 nt, 96-parallel) and Austria (Kilobaser, ~150 nt) — but both are jurisdictionally reachable and gated by proprietary reagent licensing. Only one device combines assembly-relevant length, high throughput, and no US reach. A secondary finding is one of opacity: across all 34 firms, adopted-screening status could not be verified from public sources, so "the benchtop layer is essentially unauditable from outside" is itself a governance result.

The secondary market dissolves point-of-sale control. Used and refurbished synthesis and gene-assembly instruments — from a used Beckman Oligo 1000 at ~£670 to a Telesis Bio/Codex DNA BioXP gene-assembly workstation at ~US$13,500 and a MerMade-class synthesizer at ~$25,000 — are listed openly on general and specialist marketplaces with no buyer verification and, in observed cases, cross-border shipping. A resold device carries none of its point-of-sale controls, and its on-device screening state is unverifiable to the next buyer; the documented export leakage of new BioXP units to embargoed destinations via resellers (Codex DNA / Telesis Bio 10-Q disclosure) shows even screened-by-design hardware reaching unscreened hands.

**Table 4. Benchtop-manufacturer landscape and jurisdictional reach (34-firm ERA/IBBIS inventory).**

| Category | Count (of 34) | Reachability under a US mandate |
|---|---|---|
| US-headquartered | 8 | Directly bound |
| Allied jurisdictions | 12 | Reachable only via harmonisation / diplomacy |
| Outside US + allied | 14 | Not reachable (13 China, 1 Russia) |
| Founded since 2019, outside jurisdiction | 5 of 9 | Newest, highest-throughput capacity |
| Predate 2010 (legacy base) | ~35% | Cannot be retrofitted (KYC / secure boot) |
| Adopted-screening status publicly verifiable | 0 of 34 | "Unauditable from outside" |

## 5. Supply-chain analysis: no durable input chokepoint

Across the whole landscape, almost no input is a durable regulatory chokepoint. The **phosphoramidite** reagent supply is a commodity market of roughly 45–60 identifiable suppliers worldwide (of which ~25–30 are true manufacturers), spanning the US, Europe and Asia, with a growing bulk role in China; the reagents are unscheduled, substitutable, and even producible on demand from more stable precursors (Sandahl et al., 2021). The **solvent** chokepoint fails similarly: propylene carbonate, a GRAS food additive, substitutes for acetonitrile in DIY synthesis (Kim et al., 2024). The concentration that does exist is at therapeutic GMP/bulk grade and is a supply-resilience and economic-security issue — the reason the BIOSECURE Act (enacted as §851 of the FY2026 National Defense Authorization Act, P.L. 119-60, signed 18 December 2025) touches this space — not a misuse chokepoint. Governance deliberately avoids reagent controls for exactly this reason (Rose et al., 2024).

The DIY input chain is even less controllable than the reagent chain, because it adds commodity hardware to commodity chemistry. Cycle reagents (activator, oxidiser, deblock, capping), solid supports, inkjet printheads, microcontrollers and pumps are all multi-sourced with overwhelming legitimate demand. The only genuine barriers are two narrow, method-specific pieces of hardware: the **digital micromirror device** at the heart of a photolithographic build (effectively single-sourced via Texas Instruments) and the custom **CMOS/microelectrode array** an electrochemical synthesizer would need (foundry-dependent). Both are access barriers — they slow a builder — but neither is a regulatable monitoring point, because their legitimate markets (projectors, semiconductors) dwarf any synthesis use. The benchtop "buy" path is the mirror image: it does contain real chokepoints — the proprietary reagent cartridge (a licensed, KYC-able consumable) and the device manufacturer (where on-device screening attaches) — but both are first-sale levers, leaked by the resale and spare-parts markets described above. The clean cross-cutting conclusion, HIGH-confidence and structural, is that **input/supply control is a dead end for DIY and only a partial, first-sale lever for benchtop**; durable control belongs at the device, the provider, and post-hoc attribution.

The scope boundary rests on the same evidence. Assembling short oligos into genes is standard, decades-old methodology — the 901 bp GFP gene has been assembled from 16-mers — but converting low-fidelity DIY oligos into a correct functional gene is gated by fidelity and a downstream error-correction, clonal-selection and verification pipeline, not by oligo length. From ~56%-full-length building blocks the correct-assembly fraction is severe (even from decent oligos, PCA of a ~1 kb fragment yielded ~4% correct product before error correction, ~31% after two rounds). Reliable assembly beyond ~7,000–10,000 bp requires bacterial and yeast host systems, and many viral sequences are toxic to those hosts (NTI, 2023). The binding constraint therefore sits downstream of synthesis, which is why the project scopes to the synthesis step and treats assembly and rescue as out of scope.

**Table 5. Supply-chain chokepoint assessment.**

| Input | Sourcing | Substitutable? | Durable control point? |
|---|---|---|---|
| Phosphoramidites | ~45–60 suppliers worldwide | Yes (on-demand from precursors) | No |
| Solvent (acetonitrile) | Commodity | Yes (propylene carbonate, GRAS) | No |
| Cycle reagents / solid supports | Commodity, multi-sourced | Yes | No |
| Inkjet printheads | Handful of makers; non-synthesis uses | n/a | No (very low) |
| DMD (photolithographic) | Effectively single-source (TI) | No | Access barrier — not regulatable |
| CMOS electrode array (electrochemical) | Foundry-dependent | No | Access barrier — not regulatable |
| Proprietary reagent cartridge (benchtop) | Vendor-locked, licensed | No | Partial (KYC-able) — leaked by resale |
| Device manufacturer | 34-firm landscape | n/a | Partial — 8/34 reach; leaked by resale |

## 6. Control-robustness across regimes

Under R0, every lever is fragile. Provider-level screening is voluntary and uneven — a 2024 provider survey (Kane & Parker) found only six IGSC organisations using a 200-nt floor, with others screening all orders or using 20–60 nt bounds, and non-members entirely unbound. Printhead sourcing, phosphoramidite supply, and solvent supply all fail as chokepoints for the structural reasons in Section 5. No single R0 lever is durable; restricting one input permits substitution of another.

Under R1, if implemented as projected, mandatory provider screening at a 50-nt window plus on-device screening, functional SOC detection, and record retention are substantially more durable — but durable only for regulated commercial devices. The five R1 levers carry different weights. Mandatory provider screening (MEDIUM–HIGH durability) benefits from the fact that tested screening tools already clear >95% sensitivity and >97% accuracy on a blinded NIST dataset (Laird et al., 2025), superseding any "validation pending" framing; its residual gap is providers outside US jurisdiction. On-device screening (MEDIUM–HIGH) is hard to circumvent on compliant new commercial devices but weak for open DIY firmware and absent for legacy/used devices. Functional SOC detection (MEDIUM–HIGH) is the response to a demonstrated vulnerability: Wittmann et al. (2025) showed AI-designed protein variants can evade similarity-based screening, and after coordinated patching by three of four providers, ~3% of the more-probably-functional variants still escaped detection (a ~97% flag rate) — the gap the October 2026 functional-SOC provision is meant to close. Record retention (MEDIUM) enables post-hoc attribution but is post-incident. International coordination (LOW–MEDIUM) is incomplete but load-bearing, because a US-only mandate would shift orders to unscreened foreign providers.

Two structural constraints push against the device lockdown R1 assumes and belong in any honest assessment: the IGSC was founded in 2009 partly to pre-empt mandated hardware locks, and right-to-repair legislation in several US states (e.g. Oregon SB 1596, 2024) restricts the manufacturer software-lock mechanism on-device screening relies on. The worst-case survival test is unambiguous on one point and conditional on the other: **HIGH confidence that supply-chain restriction is not a durable control point** (structural; survives worst-case), and **MEDIUM/conditional confidence that R1 device-level control will prove effective**, depending on the framework revision being issued, S. 3741 (or equivalent) being enacted, and the DIY-classification question being resolved.

**Table 6. Control-lever robustness, R0 → R1, with durability tiering.**

| Control lever | R0 durability | R1 durability | Durability tier |
|---|---|---|---|
| Provider screening (domestic) | LOW | MED–HIGH | Tier 1 (enforcement-dependent) |
| On-device screening (new devices) | N/A | MED–HIGH | Tier 1 (weak for DIY / legacy) |
| Functional SOC detection | N/A (homology only) | MED–HIGH | Tier 1 |
| Record retention | N/A | MEDIUM | Tier 2 (post-hoc) |
| International coordination | N/A | LOW–MEDIUM | Tier 3 |
| Supply-chain restriction | VERY LOW | VERY LOW | Tier 4 (not durable) |

## 7. Synthesis-route attribution, proven on real data

Because prevention is imperfect by design, the project specifies — and now demonstrates — a post-hoc capability: infer the synthesis route from characteristic error signatures in a product's sequence, using reads alone and without device cooperation. This complements the genetic-engineering-attribution (GEA) literature, which identifies the *designer* of a construct (Nielsen & Voigt, 2018; Alley et al., 2020; Wang et al., 2021; Crook et al., 2022) but not the synthesis method, instrument, or chemistry — the gap this framework fills.

The premise is no longer only cited. Reprocessing four deposited datasets from raw reads reproduces their published per-method signatures to within ~±20%. Column phosphoramidite is deletion-dominated with a capping-driven G→A substitution bias: the Masaki et al. (2022) capping shift (Ac₂O → Pac₂O) reproduces at 12.2× (paper ~13×), the error phenotype is polymerase-independent (1.08× spread across three high-fidelity enzymes), and the non-canonical-dG rescue is position-local. Photolithographic synthesis is deletion-dominated with a G→T bias and an array spatial gradient (Lietard et al., 2021), with the capping-driven G→T drop reproduced (0.28% → 0.08%). Electrochemical synthesis is the most deletion-prone method measured — 18.8× the deletion rate of material deposition (Gimpel et al., 2023), with a 5′-ward positional gradient. On a single co-processed reference atlas (65 runs across the four datasets, shared denominators and features), **the four synthesis chemistries separate at 100% balanced accuracy** under leave-one-run-out cross-validation (chance 25%, permutation p≈0.01), and capping chemistry separates at 100% (Masaki) — both label-shuffle-controlled.

The framework is honest about what is hard. **Within-chemistry vendor attribution is leakage-sensitive and weak.** Under leakage-safe leave-one-lot-out validation, four-vendor attribution is data-limited (Eurofins and BioSearch have a single deposited lot each) and the near-neighbour IDT-vs-Sigma pair reaches only ~72% balanced accuracy (borderline, p≈0.05); an earlier ~75% estimate was inflated by replicate leakage across folds. Cross-chemistry attribution is the strong, defensible result; within-chemistry vendor attribution is not. Following the GEA literature, **exclusion is the primary value** — ruling out a commercial-provider origin from an anomalous error profile redirects an investigation from subpoenaing order records toward searching for equipment, which is a meaningful fork even without identifying an actor.

Two DIY-specific discriminators follow. The **column-DIY route (OpenIDS)** omits the capping step, so its product should show suppressed G→A and elevated n−1 internal deletions relative to capped commercial column synthesis — a testable DIY-vs-commercial phenotype, mechanistically anchored in the reproduced Masaki result, though it awaits collaborator product data (infohazard-reviewed via IBBIS; no synthesis is performed in-house). The **photolithographic-DIY route (MAS 2.0)** needs no prediction: it runs the same NPPOC chemistry as the reproduced Lietard dataset, so its class-level signature is already measured, and the developer confirms two complementary markers — a likely low-rate UV photo-induced damage signature (under active characterisation) and, because photolithographic deblocking uses light rather than acid, a lower depurination rate than acid-deblock column chemistry, a genuine column-vs-photolithographic discriminator. (Disclosure: the lead author of the reproduced Lietard dataset is a co-founder of Helices, which sells MAS 2.0; this does not affect the use of the published rates.)

Scope limits are documented, not hidden: post-synthesis error-correction and assembly progressively erase the oligo-level signal (driving the likelihood ratio toward the uninformative), and chemistry-level suppression via non-canonical guanosines can flatten the G→A feature — though because that suppression is position-local, a position-resolved feature still exposes it. The framework is therefore designed to lead with exclusion, to report calibrated likelihood ratios rather than point calls (per ENFSI 2015 forensic convention), and to validate by leave-group-out with a label-shuffle negative control.

**Table 7. Reproduction scorecard — four deposited datasets reprocessed from raw reads.**

| Dataset (accession) | Chemistry class | Signature | Measured (ours) vs published |
|---|---|---|---|
| Masaki (DDBJ DRA013805) | Column phosphoramidite | Capping-driven G→A | 12.2× capping shift (paper ~13×); polymerase-independent (1.08× spread) |
| Filges (SRA PRJNA727098) | Column, 4 manufacturers | Deletion-dominated, 5′ bias | IDT 0.207%/nt (paper ~0.20%); vendor extremes reproduce |
| Lietard (ENA PRJEB43002) | Photolithographic | G→T + array spatial gradient | G→T 0.28→0.08% capping drop (paper 0.31→0.07%) |
| Gimpel (ENA PRJEB65931) | Electrochem. vs deposition | High deletion + 5′ gradient | 18.8× ratio (paper ~23×); deposition 0.044%/nt |

**Table 8. Attribution classification tasks (leakage-safe validation).**

| Task | Grouping | Balanced accuracy | Chance | Significance |
|---|---|---|---|---|
| Cross-chemistry (4-class) | leave-one-run-out | 100% | 25% | p≈0.01 |
| Capping chemistry (Masaki) | leave-one-run-out | 100% | 50% | p≈0.01 |
| Manufacturer (4-vendor) | leave-one-lot-out | collapses (data-limited) | 25% | not significant |
| IDT vs Sigma (near-neighbour) | leave-one-lot-out | ~72% (borderline) | 50% | p≈0.05 |

## 8. Limitations, uncertainties, and confidence

The review is explicit about what it does and does not establish. HIGH confidence attaches to: the OpenIDS cost anchor, TRL, and yield; current enzymatic commercial pricing; the electrochemical TRL-3 status; the non-durability of supply-chain restriction; and the reproduced cross-chemistry attribution results. MEDIUM or conditional confidence attaches to: the OpenIDS cost trajectory (rate transfer without market drivers); the R0/R1 evasion scoring (modelled from policy documents, not observed); and the effectiveness of R1 device-level control, which depends on unissued instruments and unenacted legislation. LOW confidence attaches to: all electrochemical value dimensions except the TRL-3 assessment itself; DropSynth DIY feasibility and cost trajectory; and all 2028–2030 cost projections. Two items warrant independent verification before external citation: the "Texas Instruments is effectively the sole DMD source" claim, and the forward-dated 2026 Frontiers risk-based-oversight reference in the supply-chain assessment. The MAS 2.0 capital figure and specifications rest on a single developer interview plus the ChemRxiv component list; company, personnel, and third-party-customer details (Ghent spatial transcriptomics, GSK therapeutic-RNA use) are the developer's account and, where private, are not independently verifiable.

**Table 9. Confidence summary.**

| Finding / estimate | Confidence |
|---|---|
| Supply-chain restriction is not a durable control point | HIGH (structural; survives worst-case) |
| OpenIDS cost anchor, TRL, yield; enzymatic commercial pricing; electrochemical TRL-3 status | HIGH |
| Cross-chemistry attribution (100%, leakage-safe) | HIGH |
| OpenIDS cost trajectory; R0/R1 evasion scoring | MEDIUM / conditional |
| R1 device-level control effectiveness | MEDIUM / conditional (unissued framework + unenacted bill) |
| Electrochemical value dimensions; DropSynth feasibility; all 2028–2030 projections | LOW |

## 9. Conclusion

The DIY frontier in de-novo DNA synthesis is narrow, academic, and skill-gated. OpenIDS and MAS 2.0 are the only reproducible open synthesizers, and both are lab-grade, expertise-heavy, and currently short-oligo or library-grade — not assembly-ready for defined genes; MAS 2.0, on the corrected figures, is a ~€200–300K, optics-alignment-gated build with no independent replication yet. DropSynth is cheap DIY assembly but inherits the screening perimeter through its commercial oligo pool; electrochemical has no DIY build; enzymatic is DIY only in a data-storage-only form; and there is no working garage synthesizer at all. The correct inference is not that screening becomes irrelevant, but that a single point-of-sale control is insufficient. Screening must be made mandatory, pushed on-device, extended internationally, and backstopped by forensic attribution for the devices and the residual DIY routes it cannot reach. The problem shifts from "prevent DIY synthesis" to "govern a proliferating-device world with a layered, mandatory, regime-conditional architecture" — which the October 2026 revisions and S. 3741 begin to build, and which this project sets out to stress-test.

## References

Alley, E. C., et al. (2020). A machine learning toolkit for genetic engineering attribution to facilitate biosecurity. *Nature Communications*, 11, 6293. https://doi.org/10.1038/s41467-020-19612-0

Crook, O. M., et al. (2022). Analysis of the first Genetic Engineering Attribution Challenge. *Nature Communications*, 13, 7374. https://doi.org/10.1038/s41467-022-35032-8

Esvelt, K. M. (2022). *Delay, Detect, Defend: Preparing for a Future in which Thousands Can Release New Pandemics.* Geneva Papers 29, GCSP.

Executive Order 14292 (2025). Improving the Safety and Security of Biological Research. *Federal Register*, 90 FR 19611 (May 8, 2025).

Filges, S., Mouhanna, P., & Ståhlberg, A. (2021). Digital quantification of chemical oligonucleotide synthesis errors. *Clinical Chemistry*, 67(10), 1384–1394.

Gimpel, A. L., Stark, W. J., Heckel, R., & Grass, R. N. (2023). A digital twin for DNA data storage based on comprehensive quantification of errors and biases. *Nature Communications*, 14, 6026. https://doi.org/10.1038/s41467-023-41729-1

Helices Biological Photolithography GmbH (2026). MAS 2.0. https://helicesbio.com/ (capital and specifications from founder interview, July 2026).

Institute for Progress / Langenkamp, M. (2024). *Securing Benchtop DNA Synthesizers.* https://ifp.org/securing-benchtop-dna-synthesizers/

International Gene Synthesis Consortium (2024). *Harmonized Screening Protocol v3.0.* https://genesynthesisconsortium.org/

Kane, A., & Parker, M. T. (2024). Screening State of Play: The Biosecurity Practices of Synthetic DNA Providers. *Applied Biosafety*, 29(2), 85–95. https://doi.org/10.1089/apb.2023.0027

Kim, J., Kim, H., & Bang, D. (2024). An open-source, 3D printed inkjet DNA synthesizer. *Scientific Reports*, 14, 3773. https://doi.org/10.1038/s41598-024-53944-x

Kim, J., Kim, H., & Bang, D. (2025). OpenIDS2. *PLOS ONE*, 20, e0338478. https://doi.org/10.1371/journal.pone.0338478

Laird, T. S., et al. (2025). Inter-tool analysis of a NIST dataset for assessing baseline nucleic acid sequence screening. *Applied Biosafety.* https://doi.org/10.1177/15356760251401228

Lafond, F., et al. (2018). How well do experience curves predict technological progress? *Technological Forecasting & Social Change*, 128, 104–117. https://doi.org/10.1016/j.techfore.2017.11.001

Lee, H. H., et al. (2019). Terminator-free template-independent enzymatic DNA synthesis for digital information storage. *Nature Communications*, 10, 2383. https://doi.org/10.1038/s41467-019-10258-1

Lietard, J., et al. (2021). Chemical and photochemical error rates in light-directed synthesis of complex DNA libraries. *Nucleic Acids Research*, 49(12), 6687–6701. https://doi.org/10.1093/nar/gkab505

Masaki, Y., Onishi, Y., & Seio, K. (2022). Quantification of synthetic errors during chemical synthesis of DNA and its suppression by non-canonical nucleosides. *Scientific Reports*, 12, 12095. https://doi.org/10.1038/s41598-022-16222-2

Nagy, B., Farmer, J. D., Bui, Q. M., & Trancik, J. E. (2013). Statistical Basis for Predicting Technological Progress. *PLoS ONE*, 8(2), e52669. https://doi.org/10.1371/journal.pone.0052669

Nielsen, A. A. K., & Voigt, C. A. (2018). Deep learning to predict the lab-of-origin of engineered DNA. *Nature Communications*, 9, 3135. https://doi.org/10.1038/s41467-018-05378-z

Nuclear Threat Initiative | bio (2023). *Benchtop DNA Synthesis Devices: Capabilities, Biosecurity Implications, and Governance.*

Palluk, S., Arlow, D. H., de Rond, T., et al. (2018). De novo DNA synthesis using polymerase–nucleotide conjugates. *Nature Biotechnology*, 36(7), 645–650. https://doi.org/10.1038/nbt.4173

Rose, S., Alexanian, T., Langenkamp, M., Cozzarini, H., & Diggans, J. (2024). Practical Questions for Securing Nucleic Acid Synthesis. *Applied Biosafety.* https://doi.org/10.1089/apb.2023.0028

Sandahl, A. F., et al. (2021). On-demand synthesis of phosphoramidites. *Nature Communications*, 12, 2760. https://doi.org/10.1038/s41467-021-22945-z

Sidore, A. M., Plesa, C., Samson, J. A., Lubock, N. B., & Kosuri, S. (2020). DropSynth 2.0: high-fidelity multiplexed gene synthesis in emulsions. *Nucleic Acids Research*, 48(16), e95. https://doi.org/10.1093/nar/gkaa600

U.S. Congress (2026). S. 3741, Biosecurity Modernization and Innovation Act of 2026, 119th Congress (Cotton, Klobuchar). https://www.congress.gov/bill/119th-congress/senate-bill/3741

Wang, Q., et al. (2021). PlasmidHawk improves lab of origin prediction of engineered plasmids using sequence alignment. *Nature Communications*, 12, 1167. https://doi.org/10.1038/s41467-021-21180-w

Wittmann, B. J., et al. (2025). Strengthening nucleic acid biosecurity screening against generative protein design tools. *Science*, 390(6768), 82–87. https://doi.org/10.1126/science.adu8578

Xu, C., Ma, B., Gao, Z., Dong, X., Zhao, C., & Liu, H. (2021). Electrochemical DNA synthesis and sequencing on a single electrode with scalability for integrated data storage. *Science Advances*, 7(46), eabk0100. https://doi.org/10.1126/sciadv.abk0100

BIOSECURE Act — enacted as §851 of the FY2026 National Defense Authorization Act (P.L. 119-60), signed 18 December 2025.
