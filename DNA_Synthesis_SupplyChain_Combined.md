# The DNA Synthesis Supply Chain — DIY and Benchtop, Combined

### A Biosecurity Monitorability & Control-Point Assessment, with a Full Compound/Component Regulatory-Feasibility Matrix

*Companion to the Phosphoramidite Supply-Chain Assessment. Monitorability framing only; no operational build detail. This document characterises **every input a synthesis route needs and whether it is a durable control point** — it is not a procurement guide. Where a compound is genuinely hard to obtain, that is noted as a natural **access barrier**, which is not the same as a **regulatable chokepoint** (an input whose sales can be meaningfully monitored or licensed).*

---

## 1. Bottom line

Across the whole landscape — DIY and benchtop, chemical and enzymatic — **almost no input is a durable regulatory chokepoint.** The reagents are commodity, the solvents are substitutable, and the few genuinely hard-to-source items are hardware, not chemistry: the photolithographic **DMD** (effectively single-sourced) and the electrochemical **CMOS electrode array** (needs a foundry). Even those are *access barriers*, not monitoring points, because their legitimate markets (projectors, semiconductors) dwarf any synthesis use.

The one asymmetry: **DIY has no controllable input at all**, while **benchtop has two partial ones** — the proprietary reagent cartridge (licensable/KYC-able) and the device manufacturer (where on-device screening attaches) — both of which are then leaked by the used-device and spare-parts markets.

**Governance conclusion (HIGH confidence, matching Ch. 2):** you cannot secure DNA synthesis by controlling its inputs. Control belongs at the **device**, the **provider/order**, and **post-hoc attribution** — not the compound.

---

## 2. How to read the "Regulate?" column

Feasibility of using an input as a biosecurity control lever, rated:

- **Infeasible** — ubiquitous commodity, many suppliers, substitutable, overwhelming legitimate demand. No plausible control.
- **Very low** — multi-sourced specialty chemical/part; no control regime; heavy non-synthesis use.
- **Low** — concentrated or specialty; few suppliers; a *partial access barrier* but weak as a monitoring lever.
- **Access barrier (not regulatable)** — genuinely hard to obtain or make (semiconductor fab, engineered enzyme), so it slows a builder — but sales cannot be monitored because legitimate markets dominate.
- **Partial chokepoint** — a real, existing control point (only the benchtop proprietary consumable and the manufacturer qualify) — but bounded by resale/aftermarket.

---

## 3. The full input matrix

*Grouped by category. "Used by" abbreviations: **Col** = column/commercial benchtop, **OID** = OpenIDS inkjet, **MAS** = MAS 2.0 photolithographic, **EC** = electrochemical, **EnzS/EnzB** = enzymatic service/benchtop, **DIY-Enz** = off-the-shelf enzymatic, **DS** = DropSynth assembly.*

