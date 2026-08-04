# Part 1 — Regime-Conditional Technology Readiness Index (TRI)

### DIY DNA Oligonucleotide Synthesis Approaches Under Governance Transitions

## 1. Introduction & scope

**Scope.** Synthesis-step characterization only (sequence acquisition, assembly, pathogen rescue, and deployment are OUT OF SCOPE). Regimes: R0 (status quo, October 2026 — present) vs R1 (projected regime in which mandatory synthesis screening and on-device benchtop screening are in force). The analytical focus is the residual DIY gap — synthesis capability that remains outside the screening perimeter once commercial providers and benchtop manufacturers are covered.

**Scope note:** This analysis characterizes seven DNA oligonucleotide synthesis approaches across nine technical and governance dimensions: (1) Technology Readiness Level (TRL), (2) capital cost, (3) per-sequence cost, (4) expertise required, (5) time-to-first-synthesis, (6) maximum sequence length, (7) synthesis yield, (8) oversight-evasion potential (regime-paired, R0/R1), and (9) supply-chain vulnerability (regime-paired, R0/R1). The analysis applies a regime-conditional framework to understand how governance changes between October 2026 (R0, present) and the projected mandatory / on-device regime (R1) affect the accessibility, evasion potential, and control-point robustness of each method.

### 1.1 Governance regime definitions

The two regimes are defined below. R0 is observed; R1 is a projection assembled from two distinct policy instruments whose implementation has not yet occurred. Those two instruments — a bill (S. 3741) and a technical framework (the OSTP screening framework) — are kept explicitly separate, because they do different things and have different enforcement pathways. Conflating them was an error in earlier drafts and is corrected here.

**Regime 0 (R0): Status Quo, October 2026 (present).** The OSTP Framework for Nucleic Acid Synthesis Screening (April 2024) was directed to be revised or replaced by Executive Order 14292 (Improving the Safety and Security of Biological Research, May 5, 2025). During the interim, no mandatory federal synthesis-screening requirement is in force. IGSC Harmonized Screening Protocol v3.0 (September 2024): voluntary; member companies self-regulate. No on-device screening requirement for benchtop synthesizer manufacturers. No bulk-nucleotide or reagent monitoring mandate. Synthesis screening relies on voluntary provider compliance (IGSC v3.0). Sources: Executive Order 14292 (Federal Register, 90 FR 19611, May 8, 2025; signed May 5, 2025); IGSC Harmonized Screening Protocol v3.0 (September 2024); OSTP Framework for Nucleic Acid Synthesis Screening (April 2024; ASPR S3).

**Regime 1 (R1): Projected mandatory / on-device regime, late 2026+.** R1 is the direction of travel implied by two separate instruments. They must not be merged.

(i) The legislative vehicle — S. 3741, Biosecurity Modernization and Innovation Act of 2026. Introduced January 29, 2026 by Sen. Tom Cotton and Sen. Amy Klobuchar; read twice and referred to the Senate Committee on Commerce, Science, and Transportation. What the bill actually does, per its text: directs the Secretary of Commerce to promulgate regulations requiring gene-synthesis providers to screen orders and customers; establishes a biotechnology governance sandbox at NIST for testing biosecurity tools and enabling more flexible policymaking; requires a 90-day White House assessment of the state of federal biosecurity/biosafety oversight, feeding an implementation plan. Critically, S. 3741 is a first-step, assessment-and-authority bill. Its enforcement vehicle is Commerce regulation, not HHS/ASPR or NIH funding/procurement conditions, and the bill text does not itself specify an on-device mandate, a 50-nucleotide window, or functional Sequence-of-Concern (SOC) definitions. (Endorsed by the National Security Commission on Emerging Biotechnology, Twist Bioscience, IDT, Ginkgo Bioworks, Aclid; commended by the Johns Hopkins Center for Health Security.)

(ii) The technical specification — the OSTP Nucleic Acid Synthesis Screening Framework. This is where the screening mechanics live: the tightened 50-nucleotide screening window, functional SOC definitions, six-frame translation, and manufacturer / on-device expectations. The April 2024 framework set a phased schedule: the requirement took effect for federally funded purchases on or after April 26, 2025 (200-nt window), with a tightening to a 50-nucleotide window and an expanded, functional SOC definition scheduled for October 13, 2026 — three years after the October 2023 HHS Guidance (OSTP Framework, Sept 2024 text). EO 14292 (May 5, 2025) then paused implementation and directed OSTP to revise or replace the framework. Separately, IGSC v3.0 requires members to transition to the 50-bp threshold by October 24, 2026 at the latest to conform to the OSTP framework (IGSC Harmonized Screening Protocol v3.0). Both dates are documented in the primary texts, not speculative — what is genuinely open is whether the October 2026 milestone takes effect on schedule, since the revised framework has not been published as of July 2026.

**Honest R1 caveat.** The "mandatory + on-device" R1 this project models is a composite projection: the screening-mandate direction of S. 3741 plus the technical spec of the OSTP framework revision. As of July 2026, S. 3741 delivers a mandate mechanism (via Commerce) and a NIST sandbox; the on-device / 50-nt / functional-SOC specifics remain in the unissued framework revision. Every R1 claim in this document is therefore doubly conditional: on the framework revision being issued substantially as projected, and on S. 3741 (or an equivalent) being enacted and implemented. The chapter does not claim R1 exists — it claims R1 is the direction policy is aimed.

**Analytical use of R1 (the residual-gap frame).** For scoring, R1 is treated as a regime in which mandatory screening is in force for commercial providers and on-device screening is required of benchtop manufacturers. The question this chapter then asks is not "does screening work?" but "what synthesis capability remains outside that perimeter?" — i.e., DIY and in-house protocols reached by neither a provider mandate nor a device mandate. That residual DIY gap is the object of interest; commercial and benchtop methods are scored mainly to establish what the perimeter covers. Sources: S. 3741, 119th Congress (congress.gov / govinfo BILLS-119s3741is); Cotton–Klobuchar press release (Feb 4, 2026); OSTP Framework for Nucleic Acid Synthesis Screening (April 2024, ASPR S3); NIST screening-specification role per the framework.

