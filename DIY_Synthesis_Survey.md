# DIY Oligonucleotide Synthesis Methods — Deep-Research Survey (2026)

**Question (Rassin Q1):** What DIY oligo-synthesis technologies exist that a person could *build or reproduce themselves* — excluding buying a finished commercial benchtop synthesizer? **Q2:** How accessible are they?

*Method: five parallel web-search streams, primary-source fetch, adversarial verification. Claims below are verified against the cited primary source; unverifiable items are flagged.*

## Bottom line

The genuinely DIY / reproducible frontier is **narrow, academic, expertise-gated, and short-oligo**. It consists of three real things — two open-hardware *de novo* synthesizers (**OpenIDS/OpenIDS2**, inkjet phosphoramidite; **MAS 2.0 / AMS**, photolithographic) and one cheap *gene-assembly* method that still consumes commercially-synthesised oligos (**DropSynth**, plus its 2025 peer **OMEGA**). Enzymatic (TdT) DIY exists only in a data-storage-only form; defined-sequence enzymatic needs bespoke reagents. Electrochemical has **no** independent build. And there is **no verified working community / garage synthesizer at all** — the biohacker scene (ODIN, Genspace, DIYbio) buys DNA; it does not make it. For a biosecurity argument this is the key finding: under a screened commercial + benchtop perimeter, the residual DIY capability is real but small, requires serious wet-chemistry/optics skill, and — for the truly independent routes — currently tops out at short homopolymers or error-prone libraries, not assembly-ready defined genes.

## Tiered landscape

### Tier A — Genuinely DIY-reproducible *de novo* synthesizers (published build + protocol)

