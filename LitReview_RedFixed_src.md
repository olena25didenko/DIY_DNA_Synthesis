# Preliminary Literature Review: DIY DNA Oligonucleotide Synthesis

### Table A — Capability and accessibility by synthesis approach

| Technology | Method (how it works) | Cost (capital / per-seq) | Usable length @ high fidelity | Material acquisition | Protocol accessibility |
|---|---|---|---|---|---|
| OpenIDS v1 | Inkjet printhead deposits phosphoramidite chemistry onto CPG-filled wafer spots; 3D-printed frame, Arduino/Pi control; array format | ~$20K / ~$1–15 | ~20–30 nt (demonstrated ~30-mer; ~98% per-step → ~55% full-length at 30, <40% at 50) | Medium — industrial inkjet printhead is the chokepoint; reagents commodity | Medium — open-source and "non-expert" buildable, but wet chemistry + calibration non-trivial |
| OpenIDS v2 | 2nd-gen OpenIDS: ~⅓ volume, custom PCB, peristaltic bulk delivery; same inkjet-microarray chemistry | ~$4K (component-level; full itemised total in supplementary — treat as approximate) / ~$12 | ~15–25 nt (validated on a 15-mer, ~56% full-length, ~96% per-step) | Medium — as v1 | Medium — more reproducible/accessible than v1 |
| MAS 2.0 / AMS | Open-source photolithographic (light-directed) synthesizer: a DMD patterns 365 nm UV to photo-deprotect features (NPPOC amidites), no physical masks | [[R~€150–170K instrument (optics ~€150K + synthesizer ~€20K); ~€200–300K fully loaded — sourced, developer interview 2026R]] / — | library-grade (error-prone; handled by downstream selection) | Medium — off-the-shelf optics + specialty photolabile amidites; no cleanroom | Medium — full open CAD/STL/software + chemistry manual; optics alignment is the barrier[[R; no independent (non-origin-lab) build yetR]] |
| DropSynth | Microarray-derived oligos pooled, barcoded, assembled into genes in picoliter emulsion droplets (multiplexed PCA) | ~$3.4K bead pool (~200 rxns) / ~$1–2 per gene | Gene-length output (~1 kb+) from short building blocks — but fidelity error-correction-dependent | Medium — needs a commercial oligo-pool source; standard mol-bio lab (vortex emulsion, no microfluidic-chip fabrication) | Moderate — bead-pool prep is fiddly; downstream is routine PCR/gel + bioinformatics |
| Electrochemical | Phosphoramidite chemistry with electrochemically-generated-acid deprotection on electrode arrays | ~$12K (est) / ~1-$5 (est.) | Not established (TRL 3) — 13–17-mer academic demos only | High ease — commodity electrodes (why it is concerning if it matures) | No independent DIY build published — academic + defunct-commercial only |
| Enzymatic (TdT, e.g. DNA Script SYNTAX) | Template-independent polymerase adds nucleotides in aqueous conditions; turnkey commercial benchtop | Commercial: ~€250–280K instrument / €0.11–0.26 per base (DNA Script vendor quote). DIY route: low capital | Commercial (SYNTAX): 80 nt Standard / 120 nt Hi-Fi. DIY (Church route): not defined-sequence | Commercial: proprietary enzyme/cartridge = licensing chokepoint. DIY: off-the-shelf TdT/dNTPs/apyrase | Benchtop ≠ DIY (closed cartridge). Only the Church terminator-free route is off-the-shelf, and it is data-storage only (see §1.4) |
| Commercial benchtop (column phosphoramidite, e.g. Kilobaser, MerMade) | Standard solid-phase phosphoramidite column synthesis in a benchtop box; individual oligos | ~$15–150K (best ~$60K; used $15–30K) / varies | ~100–150+ nt at good fidelity — mature chemistry | Medium — reagents commodity; instruments on used market (eBay) | Medium–High — turnkey, established protocols (baseline, not DIY) |
| Commercial provider (mail-order, e.g. Twist/IDT/GenScript) | Centralized industrial synthesis + gene assembly; order online, receive DNA | none / ~$0.07–0.10 per bp | Genes/genomes, high fidelity (the benchmark) | N/A (service) | Highest ease — but this is the screened channel (IGSC / SecureDNA) |

### Table B — Risk and readiness (the biosecurity read)

| Technology | TRL | Assembly readiness | Detectability | Control / biosecurity note |
|---|---|---|---|---|
| OpenIDS v1 | 5 | Low — short, ~50% full-length oligos; not directly gene-assembly-ready | Moderate | Visible bench kit; printhead sourcing traceable; low assembly-readiness caps the threat |
| MAS 2.0 / AMS | 5 | Medium — library-grade output for assembly | Moderate | Fully open photolithographic build; optics + photolabile-amidite barrier; the DIY twin of the array/photolith class[[R; capital ~€150–170K instrument (developer interview), not "tens of $K" — above garage rangeR]] |
| OpenIDS v2 | 5 | Low — as v1 | Moderate | As v1; slightly more reproducible/accessible |
| DropSynth | 4 | High (it is an assembly method) — but gated by expertise | Moderate | Assembles genes (higher intrinsic risk) but high expertise barrier + needs oligo-pool source; not DIY-adopted |
| Electrochemical | 3 | Unknown (pre-commercial) | High (≈9/10, near-invisible) | Highest potential concern — portable, commodity materials — but TRL 3: conditional-future, not present capability. No commercial instance exists (see Part 2) |
| Enzymatic | 5 | Medium–High — longer, cleaner oligos | Low–Moderate | Enzyme/cartridge licensing is a genuine control point; defined-sequence enzymatic needs bespoke reagents a well-resourced lab must make |
| Commercial benchtop | 9 | High — long, high-fidelity, directly assembly-ready | Low | The real near-term concern — mature, ≥150 nt, assembly-ready, largely unscreened, resale market |
| Commercial provider | 9 | Highest — delivers assembled constructs | Low | Baseline + the currently-screened chokepoint; R0/R1 controls act here (IGSC ~80% capacity) |

## PART 1: CORE TECHNOLOGY LANDSCAPE

### 1.1 OpenIDS: Inkjet-Based Synthesis (TRL 5 — Demonstrated)

**Primary Reference:** Kim, J., Kim, H., & Bang, D. (2024). "An open-source, 3D printed inkjet DNA synthesizer." Scientific Reports, 14, 3773. https://doi.org/10.1038/s41598-024-53944-x

**Key Technical Specifications:**

- Synthesized oligonucleotides on 144 spots on a 15 × 25-mm silicon wafer filled with controlled pore glass, with approximately 98% synthesis yield per cycle. This is per-step coupling efficiency, not full-length correct-product fraction. The two diverge sharply with length: at 98%/step a 30-mer is ~55% full-length and a 50-mer is <40%. OpenIDS2 (below) measured ~96.1%/step and only ~56% full-length for a 15-mer. Usable high-fidelity length is therefore ~15–30 nt, and OpenIDS output is not directly assembly-ready for gene-length constructs.
- Architecture: 3D printing, Arduino, and Raspberry Pi, achieving robust stability with an industrial inkjet printhead.
- Maintenance of low production costs makes it suitable for self-fabrication and optimization in academic laboratories; even non-experts can create and control the synthesizer with a high degree of freedom for structural modifications.