### 1.2 Boundary Clarity

IN SCOPE: oligonucleotide synthesis methods; system-level characterization (TRL, cost, expertise, accessibility); regime-conditional evasion potential and supply-chain vulnerability. OUT OF SCOPE: sequence acquisition / order placement; oligo assembly into genetic constructs; pathogen culture / deployment; operational build protocols. Synthesis technologies are cited at existence level only (what has been demonstrated, and at what maturity). Reading the oversight-evasion axis (dimension 8): higher = more able to evade oversight under the stated regime; lower = more readily detected / controlled.

### 1.3 Reading the TRL scale, and the DIY focus

**What TRL measures here.** Technology Readiness Level (TRL 1–9) ranks how close a synthesis route is to a working, assembly-ready capability a non-expert could actually stand up — not its scientific novelty. Read as bands: TRL 1–2 — basic principle / concept only; TRL 3–4 — early proof-of-concept or lab-validated prototype (electrochemical; DropSynth); TRL 5–6 — demonstrated and reproducible (OpenIDS); commercial instrument or service operational (enzymatic); TRL 7–9 — production-qualified, mature commercial systems (benchtop phosphoramidite).

**Why it matters here.** The zone of interest is TRL 3–6: mature enough to work, accessible enough to reproduce or stand up outside a major provider. High-TRL commercial systems (7–9) are included only as a baseline/reference — high-capability, but reached through purchase or secondhand acquisition, not DIY reproduction. A route's governance interest is highest where capability meets accessibility, which is the DIY/in-house band, not the commercial ceiling. Definitions. Time to first usable oligo — elapsed time from starting a build/setup to producing the first correct product (build + calibration). OOS — out of scope. Assembly-ready — product usable directly as a building block for gene-length assembly.

## 2. Technology landscape: the seven approaches

**Figure 1.1** — Technology readiness by synthesis approach.

### 2.1 OpenIDS (inkjet-based, TRL 5)

**Technology & status.** OpenIDS is an open-source, 3D-printed, inkjet-based oligonucleotide synthesizer built from commercial off-the-shelf components (Kim, Kim & Bang, 2024, Scientific Reports 14:3773). A second-generation design, OpenIDS2 (Kim, Kim & Bang, 2025, PLOS ONE), reduces device volume to roughly one-third, integrates custom PCBs, and improves stability via peristaltic bulk-solution delivery.

**TRL: 5 (Demonstrated, Reproducible).** Peer-reviewed; open-source and documented; reproducible in academic settings — the governance-relevant maturity marker is that the design is public and reproducible, not proprietary.

**Forensically relevant build detail.** The published protocol omits the capping step. Because the diagnostic G→A substitution signature of column phosphoramidite chemistry is capping-driven (Masaki, Onishi & Seio, 2022; see Chapter 4), OpenIDS oligos are expected to carry a distinguishable error phenotype relative to standard capped column synthesis.

| Dimension | Best | Range | Confidence | Source / note |
|---|---|---|---|---|
| Capital cost | $19,900 | $15,000–25,000 | HIGH | Kim et al. 2024 BOM |
| Per-seq cost | ~$2/seq | $0.50–10 | MED–HIGH | Kim et al. 2024 reagent analysis |
| Expertise (1–10) | 6/10 | 5–8 | MED–HIGH | — |
| Time-to-first | ~4 weeks | 2–8 wk | MED | build time |
| Usable length @ high fidelity | ~15–30 nt | advertised oligo-scale ~100–200 nt | MED | only poly-dT ≤30-mer demonstrated; not gene-assembly-ready |
| Throughput | ~144 spots/array | — | MED | array format |
| Yield (per-cycle coupling) | ~94–98%/cycle | 95–99% | MED | PC coupling 94-98% per Kim 2024; OpenIDS2 ~56% full-length for a 15-mer |

Propylene carbonate (a GRAS food-additive solvent) substitutes for acetonitrile (Kim et al., 2024). Accessibility of published plans is not the same as accessibility of working capability — the expertise barrier is real.

**Oversight-evasion & supply-chain (R0 vs R1).** R0: Evasion — Medium; Supply-chain vulnerability — High. Distinctive printhead but unmonitored; commodity solvent/reagents; voluntary IGSC screening does not reach DIY builders. R1: Evasion — Low; Supply-chain vulnerability — Medium. If classified as a benchtop synthesizer under the framework revision, an on-device screening mandate would reach synthesis activity directly; reagent sourcing stays uncontrolled but device-level detection becomes the primary lever. Policy delta (conditional on R1 implementation): control shifts from supply-chain chokepoints (not durable) toward device-level detection (more durable). Projected improvement, not observed.

### 2.2 MAS 2.0 / Advanced Maskless Synthesizer (Photolithographic, Open-Source, TRL 5)

**Technology & status.** MAS 2.0 (the Advanced Maskless Synthesizer) is a fully open-source, benchtop photolithographic (light-directed) oligonucleotide synthesizer (Somoza group, ChemRxiv 2024, DOI 10.26434/chemrxiv-2024-j4c90). It uses phosphoramidites with photolabile 5′-protecting groups (NPPOC/BzNPPOC) and a digital micromirror device (DMD) to pattern ~365 nm UV onto the substrate — photo-deprotecting only the illuminated features so the next base couples only there. "Maskless" means the DMD (a reprogrammable micromirror array, as in a DLP projector) replaces the fabricated physical photomasks of the original Affymetrix approach; any array pattern is set in software.

**TRL: 5 (Demonstrated, Open Build).** Full open hardware — CAD/STL, a costed component list, Python control software, and a chemistry/process manual — demonstrated by the originating lab; broad independent replication is still emerging. Accuracy and usable length for this method class are published in the light-directed synthesis literature (Lietard et al., 2021, NAR 49(12):6687; Agbavwe et al., 2011, J. Nanobiotechnol. 9:57), not as headline figures in the device paper itself. It is the DIY instantiation of the photolithographic class whose error signature is reproduced in the attribution framework (Chapter 4, Lietard class).

