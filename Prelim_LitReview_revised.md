# Preliminary Literature Review: DIY DNA Oligonucleotide Synthesis

*Revised 2026 — scope realigned toward DIY / accessible in-house synthesis; corrected against a 2026 deep-research survey (see change notes in-line). Commercial benchtop and provider rows are retained only as the screenable baseline for contrast.*

## Table A — Capability and accessibility by synthesis approach

| Technology | Method (how it works) | Cost (capital / per-seq) | Usable length @ high fidelity | Material acquisition | Protocol accessibility |
|---|---|---|---|---|---|
| **OpenIDS v1** | Inkjet printhead deposits phosphoramidite chemistry onto silicon-wafer spots; 3D-printed frame, Arduino/Pi control; array format | ~$20K / ~$1–15 | **~20–30 nt** (demonstrated only a poly-dT 30-mer; ~98%/step → ~55% full-length at 30, <40% at 50) | Medium — industrial inkjet printhead is the chokepoint; reagents commodity | Medium — open-source, "non-expert" buildable, but anhydrous wet chemistry + calibration non-trivial |
| **OpenIDS v2** | 2nd-gen OpenIDS: ~⅓ volume, custom PCB, 3D-printed peristaltic pumps; same inkjet-microarray chemistry | **~$4K** / ~$12 | ~15–25 nt (validated on a 15-mer poly-dT, ~56% full-length, ~96%/step) | Medium — as v1 | Medium — more reproducible/accessible than v1 (full open Gerber/CAD/BOM/code) |
| **MAS 2.0 / AMS** *(new — 2024)* | Open-source **photolithographic** (light-directed) synthesizer: a DMD patterns 365 nm UV to photo-deprotect features (NPPOC amidites), no physical masks | ~tens of $K (component list in supplement) / — | library-grade (error-prone; handled by downstream selection) | Medium — off-the-shelf optics + specialty photolabile amidites; **no cleanroom** | Medium — full open CAD/STL/software + chemistry manual; optics alignment is the barrier |
| **DropSynth** | Assembles **commercial** microarray-derived oligos into genes: barcoded magnetic beads pull each gene's oligo set into a **vortex-made** water-in-oil emulsion, then PCA/Golden-Gate assembly | **~$3.4K bead pool** (~200 rxns) / **~$1–2 per gene** | Gene-length (~1–3 kb) from short blocks — fidelity ~25% perfect, error-correction-dependent | Medium — needs a **commercial oligo-pool source**; assembly is **standard mol-bio kit + vortex — no microfluidic chip, no cleanroom** | Moderate — bead-pool prep is fiddly; downstream is routine PCR/gel + bioinformatics |
| **Electrochemical** | Phosphoramidite chemistry with electrochemically-generated-acid deprotection on electrode arrays | ~$10K / ~$5 (est.) | Not established (TRL 3) — 13–17-mer academic demos only | High ease — commodity electrodes (why it is concerning *if* it matures) | **No independent DIY build published** — academic + defunct-commercial only |
| **Enzymatic (TdT)** | Template-independent polymerase adds nucleotides in aqueous conditions | *Commercial:* ~€250–280K instrument / €0.11–0.26 per base (DNA Script vendor quote). *DIY route:* low capital | *Commercial (SYNTAX):* 80 nt Standard / 120 nt Hi-Fi. *DIY (Church route):* not defined-sequence | *Commercial:* proprietary enzyme/cartridge = licensing chokepoint. *DIY:* off-the-shelf TdT/dNTPs/apyrase | **Benchtop ≠ DIY** (closed cartridge). Only the Church terminator-free route is off-the-shelf, and it is **data-storage only** (see §1.4) |
| **Commercial benchtop** (column phosphoramidite, e.g. Kilobaser, MerMade) | Standard solid-phase phosphoramidite column synthesis in a benchtop box | ~$15–150K (best ~$60K; used $15–30K) / varies | ~100–150+ nt at good fidelity — mature | Medium — reagents commodity; instruments on used/eBay market | Medium–High — turnkey, established (baseline, not DIY) |
| **Commercial provider** (mail-order, e.g. Twist/IDT/GenScript) | Centralized industrial synthesis + gene assembly; order online, receive DNA | none / ~$0.07–0.10 per bp | Genes/genomes, high fidelity (the benchmark) | N/A (service) | Highest ease — but this is the screened channel (IGSC / SecureDNA) |

**How to read Table A (DIY focus).** The genuinely DIY-reproducible *de novo* synthesizers are **OpenIDS/OpenIDS2** (inkjet) and **MAS 2.0** (photolithographic). **DropSynth** is DIY-reproducible *gene assembly* but still consumes a commercial (screenable) oligo pool. Enzymatic-benchtop and both commercial rows are the **screenable baseline**, shown only for contrast. *Are these the only DIY routes?* Effectively yes for reproducible published builds — a 2026 survey found no working homebrew/garage synthesizer beyond these academic open-hardware platforms plus DropSynth-style assembly (§5). *OOS = out of scope.*