**Cost Analysis:**

- Full 5-printhead system: ~$19,900 (compared to $34,000 for the previous POSaM system, and $15–30K for used commercial synthesizers).
- Scalability: modular design allows addition of printheads for increased parallelism.
- Reagent cost per sequence: estimates suggest $1–5 per sequence at scale (1000+ sequences).

**GitHub Repository & Resources:** https://github.com/regiregire/OpenIDS — an easy-to-build and highly scalable open-source inkjet-based microarray synthesis device built using 3D printing, Arduino, and Raspberry Pi.

**Follow-up (OpenIDS2):** Kim, Kim & Bang (2025), PLOS ONE 20(12):e0338478. Reduces device volume to ~⅓, integrates a custom PCB, and replaces ~$4K of commercial syringe pumps with 3D-printed peristaltic pumps (<$164). Total build cost is reported as ~$4,000 based on the paper's component-level figures; the full itemised total sits in the supplementary S1 table, so treat ~$4K as approximate (an earlier "~$12K" figure is not in the paper). Note: Chapter 1 currently treats OpenIDS2 as having "no itemised total" — reconcile the two documents to one wording. Reported ~96.1%/step; ~56.2% full-length for a 15-mer poly-dT. Full package: https://github.com/regiregire/OpenIDS2

**Chemistry Innovation:** Propylene carbonate (PC) is used as a less-volatile alternative to acetonitrile, achieving coupling efficiency of 94–98% for inkjet oligonucleotide synthesis. Biosecurity Implication: propylene carbonate is a food additive and industrial solvent — completely unregulated, unlike acetonitrile (which is tracked as a precursor chemical in many jurisdictions).

**Forensically relevant build detail:** the published OpenIDS protocol omits the capping step to simplify synthesis. Because the diagnostic G→A substitution signature of column phosphoramidite chemistry is capping-driven (Masaki et al., 2022), OpenIDS oligos are expected to carry a distinguishable error phenotype relative to standard capped column synthesis — relevant to the attribution framework.

### 1.2 DropSynth

**Primary Reference:** Sidore et al. (2020), "DropSynth 2.0: high-fidelity multiplexed gene synthesis in emulsions," Nucleic Acids Research, 48(16), e95 (DOI 10.1093/nar/gkaa600); orig. Plesa et al. (2018), Science 359:343 (DOI 10.1126/science.aao5167).

**How it works:** Genes are bioinformatically split into oligos, each tagged with a 12-nt microbead barcode common to all oligos of one gene; a commercial microarray oligo pool is amplified, nicked to expose the barcode, and hybridised to a pool of barcoded magnetic beads so each bead captures one gene's oligos. Beads are compartmentalised by vortexing into picolitre water-in-oil droplets (bulk emulsification — no microfluidic chip and no cleanroom), and the gene is assembled inside each droplet (PCA in 1.0/2.0; Golden Gate in later variants).

**Advantages Over Inkjet:**

- Massively parallel synthesis (100s–1000s of sequences simultaneously).
- Extremely low per-droplet volumes (picoliter scale).
- [[RCorrection: DropSynth compartmentalises by bulk vortex emulsification, not microfluidic droplet generation. The earlier "~1,000,000 droplets/hr, 6-pL/droplet, ~10⁶-fold cost reduction" figures describe droplet microfluidics in general and do NOT apply to the DropSynth workflow, which uses no microfluidic chip and no fabrication.R]]

**Note on category:** DropSynth is an assembly method built on an upstream commercial oligo-pool source, not a standalone de novo synthesizer, and it inherits the screening perimeter through that oligo pool.

### 1.3 MAS 2.0 / Advanced Maskless Synthesizer — open-source photolithographic synthesis

**Primary Reference:** Somoza group, "Advanced Maskless Synthesizer (MAS 2.0)," ChemRxiv 2024, DOI 10.26434/chemrxiv-2024-j4c90.

**How it works:** phosphoramidite synthesis using photolabile 5′-protecting groups (NPPOC/BzNPPOC) instead of acid-labile DMT. A digital micromirror device (DMD) patterns ~365 nm UV onto the substrate, photo-deprotecting only illuminated features so the next amidite couples only there ("maskless" = the DMD replaces physical photomasks). 1.5 µm feature resolution.

**Why it matters here:** this is the first fully open-source, reproducible photolithographic synthesizer — full CAD/STL/optical drawings, a costed component list, Python control software, and a chemistry/process manual. It uses off-the-shelf optics + a high-power UV LED and needs no cleanroom (unlike electrochemical). Barriers: optics alignment, DMD control, anhydrous amidite fluidics, and specialty photolabile amidites [[R(available from several suppliers, three generations NPPOC/BzNPPOC/SPh-NPPOC; not commodity)R]]. [[RCapital is now sourced from the developer, not estimated: optics alone ~€150,000 and a realistic end-to-end build ~€200,000–300,000 (M. Somoza, co-founder, Helices Biological Photolithography, interview Jul 2026; corroborated by the ChemRxiv component list). For a like-for-like TRI comparison the instrument figure is ~€150–170K (optics ~€150K + nucleic-acid synthesizer ~€20K); the ~€200–300K includes gases, pressure regulators, and a climate-controlled lab. This is well above the earlier "tens of $K" estimate and above garage range.R]] Published accuracy/length for this method are in the light-directed synthesis literature (Lietard et al., 2021, NAR 49(12):6687; Agbavwe et al., 2011, J. Nanobiotechnol. 9:57), not the device paper; independent (non-Somoza) DIY builds are not yet published.[[R The developer confirms no one has yet independently reproduced the open build; the first in-house build took months (now down to a few weeks), gated chiefly by optical alignment.R]] It is the DIY instantiation of the photolithographic class reproduced in Chapter 4 (Lietard). Output is library-grade (error-prone), not per-strand perfect.

[[R**Commercial vendor & specs (helicesbio.com):** the MAS 2.0 is sold by Helices Biological Photolithography GmbH, Vienna; founders Erika Schaudy (CEO), Mark Somoza, and Jory Lietard — note Lietard also authored the NAR error-rate paper cited above, a scholarly disclosure worth a footnote in Chapter 4. Vendor specifications: Texas Instruments DMD; up to 786,432 (XGA DMD) or 2,073,600 (1080p DMD) unique sequences; 365 nm UV LED source; ~15 s coupling; photodeprotection 60 s (NPPOC) / 30 s (Bz-NPPOC) / 6 s (SPh-NPPOC); reverse 5′→3′ synthesis available (3′-photolabile amidites) for spatial-transcriptomics arrays. The vendor page also confirms the "no acidic deblock" point used in the attribution chapter — the photolabile group "directly replaces the acid-labile dimethoxytrityl (DMTr)."R]]