| Dimension | Best (est) | Range | Confidence |
|---|---|---|---|
| Capital cost | [[R~€150–170K instrument (optics ~€150K + nucleic-acid synthesizer ~€20K); ~€200–300K fully loadedR]] | [[R€150K–300KR]] | [[RMED–HIGH — now SOURCED (developer interview, Somoza/Helices, Jul 2026; corroborated by the ChemRxiv component list)R]] |
| Per-oligo cost | — | — | LOW (not reported) |
| Expertise | 8/10 | 7–9 | MED |
| Time-to-first usable oligo | ~8–16 weeks | — | LOW |
| Usable length @ fidelity | library-grade (error-prone) | — | MED |
| [[RThroughputR]] | [[Rup to 786,432 (XGA DMD) / 2,073,600 (1080p DMD) unique sequencesR]] | [[R—R]] | [[RHIGH (vendor spec)R]] |
| [[RCycle / opticsR]] | [[R~15 s coupling; photodeprotection 60/30/6 s (NPPOC/Bz-NPPOC/SPh-NPPOC); 365 nm UV LED; TI DMDR]] | [[R—R]] | [[RHIGH (vendor spec)R]] |

Barriers are optics alignment, DMD control, anhydrous amidite fluidics, and specialty photolabile amidites [[R(available from several suppliers, three generations NPPOC/BzNPPOC/SPh-NPPOC; not commodity)R]]. It needs no cleanroom. [[RCapital is now sourced from the developer, not estimated: optics alone ~€150,000 and a realistic end-to-end build ~€200,000–300,000 (M. Somoza, co-founder, Helices Biological Photolithography GmbH, Vienna — helicesbio.com; interview Jul 2026). For a like-for-like TRI comparison the instrument figure is ~€150–170K (optics ~€150K + synthesizer ~€20K); the ~€200–300K includes gases, pressure regulators, and a climate-controlled lab. This is roughly a 10× correction to the earlier "tens of $K" estimate and places MAS 2.0 above garage range. The developer confirms no independent (non-origin-lab) build exists yet; the first in-house build took months (now down to a few weeks), gated chiefly by optical alignment. Founders: Erika Schaudy (CEO), Mark Somoza, Jory Lietard — note Lietard also authored the Lietard 2021 NAR error-rate paper cited here (worth a disclosure footnote where that paper anchors the Chapter 4 photolithographic signature). The vendor page also confirms the "no acidic deblock" point used in Chapter 4: the photolabile group "directly replaces the acid-labile dimethoxytrityl (DMTr)."R]] Historical predecessor: POSaM (Lausted et al., 2004, Genome Biology 5(8):R58) — the original open-source inkjet synthesizer (build cost ~$34K per the OpenIDS 2024 characterization); open synthesizer designs are 20 years old.

**Oversight-evasion & supply-chain (R0 vs R1).** R0: Evasion — Medium; Supply-chain vulnerability — Medium. A visible bench build; optics/amidite sourcing partly traceable; library-grade (not per-strand-perfect) output caps assembly-readiness. R1: Evasion — Low. If classified as a benchtop synthesizer, an on-device mandate would reach it; the specialty photolabile amidites are a partial (not durable) supply chokepoint.

### 2.3 Electrochemical synthesis (TRL 3)

**Technology & status.** Phosphoramidite chemistry with electrochemically triggered deprotection (Xu et al., 2021, Science Advances 7(46):eabk0100). In Xu et al., a positive potential at a gold electrode generates protons that strip the acid-labile DMT group; the demonstration synthesized a 13-mer — a DNA-data-storage proof, not a general-purpose synthesizer. The electrochemical-array mechanism was commercialized historically by CombiMatrix/CustomArray (acquired by GenScript, 2017), but no user-buildable design and no independent/DIY build has been published as of 2026. All present-day DIY accessibility claims are conditional-future framing, not present-tense. TRL: 3 (Early Proof-of-Concept).

| Dimension | Best (est) | Range | Confidence |
|---|---|---|---|
| Capital cost | ~$12,000 | $8,000–20,000 | LOW |
| Per-seq cost | ~$1 | $0.50–5 | LOW |
| Expertise | 7/10 | 6–9 | MED |
| Time-to-first | ~12 weeks | 8–24 weeks | LOW |
| Usable length @ fidelity | ~13–17 nt (demonstrated) | not established | LOW |
| Yield | ~85–90%/cycle | 70–95% | LOW |

Cost figures are coarse component-level estimates extrapolated from the source paper; no operational data exists. Requires electrochemistry expertise uncommon in synthetic biology. Oversight-evasion / supply-chain (R0/R1): not scored with confidence at TRL 3; treated as conditional-future. If matured and classified as a benchtop device, R1's on-device logic would in principle reach it; if it remained portable/bespoke, enforcement reach would be lower. Scenario note, not a finding.

### 2.4 Enzymatic DNA synthesis — service model (TRL 5)

**Technology.** Terminal deoxynucleotidyl transferase (TdT) in a template-independent, single-nucleotide-addition cycle (Palluk, Arlow, de Rond et al., 2018, Nature Biotechnology 36:645–650). Delivered commercially as a service by Ansa Biotechnologies (clonal DNA up to ~50 kb via assembly; direct synthesis ~900 bp). TRL 5 (emerging technology; a commercial enzymatic service is operational, but the enzymatic synthesis technology is scored as emerging — TRL 5 — consistent with the literature review).

| Dimension | Value | Range | Confidence |
|---|---|---|---|
| Capital (customer) | $0 (service) | — | HIGH |
| Cost per usable base | $0.13–0.38/bp (clonal, length-tiered); $195/construct ≤1.5 kb | — | VENDOR |
| Expertise | 2/10 | 1–3 | HIGH |
| Turnaround | ~7 days | 3–14 d | MED |
| Usable length @ high fidelity | verified product (service) | — | MED |
| Assembled length (OOS) | up to ~50 kb via assembly | — | MED |

**Oversight-evasion (R0 → R1).** R0: evasion Low, supply-chain vulnerability Low (the provider is the controllable chokepoint; Ansa screens voluntarily as an IGSC-aligned provider). R1: evasion Very Low, supply-chain vulnerability Very Low (mandatory screening + federal enforcement make the service model more controllable; commodity enzymes/dNTPs mean provider-level screening, not supply restriction, is the lever).