## Table B — Risk and readiness (the biosecurity read)

| Technology | TRL | Assembly readiness | Detectability | Control / biosecurity note |
|---|---|---|---|---|
| **OpenIDS v1 / v2** | 5 | Low — short (~15–30 nt), ~55% full-length; not directly gene-assembly-ready | Moderate | Visible bench kit; printhead sourcing traceable; low assembly-readiness caps the threat |
| **MAS 2.0 / AMS** | 5–6 (open build) | Medium — library-grade output for assembly | Moderate | Fully open photolithographic build; optics + photolabile-amidite barrier; the DIY twin of the array/photolith class |
| **DropSynth** | 4 | High (it *is* assembly) — but gated by expertise + a commercial oligo pool | Moderate | Assembles genes (higher intrinsic risk) but **inherits the screening perimeter via its oligo-pool input**; not DIY-adopted |
| **Electrochemical** | 3 | Unknown (pre-commercial) | High (≈9/10, near-invisible) | Highest *potential* concern — portable, commodity materials — but **no DIY build exists**; conditional-future (see Part 2) |
| **Enzymatic** | 5 (commercial) / low (DIY) | Commercial: Medium–High. DIY: low (data-storage only) | Low–Moderate | Enzyme/cartridge licensing is a genuine control point; **defined-sequence enzymatic needs bespoke reagents a well-resourced lab must make** |
| **Commercial benchtop** | 9 | High — long, high-fidelity, directly assembly-ready | Low | The real near-term concern — mature, ≥150 nt, assembly-ready, largely unscreened, resale market (baseline) |
| **Commercial provider** | 9 | Highest — delivers assembled constructs | Low | Baseline + the currently-screened chokepoint; R0/R1 controls act here (IGSC ~80% capacity) |

---

## PART 1: CORE TECHNOLOGY LANDSCAPE

### 1.1 OpenIDS: Inkjet-Based Synthesis (TRL 5 — Demonstrated)

**Primary Reference:** Kim, J., Kim, H., & Bang, D. (2024). "An open-source, 3D printed inkjet DNA synthesizer." *Scientific Reports*, 14, 3773. https://doi.org/10.1038/s41598-024-53944-x

**Key Technical Specifications:**
- Synthesized oligonucleotides on 144 spots on a 15 × 25-mm silicon wafer filled with controlled-pore glass, with ~98% synthesis yield per cycle. *This is per-step coupling efficiency, not full-length correct-product fraction.* The two diverge sharply with length: at 98%/step a 30-mer is ~55% full-length and a 50-mer is <40%. OpenIDS2 (below) measured ~96.1%/step and only ~56% full-length for a 15-mer. **Usable high-fidelity length is therefore ~15–30 nt, and OpenIDS output is not directly assembly-ready for gene-length constructs.**
- Architecture: 3D printing, Arduino, and Raspberry Pi, with an industrial Xaar-128 inkjet printhead.
- Low production cost suits self-fabrication in academic labs; even non-experts can build and control it.

**Cost Analysis:**
- Full 5-printhead system: **~$19,900** (vs $34,000 for the earlier POSaM system, and $15–30K for used commercial synthesizers).
- Consumables ~$100–500 for the initial build; ~$1–5 per sequence at scale (1000+ sequences).

**GitHub:** https://github.com/regiregire/OpenIDS (archived, superseded by OpenIDS2).

**Follow-up — OpenIDS2 (2025):** Kim, Kim & Bang, *PLOS ONE* 20(12):e0338478. Reduces device volume to ~⅓, integrates a custom PCB, and replaces ~$4K of commercial syringe pumps with 3D-printed peristaltic pumps (<$164). **Total build cost ~$4,000 — about 20% of OpenIDS v1** *(correction: an earlier "~$12K" figure is not in the paper).* Reported ~96.1%/step; ~56.2% full-length for a 15-mer poly-dT (urea-PAGE + HPLC). Full open package (Gerber/CAD/BOM/code): https://github.com/regiregire/OpenIDS2.

**Chemistry innovation:** Propylene carbonate (PC) replaces acetonitrile as the inkjet solvent (94–98% coupling). *Biosecurity implication:* PC is a food additive / industrial solvent — effectively unregulated, unlike acetonitrile.

**Forensically relevant build detail:** the published OpenIDS protocol **omits the capping step**. Because the diagnostic G→A substitution signature of column phosphoramidite chemistry is capping-driven (Masaki et al., 2022), OpenIDS oligos are expected to carry a **distinguishable error phenotype** relative to standard capped column synthesis — the DIY-specific signature developed in the attribution framework (Chapter 4).

### 1.2 DropSynth: Emulsion Gene Assembly (Research method) — *not* a de novo synthesizer