**Historical predecessor:** POSaM (Lausted et al., Genome Biol. 2004, 5:R58) — the original open-source inkjet synthesizer (~$34K) OpenIDS builds on; documents that open synthesizer designs are 20 years old.

### 1.4 Electrochemical DNA Synthesis (Pre-Commercial, 2-5 Years to Maturity)

**Technical Approach:** Phosphoramidite chemistry with electrochemically triggered deprotection. A positive potential applied to a gold electrode generates protons that remove the acid-labile DMT protecting group, exposing the hydroxyl for the next cycle. Potential for lower cost, no hazardous reagent handling, portable setup.

**Primary Reference:** Xu, C., Ma, B., Gao, Z., Dong, X., Zhao, C., & Liu, H. (2021). "Electrochemical DNA synthesis and sequencing on a single electrode with scalability for integrated data storage." Science Advances, 7(46), eabk0100. https://doi.org/10.1126/sciadv.abk0100

Synthesis is based on phosphoramidite chemistry with electrochemical deprotection; sequencing relies on charge redistribution originating from polymerase-catalyzed primer extension. Context caveat: the source paper is a DNA data-storage demonstration synthesizing short sequences on electrodes, not a general-purpose oligo synthesizer — a further reason its accessibility figures are conditional-future.

**Limitations:** For planar glass substrates, electrochemical deblocking methods face challenges with incomplete deblocking and losses due to depurination during electrochemically induced acid deprotection.

**Status:** the electrochemical deblocking mechanism is well established — CombiMatrix/CustomArray commercialised electrochemical array synthesis (acquired by GenScript, 2017), and Xu et al. (2021) demonstrated single-electrode synthesis-and-sequencing — but a benchtop, gene-length, DIY-accessible electrochemical synthesizer remains pre-commercial. No such device appears in the 34-firm landscape (Part 2), corroborating the TRL-3 assessment for the DIY-relevant form. No commercial instance exists in the 34-firm benchtop landscape (Part 2) — independent market-side corroboration of TRL 3.

### 1.5 Enzymatic DNA Synthesis (Emerging Commercial)

**Technology:** Terminal deoxynucleotidyl transferase (TdT) in a template-independent, single-nucleotide-addition cycle — Palluk, S., Arlow, D.H., de Rond, T., et al. (2018). "De novo DNA synthesis using polymerase–nucleotide conjugates." Nature Biotechnology, 36(7), 645–650. https://doi.org/10.1038/nbt.4173

**Instrument capability (vendor-confirmed):** DNA Script SYNTAX synthesizes up to 96 oligos in parallel; the Standard kit reaches 80 nt and the Hi-Fidelity kit reaches 120 nt, vendor-positioned for gene assembly, protein mutagenesis, and CRISPR editing. Instrument cost ~€250–280K (DNA Script vendor quote, 2026; IFP 2024 STX-200 $292,000 corroborates). The system synthesizes, desalts, quantifies, and normalizes on-device.

**Market Status:** The global enzymatic DNA synthesis market was valued at ~USD 296.35 million in 2024 and is projected to reach ~USD 3,159.16 million by 2034, at ~26.7% CAGR (Nova One Advisor/Precedence Research). By technology, polymerase-based platforms led with 44.25% share in 2024, while TdT systems are projected to climb at 30.42% CAGR through 2030 (Mordor Intelligence).

**Recent Advances (2024–2025):**

- Evaluation of enzymatically synthesized DNA for gene assembly: oligos produced using a benchtop EDS instrument were available in half the time of commercially produced oligonucleotides and were sufficient to assemble functional GFP sequences without producing hazardous organic chemical waste.
- Molecular Assemblies, Inc. launched a partnering program to license its Fully Enzymatic Synthesis (FES) technology for on-site DNA production in May 2024.

**DIY Accessibility Assessment:**

- Moderate complexity (biochemistry knowledge required, but no electrical engineering).
- Key advantage for DIY: uses commodity chemicals; avoids phosphoramidite toxicity concerns.
- Key disadvantage: requires temperature control and specialized enzymes — and in practice the proprietary enzyme/cartridge supply is a licensing chokepoint, which is why the commercial enzymatic route is more controllable than DIY chemical routes despite comparable length.

### 1.6 From Oligos to Genes: Assembly Feasibility and the Fidelity Constraint

The preceding sections characterise oligonucleotide synthesis. A biosecurity assessment scoped to the synthesis step must nonetheless state clearly what stands between a DIY oligo synthesizer and a functional gene, because the two are often conflated. The literature supports a precise, and for this project favourable, conclusion: assembly of short oligos into genes is standard, decades-old methodology, but converting low-fidelity DIY oligos into a correct functional gene is gated by fidelity and by a downstream error-correction pipeline — not by the oligo length itself.

Chemical (phosphoramidite) synthesis is limited to roughly 200 nt, so all gene synthesis proceeds by assembling short oligos into longer constructs (ATDBio, Nucleic Acids Book). The two established routes are polymerase cycling assembly (PCA): short oligos alternating between both strands, overlapping by ~20–30 bp, are extended by a polymerase and then amplified by PCR; and ligation-based assembly (e.g. ligase chain reaction, LCR): overlapping oligos are joined by DNA ligase; lower error rate than PCA but more constrained. Both are textbook techniques used by every commercial provider.

A common assumption is that oligos shorter than ~40–60 nt cannot be assembled. The literature contradicts this as an absolute claim: the 901 bp GFP gene has been assembled from pools of 16-mers, as well as from 30-mers and 40-mers, using ligase chain reaction followed by PCA and PCR (USPTO 12,018,316, Methods for assembling nucleic acids, Example 2). Assembly from oligos in the OpenIDS length range is therefore demonstrated in principle. The practical penalty of short building blocks is not impossibility but multiplicity: a 1 kb gene assembled from 30-mers requires roughly twice the oligos and junctions of one assembled from 60-mers, multiplying the opportunities for error.

**Fidelity, not length, is the binding constraint.** Assembly quality is governed by the full-length fraction of the building-block oligos, and errors compound across junctions. Standard practice targets >90% full-length oligos for gene assembly; below ~70% full-length, redesign or a different synthesis route is indicated (standard gene-synthesis practice). This is precisely where DIY output falls short: OpenIDS2 delivers ~56% full-length product for a 15-mer (~96.1%/step) — far below the assembly-grade threshold. The consequence at scale is severe: even from decent oligos, PCA of a ~1 kb fragment yielded only 4.2 ± 2.1% correct product before error correction, rising to 31.3 ± 3.1% after two rounds of enzymatic correction (Optimization of PCA Error Correction Conditions to Improve Efficiency of Virus Genome De Novo Synthesis, 2024, PMC11547124). From ~56%-full-length building blocks the correct-assembly fraction would be substantially lower.

Recovering a correct, functional gene from low-fidelity oligos therefore requires a downstream error-correction and verification pipeline: enzymatic mismatch cleavage (e.g. T7 endonuclease I and comparable mismatch-recognition enzymes; benchmarked by Lubock et al., 2017, NAR 45(15), 9206–9217, DOI 10.1093/nar/gkx691), followed by clonal selection and sequence verification (Sanger or NGS) to identify error-free molecules — added expertise, reagents, and instrumentation, not a further step of synthesis itself.