| # | Compound / component | Category | Function | Used by | Sourcing & substitutability | Legit (dual-use) demand | **Regulate?** |
|---|---|---|---|---|---|---|---|
| 1 | **dA / dC / dG / dT phosphoramidites** (DMT-protected) | Core reagent | The four activated, protected DNA building blocks | Col, OID, MAS, EC | ~45–60 suppliers worldwide (Glen Research, ChemGenes, Biosearch/LGC, Hongene, Sigma…); substitutable across vendors; can be made on demand (Sandahl 2021) | Enormous — therapeutics (ASO/siRNA/mRNA), diagnostics, research | **Infeasible** (see phosphoramidite doc) |
| 2 | **Modified / RNA amidites** (2′-OMe, LNA, etc.) | Core reagent | Optional modified bases | Col, MAS | Many specialty suppliers; not needed for basic DNA | Large (RNA drugs) | **Infeasible** |
| 3 | **Photolabile amidites — NPPOC / BzNPPOC** | Specialty reagent | 5′-photocleavable protecting group for light-directed synthesis | MAS | Few specialty suppliers; **not commodity** | Niche (array/library synthesis) | **Low** — one of the few real reagent frictions, but narrow and method-specific |
| 4 | **Activator** — 1H-tetrazole / ETT / DCI / BTT | Cycle reagent | Activates amidite for coupling | Col, OID, MAS, EC | Standard from every oligo-reagent house; four interchangeable options | Large | **Infeasible** (substitutable class) |
| 5 | **Oxidiser** — iodine / pyridine / water / THF (or CSO for non-aqueous) | Cycle reagent | Oxidises phosphite triester → phosphate | Col, OID, MAS, EC | Iodine is a bulk commodity; non-aqueous substitute exists | Vast (iodine is ubiquitous) | **Infeasible** |
| 6 | **Deblock acid** — di-/tri-chloroacetic acid in DCM/toluene | Cycle reagent | Removes 5′-DMT to expose next coupling site | Col, OID, MAS | Bulk commodity chemicals | Vast | **Infeasible** |
| 7 | **Capping A** — acetic anhydride (Ac₂O; or Pac₂O) | Cycle reagent | Caps failed sequences (terminates n−1) | Col, MAS, EC | Bulk commodity; **omitted in OpenIDS** (forensic signature, Ch. 4) | Vast (Ac₂O is a huge-volume industrial chemical) | **Infeasible** |
| 8 | **Capping B** — N-methylimidazole (NMI) | Cycle reagent | Catalyst for capping | Col, MAS, EC | Commodity | Large | **Infeasible** |
| 9 | **Coupling/wash solvent** — anhydrous acetonitrile (MeCN) | Solvent | Reaction/wash solvent | Col, OID, MAS, EC | **Substitutable by propylene carbonate (GRAS)** — Kim 2024 | Vast | **Infeasible** (Ch. 2 solvent finding) |
| 10 | **Cleavage/deprotection** — aq. ammonia (NH₄OH) or AMA | Reagent | Cleaves product from support; removes base protection | Col, OID, MAS, EC | Bulk commodity | Vast | **Infeasible** |
| 11 | **Inert gas** — argon / nitrogen | Consumable | Maintains anhydrous atmosphere | Col, OID, MAS, EC | Industrial-gas commodity | Vast | **Infeasible** |
| 12 | **Solid support** — controlled-pore glass (CPG) / polystyrene / universal support | Support | Anchors the growing chain | Col, OID | Multi-sourced (Prime Synthesis, Glen, ChemGenes, Kisker…) | Large | **Very low** — mildly specialised, no control regime |
| 13 | **Functionalised glass/silica slides** | Support/substrate | Array synthesis surface | MAS | Standard microarray substrates; multi-sourced | Large (microarrays) | **Very low** |
| 14 | **Electrolyte + electrogenerated-acid system** (e.g. quinone/hydroquinone mediator + confining base) | EC reagent | Generates acid at active electrodes for spatially-controlled deblock | EC | Standard electrochemistry reagents | Broad (electrochemistry) | **Infeasible** |
| 15 | **Industrial piezo inkjet printhead** | Hardware | Deposits reagent droplets onto array spots | OID | A handful of makers (Fujifilm Dimatix, Xaar, Konica Minolta, Epson, Ricoh, Kyocera); commodity | Vast (textile, ceramic, label, 3D printing) | **Very low** — Ch. 2 "printhead lever" fails on cover demand |
| 16 | **Digital micromirror device (DMD)** | Hardware | Patterns UV to photo-deprotect chosen features | MAS | **Effectively single-sourced (Texas Instruments DLP)** | Vast (every DLP projector) | **Access barrier (not regulatable)** — near single-source, but monitoring sales is hopeless vs projector market |
| 17 | **UV source ~365 nm + projection optics** | Hardware | Illumination for photo-deprotection | MAS | Commodity UV LEDs (Nichia etc.) + standard optics | Large | **Very low** |
| 18 | **CMOS / microelectrode array chip** | Hardware | Addressable electrodes for site-selective electrochemistry | EC | **Custom semiconductor fabrication — foundry access + chip design** | Vast (all CMOS) | **Access barrier (not regulatable)** — the hardest single DIY item, but TRL 3 / conditional-future |
| 19 | **Microcontroller** (Arduino / Raspberry Pi) | Hardware | Device control | OID, MAS, EC | Ubiquitous commodity electronics | Vast | **Infeasible** |
| 20 | **Pumps / valves / PEEK manifolds / tubing / seals** | Hardware | Anhydrous reagent fluidics | Col, OID, MAS, EC | Commodity lab-fluidics + à-la-carte webshops (OligoMaker) | Large | **Very low** |
| 21 | **3D-printed structural parts** | Hardware | Device frame/chassis | OID, MAS | Self-produced from open CAD | n/a | **Infeasible** |
| 22 | **Terminal deoxynucleotidyl transferase (TdT)** | Enzyme | Template-independent base addition | EnzS, EnzB, DIY-Enz | Commercial (NEB, Thermo…) for wild-type; **engineered TdT is proprietary** for defined-sequence | Large (research) | Commodity **Infeasible** for WT; **Access barrier** for engineered variant |
| 23 | **dNTPs** — natural | Enzyme reagent | Substrate for TdT / assembly | all enzymatic, DS | Commodity | Vast | **Infeasible** |
| 24 | **Modified / reversible-terminator dNTPs or TdT–dNTP conjugates** | Specialty reagent | Enable *defined-sequence* enzymatic synthesis | EnzB (defined-seq) | **Bespoke, co-developed with the enzyme — proprietary, multi-year** | Emerging (enzymatic DNA firms) | **Access barrier (not regulatable)** — capability barrier, not a purchasable input |
| 25 | **Apyrase** | Enzyme | Degrades excess dNTP (kinetic control) | DIY-Enz (Lee 2019) | Commodity (Sigma) | Research | **Infeasible** |
| 26 | **Divalent-cation cofactor** (Co²⁺ / Mg²⁺ / Mn²⁺) + buffer | Reagent | TdT catalytic cofactor | all enzymatic | Commodity salts | Vast | **Infeasible** |
| 27 | **Reversible-terminator cleavage reagent** (e.g. TCEP or specific conditions) | Reagent | Unblocks 3′ end each cycle | EnzB (defined-seq) | Commodity or method-specific | Large | **Infeasible** |
| 28 | **Commercial microarray oligo pool** | Input | The oligos DropSynth assembles into genes | DS | Ordered from a **screenable provider** | Large | **Partial chokepoint (via provider screening)** — DropSynth *inherits the perimeter* through this input |
| 29 | **Barcoded microbeads** | Consumable | Compartment barcoding for pooled assembly | DS | Specialty consumable (~$3.4K pool) | Niche | **Low** — specialty but no control rationale |
| 30 | **Emulsion oil / surfactant** | Consumable | Water-in-oil compartments (vortex, no microfluidics) | DS | Commodity | Large | **Infeasible** |
| 31 | **Assembly enzymes** — polymerases, T4 ligase, Type IIS (BsaI/BsmBI) | Enzyme | PCR assembly / Golden Gate | DS | Commodity molecular-biology reagents | Vast | **Infeasible** |
| 32 | **Proprietary reagent cartridge / kit** (DNA Script SYNTAX; Kilobaser chip; BioXP kit) | Consumable | Closed, licensed consumable a benchtop runs on | EnzB, some Col benchtops | **Vendor-locked, licensed** | Moderate (instrument owners) | **Partial chokepoint** — the strongest benchtop lever (KYC-able) — but see resale (#34) |
| 33 | **The instrument itself** (benchtop synthesizer / assembly workstation) | Device | The synthesis engine; on-device screening point | Col, EnzB | 34-firm manufacturer landscape; ~8 US-bound / ~14 outside | Legitimate labs | **Partial chokepoint** — manufacturer/on-device lever, but ~8/34 reach + ~35% legacy |
| 34 | **Used / resold instruments + spare parts** | Aftermarket | Second-hand devices, à-la-carte parts & reagents | Col, EnzB | Open resale (eBay, LabX, EquipNet); OligoMaker parts/amidites | — | **Anti-chokepoint** — routes around both #32 and #33; no buyer verification |

---

## 4. What the matrix shows (summary by category)

- **Cycle chemistry (rows 1, 4–11, 14):** uniformly **infeasible** to regulate — commodity, substitutable, vast legitimate demand. This is the phosphoramidite finding generalised to every ancillary reagent.
- **Supports (12–13):** very low — mildly specialised, no regime.
- **Hardware (15–21):** almost all very low/infeasible. The two exceptions — the **DMD (16)** and **CMOS array (18)** — are genuine *access barriers* but **not regulatable**, because you cannot monitor sales against the projector and semiconductor markets.
- **Enzymatic (22–27):** the *useful* (defined-sequence) route is gated by an **engineered enzyme + bespoke nucleotides** — a capability barrier, not a supply one; the off-the-shelf route uses only commodities and can't make defined sequence anyway.
- **Assembly (28–31):** commodity, **except** the oligo pool (28), which is *screenable* — a control feature, not a gap.
- **Benchtop-only (32–34):** the **only** real chokepoints in the entire landscape (proprietary cartridge, manufacturer) — both **first-sale levers leaked by the aftermarket (34).**

**Count:** of 34 inputs, ~28 are Infeasible/Very-low, 3 are Low, 2 are Access-barriers-but-not-regulatable (DMD, CMOS array), and only **3 are genuine (partial) chokepoints** — all benchtop-side (oligo pool via provider, proprietary cartridge, manufacturer), and the last two are eroded by resale.

---

## 5. Governance verdict — the DIY vs benchtop asymmetry

| | DIY chain | Benchtop chain |
|---|---|---|
| Durable input chokepoint? | **None** (commodity chemistry + commodity hardware) | **Two, partial** (proprietary cartridge; manufacturer) |
| Genuine access barriers | DMD (photolith.), CMOS array (electrochem.) — narrow, method-specific, not regulatable | — |
| Screenable input | DropSynth oligo pool (inherits perimeter) | — |
| What breaks the levers | Substitutability + commodity hardware | Resale + spare-parts aftermarket |
| Net | Input control is a **dead end** | Input control is a **partial, first-sale lever only** |

**Therefore:** reagent/component control is not a viable primary lever for either path. Durable control belongs at **on-device screening** (compliant new devices), **provider/order screening** (reaches DropSynth's oligo input and all services), **record retention**, and **post-hoc attribution** (Ch. 4) — with **international harmonisation** load-bearing because the one real device-side lever (the manufacturer) is jurisdictionally capped at ~8 of 34.

---

## 6. Verify before finalising

- **"TI is effectively the sole DMD source" (row 16)** — strong and useful; confirm against the current DMD-supplier market with a one-line citation.
- **Cartridge-lock claims (row 32)** — SYNTAX and Kilobaser are cartridge/chip-based; verify the column-benchtop reagent-kit lock-in per vendor before asserting it broadly.
- **Engineered-TdT / modified-dNTP barrier (rows 22, 24)** — frame as a *capability* barrier (co-developed enzyme + nucleotide), not a purchasable-input barrier.
- **Supplier/maker example lists** are illustrative, not censuses — don't quote counts from them without a source.
- **34-firm / 8-of-34 figures** — cite the ERA/IBBIS manufacturer inventory as the source, per your updated Chapter 1 and IBBIS summary.

*References carried from Chapters 1–2 and 4 and the phosphoramidite assessment: Kim, Kim & Bang 2024 (OpenIDS); Somoza et al. 2024 (MAS 2.0); Xu et al. 2021 (electrochemical); Palluk et al. 2018 & Lee et al. 2019 (enzymatic); Sidore/Plesa/Kosuri 2020 (DropSynth); Sandahl et al. 2021 (on-demand amidites); Masaki et al. 2022 (capping signature); IFP/Langenkamp 2024; NTI 2023.*