**Primary Reference:** Sidore et al. (2020), "DropSynth 2.0: high-fidelity multiplexed gene synthesis in emulsions," *Nucleic Acids Research*, 48(16), e95 (DOI 10.1093/nar/gkaa600); orig. Plesa et al. (2018), *Science* 359:343 (DOI 10.1126/science.aao5167).

**How it works:** Genes are bioinformatically split into oligos, each tagged with a 12-nt microbead barcode common to all oligos of one gene; a **commercial microarray oligo pool** is amplified, nicked to expose the barcode, and hybridised to a pool of barcoded magnetic beads so each bead captures one gene's oligos. Beads are compartmentalised **by vortexing** into picolitre water-in-oil droplets, and the gene is assembled inside each droplet (PCA in 1.0/2.0; Golden Gate in DropSynth-Gold, 2026).

**Corrections vs the earlier draft (from 2026 verification):**
- **No microfluidic chip and no cleanroom.** The emulsion is made with a **Vortex Genie 2** and BioRad droplet-generation oil — deliberately "poor-man's" compartmentalisation. The equipment is a standard molecular-biology kit (thermocycler, magnet, vortex, gel). The earlier "microfluidic chip fabrication / fab access required" framing was **incorrect**.
- **Capital is a ~$3,400 barcoded-bead pool** (good for ~200 reactions, ~$0.04/gene amortised), **not ~$75K**; per-gene reagents+oligos are **~$1–2** (384-plex), lower at 1536-plex.
- **It is assembly, not synthesis.** DropSynth makes no new nucleotides — it multiplexes access to genes from an upstream **commercial oligo pool**, so it **inherits the screening perimeter** rather than escaping it.

**Reproducibility:** strong — now developed in the Plesa lab (U. Oregon), with open protocols/code at dropsynth.org and a commercial offering (SynPlexity, 2025). Fidelity ~23–28% perfect assemblies (2.0); newer generations reach ~1 kb (Degenerate DropSynth, 2023) and ~3 kb (DropSynth-Gold, 2026).

**2025 peer — OMEGA** (Romero lab, bioRxiv 2025, DOI 10.1101/2025.03.22.644747): pooled **Golden Gate** gene assembly with **no beads and no emulsion** (pure standard-lab), ~$1.50/gene, up to 2.6 kb, 94–97% recovery — arguably *more* DIY than DropSynth, and the main current alternative for cheap pooled gene libraries.

### 1.3 MAS 2.0 / Advanced Maskless Synthesizer — open-source photolithographic synthesis *(new)*

**Primary Reference:** Somoza group, "Advanced Maskless Synthesizer (MAS 2.0)," ChemRxiv 2024, DOI 10.26434/chemrxiv-2024-j4c90.

**How it works:** phosphoramidite synthesis using **photolabile 5′-protecting groups** (NPPOC/BzNPPOC) instead of acid-labile DMT. A **digital micromirror device (DMD)** patterns ~365 nm UV onto the substrate, photo-deprotecting only illuminated features so the next amidite couples only there ("maskless" = the DMD replaces physical photomasks). 1.5 µm feature resolution.

**Why it matters here:** this is the first **fully open-source, reproducible** photolithographic synthesizer — full CAD/STL/optical drawings, a costed component list, Python control software, and a chemistry/process manual. It uses off-the-shelf optics + a high-power UV LED and **needs no cleanroom** (unlike electrochemical). Barriers: optics alignment, DMD control, anhydrous amidite fluidics, and **specialty photolabile amidites** (available but not commodity). Capital is in the tens of $K (exact figure in the supplementary spreadsheet; flag as unverified). It is the **DIY instantiation of the photolithographic class reproduced in Chapter 4 (Lietard)** — closing the loop between the DIY landscape and the attribution atlas. Output is library-grade (error-prone, handled by downstream selection), not per-strand perfect.

*Historical predecessor:* **POSaM** (Lausted et al., *Genome Biol.* 2004, 5:R58) — the original open-source inkjet synthesizer (~$34K) OpenIDS builds on; documents that open synthesizer designs are 20 years old.

### 1.4 Electrochemical DNA Synthesis (Pre-Commercial; no DIY build)

**Technical approach:** phosphoramidite chemistry with electrochemically-generated-acid (EGA) deprotection — a positive potential at an electrode generates protons that strip the DMT group locally, giving per-pixel spatial selectivity.

**Primary Reference:** Xu et al. (2021), *Science Advances*, 7(46), eabk0100 (DOI 10.1126/sciadv.abk0100). *Context caveat:* this is a DNA data-storage demonstration synthesizing a **13-mer** on electrodes, not a general-purpose synthesizer.

**Status:** the EGA mechanism is well established — CombiMatrix/CustomArray commercialised electrochemical array synthesis (acquired by GenScript, 2017), and Egeland & Southern (2005) demonstrated 17-mers — **but a benchtop, gene-length, DIY-accessible electrochemical synthesizer remains pre-commercial, and a 2026 survey found no independent/open build published anywhere.** The barrier is custom CMOS/microelectrode fabrication (cleanroom/foundry). No such device appears in the 34-firm landscape (Part 2), corroborating the TRL-3 assessment for the DIY-relevant form. (This is the class reproduced from the *commercial* side as the Gimpel/Genscript electrochemical fingerprint in Chapter 4.)