### 2.5 Enzymatic DNA synthesis — benchtop instrument (TRL 5)

DNA Script SYNTAX is production-ready but not yet widely adopted. **DIY enzymatic — the honest picture.** The only off-the-shelf DIY enzymatic route (commercial TdT + natural dNTPs + apyrase; Lee et al., 2019, Nat. Commun. 10:2383) is terminator-free / kinetic — it makes stochastic homopolymer runs for data storage, not a defined sequence. Defined-sequence enzymatic (reversible-terminator or TdT–dNTP-conjugate routes) needs bespoke reagents a well-resourced lab must make or license, so enzymatic is not a low-barrier DIY path to a functional oligo.

| Dimension | Value | Range | Confidence | Note |
|---|---|---|---|---|
| Capital | €250K cloud / €280,500 on-premises (~$270–303K) | — | VENDOR QUOTE | DNA Script quote, Jul 2026; corroborates IFP $292K. Cloud routes sequences via DNA Script cloud (screenable); on-premises air-gapped |
| Cost per usable base | €0.11–0.26/base (~$0.12–0.28) incl. kits | best €0.11 (384-plex) / €0.19 (120 nt Hi-Fi) | VENDOR QUOTE | kit €1,400 (12,000 bases, ~4 runs) + run kits €150–1,094 |
| Expertise | 5/10 | 4–7 | MED | closed proprietary system |
| Time-to-first | 3–5 days | 1–7 d | MED | |
| Usable length @ high fidelity | 80–120 nt (oligo) | 15–120 nt | MED–HIGH | not 10 kb; kilobase output is assembly (OOS) |
| Throughput | 96 parallel | — | HIGH | |
| Yield (per-cycle) | ~95%+ | 90–99% | HIGH | |

**Note — benchtop ≠ DIY.** The SYNTAX system is purchasable but not independently reproducible: it runs on proprietary reagent cartridges under licensing, so the consumable is a closed chokepoint. A lab cannot "do it on their own" — it buys (or acquires secondhand) a device gated by a controlled consumable. Its DIY-relevance is through acquisition, not reproduction. Oversight-evasion / supply-chain. R0 evasion Medium (distinctive but unmonitored equipment) → R1 evasion Low (on-device mandate applies). Supply-chain vulnerability Low → Very Low as control moves to the device/manufacturer and to proprietary-reagent KYC.

### 2.6 DropSynth (emulsion assembly, TRL 4)

**Technology & status.** DropSynth builds gene-length fragments by compartmentalizing and assembling microarray-derived oligos in emulsions (Sidore, Plesa, Samson, Lubock & Kosuri, 2020, Nucleic Acids Research 48(16):e95, DOI 10.1093/nar/gkaa600). It is an assembly method on an upstream oligo-pool source, not a standalone de novo synthesizer. TRL 4 (lab-validated research prototype); benchtop DIY feasibility is high-uncertainty.

| Dimension | Value (est) | Range | Confidence |
|---|---|---|---|
| Capital (bead pool) | ~$3,400 | $3-4K | MED |
| Cost per usable base | $1.24/gene (384-plex); $0.72/gene (1,536-plex) incl. amortised beads | — | PAPER |
| Expertise | 8/10 | 7–9 | MED |
| Time-to-first | ~16 weeks | 8–26 wk | LOW |
| Usable length @ high fidelity (building block) | short oligos; gene-length via assembly (OOS) | — | LOW |
| Throughput | 100s–1000s (pooled) | — | MED |
| Yield | ~95% | 90–98% | MED |

Uses only a standard molecular-biology kit (thermocycler, magnet, vortex, gel) plus the ~$3,400 barcoded-bead pool (a consumable, ~200 reactions) — the bead-pool prep is the fiddly step; compartmentalization is by vortexing into a water-in-oil emulsion, with no microfluidic chip and no cleanroom. Fidelity is error-correction-dependent. A 2025 standard-lab alternative, OMEGA (Romero lab, bioRxiv 2025), does pooled Golden-Gate assembly without beads or emulsion at ~$1.50/gene, up to ~2.6 kb.

[[R**Input-oligo fidelity sets the ceiling (Calin [surname/affiliation TBC], personal communication, Jul 2026).** A DropSynth practitioner confirms the binding constraint is input-oligo quality, not the assembly chemistry, which is now optimised to add few errors of its own. Input errors pass through and compound: if the input oligos are X% perfect and a gene assembles from N of them, the product is at best X^N perfect, and the errors are dominated by deletions (frameshifts) that most biological systems tolerate poorly. So DropSynth carries a hard fidelity floor set by its oligo source. Oligos from electrochemical-deprotection array vendors (GenScript/CustomArray, LinkZill) have deletion rates too high to use; they produce garbage in assembly, consistent with the high electrochemical deletion rate in Ch.4 §4.1(d) (~1.35%/nt reported; 0.835%/nt in our reproduction). Only a few vendors reliably clear the roughly 1-in-500-bp array-oligo error floor: Twist, Agilent, and Dynegene. Fishing a single perfect gene out of a dirty pool by dial-out PCR runs about 70% success for products under ~1 kb, and only when perfects are present and observable at the sequencing depth and diversity bottleneck; selection helps less than assumed (transformation bottlenecks, cheating cells, hitchhikers/parasites). For governance this tightens the "inherits the perimeter" reading rather than loosening it: usable DropSynth output needs high-fidelity commercial array input from a short, screenable vendor list.R]]

### 2.7 Commercial benchtop (chemical-based, TRL 9)

**Technology & status.** Mature phosphoramidite instruments (e.g. MerMade/LGC, Dr Oligo/Biolytic, Kilobaser), qualified for high-throughput synthesis with >99% per-cycle yield and QC. TRL 9 (mature, production-qualified commercial instruments — decades-established phosphoramidite chemistry); major vendors offer screened devices.