- **OpenIDS** (Kim, Kim & Bang, *Sci. Rep.* 14:3773, 2024, [10.1038/s41598-024-53944-x](https://www.nature.com/articles/s41598-024-53944-x)). Open-source, 3D-printed **inkjet** synthesizer: industrial Xaar-128 piezo printhead deposits phosphoramidite chemistry onto a silicon wafer; Arduino/Raspberry-Pi control; GitHub repo. **Standard phosphoramidite, capping step omitted** (the forensic hook for Ch. 4). Solvent: **propylene carbonate** replaces acetonitrile for the inkjet (ACN too volatile). **Capital ~$19,900.** Demonstrated **only a 30-nt poly(dT) homopolymer**, ~98%/cycle, urea-PAGE only — no mixed-base sequence, no sequencing.
- **OpenIDS2** (Kim, Kim & Bang, *PLOS ONE* 20(12):e0338478, 2025, [10.1371/journal.pone.0338478](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0338478)). 2nd-gen: ~⅓ volume, custom PCB, 3D-printed peristaltic pumps replace ~$4K of syringe pumps. **Total build ~$4,000** *(correction: the earlier "~$12K" figure is not in the paper — do not use it).* Demonstrated **15-mer poly(dT)**, ~96.1%/step, **53.7% full-length by HPLC**. Fully open (Gerber/CAD/BOM/code). The more reproducible of the two.
- **MAS 2.0 / Advanced Maskless Synthesizer** (Somoza group, ChemRxiv 2024, [10.26434/chemrxiv-2024-j4c90](https://chemrxiv.org/engage/chemrxiv/article-details/65ba15e39138d231611ab534)) — **NEW, and the biggest find.** A **fully open-source benchtop photolithographic (light-directed) synthesizer**: DMD patterns 365 nm UV to photo-deprotect features; full CAD/STL/optical drawings, a costed component list, Python control software, and a chemistry/process manual. 1.5 µm resolution. Needs optics alignment + **photolabile (NPPOC) amidites** (specialty, not commodity); no cleanroom. **Capital ~tens of $k (exact figure in the supplementary spreadsheet, not extracted — flag).** This is the *DIY instantiation of the photolithographic class you reproduced in Ch. 4 (Lietard).*
- **POSaM** (Lausted et al., *Genome Biol.* 5:R58, 2004, [10.1186/gb-2004-5-8-r58](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2004-5-8-r58)) — the seminal open-source inkjet synthesizer (~$34K) OpenIDS builds on. Historical predecessor; documents that open synthesizer designs are 20 years old.

### Tier B — DIY-reproducible gene *assembly* (cheap, but depends on a commercial oligo pool)

- **DropSynth 1.0 / 2.0** (Plesa et al., *Science* 359:343, 2018, [10.1126/science.aao5167](https://www.science.org/doi/10.1126/science.aao5167); Sidore et al., *NAR* 48:e95, 2020, [10.1093/nar/gkaa600](https://academic.oup.com/nar/article/48/16/e95/5874357)). Assembles **commercial microarray oligo pools** into genes via barcoded magnetic beads + **vortex-made water-in-oil emulsion** — *no microfluidic chip, no cleanroom* (correction to a common misconception; it's a Vortex Genie). Standard mol-bio kit only. **~$1–2/gene** + a **~$3,400 bead pool** (~200 reactions). Fidelity **~23–28% perfect** (2.0). Reproducible beyond the origin lab (Plesa lab; dropsynth.org; now commercial via SynPlexity). Newer: **Degenerate DropSynth** (2023, ~1 kb) and **DropSynth-Gold** (2026, ~3 kb, Golden Gate).
- **OMEGA** (Romero lab, bioRxiv 2025, [10.1101/2025.03.22.644747](https://www.biorxiv.org/content/10.1101/2025.03.22.644747v1)) — DropSynth's 2025 peer: pooled Golden Gate gene assembly, **no beads/emulsion**, pure standard-lab, ~$1.50/gene, up to 2.6 kb, 94–97% recovery. Arguably *more* DIY than DropSynth.
- *Key limit:* both are **assembly, not synthesis** — they still require an upstream commercial (screenable) oligo pool. They multiplex access to genes; they do not remove the dependence on industrial synthesis.

### Tier C — Enzymatic (TdT): DIY only at the low end

- **Church terminator-free / kinetic** (Lee et al., *Nat. Commun.* 10:2383, 2019, [10.1038/s41467-019-10258-1](https://www.nature.com/articles/s41467-019-10258-1)) — **the most DIY-reproducible enzymatic route**: **commercial TdT + natural dNTPs + apyrase**, all off-the-shelf, no engineered enzyme, no modified nucleotides. **But** it encodes information in nucleotide *transitions* (stochastic homopolymer runs), not defined sequence — data-storage only, needs a codec + sequencing readout.
- **TdT–dNTP conjugates** (Palluk et al., *Nat. Biotechnol.* 36:645, 2018, [10.1038/nbt.4173](https://www.nature.com/articles/nbt.4173)) and **3′-O reversible-terminator** routes (Mathews 2016; engineered ZaTdT variants, *NAR* 2025, [10.1093/nar/gkaf115](https://academic.oup.com/nar/article/doi/10.1093/nar/gkaf115)) — produce *defined* sequence but require **expressing engineered TdT mutants and synthesising/conjugating modified nucleotides yourself**. Reproducible from the papers by a well-resourced lab; **no reagents are sold as a kit**. This is the answer to Rassin's "can a lab do enzymatic on its own?" — **only a well-resourced one, and only the low-fidelity data-storage variant is truly off-the-shelf.**

### Tier D — Not DIY (conditional-future or purchase-only)

- **Electrochemical** (Xu et al., *Sci. Adv.* 7:eabk0100, 2021, [10.1126/sciadv.abk0100](https://www.science.org/doi/10.1126/sciadv.abk0100); Egeland & Southern 2005; CustomArray/CombiMatrix). Mechanism = electrochemically-generated acid deprotects per electrode. **No independent DIY build exists** — all work is academic (13–17-mers) or defunct-commercial. Barrier: custom CMOS/microelectrode fabrication. **Conditional-future** (this is the class you reproduced in Ch. 4 as Gimpel/Genscript, from the *commercial* side).
- **Enzymatic service** (Ansa) and **commercial benchtop** (DNA Script SYNTAX, Kilobaser ~$35.5–49.5K, Telesis BioXp) — purchase/service, closed cartridges/licensing. Not DIY; the screenable baseline.

### Tier E — Community / garage: nothing working (honest null result)

- **The ODIN, Genspace, Counter Culture Labs, DIYbio, Hackaday, the diyhpl wiki** — all *buy* synthetic DNA; **none synthesise de novo**. The oft-cited diyhpl "DNA synthesis" page is lecture notes, not a build. No verified homebrew synthesizer exists (NTI 2023 confirms the biosecurity concern is *commercial benchtop* devices, not a garage scene). *This null result is itself a reportable governance finding.*

## Master comparison

| Method | Chemistry | DIY-reproducible? | Capital | Per-unit | Usable length @ high fidelity | Reagent access | Expertise | Maturity |
|---|---|---|---|---|---|---|---|---|
| **OpenIDS / OpenIDS2** | inkjet phosphoramidite (no capping) | **Yes** (open build) | ~$20K / **~$4K** | ~$100/run | only poly(dT) 15–30-mer shown | commodity-ish amidites | high (anhydrous wet-chem) | demonstrated, short homopolymer |
| **MAS 2.0 / AMS** | photolithographic (DMD, NPPOC) | **Yes** (open build) | ~tens of $k* | — | library-grade (error-prone) | specialty photo-amidites | high (optics + chem) | demonstrated (origin lab) |
| **DropSynth / OMEGA** | assembly of commercial oligo pool | **Yes** (protocol) | ~$3.4K pool | ~$1–2/gene | genes to ~1–3 kb, ~25% perfect | off-the-shelf + **commercial oligo pool** | moderate | mature, reproduced widely |
| **Enzymatic — Church** | TdT terminator-free | **Yes** (off-the-shelf) | low | low | not defined-sequence (data storage) | commercial TdT/dNTPs/apyrase | high (biochem) | data-storage demo |
| **Enzymatic — defined** | TdT + bespoke terminators | lab-only | — | — | defined but proof-of-concept (≤10-mer academic) | **bespoke, not sold** | very high | proof-of-concept |
| **Electrochemical** | EGA phosphoramidite | **No** build | — | — | 13–17-mer academic | — | — | conditional-future |
| Commercial benchtop / service | phosphoramidite / enzymatic | No (buy) | $35K–$100K+ | — | vendor spec | closed cartridges | low | mature (baseline) |

\*MAS 2.0 dollar figure is in a supplementary spreadsheet not extracted — flag as unverified.

## How it fits your chapters

**Chapter 1 (TRI) — this is Rassin's Q1 + Q2, and it needs three refinements:**
1. **Add MAS 2.0 / AMS** as a DIY method — it's the open-source photolithographic synthesizer, a genuinely new and reproducible build, and it pairs with your Ch. 4 Lietard class. Add **OMEGA** alongside DropSynth, and **POSaM** as the historical open predecessor.
2. **Relabel** enzymatic-service and commercial-benchtop as *baseline, not DIY* (already started), and split enzymatic into "off-the-shelf Church route (data-storage only)" vs "defined-sequence (bespoke, lab-only)".
3. **Corrections the research forces:** OpenIDS2 capital ≈ **$4K** (not $12K); OpenIDS "usable length at high fidelity" is **much lower than the table's ~100–200 nt** — only poly(dT) 15–30-mer is demonstrated, ~54–56% full-length (this is exactly Tessa's usable-length point); and **DropSynth needs no cleanroom/microfluidic chip** (§2.5's "cleanroom fabrication access" is wrong — it's a vortex emulsion). Fixing these tightens the accessibility scoring.

**Chapter 4 (attribution) — the DIY landscape maps onto the classes you already reproduced:** inkjet/column DIY (OpenIDS) → your **column** class; **MAS 2.0 photolithographic** → your **Lietard** class; **electrochemical** → your **Gimpel** class. So the same four fingerprints cover the DIY frontier, and OpenIDS's capping omission is a *DIY-specific* signature you predicted and can test — the strongest link between Q1 and the attribution backstop.

**Rassin's Q3 (residual gap under mandatory commercial + benchtop screening) — the research answers it directly:** once commercial providers and benchtop devices are screened, the residual is (a) a *narrow set of academic open-hardware builds* (OpenIDS, MAS 2.0) that are expertise-gated and currently short-oligo/library-grade, (b) *DropSynth/OMEGA assembly* — which still depends on a screenable commercial oligo pool, so it inherits the perimeter rather than escaping it, and (c) *no working garage capability at all*. The gap is real but small and skill-bounded — a defensible, concrete answer, and one that points to where a mandate would need to reach (open-hardware builds + the assembly-from-pool route) versus where it already bites (the oligo pool upstream of DropSynth).
