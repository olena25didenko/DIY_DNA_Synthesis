# The DIY DNA Synthesis Supply Chain — A Biosecurity Monitorability & Control-Point Assessment

*Companion to the Phosphoramidite Supply-Chain Assessment. Detection/attribution framing only; no operational build detail. This document characterises **what a DIY builder must source and whether any of it is a durable control point** — it is not a procurement guide.*

## 1. Bottom line

Across every DIY synthesis route, **no single input is a durable control point**. The reagents are commodity, the solvents are substitutable, and the only genuinely hard-to-source items are two method-specific pieces of *hardware*: the custom CMOS/microelectrode array an electrochemical synthesizer needs, and — more sharply than usually noted — the **digital micromirror device (DMD)** at the heart of a photolithographic build, which is effectively single-sourced. Everything else (activator, oxidiser, deblock, capping reagents, controlled-pore glass, inkjet printheads, microcontrollers, pumps, TdT enzyme, dNTPs) is multi-sourced with overwhelming legitimate demand. The governance implication is identical to the phosphoramidite finding and reinforces it: **you cannot secure DIY synthesis by controlling its inputs; control belongs at the device and at post-hoc attribution.**

The one asymmetry worth surfacing: **inkjet (OpenIDS) and column DIY have no hardware chokepoint at all, whereas photolithographic (MAS 2.0) and electrochemical each have exactly one** — the DMD and the electrode array, respectively. That is a real, method-specific access barrier, but it is narrow and does not generalise.

## 2. Scope

The DIY landscape spans five routes (per the TRI): OpenIDS inkjet, MAS 2.0 photolithographic, electrochemical (conditional-future, TRL 3), enzymatic-DIY (off-the-shelf, data-storage-only), and DropSynth emulsion assembly. Each needs a different bill of materials; this assessment groups those materials into input categories and asks, for each, whether restriction or monitoring is a durable lever.

## 3. The DIY input categories

### 3.1 Cycle reagents (phosphoramidite routes: OpenIDS, MAS 2.0, electrochemical)

The phosphoramidite reaction cycle needs four ancillary reagent classes beyond the amidites themselves:

- **Activator** — tetrazole, 5-ethylthio-1H-tetrazole (ETT), 4,5-dicyanoimidazole (DCI), or benzylthiotetrazole (BTT)
- **Oxidiser** — iodine in pyridine/water/THF (or a non-aqueous alternative)
- **Deblock / detritylation** — di- or trichloroacetic acid in dichloromethane or toluene
- **Capping** — acetic anhydride (Cap A) + N-methylimidazole (Cap B) — **note: OpenIDS omits capping entirely**, which is both what makes it cheaper and what creates its forensic signature (suppressed G→A, elevated n−1; Ch. 4)

**Chokepoint status: NONE.** These are standard research chemicals sold by every oligo-reagent house (Glen Research, ChemGenes, Biosearch/LGC, Sigma-Aldrich, and many others) and, for the bulk chemicals, by general chemical suppliers. No scheduling, no KYC, substitutable within each class.

### 3.2 Solvents

Anhydrous acetonitrile is the standard wash/coupling solvent. Kim et al. (2024) demonstrated OpenIDS running on **propylene carbonate**, a GRAS food additive, and other aprotic substitutes exist.

**Chokepoint status: NONE** — an unregulated commodity with a demonstrated GRAS substitute. (This is already the Ch. 2 solvent finding; it applies to any phosphoramidite DIY route, not just OpenIDS.)

### 3.3 Solid supports / substrates

Column routes use **controlled-pore glass (CPG)** or macroporous polystyrene loaded with the first nucleoside (universal supports also exist). Array routes (MAS 2.0) use functionalised glass/silica slides.

**Chokepoint status: WEAK.** CPG is a mildly specialised consumable but multi-sourced (e.g. Prime Synthesis, Glen Research, ChemGenes, Kisker, and others); functionalised slides are standard microarray substrates. No single supplier, no control regime.

### 3.4 Device hardware — the one place chokepoints actually appear

This is where the routes diverge, and it is the analytically important part:

| Route | Key hardware | Chokepoint? |
|---|---|---|
| **OpenIDS (inkjet)** | Industrial piezoelectric printhead; 3D-printed frame; Arduino/Raspberry Pi; syringe/peristaltic pumps, valves, tubing | **Weak.** Industrial printheads come from a handful of makers (e.g. Fujifilm Dimatix, Xaar, Konica Minolta, Epson, Ricoh) but are commodity items with huge non-synthesis demand (textile, ceramic, label printing). The Ch. 2 "printhead sourcing" lever fails for exactly this reason. |
| **MAS 2.0 (photolithographic)** | **DMD chip**; ~365 nm UV source/optics; **photolabile amidites (NPPOC/BzNPPOC)** | **Partial — and the strongest DIY case.** The DMD is effectively **single-sourced** (Texas Instruments DLP is the dominant commercial micromirror device). The photolabile amidites are a specialty, non-commodity reagent from few suppliers. UV LEDs and optics are commodity. So photolithographic DIY carries *two* narrow frictions — one hardware, one reagent — neither absolute. |
| **Electrochemical (TRL 3)** | **Custom CMOS / microelectrode array** | **Yes — genuine fabrication barrier.** A bespoke semiconductor part requires foundry access and chip-design expertise; this is the hardest single item in the whole DIY landscape. But the method is TRL 3 with no independent build, so it is a *conditional-future* chokepoint, not a present one. |