| Dimension | Value | Range | Confidence | Source |
|---|---|---|---|---|
| Capital | ~$60,000 | $15–150K | MED | Kilobaser ~$35,500 (Basic; ~$49,500 Extended). MerMade/Dr Oligo quote-only. Tier to MerMade-class ~$120K+ |
| Cost per usable base | ~$0.30/bp (market est.) | $0.05–1 | MARKET | cf. mail-order provider $0.07–0.10/bp (sourced, verified) |
| Expertise | 2/10 | 1–4 | HIGH | highly automated |
| Time-to-first | 1–2 days | 0.5–3 d | HIGH | overnight cycle |
| Usable length @ high fidelity | ~100–150 nt | 50 nt–~1 kb spec | HIGH | model-dependent |
| Throughput | model-dependent (1–48 columns typ.) | — | MED | |
| Yield (per-cycle) | ~99% | 98–99.5% | HIGH | QC-maintained |

IFP (2024) separately modeled a predicted cost distribution for a hypothetical 5-kbp benchtop synthesizer in 2030, with the density peaking near ~$190,000 (2024 USD), 25th–75th-percentile ~$112,000–$298,000. (This $190K is a 2030 forecast for a future device, not a price for any shipping instrument.) Oversight-evasion (R0 → R1). R0: evasion Medium, supply-chain vulnerability Low (manufacturer is a single controllable integration point, but voluntary screening is uneven and federal enforcement is absent). R1: evasion Low, supply-chain vulnerability Very Low (mandatory compliance + on-device screening make manufacturer-level control durable).

**Figure 1.2** — Instrument capital cost only (not a price-per-product comparison; see Figure 1.7). [[R(Regenerated: MAS 2.0 corrected from ~$30K to the sourced ~$175K instrument figure, whisker to ~$326K fully-loaded.)R]]

**Figure 1.3** — Expertise barrier to DIY use (scores defined by the §2.8 rubric).

### 2.8 How the expertise scores were assigned (rubric)

The 1–10 "expertise required" score is a judgement, not a measured quantity — no paper reports it. To make it reproducible rather than arbitrary, each method is scored against a defined scale and four sub-dimensions, and the composite is the level a competent operator would need to obtain usable product from a standing start.

| Band | Meaning |
|---|---|
| 1–2 — minimal | Push-button. Upload/submit a sequence and receive DNA, or load a cartridge and press start. No build, no troubleshooting. |
| 3–4 — basic | Standard lab competence; follow an established protocol; routine handling and QC. |
| 5–6 — moderate | Solid molecular-biology skill plus instrument setup/calibration or reagent handling, with some troubleshooting; or operating a closed instrument whose output still needs molecular-biology competence to use. |
| 7–8 — high (multi-domain) | Two or more specialist domains at once (wet chemistry + electrochemistry/hardware, or microfluidics + bioinformatics); device build or fabrication; significant iterative troubleshooting. |
| 9–10 — frontier | Research-grade custom fabrication plus deep domain expertise; not reproducible without specialist training. |

Sub-dimensions considered: (i) molecular-biology / wet-lab skill; (ii) hardware / engineering / fabrication; (iii) bioinformatics / computational; (iv) turnkey vs. troubleshooting.

| Method | Wet-lab | Hardware/fab | Bioinformatics | Turnkey? | Score | Why |
|---|---|---|---|---|---|---|
| Mail-order provider | none | none | minimal | fully | 1–2 | Submit sequence online, receive verified DNA. Baseline. |
| Enzymatic service (Ansa) | none | none | minimal | fully | 2 | Send sequence, receive clonal DNA; no in-house capability needed. |
| Commercial benchtop (column) | low | low (vendor-maintained) | none | mostly | 2 | Turnkey automated instrument; load reagents, run overnight cycle. |
| Enzymatic benchtop (SYNTAX) | moderate | low (vendor-maintained) | low–moderate | mostly | 5 | Push-button instrument, but a closed proprietary system; operator needs MB competence to design/use the oligos. |
| OpenIDS (inkjet) | moderate | moderate–high (must build the device) | low | no | 6 | Build from 3D-printed parts + Arduino/Pi + printhead, then run wet chemistry with calibration; designed as "non-expert buildable." |
| Electrochemical | moderate | high (custom build; no product) | low | no | 7 | Pre-commercial: electrochemistry expertise uncommon in synbio + bespoke build + wet chemistry, no turnkey path. |
| DropSynth | moderate | low (standard mol-bio kit; no fabrication) | high (pool design, 12-nt barcoding, assembly & error analysis) | no | 8 | Stacks heavy bioinformatics on top of careful bench execution — not fabrication. |

## 3. Cost trajectory & learning curve

### 3.1 Historical DNA synthesis cost decline

Commercial DNA-synthesis cost per base has fallen to the order of a few cents per base for standard commodity oligos, tracked by Carlson/Field at synthesis.cc. Verify the exact current figure at synthesis.cc before quoting a number; use the trajectory for shape, not a point forecast.

### 3.2 Learning-curve DIY projections (conditional, with bands)

Cost is modeled as declining with cumulative volume, conditional on continued development and gated by TRL — low-maturity approaches receive no point-estimate futures.

| Approach | 2026 | 2028 (conditional) | Basis |
|---|---|---|---|
| OpenIDS | ~$18–22K | ~$15–18K if OSS development continues | Kim 2024 → OpenIDS2 2025 |
| Electrochemical | ~$10–15K (est) | ~$8–10K only if TRL advances 3→5–6 | no commercial benchmark; TRL 3 caveat |
| Enzymatic benchtop | ~$250–292K | ~$180–250K if enzyme costs fall + scale | $292K base (IFP 2024) |
| Commercial benchtop | ~$15–150K (best ~$60K) | ~$15–120K (slow decline) | device tier varies |

### 3.3 DNA sequencing as analog (NHGRI)

NHGRI's cost per genome fell ~5 orders of magnitude over ~20 years — ~$95M (2001) → ~$10M (2007) → ~$0.75M (Oct 2008, NGS inflection) → ~$50K (2010) → ~$4K (2015) → a few hundred dollars recently (Wetterstrand, NHGRI). NHGRI stopped updating in 2022; use for curve shape, not extrapolation, and anchor synthesis-specific projections to synthesis.cc.