**The assembly ceiling.** Even with error correction, PCA-based assembly is practically bounded at roughly 7,000–10,000 bp; beyond that, reliable assembly requires bacterial and yeast host systems for their DNA-processing and error-correction machinery, and many viral sequences are toxic to those hosts (NTI, 2023, Box 4; consistent with the recombinant-assembly literature). Booting a functional infectious agent from an assembled dsDNA genome adds further virus-specific expertise and mammalian cell-culture infrastructure.

**Implication for scope and for attribution.** Two conclusions follow, both of which reinforce this project's design. First, the binding constraint sits downstream of oligo synthesis: DIY oligo synthesis is real; assembly of short oligos into genes is standard; but converting DIY-grade oligos into a correct, functional gene depends on an error-correction, clonal-selection, verification, and (beyond ~10 kb) host-system pipeline that is expertise- and equipment-intensive. This is the same barrier NTI (2023) identifies from independent expert consensus, and it is why this project scopes to the synthesis step and treats assembly and rescue as out of scope — a principled boundary, not a convenient one. Second, synthesis-route error signatures propagate into the assembled product: because assembly copies the building-block oligos (with characteristic per-route error phenotypes) into the final construct, the synthesis-method signature is in principle detectable after assembly, in the sequenced gene. This is directly relevant to the attribution framework (Chapter 4): route attribution need not be performed on raw oligos, but may be recoverable from an assembled or deployed construct.

## Part 2: Commercial Benchtop Manufacturer Landscape

This section moves from chemistry (Part 1) to the products that instantiate it — but, per the realigned scope, it does not re-inventory manufacturers (the 34-firm list is compiled within the ERA/IBBIS working group; Alexanian, 2026). The contribution here is the accessibility-and-reach scoring — jurisdiction, vintage, per-device capability, and the secondhand/legacy channels that place capability outside a mandate — not the census.

### 2.1 Jurisdictional reach under a US mandate

Because S. 3741 and the OSTP framework are US instruments, a first question is how much of the landscape a US mandate actually binds:

- 8 of 34 manufacturers are US-headquartered (directly bound).
- 12 of 34 are in allied jurisdictions (GB, DE, FR, JP, DK, SE, AT) — reachable via harmonisation or diplomacy, not by US rule alone.
- 14 of 34 sit outside US and allied reach (13 China, 1 Russia).
- 5 of the 9 firms founded since 2019 are outside-jurisdiction, including the highest-throughput array-based class.
- ~35% predate 2010 — a legacy installed base that cannot be retrofitted with KYC, secure boot, or on-device screening, and where forensic attribution is the only available control layer.

**Finding:** a US mandate directly reaches under a quarter of known manufacturers, and the newest, most capable capacity is concentrating where it does not reach. International harmonisation is therefore not optional to the control architecture.

### 2.2 Capability is uneven, and capability + unreachability is rare

Three vendor-confirmed data points anchor the capability picture:

| Firm | Chemistry | Jurisdiction | Usable length | Throughput | Note |
|---|---|---|---|---|---|
| LinkZill (TruSynth) | Array (TFT-semiconductor) | China (outside) | 200 nt (public spec); ≥98.5% coupling | 4,096 / chip (spec sheet) | Public: 200 nt, ≥98.5% coupling. Sub-specs (4,096/chip; "150 nt unlockable to 200") are per the TruSynth spec sheet, not independently public. TFT semiconductor process. The one device combining assembly-relevant length, high throughput, and no US reach |
| DNA Script (SYNTAX) | Enzymatic (TdT) | France (allied) | 80 nt Standard / 120 nt Hi-Fidelity | 96 parallel | Vendor-positioned for gene assembly; reagent licensing chokepoint; ~€250–280K (vendor quote, 2026) |
| Kilobaser (one / one-XT) | Phosphoramidite column | Austria (allied) | ~150 nt (cartridge base budget) | 1 per run | Offline/air-gap operation, ~150-base cartridge, one per run — Kilobaser Technical Specifications; proprietary cartridge chokepoint; low throughput |

The pattern is the analytical crux: devices reaching 120–150 nt exist in several jurisdictions, but only one (LinkZill) is simultaneously capable, high-throughput, and outside US reach. Capability is common; the combination of capability with unreachability is rare. Durable control must therefore attach to capability and jurisdiction, not to chemistry class.

A second corollary strengthens the TRL framing from Part 1: the same chemistry spans the full accessibility range. OpenIDS (DIY, ~30 nt, ~55% full-length) and LinkZill's TruSynth (industrial, up to 150 nt, 4,096-plex) are both array-based. Capability is a property of the engineering and capital applied to a chemistry, not of the chemistry itself.

### 2.3 Screening-tool landscape and the opacity finding

Screening tools available to providers and benchtop manufacturers (Johns Hopkins Center for Health Security, Gene Synthesis Screening Information Hub), split by detection floor:

- 30 bp floor: SecureDNA (free, non-profit, privacy-preserving cryptographic screening, hardware-integrable), Aclid (commercial, IGSC member).
- 50 bp floor: Battelle UltraSEQ (commercial, IGSC member), IBBIS Common Mechanism (free, open-source, IGSC member), RTX BBN FAST-NA Scanner (commercial, IGSC member), Signature Science SeqScreen-Nano (free).
- General-purpose: NCBI BLAST (free; adaptable for in-house screening, not purpose-built).

The 30-vs-50 bp split maps directly onto the framework/S. 3741 window debate, and onto whether short-oligo benchtop output (most shipping Chinese column devices) is even screenable.

**Opacity finding:** across all 34 manufacturers, adopted-screening status could not be verified from public sources. The authoritative screening-tool list does not map firms to tools. If this holds after fuller research, "the benchtop layer is essentially unauditable from outside" is itself a reportable result about the current state of governance.

### 2.4 Feasibility constraints on device-level control

Two structural constraints push against the device lockdown a mandatory on-device regime assumes. The IGSC (formed 2009; members represent a majority of commercial gene-synthesis capacity, commonly estimated ~80%) provides voluntary order screening. Right-to-repair legislation in several US states (e.g. Oregon SB 1596, 2024, banning parts-pairing software locks) restricts the same manufacturer software-lock mechanism on-device screening relies on. And documented resale/export leakage — Codex DNA's (now Telesis Bio) Form 10-Q for Q2 2022 discloses BioXp systems reaching embargoed countries including Russia via distributors and resellers — is a concrete instance of point-of-sale KYC being undermined downstream.

## PART 3: SYNTHESIS SCREENING POLICY LANDSCAPE (2024-2026)

Two distinct US instruments are frequently conflated. Keeping them separate matters: one is funding-conditional guidance, the other is proposed statute with a different lead agency.

### 3.1 OSTP Framework for Nucleic Acid Synthesis Screening (April 2024)