**Reading this:** the durable barriers in DIY are not reagents at all — they are the DMD (photolithographic) and the CMOS array (electrochemical). Both are method-specific, and the two most accessible routes (inkjet OpenIDS, and any column build) have *no* hardware chokepoint.

### 3.5 Enzymes and nucleotides (enzymatic-DIY)

The off-the-shelf DIY enzymatic route (Lee et al. 2019) uses commercial **TdT + natural dNTPs + apyrase** — all commodity (NEB, Thermo, Sigma). But this route makes only stochastic homopolymers for data storage, **not defined sequences**. A *useful* (defined-sequence) enzymatic route needs engineered TdT + modified/reversible-terminator dNTPs that must be co-developed — a proprietary, multi-year capability, not a purchasable input.

**Chokepoint status: SPLIT.** Commodity for the route that doesn't make usable sequence; a genuine capability barrier (not a supply barrier) for the route that does. Either way, reagent *restriction* is not the lever.

### 3.6 Assembly inputs (DropSynth)

DropSynth consumes a **commercial microarray oligo pool** plus barcoded beads and standard assembly enzymes (polymerases, ligases, Type IIS restriction enzymes such as BsaI/BsmBI). The bead pool and enzymes are commodity molecular-biology items.

**Chokepoint status: the oligo pool is the exception that proves the rule.** DropSynth's one non-commodity input is a *provider-screenable* oligo pool — so DropSynth **inherits the screening perimeter through its inputs** rather than sitting outside it. This is a control *feature*, not a gap.

## 4. Chokepoint summary (DIY)

| Input category | Durable standalone control? |
|---|---|
| Cycle reagents (activator/oxidiser/deblock/cap) | No |
| Solvents (incl. GRAS substitute) | No |
| Solid supports / substrates (CPG, slides) | No (weak) |
| Inkjet printheads / microcontrollers / pumps | No (weak) |
| **Photolabile amidites (photolithographic)** | Partial (specialty reagent) |
| **DMD (photolithographic)** | Partial → strong (near single-source: TI) |
| **CMOS / microelectrode array (electrochemical)** | Yes, but conditional-future (TRL 3) |
| Enzymatic reagents (TdT/dNTPs) | No (commodity); useful route gated by capability, not supply |
| DropSynth oligo pool | Screenable — inherits the perimeter |

## 5. Governance verdict

For misuse control, the DIY supply chain is **low value as a lever**: the accessible routes (OpenIDS, column) have no controllable input, and even the routes with a hardware chokepoint (photolithographic DMD, electrochemical array) are reached far more effectively at the *device* than at the *component* — you cannot meaningfully monitor DMD or printhead sales, both of which are swamped by legitimate demand. This directly corroborates the Ch. 2 conclusion that supply-chain restriction is not durable, and extends it: **the DIY input chain is even less controllable than the phosphoramidite chain, because it adds commodity hardware to commodity chemistry.**

The two narrow exceptions (DMD, CMOS arrays) are worth naming in the thesis precisely because they are the *only* places a component-level barrier exists — and both are method-specific, neither is absolute, and both are better addressed as *device classification* questions than as supply controls.

**Where control is tractable instead:** the synthesis order (for DropSynth's oligo-pool input), the device (on-device screening, if DIY builds are classified), and post-hoc attribution (Ch. 4) — the same three levers the phosphoramidite assessment lands on.

## 6. Open items to verify before finalising

- Confirm the specific printhead and DMD part used in the OpenIDS and MAS 2.0 papers if you want to cite exact models (kept generic here deliberately).
- The "TI is effectively the sole DMD source" claim is strong and useful but worth a one-line citation check against the current DMD-supplier market.
- CPG supplier list is illustrative, not a census — verify before asserting a count.

*References carried from Chapters 1–2 and 4: Kim, Kim & Bang 2024 (OpenIDS); Somoza et al. 2024 (MAS 2.0); Xu et al. 2021 (electrochemical); Lee et al. 2019 (enzymatic-DIY); Sidore/Plesa/Kosuri 2020 (DropSynth); Sandahl et al. 2021 (on-demand amidites).*
