# Book of Abstracts (ERA)

**AIxBio Summer 2026**

**Olena Didenko** (mentor: Rassin Lababidi, IBBIS)

**Bio:** I'm a PhD candidate at UCL's Wolfson Institute investigating chemogenetic silencing of nociceptors via PSAM⁴-GlyR systems. My parallel expertise is in biotech entrepreneurship and venture capital — I work with precision immunomics startups (Infinitopes), navigate the founder ecosystem (Nucleate UK, Baby VC), and think deeply about how biosecurity integrates into biotech pipelines and capital allocation.

---

## PROJECT TITLE

**DNA Synthesis Screening Under Device Proliferation: A Regime-Conditional Analysis of DIY Readiness, Control Robustness, and Forensic Attribution (2026–2030)**

*(Working title. If you'd rather keep the older subtitle, swap in: "A Regime-Conditional Readiness Index, Manufacturer Landscape, and Attribution Architecture" — but the version above matches the DIY-focused, four-workstream structure below.)*

---

## OVER THE SUMMER FELLOWSHIP, I WILL:

### 1. Build a regime-conditional Technology Readiness Index (TRI), weighted toward DIY

Score seven synthesis approaches — OpenIDS (inkjet), MAS 2.0 (open-source photolithographic), electrochemical, enzymatic (service and benchtop), DropSynth (emulsion assembly), and commercial column benchtop as a baseline — across nine technical and governance dimensions, with **regime-dependent** detectability and supply-chain scoring (R0 vs R1). The analytical weight sits in the TRL 3–6 band (mature enough to work, accessible enough to reproduce); high-TRL commercial systems are scored only as a reference ceiling.

Two disciplines give the index its rigour. **Capability is scored by usable length at high fidelity, not advertised maximum** — at 98% per-step coupling a 30-mer is full-length only ~55% of the time, and OpenIDS delivers ~55–56% full-length for a short oligo, well below the >90% gene assembly needs. And **every input carries [Lower, Best, Upper] bounds and a HIGH/MEDIUM/LOW confidence tag**, with a worst-case survival test on the qualitative conclusions.

*Deliverable:* a regime-conditional TRI (R0 vs R1 detectability side-by-side) with an open annex scoring workbook and a sensitivity analysis of which inputs drive rank changes.

### 2. Model cost & accessibility trajectories to 2030

State projections as conditional annual-decline scenarios with explicit TRL gating, not mechanical curve fits. OpenIDS — the only DIY route with a real cost anchor ($19,900, Kim et al. 2024) — is modelled at ~5/8/15%/yr: base case ~$16.8K (2026) → ~$12.1K (2030), crossing <$15K around 2027 and <$10K only ~2028 (optimistic) / ~2032 (base). Electrochemical cost is undefined at TRL 3 (maturation modelled first, cost second); the enzymatic benchtop is commercial-only (~$270–303K now; IFP's 2030 model peaks near ~$190K, IQR ~$112–298K). The load-bearing conclusion: because commercial cost-per-base has plateaued (~$0.07/bp), **the DIY accessibility barrier is capital cost, not per-base cost** — and even where OpenIDS undercuts providers at volume, it yields raw short oligos, not assembled, verified, screened product.

*Deliverable:* conditional cost-trajectory figures with scenario bands and the like-for-like cost-per-usable-base comparison.

### 3. Conduct a regime-conditional control-robustness assessment (incl. the supply-chain and resale analyses)

Assess which control points survive under both regimes, and fold in the supply-side evidence that reagent and device channels are not durable levers.

- **R0 (status quo, October 2026):** OSTP framework revision paused; IGSC v3.0 voluntary; no on-device mandate; no reagent monitoring. Every lever is fragile.
- **R1 (projected mandatory + on-device, October 2026 onward):** S. 3741 (Commerce-enforced screening) + the OSTP framework's 50-nt window, functional SOC definitions, and on-device expectations. Durable **for regulated commercial devices** — but open firmware weakens on-device screening for DIY, and legacy/secondhand devices escape it.
- **Supply-chain evidence (three companion analyses):** phosphoramidites (~45–60 suppliers, commodity, substitutable); the **DIY input chain** (commodity chemistry + commodity hardware, with only two narrow method-specific hardware exceptions — the photolithographic DMD and the electrochemical CMOS array); and the **benchtop chain** (two real chokepoints — proprietary reagent cartridges and the device manufacturer — but both leaked by the used-device and spare-parts markets).
- **Secondary-market monitorability:** used benchtop and gene-assembly instruments (from ~£670 to ~$25K) resell openly with no buyer verification and cross-border shipping, carrying none of their point-of-sale controls.

*Reach context (from the ERA/IBBIS manufacturer inventory):* a US mandate directly binds only ~8 of 34 known benchtop manufacturers, with ~14 outside reach and the newest, highest-throughput capacity concentrating there — so international harmonisation is load-bearing, not optional.

*The headline finding, HIGH-confidence and surviving worst-case:* **supply-chain restriction is not a durable control point under either regime; control belongs at the device and the provider, not the input.**

*Deliverable:* a control-architecture diagram (levers, regime dependence, robustness) + a worst-case survival matrix, with the DIY/benchtop supply-chain and resale annexes as supporting evidence.

### 4. Build and prove a synthesis-route attribution framework

Specify — and now demonstrate — a post-hoc capability: infer the synthesis route from characteristic error signatures in a product's sequence, using reads alone, with no device cooperation.

**From specification to proof.** Reprocessing four deposited datasets (Masaki, Filges, Lietard, Gimpel) from raw reads reproduces their published per-method signatures to within ~±20% — column phosphoramidite (capping-driven G→A; Ac₂O→Pac₂O shift at 12.2×), photolithographic (G→T), and electrochemical vs material-deposition (18.8× deletion-rate separation). On a single co-processed reference atlas (65 runs), the **four synthesis chemistries separate at 100% balanced accuracy** (leave-one-run-out, permutation p≈0.01), while within-chemistry vendor attribution is **hard** under leakage-safe leave-one-lot-out (near-neighbour IDT-vs-Sigma only ~72%, borderline). Cross-chemistry attribution is the strong, defensible result.

**Honest scope.** Class-level, not device-level ("this came off an array-based process," not a serial number); value scales inversely with how many devices share a signature; following the GEA literature (Alley et al. 2020; Crook et al. 2022), **exclusion is the primary output** — ruling out a commercial-provider origin redirects an investigation from order records toward equipment. A concrete DIY-vs-commercial discriminator is specified (OpenIDS omits capping → suppressed G→A + elevated n−1), mechanistically anchored in the reproduced Masaki result and awaiting collaborator product data (infohazard-reviewed via IBBIS; no synthesis performed in-house).

*Deliverable:* an attribution-framework specification (2–3 pages) with feasibility assessment, reproduction results, and evidence tiers.

### 5. Translate findings into policy recommendations

Stakeholder-specific recommendations for regulators (OSTP, HHS/ASPR, IGSC), manufacturers, researchers (IBBIS, academia), and funders — spanning the October 2026 framework revisions, the jurisdictional ceiling, forensic-capability investment, proprietary-reagent tracking, the resale/legacy gap, and functional-SOC detection.

*Deliverable:* stakeholder-specific recommendations (2–3 pages) with investment priorities and timelines.

---

## DELIVERABLES

**Technical Report (~5,000 words)** — regime-conditional TRI (R0 vs R1); cost & accessibility trajectories; control-robustness analysis with the DIY/benchtop/phosphoramidite supply-chain and secondary-market annexes; attribution framework and reproduction results; limitations and confidence bounds; policy recommendations by stakeholder and timeframe.

**Policy Brief (~2,000 words)** — *DNA Synthesis Screening Under Device Proliferation: Governance Architecture for 2026–2030.* Audience: OSTP, HHS/ASPR, IGSC, congressional staff, international coordinators.

**Open annexes:** TRI scoring workbook; supply-chain and secondary-market monitorability analyses.

**Expert validation:** 2–3 reviews confirming analytical validity.

---

## ABSTRACT

DNA synthesis screening is not approaching obsolescence through clever evasion. It is being strengthened — made mandatory and pushed onto the synthesis device itself (S. 3741, January 2026; OSTP framework revision due October 2026) — at the same moment that benchtop and DIY synthesis capability is proliferating into jurisdictions a US mandate cannot reach.

The policy question is therefore not *"How do we prevent synthesis screening from failing?"* but *"As screening becomes mandatory and on-device while devices proliferate, where does control remain robust, where does it erode, and where must policy shift to keep pace through 2030?"*

This fellowship characterises the regime-conditional control architecture for DIY synthesis governance (2026–2030) through four workstreams: **(1)** a regime-conditional Technology Readiness Index scoring seven synthesis approaches by usable length at high fidelity, with full confidence bounds; **(2)** conditional cost & accessibility trajectories to 2030; **(3)** a control-robustness assessment across both regimes, incorporating the reagent, DIY-hardware, benchtop-consumable, and secondary-market supply chains as evidence that input-level restriction is not durable; and **(4)** a synthesis-route attribution framework — now proven on real data — that infers the production route from sequencing reads alone.

Two findings anchor the work. First, **supply-chain restriction is not a durable control point under either regime** (HIGH confidence, surviving worst-case): the DIY input chain is commodity chemistry plus commodity hardware, and the benchtop chain's two genuine chokepoints (proprietary consumables, the manufacturer) are leaked by an open resale and spare-parts market — so control belongs at the device and the provider, not the input. Second, reprocessing four deposited datasets from raw reads reproduces their published error signatures to within ~±20%, and a co-processed reference atlas separates the four synthesis chemistries at **100% balanced accuracy** (leave-one-run-out, p≈0.01), while within-chemistry vendor attribution is hard under leakage-safe validation — establishing class-level attribution as a feasible forensic backstop for the devices manufacturer-side controls cannot reach.

**Scope.** Analysis is limited to the synthesis step. Downstream stages (assembly, pathogen rescue, deployment) are out of scope: per NTI (2023) expert consensus, near-future benchtop devices are expected to produce dsDNA up to roughly 7,000 bp, while reliable assembly beyond ~7,000–10,000 bp requires bacterial and yeast host systems and virus-specific expertise. The binding constraint sits downstream of synthesis, which is precisely why the synthesis step is the governable chokepoint worth characterising. Method-level detectability and supply-chain scoring are held pending IBBIS infohazard review.

**Impact.** Shifts the synthesis-screening conversation from threat-ranking toward governance-architecture design: which controls remain robust, which are fragile, and where policy must invest so that a mandatory, on-device regime is actually effective — and actually reaches far enough — through 2030.

---

## RESEARCH INTERESTS

Supply-chain vulnerability analysis and realistic control-point identification · technology forecasting for dual-use biotechnology capabilities · biosecurity infrastructure resilience beyond synthesis screening · detection and forensic-attribution frameworks for DNA synthesis · policy gaps and governance options for the post-screening biosecurity landscape · economic and accessibility trends in synthetic-biology tools (learning curves, cost reductions) · international coordination and enforcement challenges in biotech governance · evidence-based policy (translating technical forecasts into actionable regulation) · responsible-innovation frameworks for biotechnology capability democratization · integration of biosecurity into biotech business models and VC investment decisions.

**Email:** olena.didenko.24@ucl.ac.uk