**Figure 1.4** — Cost trajectories: conditional DIY/benchtop projections vs. the sequencing-cost analog. [[R(Regenerated: MAS 2.0 added as a DIY capital anchor — flat line at ~$175K, single 2026 anchor with no OSS trajectory.)R]]

### 3.4 Cost per usable base — the like-for-like comparison (sourced methods only)

Capital cost (Figure 1.2) and the per-sequence figures are on different scales and cannot be compared directly, because two approaches (mail-order providers, the Ansa service) have no capital cost while the others are dominated by it, and the per-unit figures mix per-oligo, per-bp, per-synthesis and per-run units. The common unit is cost per usable base — full-length, and (for anything assembled) error-corrected and verified — modelled in two parts: cost per usable base = (consumable cost per usable base) + (capital ÷ cumulative usable bases synthesised).

Because the capital term shrinks with volume, the honest output is a curve, not a single price. Only three methods can be placed on this axis from sourced numbers: mail-order providers ($0.07–0.10/bp; Twist list, magnitude Kosuri & Church 2014), OpenIDS (capital $19,900 and run cost $102.61 from Kim 2024, with a derived 55% full-length fraction), and DNA Script as a capital floor only. (The ~55% derived full-length fraction for the OpenIDS cost model and the ~56% OpenIDS2-measured value in §2.1 refer to different builds; both are approximate.)

**Figure 1.7** — Cost per usable base vs synthesis volume (sourced methods only). [[R(Regenerated: MAS 2.0 added as a capital-floor-only curve, same treatment as DNA Script — ~$175K capital, no published per-base consumable, so a lower bound only.)R]]

Providers sit flat at $0.07–0.10/bp and deliver assembled, verified DNA; OpenIDS undercuts them only above ~480,000 usable bases (~200 runs), and even then produces raw short oligos, not genes — so the two are not the same product.

**Applying it to a viral genome (two layers).** Beyond short oligos, a viral-length construct needs assembly, error-correction, verification and — above ~7–10 kb — bacterial/yeast host systems (NTI 2023), which are out of scope. The only fully-sourced figure is the commercial-provider cost (which already includes their assembly and screening):

| Reference genome | Length | Provider cost ($0.07–0.10/bp) | Note |
|---|---|---|---|
| Single gene | 1.5 kb | $105–150 | routine clonal order |
| IFP benchmark / small construct | 5 kb | $350–500 | within single-clonal range |
| Picornavirus (poliovirus-scale) | 7.5 kb | $525–750 | near the synthesis/assembly boundary |
| Coronavirus (SARS-CoV-2-scale) | 30 kb | $2,100–3,000 | exceeds single-clonal limits; fragments + host assembly |

A DIY route cannot be quoted as "$/bp × length": the oligos are the cheap part (~$0.044/usable base at volume), and the cost is dominated by the unpriced assembly, error-correction and host-system pipeline — which is exactly why the project scopes to the synthesis step.

## 4. Regime-conditional oversight-evasion & supply-chain analysis

Scoring uses qualitative bands, not a numeric scale. The policy-relevant quantity is the R0→R1 delta.

### 4.1 Oversight-evasion delta (R0 → R1)

| Approach | R0 (evasion) | R1 (evasion) | Delta | Mechanism (conditional on R1) |
|---|---|---|---|---|
| OpenIDS | Medium | Low | Tightens | on-device screening reaches synthesis |
| MAS 2.0 | Medium | Low | Tightens | On-device screening reaches a visible bench build |
| Electrochemical | High* | Medium* | Mixed | *conditional-future (TRL 3) |
| Enzymatic (service) | Low | Very Low | Tightens | mandatory provider compliance |
| Enzymatic (benchtop) | Medium | Low | Tightens | on-device mandate |
| DropSynth | Medium | Low | Tightens | Inherits the perimeter via its commercial oligo-pool input; expertise barrier |
| Commercial | Medium | Low | Tightens | mandatory manufacturer compliance |

**Figure 1.5** — Oversight tightens under R1 (dot = R0 → arrow = R1).

### 4.2 Supply-chain vulnerability — the governance conclusion

**Finding (HIGH confidence):** supply-chain restriction is not a durable control point under either regime. The reasoning is structural: the inputs common to these methods are substitutable or commodity, so a restriction on any single input is routed around rather than enforced. This holds for the solvent (an unregulated substitute is demonstrated), for the core reagents and enzymes/dNTPs (many suppliers, ordinary research reagents), and for device components (multiple industrial suppliers with non-synthesis uses). The one partial exception is specialized fabrication — the custom CMOS/microelectrode arrays an electrochemical synthesizer would need, and the optics/photolabile-amidite chain for photolithographic (MAS 2.0) — which retains a genuine access barrier, but is method-specific.

| Input category | Durable as a standalone control? |
|---|---|
| Solvents (incl. GRAS substitutes) | No |
| Core reagents (phosphoramidites) | No |
| Enzymes / dNTPs | No |
| Device components (printheads, electrodes) | No (weak at best) |
| Specialized fabrication (CMOS electrodes; photolithography optics) | Partial (method-specific access barrier) |

**Implication:** because supply-chain chokepoints are not durable, the sustainable levers are device-level screening, mandatory provider compliance, and functional detection — i.e., exactly where R1 is directed.

## 5. Timelines & inflection points

### 5.1 Present-day "accessible" status (2026)

| Approach | Status | Note |
|---|---|---|
| OpenIDS | Accessible (DIY) | TRL 5, demonstrated (short oligos) |
| MAS 2.0 | [[RAccessible only to well-resourced labs (open build, but ~€200–300K and optics-alignment-gated; no independent build yet)R]] | TRL 5, photolithographic (developer interview, Jul 2026) |
| Enzymatic (service) | Accessible (service) | no capital; ~$300/synthesis |
| Enzymatic (benchtop) | Capital-expensive, not DIY | TRL 5; ~$292K |
| Commercial | Mature (baseline) | TRL 9; not accessible to all labs, not DIY |
| Electrochemical | Conditional-future | TRL 3 |
| DropSynth | Assembly (needs commercial oligo pool) | TRL 4; standard mol-bio lab, no fabrication; expertise-gated |

### 5.2 Governance inflection points