### 1.5 Enzymatic DNA Synthesis — and whether a lab can do it alone

**Technology:** Terminal deoxynucleotidyl transferase (TdT), template-independent single-nucleotide addition — Palluk, Arlow, de Rond et al. (2018), *Nature Biotechnology*, 36(7), 645–650 (DOI 10.1038/nbt.4173).

**Can enzymatic synthesis be done independently in a lab?** The 2026 survey gives a nuanced answer:
- **Off-the-shelf DIY, but data-storage only:** the Church "terminator-free / kinetic" route (Lee et al., 2019, *Nat. Commun.* 10:2383) uses **commercial TdT + natural dNTPs + apyrase** — no engineered enzyme, no modified nucleotides. But it encodes information in nucleotide *transitions* (stochastic homopolymer runs), so it does **not** produce a defined arbitrary sequence; it needs a codec + sequencing readout. Realistic for data storage, not for making a specified oligo.
- **Defined sequence, but bespoke reagents (well-resourced lab only):** the TdT–dNTP-conjugate (Palluk 2018) and 3′-O reversible-terminator routes produce defined sequence but require **expressing engineered TdT mutants and synthesising/conjugating modified nucleotides yourself** — reproducible from the papers, but **no reagents are sold as a kit**.
- **Turnkey, but not DIY:** DNA Script SYNTAX (engineered TdT + proprietary 3′-blocked terminators + instrument) reaches 80–120 nt at high fidelity — **proprietary enzyme, nucleotides, and instrument; not reproducible**. **Benchtop ≠ DIY:** it is a purchasable device gated by a closed reagent cartridge, which is exactly why the commercial enzymatic route is *more* controllable than DIY chemical routes.

**Instrument capability (vendor-confirmed):** SYNTAX synthesizes up to 96 oligos in parallel (80 nt Standard / 120 nt Hi-Fi); instrument ~€250–280K (DNA Script vendor quote, 2026; IFP 2024 STX-200 $292,000 corroborates); on-device desalt/quant/normalise.

**Market status:** enzymatic DNA synthesis market ~USD 296M (2024) → ~USD 3.16B (2034), ~26.7% CAGR (Precedence/Mordor). Molecular Assemblies licenses its Fully Enzymatic Synthesis (FES) for on-site production (2024).

### 1.6 From Oligos to Genes: Assembly Feasibility and the Fidelity Constraint

The preceding sections characterise oligonucleotide synthesis. A biosecurity assessment scoped to the synthesis step must state clearly what stands between a DIY oligo synthesizer and a functional gene. The literature supports a precise, and for this project favourable, conclusion: **assembly of short oligos into genes is standard, decades-old methodology, but converting low-fidelity DIY oligos into a correct functional gene is gated by fidelity and by a downstream error-correction pipeline — not by the oligo length itself.**

Chemical synthesis is limited to ~200 nt, so all gene synthesis proceeds by assembling short oligos. The two routes are **polymerase cycling assembly (PCA)** (overlapping oligos extended by polymerase, then PCR) and **ligation-based assembly (LCR)** (overlapping oligos joined by ligase; lower error rate, more constrained). Both are textbook techniques used by every commercial provider.

A common assumption is that oligos shorter than ~40–60 nt cannot be assembled. The literature contradicts this as an absolute: the 901 bp GFP gene has been assembled from pools of 16-mers, 30-mers, and 40-mers via LCR + PCA + PCR (USPTO 12,018,316, Example 2). Assembly from oligos in the OpenIDS length range is therefore demonstrated in principle. The practical penalty of short building blocks is not impossibility but **multiplicity**: a 1 kb gene from 30-mers needs roughly twice the oligos and junctions of one from 60-mers, multiplying error opportunities.

**Fidelity, not length, is the binding constraint.** Assembly quality is governed by the full-length fraction of the building-block oligos, and errors compound across junctions. Standard practice targets **>90% full-length** oligos; below ~70%, redesign or a different route is indicated. This is where DIY output falls short: OpenIDS2 delivers **~56% full-length for a 15-mer** — far below assembly-grade. The consequence at scale is severe: even from decent oligos, PCA of a ~1 kb fragment yielded only **4.2 ± 2.1% correct product before error correction, rising to 31.3 ± 3.1% after two rounds** (Cui et al., 2024, PMC11547124). From ~56%-full-length building blocks the correct-assembly fraction would be substantially lower.

Recovering a correct, functional gene from low-fidelity oligos therefore requires a downstream **error-correction and verification pipeline**: enzymatic mismatch cleavage (T7 endonuclease I and comparable enzymes; benchmarked by Lubock et al., 2017, *NAR* 45(15), 9206–9217, DOI 10.1093/nar/gkx691), then clonal selection and sequence verification (Sanger/NGS) — added expertise, reagents, and instrumentation, not a further step of synthesis.