**Policy Timeline:** The White House Office of Science and Technology Policy released the Framework for Nucleic Acid Synthesis Screening on April 29, 2024, establishing requirements — as a condition of receiving U.S. governmental life sciences research funding — that synthetic nucleic acids, and benchtop devices capable of synthesizing them, are only procured from providers and manufacturers that comply with the Framework. It built on the 2023 HHS Screening Framework Guidance.

**Implementation Dates:**

- April 26, 2025 (Stage 1, took effect): screening required for sequences ≥200 nucleotides.
- October 13, 2026 (Stage 2, SCHEDULED — not yet in force): screening window reduced to 50 nucleotides, plus an expanded, functional SOC definition covering sequences known to contribute to pathogenicity or toxicity even where not derived from a listed agent. An OSTP-designated interagency group is to assess the state of the art before this date.

**Key Requirements:** screen DNA/RNA ≥200 nt against a Regulated Pathogen Database (US Select Agents, Australia Group, EU dual-use/CCL); six-frame translation to catch codon-optimised evasion; customer identity verification; apply NIST standards for mechanism sufficiency where available.

**Policy Pause (May 2025):** Executive Order 14292, "Improving the Safety and Security of Biological Research" (signed May 5, 2025; Fed. Reg. 90 FR 19611, May 8, 2025), directed OSTP to revise or replace the 2024 Framework within 90 days. As of July 2026 the ASPR page states the framework will be revised or replaced and will be updated when new guidance is available — i.e. the replacement remains unpublished, and whether the October 2026 milestone survives on schedule depends on it.

**Regulatory Citations:** https://aspr.hhs.gov/S3/Pages/OSTP-Framework-for-Nucleic-Acid-Synthesis-Screening.aspx ; OSTP Framework PDF (Sept 2024): https://aspr.hhs.gov/S3/Documents/OSTP-Nucleic-Acid-Synthesis-Screening-Framework-508.pdf

### 3.2 S. 3741 — Biosecurity Modernization and Innovation Act of 2026 (the statutory vehicle)

Introduced January 29, 2026 by Sen. Tom Cotton (R-AR) and Sen. Amy Klobuchar (D-MN); referred to the Senate Committee on Commerce, Science, and Transportation. Per the bill text, it:

- Directs the Secretary of Commerce to promulgate regulations requiring gene-synthesis providers to screen orders and customers.
- Requires that any person receiving federal funds purchase only from a compliant covered provider.
- Provides for exemptions for clearly non-hazardous sequences, and a technical-assistance program for providers with ambiguous screening results.
- Establishes a biotechnology governance sandbox at NIST.

**Distinction that matters:** the OSTP framework is OSTP/HHS-led and funding-conditional; S. 3741 is Commerce-led and statutory. S. 3741 supplies the mandate mechanism; the OSTP framework supplies the technical specification (50-nt window, functional SOCs, six-frame translation, manufacturer expectations). Neither alone constitutes the "mandatory + on-device" regime this project models as R1 — that is a composite projection, doubly conditional on the framework revision being issued as expected and on S. 3741 (or equivalent) being enacted.

Sources: congress.gov/bill/119th-congress/senate-bill/3741; govinfo BILLS-119s3741is; Cotton press release (Feb 4, 2026).

### 3.3 IGSC Harmonized Screening Protocol (v3.0, September 2024)

**Background:** The IGSC (formed 2009) comprises leading commercial DNA synthesis companies; members voluntarily commit to sequence screening comparing all double-stranded DNA orders against a Regulated Pathogen Database derived from the U.S. Federal Select Agents and Toxins List, including checking all six reading frames (translated to amino acid sequences) to catch codon-optimized sequences.

**Current Protocol Scope:**

- 200+ bp orders screened against the RPD (U.S. Select Agents, Australia Group, EU dual-use lists).
- Six-frame translation detects codon-optimized evasion attempts.
- Customer screening includes identity verification, institutional affiliation checks, and written justification for select-agent sequences.
- 8-year retention of sequences and customer data.
- Members are required to transition to the 50-bp threshold to conform with the OSTP framework.

**IGSC Members (major synthesis providers):** Thermo Fisher Scientific, Integrated DNA Technologies, GenScript Biotech, Twist Bioscience, Eurofins Scientific, and others. Members represent ~80% of global commercial gene-synthesis capacity.

### 3.4 Recent Biosecurity Research: AI-Designed Protein Evasion (October 2025)

**The Paraphrase Project (Wittmann et al., 2025). Primary Reference:** Wittmann, B.J., Alexanian, T., Bartling, C., Beal, J., Clore, A., Diggans, J., Flyangolts, K., Gemler, B.T., Mitchell, T., Murphy, S.T., Wheeler, N.E., & Horvitz, E. (2025). "Strengthening nucleic acid biosecurity screening against generative protein design tools." Science, 390(6768), 82–87. https://doi.org/10.1126/science.adu8578

**Study design:** Using three open-source protein sequence generative models (ProteinMPNN, EvoDiff-MSA, and EvoDiff-Seq), the authors generated 76,080 synthetic homologs across a range of mutational loads for 72 wild-type proteins of concern — primarily toxins (where a single sequence can constitute a threat), plus a small number of proteins from controlled viral species to ensure the results were not toxin-specific. Templates were referred to only by randomly assigned index rather than by name, on the authors' judgment that linking protein identities to evasion results would itself constitute an information hazard. No sequences were synthesized or tested in a wet lab; function-retention likelihood was estimated in silico via TM-Score and ΔpLDDT from OpenFold structure predictions.

**Key findings:**

- Best-match BSS is vulnerable to generative design. Because AI-designed "synthetic homologs" can retain predicted structure/function while having low amino-acid identity to a controlled sequence, they evade similarity-based screening. Against the wild-type templates all tools showed near-perfect sensitivity and specificity; against the AI-reformulated variants, detection was inconsistent and the number of misses varied by tool.
- Coordinated "zero-day" disclosure. The vulnerability was treated as a biological zero-day: before public disclosure, the team worked through the IGSC and with US OSTP, NIST, DHS and OPPR, and with four commercial DNA-synthesis / BSS developers, to develop and deploy patches. Three of the four providers updated their tools (the fourth declined, judging it unclear whether its "misses" should be flagged at all).
- Patching helped but did not close the gap. After patching, the fraction of more-probably-functional variants (defined as TM-Score > 0.5 and ΔpLDDT > −10) that still escaped detection was ~1% (Tool 1), ~3% (Tool 2), ~3% (Tool 3) and ~7% (Tool 4) — an average of ~3% still unflagged, i.e. a ~97% flag rate. Most of the residual misses were concentrated in a few templates where whether the sequence should count as a "concern" is genuinely contested.
- Obfuscation compounds the problem. A second experiment fragmenting and shuffling the encoding DNA further reduced detection, though standard molecular-biology techniques could rebuild the original gene — a reminder that downstream assembly is the accessible step (cf. §1.5).

**Implications for screening:** current biosecurity screening software (BSS) depends almost entirely on similarity searches against databases of natural sequences, so it becomes less robust as AI-generated orders grow more sequence-diverse. Functional proteins designed by AI may resemble nothing in nature, eroding best-match approaches. This is precisely the gap the October 2026 functional-SOC provision is intended to address — shifting from "best match to a listed agent" toward screening for sequences with demonstrated pathogenic or toxic function.