**OSTP framework 50-nt milestone — October 13, 2026 (documented, but paused).** The April 2024 framework scheduled the 200→50-nt window reduction and the expansion to functional SOC definitions for October 13, 2026 (three years after the October 2023 HHS Guidance). IGSC members are required to align by October 24, 2026 (IGSC v3.0). EO 14292 (May 5, 2025) paused implementation and directed OSTP to revise or replace the framework, so whether the October 2026 milestone takes effect on schedule now depends on the revised framework — unpublished as of July 2026.

**Already established (not future):** the NIST inter-tool benchmark of screening software is published — Laird et al., Applied Biosafety (2025), DOI 10.1177/15356760251401228 — reporting >95% sensitivity and >97% accuracy, with most tools already screening to 50 nt. This supersedes any "NIST validation pending" framing. What remains open is functional detection: Wittmann et al. (2025, Science 390:82–87) showed that similarity-based screening can be evaded by AI-designed protein variants, with ~3% of the more-probably-functional variants still escaping detection after coordinated patching — the gap the October 2026 functional-SOC provision is meant to close. 2027–2030 (projected): device-screening adoption matures; DIY-cost trajectories evolve as in §3.2, all conditional.

## 6. Confidence, uncertainty & worst-case test

**Figure 1.6** — Confidence in each estimate.

High confidence: OpenIDS (TRL, capital, yield); enzymatic benchtop (TRL, throughput, expertise, turnaround); commercial (TRL, expertise, yield); the non-durability of supply-chain restriction. Medium confidence: enzymatic per-synthesis and capital costs; DropSynth expertise/timeline; the R0/R1 evasion scoring (modeled from policy documents, not observed). Low confidence: electrochemical (all value dimensions except the TRL-3 assessment itself); DropSynth DIY feasibility and cost trajectory; all 2028–2030 cost projections.

**Worst-case survival test (headline claim).** The headline — at least one demonstrated route (OpenIDS, TRL 5) reaches useful capability without a single durable supply-chain chokepoint, so control must move to the device and to attribution — is tested against the least-favorable bounds of the weak inputs. Setting electrochemical to $30K and TRL 2 leaves the headline unaffected, because it rests on OpenIDS (HIGH-confidence) and the commodity/substitutable nature of shared inputs. Setting OpenIDS capital to its upper bound ($25K) and per-seq to $10 still leaves an accessible, demonstrated route with no single controllable input. The qualitative headline survives; what does not survive worst-case is any quantitative ranking of evasion across methods — hence evasion is reported in bands and deltas, not scores.

## 7. Synthesis & policy implications

**7.1 Durable vs. illusory control points.** Durable (conditional on R1 implementation): on-device screening; mandatory provider/manufacturer compliance with federal enforcement; functional-SOC detection (needed because similarity screening has a demonstrated AI-design gap, Wittmann et al., 2025); international coordination. Illusory: supply-chain restriction on solvents, core reagents, enzymes/dNTPs, and device components, for the structural reasons in §4.2.

**7.2 The jurisdictional ceiling makes international coordination non-optional.** International coordination is not a soft add-on. The companion manufacturer-landscape analysis finds that a US mandate directly binds only 8 of 34 known benchtop manufacturers, with 14 outside US and allied reach and the newest, highest-throughput capacity concentrating outside reach. Device-level control therefore has a hard ceiling that only harmonisation can raise.

**7.3 Forensic-attribution gap.** Synthesis chemistry leaves condition-dependent error signatures (e.g. the capping-driven G→A phenotype, Masaki et al., 2022), suggesting method-level attribution may be feasible from product-sequence data. No synthesis-method error-signature catalogue or attribution framework yet exists; Chapter 4 develops that specification as a complement to prevention.

## 8. Summary table

| Dimension | OpenIDS | MAS 2.0 | Electrochemical | Enz. (service) | Enz. (benchtop) | DropSynth | Commercial |
|---|---|---|---|---|---|---|---|
| TRL | 5 [HIGH] | 5 [MED] | 3 [LOW*] | 5 [HIGH] | 5 [HIGH] | 4 [MED] | 9 [HIGH] |
| Capital | $20K [15–25K] | [[R~€150–170K instr [~€200–300K loaded; sourced]R]] | ~$12K est [8–20K] | $0 | ~$292K [single est.] | ~$3,400 | ~$60K [15–150K] |
| Cost/usable base | ~$0.044 floor | not reported | array $0.00001–0.001/base (diff. context) | $0.13–0.38/bp (Ansa) | consumable unpub. | $0.72–1.24/gene (Sidore 2020) | ~$0.30/bp (market) |
| Expertise | 6/10 | 8/10 | 7/10 | 2/10 | 5/10 | 8/10 | 2/10 |
| Time-to-first | ~4 wk | ~8–16 wk | ~12 wk | ~7 d | 3–5 d | ~16 wk | 1–2 d |
| Usable length @ hi-fi | ~15–30 nt | Library grade | not established | verified (service) | 80–120 nt | short (assembly OOS) | ~100–150 nt |
| Throughput | ~144/array | [[Rhigh (array); up to 0.79–2.07M seqsR]] | — | N/A (service) | 96 parallel | 100s–1000s | 1–48 columns |
| Yield (per-cycle) | ~98% | Photolimited | ~85% est | provider-side | ~95%+ | ~95% | ~99% |
| Evasion (R0) | Medium | Medium | High* | Low | Medium | Medium | Medium |
| Evasion (R1) | Low | Low | Medium* | Very Low | Low | Low | Low |

Electrochemical/DropSynth values are conditional-future (TRL 3/4); evasion scores are scenario notes, not findings.

**TRL note.** These seven approaches match the literature review's readiness scores: OpenIDS 5, electrochemical 3, enzymatic 5, DropSynth 4, commercial benchtop 9. The literature review additionally scores the centralized mail-order commercial provider (Twist/IDT/GenScript) at TRL 9 as the screened baseline; it is not a benchtop approach and so is not scored as a separate row here.

## 9. Conclusion