**The assembly ceiling.** Even with error correction, PCA-based assembly is practically bounded at ~7,000–10,000 bp; beyond that, reliable assembly requires bacterial and yeast host systems, and many viral sequences are toxic to those hosts (NTI, 2023, Box 4). Booting a functional infectious agent adds virus-specific expertise and mammalian cell-culture infrastructure.

**Implications (both reinforce the project design):**
1. **The binding constraint sits downstream of oligo synthesis.** DIY oligo synthesis is real; assembly of short oligos is standard; but converting DIY-grade oligos into a correct functional gene depends on an error-correction/clonal-selection/verification and (beyond ~10 kb) host-system pipeline that is expertise- and equipment-intensive — the same barrier NTI (2023) identifies. This is why the project scopes to synthesis and treats assembly/rescue as **out of scope (OOS)** — a principled boundary.
2. **Synthesis-route error signatures propagate into the assembled product.** Because assembly copies the building-block oligos (with their per-route error phenotypes) into the final construct, the synthesis-method signature is in principle detectable *after* assembly, in the sequenced gene — directly relevant to the attribution framework (Chapter 4).

---

## PART 2: Accessibility & Reach of the Commercial Benchtop Landscape *(baseline; inventory deferred to IBBIS)*

This section moves from chemistry (Part 1) to the products that instantiate it — but, per the realigned scope, it does **not** re-inventory manufacturers (the 34-firm list is compiled within the ERA/IBBIS working group; Alexanian, 2026). The contribution here is the **accessibility-and-reach scoring** — jurisdiction, vintage, per-device capability, and the secondhand/legacy channels that place capability outside a mandate — not the census. Per-device security-posture assessment is held pending IBBIS infohazard review.

### 2.1 Jurisdictional reach under a US mandate

- **8 of 34** manufacturers are US-headquartered (directly bound).
- **12 of 34** are in allied jurisdictions (GB, DE, FR, JP, DK, SE, AT) — reachable via harmonisation/diplomacy.
- **14 of 34** sit outside US and allied reach (13 China, 1 Russia).
- **5 of the 9** firms founded since 2019 are outside-jurisdiction, including the highest-throughput array class.
- **~35% predate 2010** — a legacy installed base that cannot be retrofitted with KYC, secure boot, or on-device screening, and where forensic attribution is the only available control layer.

**Finding:** a US mandate directly reaches under a quarter of known manufacturers, and the newest, most capable capacity is concentrating where it does not reach. **International harmonisation is load-bearing, not optional.** Reach erodes further once **secondhand/used-equipment** channels are counted (below).

### 2.2 Capability is uneven, and capability + unreachability is rare

| Firm | Chemistry | Jurisdiction | Usable length | Throughput | Note |
|---|---|---|---|---|---|
| **LinkZill (TruSynth)** | Array (TFT-semiconductor) | China (outside) | 200 nt (public spec); ≥98.5% coupling | 4,096 / chip (spec) | The one device combining assembly-relevant length, high throughput, and no US reach |
| **DNA Script (SYNTAX)** | Enzymatic (TdT) | France (allied) | 80 nt Std / 120 nt Hi-Fi | 96 parallel | Reagent-licensing chokepoint; ~€250–280K (vendor quote) |
| **Kilobaser (one/one-XT)** | Phosphoramidite column | Austria (allied) | ~150 nt (cartridge budget) | 1 per run | Offline/air-gap; proprietary cartridge chokepoint; low throughput |

Devices reaching 120–150 nt exist in several jurisdictions, but only **LinkZill** is simultaneously capable, high-throughput, and outside US reach. **Capability is common; the combination of capability with unreachability is rare.** Durable control must attach to capability and jurisdiction, not to chemistry class — reinforced by the observation that the same array chemistry spans OpenIDS (DIY, ~30 nt, ~55% full-length) and TruSynth (industrial, 4,096-plex). Capability is a property of the engineering and capital applied to a chemistry, not of the chemistry itself.

### 2.3 Screening-tool landscape and the opacity finding

Tools by detection floor (JHU CHS Gene Synthesis Screening Hub): **30 bp** — SecureDNA (free, cryptographic, hardware-integrable), Aclid (commercial); **50 bp** — Battelle UltraSEQ, IBBIS Common Mechanism (free, open-source), RTX BBN FAST-NA, Signature Science SeqScreen-Nano (free); **general** — NCBI BLAST. The 30-vs-50 bp split maps onto the framework/S. 3741 window debate and onto whether short-oligo benchtop output is even screenable.

**Opacity finding:** across all 34 manufacturers, adopted-screening status could not be verified from public sources. If this holds, "the benchtop layer is essentially unauditable from outside" is itself a reportable governance result.

### 2.4 Feasibility constraints on device-level control (incl. secondhand leakage)