**Counterpoint (cited by the authors themselves):** a follow-up TEVV (testing, evaluation, validation, verification) study — Ikonomova et al. (2025), Experimental Evaluation of AI-Driven Protein Design Risks Using Safe Biological Proxies, bioRxiv 2025.05.15.654077 — found that the generative models in use as of early 2024 are not yet reliably able to rewrite a protein while simultaneously retaining function and evading screening. This is a near-term reassurance the Wittmann authors expect to weaken as models improve.

**Independent validation of baseline screening:** a NIST inter-tool analysis compared six sequence-screening tools against a blinded test dataset, reporting baseline performance above 95% sensitivity and 97% accuracy, with disagreements traced largely to differing sequence-of-concern definitions or algorithmic methods (Laird et al., 2025, Applied Biosafety, doi:10.1177/15356760251401228). This supersedes any "NIST validation pending" framing: screening tools already perform well against known SOCs. The open problem is definitional and functional (what counts as an SOC, and catching AI-designed variants), not baseline accuracy.

## PART 4: SUPPLY CHAIN & ACCESSIBILITY ANALYSIS

### 4.1 DNA Synthesis Market Growth (2025–2036)

Estimates of the global DNA synthesis market vary widely across commercial research vendors and cannot be reconciled, because the reports use incompatible scope definitions (oligos only vs genes vs services vs instruments vs clinical devices). Four current reports illustrate the spread:

| Source | 2025 size | ~2034–36 projection | CAGR |
|---|---|---|---|
| Future Market Insights (2026) | ~USD 3.70 billion | ~USD 15.64 billion (2036) | ~14.0% |
| Fortune Business Insights (2026) | ~USD 5.19 billion | ~USD 24.06 billion (2034) | ~19.1% |
| Grand View Research–type estimate | ~USD 2.5 billion | ~USD 11.5 billion (2035) | ~16.3% |
| Higher-scope estimate | ~USD 5.93 billion | ~USD 34.39 billion (2035) | ~19.2% |

That is a 2.4× spread on the 2025 base year and CAGRs from ~14% to ~19% — a difference in definition, not in genuine disagreement about growth.

**How this analysis treats it:** precise market sizing is not load-bearing here and no single number is presented as definitive. The robust, cross-vendor signals are only two, and both are on-thesis. First, the market is growing at a double-digit CAGR (~14–19% across all four vendors) — decentralisation and demand are rising, consistent with the accessibility trend this review examines. Second, provider revenue is concentrated among a handful of firms — Thermo Fisher, Integrated DNA Technologies, GenScript, Twist Bioscience and Eurofins recur as the leaders in every vendor's list. This concentration, together with IGSC members covering ~80% of commercial capacity, is precisely what makes provider-level screening a viable chokepoint — which is the point that matters for the control analysis.

### 4.2 Phosphoramidite Supply Chain (Critical Reagent)

**Market overview:** Two current reports value the global phosphoramidite market at roughly USD 1.1–1.2 billion (2024–2025), projected to USD 1.7–2.3 billion by 2031–2033 at ~6–8% CAGR: Grand View Research (2025): USD 1.1 billion (2024) → USD 1.3 billion (2026) → USD 2.3 billion by 2033, at 8.1% CAGR (2025–2033); Mordor Intelligence (2026): USD 1.20 billion (2025) → USD 1.28 billion (2026) → USD 1.74 billion by 2031, at 6.34% CAGR.

**Regional concentration:** North America is the largest market — ~39% share (39.3% per Grand View Research 2024; 39.78% per Mordor 2025); Asia-Pacific is the fastest-growing region.

**Major suppliers:** Glen Research, ChemGenes Corporation, Link Technologies Ltd., Merck KGaA, Sigma-Aldrich (MilliporeSigma), LGC Biosearch Technologies, Thermo Fisher Scientific, GenScript Biotech, Biosynth, ATDBio Ltd., Bioneer Corporation, Lumiprobe, PolyOrg Inc., QIAGEN, TriLink BioTechnologies, Hongene Biotech.

**Availability assessment for DIY:** Commercial availability: all four standard phosphoramidites (dA, dC, dG, dT) are continuously available through Sigma-Aldrich, ChemGenes and others, and the catalog of nucleoside and non-nucleoside building blocks (fluorophores, dyes, ligands, redox tags) runs to several hundred items (Glen Research catalog; Sandahl et al. 2021). Regulatory status: unlike some solvents, phosphoramidites themselves are not restricted and can be ordered by academic/research institutions. Cost trend: a growing, multi-supplier market (~6–8% CAGR) is consistent with stable-to-declining per-unit cost over time.