This TRI characterizes seven oligonucleotide-synthesis approaches under a governance transition from R0 (observed) to R1 (projected). Present-day accessibility: OpenIDS (DIY, ~$20K) and enzymatic services (~$300/synthesis) are the accessible routes; electrochemical (TRL 3) and DropSynth (TRL 4) are conditional-future; the enzymatic benchtop instrument is real but capital-expensive (~$292K)[[R; MAS 2.0, though open-source, is now known to be a ~€200–300K, optics-alignment-gated build with no independent replication yet — a lab capability, not a garage oneR]]. R0→R1 delta: if implemented as projected, on-device screening plus mandatory enforcement tightens oversight for device-based methods and makes service-based synthesis more controllable, while supply-chain restriction stays ineffective. Durable architecture: device-level detection + mandatory provider/manufacturer screening + functional-SOC detection + international coordination (the last made non-optional by the 8-of-34 jurisdictional ceiling). Attribution gap: no synthesis-method error-signature framework exists; Chapter 4 develops one.

**Confidence, split honestly.** HIGH that supply-chain restriction is not a durable control point (structural; survives worst-case). MEDIUM / conditional that R1 device-level control will prove effective — this depends on the OSTP framework revision being issued and implemented as projected, and on S. 3741 (or equivalent) being enacted, neither of which has occurred. The chapter does not claim R1 works; it claims R1 is aimed at the right lever.

## References

**Peer-reviewed.** Palluk, S., Arlow, D. H., de Rond, T., et al. (2018). De novo DNA synthesis using polymerase–nucleotide conjugates. Nature Biotechnology, 36(7), 645–650. https://doi.org/10.1038/nbt.4173 · Kim, J., Kim, H., & Bang, D. (2024). An open-source, 3D printed inkjet DNA synthesizer. Scientific Reports, 14, 3773. https://doi.org/10.1038/s41598-024-53944-x · Kim, J., Kim, H., & Bang, D. (2025). OpenIDS2. PLOS ONE, 20, e0338478. https://doi.org/10.1371/journal.pone.0338478 · Sidore, A. M., Plesa, C., Samson, J. A., Lubock, N. B., & Kosuri, S. (2020). DropSynth 2.0. Nucleic Acids Research, 48(16), e95. https://doi.org/10.1093/nar/gkaa600 · Plesa, C., et al. (2018). Multiplexed gene synthesis in emulsions. Science, 359(6373), 343–347. https://doi.org/10.1126/science.aao5167 · Somoza, M. M., et al. (2024). An open-source advanced maskless synthesizer. ChemRxiv. https://doi.org/10.26434/chemrxiv-2024-j4c90 · Lietard, J., et al. (2021). Chemical and photochemical error rates in light-directed synthesis. Nucleic Acids Research, 49(12), 6687–6701. https://doi.org/10.1093/nar/gkab505 · Lausted, C., et al. (2004). POSaM. Genome Biology, 5(8), R58. https://doi.org/10.1186/gb-2004-5-8-r58 · Xu, C., et al. (2021). Electrochemical DNA synthesis and sequencing on a single electrode. Science Advances, 7(46), eabk0100. https://doi.org/10.1126/sciadv.abk0100 · Masaki, Y., Onishi, Y., & Seio, K. (2022). Quantification of synthetic errors. Scientific Reports, 12, 12095. https://doi.org/10.1038/s41598-022-16222-2 · Lee, H. H., et al. (2019). Terminator-free template-independent enzymatic DNA synthesis. Nature Communications, 10, 2383. https://doi.org/10.1038/s41467-019-10258-1 · Kosuri, S., & Church, G. M. (2014). Large-scale de novo DNA synthesis. Nature Methods, 11(5), 499–507. https://doi.org/10.1038/nmeth.2918 · Sandahl, A. F., et al. (2021). On-demand synthesis of phosphoramidites. Nature Communications, 12, 2760. https://doi.org/10.1038/s41467-021-22945-z · Wittmann, B. J., et al. (2025). Strengthening nucleic acid biosecurity screening against generative protein design tools. Science, 390(6768), 82–87. https://doi.org/10.1126/science.adu8578 · Laird, T. S., et al. (2025). Inter-tool analysis of a NIST dataset. Applied Biosafety. https://doi.org/10.1177/15356760251401228 · Romero, P. A., et al. (2025). OMEGA. bioRxiv (preprint).

**Policy & grey literature.** Executive Order 14292 (2025). Federal Register, 90 FR 19611 (May 8, 2025). · U.S. Congress (2026). S. 3741, 119th Congress. https://www.congress.gov/bill/119th-congress/senate-bill/3741 · OSTP (2024). Framework for Nucleic Acid Synthesis Screening. https://aspr.hhs.gov/S3/ · IGSC (2024). Harmonized Screening Protocol v3.0. https://genesynthesisconsortium.org/ · Langenkamp, M. / IFP (2024). Securing Benchtop DNA Synthesizers. https://ifp.org/securing-benchtop-dna-synthesizers/ · NTI | bio (2023). Benchtop DNA Synthesis Devices.

**Industry & cost data.** Ansa Biotechnologies (2025). https://ansabio.com/ · DNA Script (2025). SYNTAX System. https://www.dnascript.com/products/syntax/ · [[RHelices Biological Photolithography GmbH (2026). MAS 2.0. https://helicesbio.com/ (capital + specs from founder interview, Jul 2026).R]] · Field, J. / Carlson, R. DNA synthesis cost tracking. http://www.synthesis.cc

[[R— Red text marks what changed in this revision. All changes concern MAS 2.0 capital cost, corrected from the earlier "tens of $K / ~$30K" estimate to a sourced ~€150–170K instrument (~€200–300K fully-loaded) figure, from a July 2026 interview with co-founder Mark Somoza (Helices Biological Photolithography GmbH, helicesbio.com) and the ChemRxiv component list — updated in §2.2 (table + prose + new spec rows), §5.1, the §8 summary table, the conclusion, and the references, and reflected in regenerated Figures 1.2, 1.4, and 1.7 (MAS 2.0 now shown at the corrected capital and added to the trajectory and cost-per-base figures). Also: §2.7 rubric renumbered to §2.8 (it previously duplicated the §2.7 commercial-benchtop number). No other claims were altered.R]]