The IGSC (formed 2009; members ~80% of commercial capacity) provides voluntary order screening. Right-to-repair legislation (e.g. Oregon SB 1596, 2024) restricts the same manufacturer software-lock mechanism on-device screening relies on. And documented **resale/export leakage** — Codex DNA's (now Telesis Bio) Q2-2022 Form 10-Q discloses BioXp systems reaching embargoed countries including Russia via distributors/resellers — is a concrete instance of point-of-sale KYC being undermined downstream, and the clearest evidence that **accessibility outside official manufacturers (secondhand/used) is a real gap**.

---

## PART 3: SYNTHESIS SCREENING POLICY LANDSCAPE (2024–2026)

Two distinct US instruments are frequently conflated. Keeping them separate matters: one is funding-conditional guidance, the other is proposed statute with a different lead agency.

### 3.1 OSTP Framework for Nucleic Acid Synthesis Screening (April 2024)

Released 29 April 2024; requires (as a condition of federal life-sciences funding) that synthetic nucleic acids and benchtop devices are procured only from Framework-compliant providers/manufacturers. Built on the 2023 HHS Guidance.

**Implementation dates:**
- **26 April 2025 (Stage 1, in effect):** screening for sequences ≥200 nt.
- **13 October 2026 (Stage 2, scheduled — not yet in force):** window reduced to 50 nt, plus an expanded functional SOC definition covering sequences that contribute to pathogenicity/toxicity even when not from a listed agent.

*Correction:* an earlier draft placed the 50-nt window at October 2025 and simultaneously described the framework as paused; it is **October 2026, and a scheduled (not implemented) milestone**.

**Key requirements:** screen DNA/RNA ≥200 nt against a Regulated Pathogen Database (US Select Agents, Australia Group, EU dual-use/CCL); six-frame translation to catch codon-optimised evasion; customer identity verification; apply NIST standards for mechanism sufficiency where available.

**Policy pause (May 2025):** Executive Order 14292 (signed 5 May 2025; 90 FR 19611) directed OSTP to revise or replace the 2024 Framework within 90 days. As of **October 2026** the replacement remains unpublished, so whether the October 2026 milestone survives on schedule depends on it.

### 3.2 S. 3741 — Biosecurity Modernization and Innovation Act of 2026 (statutory vehicle)

Introduced 29 January 2026 (Cotton, Klobuchar); referred to Senate Commerce. Per the bill text, it directs the Secretary of Commerce to require gene-synthesis providers to screen orders and customers; requires federal-fund recipients to buy only from compliant providers; provides exemptions for clearly non-hazardous sequences and technical assistance for ambiguous results; and establishes a biotechnology governance sandbox at NIST.

**Distinction:** OSTP framework = OSTP/HHS-led, funding-conditional; S. 3741 = Commerce-led, statutory. S. 3741 supplies the mandate mechanism; the OSTP framework supplies the technical spec. Neither alone constitutes the "mandatory + on-device" regime this project models as **R1** — a composite projection, doubly conditional on the framework revision being issued and on S. 3741 (or equivalent) being enacted.

### 3.3 IGSC Harmonized Screening Protocol (v3.0, September 2024)

IGSC members voluntarily screen all dsDNA orders against a Regulated Pathogen Database, including six-frame translation. Scope: 200+ bp against the RPD; customer identity/affiliation checks; **8-year retention**; members required to transition to the 50-bp threshold to conform with the OSTP framework. Members (Thermo Fisher, IDT, GenScript, Twist, Eurofins, others) represent ~80% of global commercial capacity.

### 3.4 Recent Biosecurity Research: AI-Designed Protein Evasion (October 2025)

**Wittmann, B.J., et al. (2025).** "Strengthening nucleic acid biosecurity screening against generative protein design tools." *Science*, 390(6768), 82–87. https://doi.org/10.1126/science.adu8578

- **Design:** three open protein-generative models (ProteinMPNN, EvoDiff-MSA, EvoDiff-Seq) produced 76,080 synthetic homologs across mutational loads for 72 wild-type proteins of concern (mostly toxins). Templates index-anonymised (info-hazard); no wet-lab synthesis; function-retention estimated in silico (TM-Score, ΔpLDDT).
- **Findings:** best-match screening is vulnerable to generative design (AI homologs retain predicted function at low identity, evading similarity search). Coordinated "zero-day" disclosure via IGSC / OSTP / NIST / DHS + four BSS developers; three of four patched. **After patching, ~1%/3%/3%/7% of the more-probably-functional variants still escaped — average ~3% unflagged (~97% flag rate)**, concentrated in a few contested templates. A shuffle/fragment experiment reduced detection further, though standard mol-bio can rebuild the gene (cf. §1.6).
- **Implication:** similarity-based screening erodes as AI orders grow sequence-diverse — exactly the gap the October 2026 **functional-SOC** provision targets (shift from "best match to a listed agent" toward "demonstrated pathogenic/toxic function").