**Reagent-stability chokepoint — being engineered away:** One residual friction point for DIY phosphoramidite use is that phosphoramidites have poor bench stability — they are preferably stored under inert atmosphere at −20 °C, and degrade in solution by autocatalytic (acrylonitrile-elimination / Arbuzov–Michael) and water-catalyzed pathways (Sandahl et al. 2021). However, on-demand flow synthesis of phosphoramidites directly from their corresponding, more-stable parent alcohols has been demonstrated, with reaction times under ~6 minutes, >98% conversion, and no purification step before the product is submitted directly to automated oligonucleotide synthesis (Sandahl, A.F., Nguyen, T.J.D., Hansen, R.A., Johansen, M.B., Skrydstrup, T. & Gothelf, K.V., 2021, Nature Communications 12, 2760, https://doi.org/10.1038/s41467-021-22945-z). The authors' stated vision is direct integration into DNA synthesizers, eliminating the manual synthesis and cold storage of phosphoramidites.

**Maturity caveat (important for accuracy):** this is a 2021 proof-of-concept flow system (HPLC pump + packed-bed reactor), demonstrated for ten nucleoside and four non-nucleoside phosphoramidites and used to build a 51-mer — not a shipping, synthesizer-integrated capability. The authors explicitly flag an unsolved inline-concentration step as "the remaining challenge." End-to-end, the on-demand 51-mer gave a slightly lower total yield (35.2%) than the conventional method (41.8%), though per-coupling yields were >98%. So the correct framing is "an alternative that removes the storage/stability constraint," not "a faster or better synthesis route."

**Governance implication:** the core reagents are commodity, multi-sourced, and substitutable, and even the residual reagent-stability barrier is being engineered away. Reagent restriction is therefore not a durable standalone control point. This is a structural conclusion, not a market forecast, and it does not depend on any of the market-size figures above.

### 4.3 Solvent Sourcing: Acetonitrile vs. Propylene Carbonate

**Acetonitrile — the real constraints:** Acetonitrile is a hazardous, flammable solvent subject to shipping, handling, and disposal constraints, and it experienced a well-documented global supply shortage (~2008–2009) that spiked prices and disrupted laboratory workflows. It is a standard synthesis and HPLC solvent whose price and availability can be volatile.

**Propylene carbonate (the OpenIDS substitution):** Propylene carbonate (PC) achieves coupling efficiencies of 94–98% for inkjet oligonucleotide synthesis (Kim, Kim & Bang 2024, the OpenIDS paper). Status: food additive (GRAS) and common industrial solvent. Regulation: effectively unregulated; purchasable without licensing or tracking. Availability: commodity chemical sourced from many suppliers globally.

**Biosecurity implication:** substituting propylene carbonate for acetonitrile removes a genuine supply/handling friction point for DIY synthesis (a hazardous, shortage-prone solvent replaced by an unregulated commodity one). It is one of the clearest documented cases in this review of a supply-chain constraint being engineered around rather than defeated — and, together with the on-demand-phosphoramidite result in §4.2, it is a direct argument for why durable control must attach to the device and to attribution rather than to reagent or solvent supply.

## PART 5: DIY BIOTECH COMMUNITY & ACCESSIBILITY TRENDS

### 5.1 Community Biohacker Spaces and Self-Governance

**Landscape.** Community biology labs — including BioCurious, Genspace, BUGSS (Baltimore), and others — operate across North America, Europe, and Asia/South America/Oceania. DIYbio.org maintains a directory of member labs. As of 2022, DIYbio.org's directory was reported to list 44 community biology labs in North America, 31 in Europe, and 17 across Asia, South America and Oceania (Labiotech.eu, 2022) — roughly 90 labs, though counts vary substantially across sources (from ~30 in 2013 to "over 100 groups" by 2020) and different tallies mix informal meetup groups with labs maintaining physical BSL-1 space.

**Genspace — the first US community biolab.** Genspace, in Brooklyn, New York, was the first nonprofit community biotechnology laboratory in the United States. It was co-founded in 2009 and opened its lab to the public in 2010, by Nurit Bar-Shai, Ellen Jorgensen, Daniel Grushkin, Russell Durrett, and Oliver Medvedik. It operates at Biosafety Level 1 (CDC standards). (genspace.org)

**BioCurious (Silicon Valley).** A community lab in the San Francisco Bay Area, launched via Kickstarter (~2011), volunteer-run and member-supported, operating on a low monthly-membership model.

**DIYbio origins and self-governance.** The DIYbio movement grew out of the San Francisco maker/programmer community in the mid-2000s; Rob Carlson's Wired essay framing the "era of garage biology" dates to this period. Mackenzie Cowell and Jason Bobe founded the nonprofit DIYbio.org in 2008. In July 2011, DIYbio organized a "congress" in San Francisco that drafted a code of ethics promoting transparency, safety, and responsibility; Genspace and BioCurious were among the labs represented. The "Ask a Biosafety Expert" (ABE) service provides free biosafety advice from a volunteer expert panel. Most community labs meet BSL-1 criteria.

### 5.2 Project Examples & Accessibility Demonstrations

**Low-cost open-source instrumentation.** Combining open-source microcontrollers (Arduino) with low-cost 3-D printing (RepRap) has enabled a broad class of very low-cost scientific instruments (documented extensively in the open-source-hardware literature, e.g. the work of J.M. Pearce and others). Multiple open-source PCR machines exist (e.g. OpenPCR).

**Typical project profile.** Documented DIYbio projects include bioluminescent bacteria, DNA-based identification (e.g. matching pet-waste DNA to samples), food-authenticity testing, plastic-degrading bacteria, and personal-gene testing. This profile is BSL-1 hobbyist and civic — which supports the scope conclusion that community labs are not, on current evidence, a pathogen-synthesis vector.

## PART 6: COST TRENDS & TECHNOLOGY READINESS

### 6.1 DNA Synthesis Cost Per Base

**Commercial cost tracking.** Long-run DNA synthesis and sequencing cost/productivity data are tracked by Rob Carlson and Jim Field at synthesis.cc, updated periodically.

**DIY OpenIDS estimates.** System cost ~$19,900 (5-printhead setup); reagent cost ~$100–500 for initial build, ~$1–5 per sequence at scale. Caveat: cost parity with commercial providers (reached at ~1,000+ sequences) is a parity on cost only — OpenIDS produces short (~15–30 nt), moderate-fidelity oligos (see §1.1), not commercial-grade long oligos, so it is not substitutable on capability.

### 6.2 Technology Readiness

| Approach | TRL | Capital | Expertise | Usable length @ fidelity | Oversight status (R0) | Status 2026 |
|---|---|---|---|---|---|---|
| OpenIDS (inkjet/array) | 5 | ~$20K | Medium (6/10) | ~15–30 nt | No oversight reaches DIY builders | Demonstrated; short-oligo only |
| DropSynth (assembly) | 4 | ~$3.4K bead pool | High (8–9/10) | Gene-length via assembly | No oversight | Research prototype; standard mol bio lab (no fabrication) |
| MAS 2.0 (photolith.) | 5 | [[R~€150–170K instrument (~€200–300K loaded)R]] | High (optics+chem) | library-grade | No oversight | Open build; origin-lab demonstrated |
| Electrochemical | 3 | ~$12K (est) | Medium (7/10) | Not established | No oversight | Pre-commercial; no commercial DIY build |
| Enzymatic — DIY (Church) | ~3 | low | High (biochem) | data-storage only | No oversight | Off-the-shelf but not defined-sequence |
| Enzymatic (DNA Script SYNTAX) | 5 | ~€250–280K (quote) | Medium (5/10) | 80–120 nt | Manufacturer/reagent control point | Commercially available |
| Commercial benchtop (column) | 9 | ~$15–150K (best ~$60K) | Low (2/10) | ~100–150+ nt | Uneven; largely unscreened | Mature; active resale market |
| Commercial provider (service) | 9 | $0 (service) | Low (1–2/10) | Genes/genomes | Screened channel (IGSC ~80% capacity) | Mature, screened baseline |

## PART 7: CRITICAL GAPS & RESEARCH OPPORTUNITIES

### 7.1 Identified Research Needs

**Accessibility mapping:** Regime-conditional TRI update incorporating 2025–2026 developments, scoring usable length at high fidelity (not advertised maximum) and throughput. Cost-trajectory characterisation with explicit TRL gating — no point forecasts for TRL-3 approaches. Supply-chain vulnerability across all reagents, not only phosphoramidites. Detectability signatures for DIY-synthesized sequences.

**Bottleneck analysis:** Error-accumulation models for DIY-produced oligos vs commercial. Assembly feasibility from short, moderate-fidelity DIY oligos — partly addressed in §1.5 (assembly from 16–30-mers is demonstrated; the binding constraint is fidelity and the downstream error-correction/verification/host pipeline, per Cui et al. 2024, Lubock et al. 2017, and NTI 2023). Remaining open question: quantify the correct-assembly yield achievable specifically from OpenIDS-grade (~56% full-length) oligos. Maximum usable sequence length on DIY systems as a function of per-step coupling efficiency.

**Policy & governance:** Control-lever effectiveness under R0 vs R1. International harmonization beyond IGSC/OSTP — sharpened by the Part 2 finding that a US mandate directly reaches only 8 of 34 known manufacturers. Benchtop-manufacturer customer-screening mechanisms (the 2024 OSTP framework covers devices, not only sequences). Detection and forensic synthesis-route attribution frameworks (developed in the attribution chapter; scoped to sequence forensics).

**Biosecurity emerging threats:** Sequence-similarity screening is vulnerable to AI-designed variants: after patching, ~3% of the more-probably-functional variants still escaped detection in the Wittmann et al. (2025) study. Function-based screening remains the unsolved problem; the scheduled October 2026 functional-SOC provision is the policy response (see Part 3).

## PART 8: KEY SOURCES & REFERENCE MATERIALS

**Primary Literature (Ranked by Relevance to DIY Synthesis):**

- OpenIDS (Core DIY Technology) — Kim, J., Kim, H., & Bang, D. (2024). "An open-source, 3D printed inkjet DNA synthesizer." Scientific Reports, 14, 3773. GitHub: https://github.com/regiregire/OpenIDS
- OpenIDS2 (2025 Update) — Kim, J., Kim, H., & Bang, D. (2025). "OpenIDS2: A low-cost, 3D-printed, open-source platform for reproducible construction of DNA microarray synthesizers." PLOS ONE.
- Synthesis Screening Policy (Current Framework) — White House OSTP (2024). "Framework for Nucleic Acid Synthesis Screening." https://aspr.hhs.gov/S3/Pages/OSTP-Framework-for-Nucleic-Acid-Synthesis-Screening.aspx
- Biosecurity Vulnerability (Screening Evasion) — Wittmann, B.J., et al. (2025). "Strengthening nucleic acid biosecurity screening against generative protein design tools." Science, 390(6768):82–87. https://doi.org/10.1126/science.adu8578
- Synthesis Screening State of Play — Kane, A. & Parker, M.T. (2024), Applied Biosafety, doi:10.1089/apb.2023.0027.
- DropSynth (Alternative Approach) — Sidore, Plesa, Samson, Lubock & Kosuri (2020). "DropSynth 2.0: high-fidelity multiplexed gene synthesis in emulsions." Nucleic Acids Research, 48(16), e95. Orig.: Plesa, C., et al. (2018). Science, 359(6373):343–347.
- Enzymatic DNA Synthesis (Emerging Technology) — Nova One Advisor / Precedence Research (2024). Enzymatic DNA Synthesis Market. Projection: $296.35M (2024) → $3,159M (2034), ~26.7% CAGR. (Technology-share figures — polymerase 44.25%, TdT 30.42% CAGR — are Mordor Intelligence.)
- DIY Biotech Community — Wikipedia (2026). "Do-it-yourself biology." DIYbio.org support organization: https://DIYbio.org

**Policy & Regulatory Documents:**

- HHS Screening Framework Guidance (2023): predecessor to OSTP framework.
- NIH NOT-OD-25-012: "Notification of NIH Requirements Regarding Procurement of Synthetic Nucleic Acids and Benchtop Nucleic Acid Synthesis Equipment."
- IGSC Harmonized Screening Protocol v3.0 (September 2024).
- Executive Order 14292 (May 5, 2025): Paused OSTP framework implementation; revision underway.

## PART 9: PRELIMINARY RESEARCH DIRECTIONS

**Priority 1: Technology Readiness Index (TRI) Expansion** — Update OpenIDS cost/feasibility with 2026 data; characterize DropSynth/electrochemical accessibility thresholds; model when each approach becomes <$10K, <$5K, <$2K. Deliverable: interactive spreadsheet + visualization.

**Priority 2: Supply Chain Vulnerability** — Map all critical reagents → suppliers → geographic concentration; identify which supply chains can be controlled via export restrictions; model substitution feasibility for each critical input; assess regulatory capture potential (can licensing/tracking actually work?). Deliverable: supply chain network graph + control assessment matrix.

**Priority 3: Detection & Forensics** — Do DIY-synthesized oligos have characteristic error signatures? Can you fingerprint the synthesis method from error patterns? What equipment signatures are detectable (power, waste, timing)? Deliverable: forensic framework specification.

**Priority 4: Policy Options Assessment** — Map all possible regulatory levers (supply chain, export controls, equipment licensing, etc.); model effectiveness, collateral damage, enforcement cost for each; game-theoretic analysis: can policies be maintained long-term or do they erode? Deliverable: policy brief (~2000 words) with cost-benefit analysis.

## APPENDIX: KEY DATA SOURCES & TRACKING RECOMMENDATIONS

**Recommended Monitoring Sources:**

- Technology Development: GitHub trending in dna-synthesis, microfluidics, biotech tags; PLOS ONE, Nature Biotechnology, Science for preprints; OpenIDS GitHub issues/discussions for community troubleshooting.
- Market Intelligence: Synthesis.cc (James Field's cost tracking): http://www.synthesis.cc ; market research reports (Mordor Intelligence, Global Market Insights, Precedence Research); earnings calls from Twist Bioscience, IDT, GenScript.
- Policy Evolution: ASPR S3 (HHS biosecurity): https://aspr.hhs.gov/S3/ ; NIH grants.gov for funding condition updates; IGSC announcements: https://www.igsc.org/
- Community Activity: DIYbio.org forum activity & new lab announcements; BioCurious, Genspace, other community lab project databases; ArXiv preprints in q-bio category.

## SUMMARY: RESEARCH LANDSCAPE AS OF JULY 2026

The DIY frontier is narrow, academic, and skill-gated. OpenIDS/OpenIDS2 (inkjet, ~$4–20K) and MAS 2.0 (photolithographic) are the only reproducible open de novo synthesizers, and both are lab-grade, expertise-heavy, and currently short-oligo/library-grade — not assembly-ready for defined genes. DropSynth (+OMEGA) is cheap DIY assembly but inherits the screening perimeter through its commercial oligo pool. Electrochemical has no DIY build; enzymatic is DIY only in a data-storage-only form; and there is no working garage synthesizer at all. The correct inference is not that screening becomes irrelevant, but that a single point-of-sale control is insufficient: screening must be made mandatory, pushed on-device, extended internationally, and backstopped by forensic attribution for the devices and the residual DIY routes it cannot reach. The problem shifts from "prevent DIY synthesis" to "govern a proliferating-device world with a layered, mandatory, regime-conditional architecture" — which the October 2026 revisions and S. 3741 begin to build, and which this project sets out to stress-test.

[[R— Red text marks what was changed or added in this revision. Summary of changes: (1) MAS 2.0 capital corrected from "tens of $K" to a sourced ~€150–170K instrument / ~€200–300K end-to-end figure (developer interview with Mark Somoza, Helices Biological Photolithography, Jul 2026, + helicesbio.com) — updated in Table A, Table B, §1.3, and the §6.2 TRL table; (2) added the commercial vendor (Helices GmbH), founders, and MAS 2.0 vendor specs in §1.3, and the "no independent build yet" point; (3) corrected the DropSynth "Advantages Over Inkjet" bullet that wrongly attributed microfluidic-droplet throughput figures to DropSynth (which uses bulk vortex emulsification, no microfluidic chip). No other claims were altered.R]]