**Counterpoint (authors' own):** Ikonomova et al. (2025, bioRxiv 2025.05.15.654077) found early-2024 generative models cannot yet reliably rewrite a protein while retaining function *and* evading screening — a near-term reassurance expected to weaken.

**Baseline screening validated:** Laird et al. (2025, *Applied Biosafety*, doi:10.1177/15356760251401228) — NIST inter-tool analysis, **>95% sensitivity, >97% accuracy** across six tools; disagreements traced to differing SOC definitions. Supersedes any "NIST validation pending" framing: the open problem is definitional/functional, not baseline accuracy.

---

## PART 4: SUPPLY CHAIN & ACCESSIBILITY ANALYSIS

### 4.1 DNA Synthesis Market Growth

Market-size estimates vary widely (incompatible scope definitions) — from ~USD 2.5B to ~USD 5.9B (2025 base), CAGRs ~14–19%. Precise sizing is not load-bearing; no single number is presented as definitive. The two robust, on-thesis signals: **(1)** the market is growing double-digit (decentralisation/demand rising); **(2)** provider revenue is concentrated among a handful of firms (Thermo Fisher, IDT, GenScript, Twist, Eurofins), which — with IGSC members at ~80% capacity — is precisely what makes provider-level screening a viable chokepoint.

### 4.2 Phosphoramidite Supply Chain

Global phosphoramidite market ~USD 1.1–1.2B (2024–25) → ~USD 1.7–2.3B by 2031–33 (~6–8% CAGR); North America ~39% share; APAC fastest-growing. All four standard amidites are continuously multi-sourced (Glen Research, ChemGenes, Merck/Sigma, LGC, Thermo, etc.) and **not restricted** for research institutions.

**Reagent-stability chokepoint — being engineered away:** phosphoramidites have poor bench stability (store −20 °C under inert gas; degrade by acrylonitrile-elimination/water pathways; Sandahl et al. 2021). But **on-demand flow synthesis of phosphoramidites from stable parent alcohols** has been demonstrated (<6 min, >98% conversion, no purification, fed directly to automated synthesis) — Sandahl et al., 2021, *Nature Communications* 12:2760 (DOI 10.1038/s41467-021-22945-z). *Maturity caveat:* a 2021 proof-of-concept (HPLC pump + packed-bed reactor), 10 nucleoside + 4 non-nucleoside amidites, used to build a 51-mer; an inline-concentration step is flagged unsolved; end-to-end yield 35.2% vs 41.8% conventional. Framing: "an alternative that removes the storage constraint," not "a faster route."

**Governance implication:** core reagents are commodity, multi-sourced, and substitutable, and even the residual stability barrier is being engineered away. **Reagent restriction is not a durable standalone control point** — a structural conclusion, independent of the market-size figures.

### 4.3 Solvent Sourcing: Acetonitrile vs. Propylene Carbonate

Acetonitrile is hazardous, flammable, shipping/disposal-constrained, and shortage-prone (2008–09). Propylene carbonate (the OpenIDS substitution) gives 94–98% inkjet coupling, is a GRAS food additive, effectively unregulated, and commodity-sourced. **Substituting PC for acetonitrile removes a genuine supply/handling friction point** — one of the clearest documented cases of a supply-chain constraint being engineered *around* rather than defeated, and (with §4.2) a direct argument for attaching durable control to the device and to attribution, not to reagent/solvent supply.

---

## PART 5: DIY BIOTECH COMMUNITY — and the null finding

### 5.1 Community landscape

Community biology labs (BioCurious, Genspace, BUGSS, Counter Culture Labs, etc.) operate across North America, Europe, and Asia/South America/Oceania; DIYbio.org listed ~90 labs as of 2022 (counts vary). Genspace (Brooklyn, 2009/2010) was the first US community biolab; most labs meet **BSL-1**. DIYbio (Cowell & Bobe, 2008) drafted a 2011 code of ethics and runs the "Ask a Biosafety Expert" service.

### 5.2 The null finding (a governance result in itself)

A 2026 survey found **no verified, reproducible community/garage oligonucleotide synthesizer.** The ODIN, Genspace, Counter Culture Labs, DIYbio, Hackaday, and the diyhpl wiki all **buy** synthetic DNA — none synthesise de novo (the ODIN sells gene-editing kits, not a synthesizer; the diyhpl "DNA synthesis" page is lecture notes, not a build). Typical documented projects are BSL-1 hobbyist/civic (bioluminescent bacteria, DNA barcoding, food-authenticity, OpenPCR). **The genuinely reproducible DIY frontier is therefore the academic open-hardware set (OpenIDS/OpenIDS2, MAS 2.0) plus DropSynth-style assembly — not a homebrew scene**, and NTI (2023) locates the biosecurity concern in *commercial benchtop* devices, not a garage capability. This null result directly answers "are these the only DIY routes?" — effectively yes.

---

## PART 6: COST TRENDS & TECHNOLOGY READINESS

### 6.1 DNA synthesis cost per base

Long-run synthesis/sequencing cost data are tracked by Carlson & Field at synthesis.cc. DIY OpenIDS: system ~$19,900 (5-printhead); reagents ~$100–500 build, ~$1–5/sequence at scale. **Caveat:** cost parity with commercial providers (~1,000+ sequences) is parity on cost only — OpenIDS produces short (~15–30 nt), moderate-fidelity oligos, **not** commercial-grade long oligos, so it is not substitutable on capability.

### 6.2 Technology readiness (corrected)

| Approach | TRL | Capital | Expertise | Usable length @ fidelity | Oversight (R0) | Status 2026 |
|---|---|---|---|---|---|---|
| **OpenIDS (inkjet)** | 5 | ~$20K (v1) / ~$4K (v2) | Medium (6/10) | ~15–30 nt | No oversight reaches DIY builders | Demonstrated; short-oligo only |
| **MAS 2.0 (photolith.)** | 5–6 | ~tens of $K | High (optics+chem) | library-grade | No oversight | Open build; origin-lab demonstrated |
| **DropSynth (assembly)** | 4 | **~$3.4K bead pool** | Moderate | gene-length via assembly | No oversight (but oligo pool is screenable) | Reproduced; **no fab/cleanroom** |
| **Electrochemical** | 3 | ~$10K (est) | Medium (7/10) | Not established | No oversight | Pre-commercial; **no DIY build** |
| **Enzymatic — DIY (Church)** | ~3 | low | High (biochem) | data-storage only | No oversight | Off-the-shelf but not defined-sequence |
| **Enzymatic — SYNTAX** | 5 | ~€250–280K | Medium (5/10) | 80–120 nt | Manufacturer/reagent control point | Commercial (baseline) |
| **Commercial benchtop (column)** | 9 | ~$15–150K (best ~$60K) | Low (2/10) | ~100–150+ nt | Uneven; largely unscreened | Mature; active resale market (baseline) |
| **Commercial provider (service)** | 9 | $0 | Low (1–2/10) | Genes/genomes | Screened channel (IGSC ~80%) | Mature, screened baseline |

---

## PART 7: CRITICAL GAPS & RESEARCH OPPORTUNITIES

**Accessibility mapping** — regime-conditional TRI scoring **usable length at high fidelity** (not advertised maximum) and throughput; cost-trajectory characterisation with explicit TRL gating (no point forecasts for TRL-3); supply-chain vulnerability across all reagents; detectability signatures for DIY-synthesized sequences; **and the residual-gap question: under mandatory commercial + benchtop screening, which DIY capability remains reachable?** (Answer, from Part 1/5: a narrow, expertise-gated set of open-hardware builds + assembly-from-a-screened-pool — real but small.)

**Bottleneck analysis** — error-accumulation models for DIY vs commercial oligos; assembly feasibility from short/moderate-fidelity DIY oligos (partly addressed in §1.6 — assembly from 16–30-mers is demonstrated; the binding constraint is fidelity + the downstream error-correction/verification/host pipeline, per Cui 2024, Lubock 2017, NTI 2023). **Open:** quantify the correct-assembly yield achievable specifically from OpenIDS-grade (~56% full-length) oligos.

**Policy & governance** — control-lever effectiveness under R0 vs R1; international harmonisation beyond IGSC/OSTP (sharpened by the Part 2 finding that a US mandate reaches only 8 of 34 manufacturers, and by the secondhand-leakage evidence); benchtop-manufacturer customer-screening; and detection/forensic synthesis-route attribution (Chapter 4).

**Emerging threats** — similarity-based screening is vulnerable to AI-designed variants (~3% still escaped after patching, Wittmann 2025); function-based screening remains the unsolved problem; the scheduled October 2026 functional-SOC provision is the policy response.

---

## SUMMARY: RESEARCH LANDSCAPE AS OF 2026

**The DIY frontier is narrow, academic, and skill-gated.** OpenIDS/OpenIDS2 (inkjet, ~$4–20K) and MAS 2.0 (photolithographic) are the only reproducible open *de novo* synthesizers, and both are lab-grade, expertise-heavy, and currently short-oligo/library-grade — not assembly-ready for defined genes. DropSynth (+OMEGA) is cheap DIY *assembly* but inherits the screening perimeter through its commercial oligo pool. Electrochemical has no DIY build; enzymatic is DIY only in a data-storage-only form; and there is no working garage synthesizer at all. **The correct inference is not that screening becomes irrelevant, but that a single point-of-sale control is insufficient: screening must be made mandatory, pushed on-device, extended internationally, and backstopped by forensic attribution for the devices and the residual DIY routes it cannot reach.** The problem shifts from "prevent DIY synthesis" to "govern a proliferating-device world with a layered, mandatory, regime-conditional architecture" — which the October 2026 revisions and S. 3741 begin to build, and which this project sets out to stress-test.
