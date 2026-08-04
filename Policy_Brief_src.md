# Policy Brief — DNA Synthesis Screening Under Device Proliferation

### Governance Architecture for 2026–2030

**Author:** Olena Didenko · AIxBio Summer Fellowship 2026 · Mentor: Rassin Lababidi (IBBIS)
**Audience:** OSTP; HHS/ASPR; IGSC; congressional staff (Senate Commerce, Science & Transportation); international coordinators (IBBIS, allied and partner governments).

---

## The problem, in one paragraph

Nucleic-acid synthesis screening is being strengthened, not quietly defeated: it is becoming mandatory and moving onto the synthesis device itself — at the same moment that do-it-yourself (DIY) and benchtop synthesis capability is proliferating and, increasingly, concentrating in jurisdictions a United States mandate cannot reach. The policy question is therefore not "how do we stop screening from failing?" but "as screening becomes mandatory and on-device while devices proliferate, where does control remain robust, where does it erode, and where must policy shift to keep pace through 2030?" This brief translates a technical review of seven synthesis approaches, the benchtop-manufacturer landscape, the reagent and device supply chains, and a demonstrated forensic-attribution capability into stakeholder-specific recommendations.

**At a glance.**

| Key figure | Value |
|---|---|
| Benchtop manufacturers directly bound by a US mandate | 8 of 34 (14 outside all reach) |
| Reproducible open DIY synthesizers | 2 — OpenIDS (~$19.9K) and MAS 2.0 (~€200–300K) |
| Cross-chemistry forensic attribution accuracy | 100% (leakage-safe); vendor-level ~72% (hard) |
| AI-designed variants still missed after patching | ~3% (~97% flag rate) |
| Phosphoramidite suppliers worldwide | ~45–60 (no chokepoint) |
| Assembly ceiling before host systems required | ~7,000–10,000 bp |

## Where policy stands (October 2026)

Two distinct US instruments define the moment and should not be conflated. The **OSTP Framework for Nucleic Acid Synthesis Screening** (April 2024) took first effect for federally funded purchases on 26 April 2025 at a 200-nucleotide window, with a second stage — a tightened 50-nucleotide window and a functional "sequence-of-concern" (SOC) definition — scheduled for 13 October 2026. Executive Order 14292 (5 May 2025) then paused the framework and directed OSTP to revise or replace it; as of July 2026 that revision is unpublished, so the October 2026 milestone's on-schedule survival is genuinely uncertain. Separately, **S. 3741, the Biosecurity Modernization and Innovation Act of 2026** (Cotton–Klobuchar, 29 January 2026), would make provider screening a statutory, Commerce-enforced requirement and establish a biotechnology governance sandbox at NIST, but does not itself specify the 50-nt window, functional SOCs, or an on-device mandate. The "mandatory + on-device" regime this brief anticipates is a composite of the two, doubly conditional on the framework revision issuing as expected and on S. 3741 (or an equivalent) being enacted. The IGSC Harmonized Screening Protocol v3.0 (September 2024) operates voluntarily in the interim, with members — covering roughly 80% of commercial gene-synthesis capacity — due to transition to the 50-bp threshold by 24 October 2026.

**Table 1. The two US instruments — keep them distinct.**

| Instrument | What it does | Enforcement mechanism | Status (Jul 2026) |
|---|---|---|---|
| OSTP Framework (Apr 2024) | Technical spec: 50-nt window, functional SOC, six-frame translation, on-device expectations | Funding / procurement conditions | Paused (EO 14292); revision unpublished |
| S. 3741 (Jan 2026) | Mandatory provider order/customer screening; NIST governance sandbox | Commerce regulation | Referred to Senate Commerce |
| IGSC v3.0 (Sep 2024) | Voluntary member screening (~80% of capacity) | Self-regulatory | In force; 50-bp transition by 24 Oct 2026 |

## Five findings that should shape the response

**1. Supply-chain restriction is not a durable control point — under either regime.** This is the brief's highest-confidence conclusion and it survives worst-case testing. Phosphoramidites are commodity reagents from ~45–60 suppliers worldwide; the solvent has a demonstrated unregulated substitute (propylene carbonate); the DIY hardware chain adds commodity components (printheads, microcontrollers, pumps). The only genuine barriers are two narrow, method-specific items — the photolithographic digital micromirror device and the electrochemical CMOS electrode array — and even these are access barriers, not monitorable chokepoints, because their legitimate markets dwarf any synthesis use. Restricting inputs burdens overwhelmingly legitimate research while a determined actor routes around it.

**2. A US mandate reaches under a quarter of the manufacturers that matter.** Of 34 inventoried benchtop manufacturers, only 8 are US-headquartered; 12 are in allied jurisdictions and 14 are outside both, and 5 of the 9 firms founded since 2019 — including the highest-throughput array-based class — sit outside US reach. Roughly 35% predate 2010, a legacy base no manufacturer-side rule can retrofit. Device-level control therefore has a hard jurisdictional ceiling that only international harmonisation can raise.

**3. The residual DIY gap is narrow, lab-scale, and skill-gated — not a garage threat today.** On a disciplined reading of usable length at high fidelity, the only reproducible open synthesizers are OpenIDS (~$19,900, usable ~15–30 nt) and MAS 2.0 — and MAS 2.0, on a newly sourced figure, is a ~€200–300K, optics-alignment-gated build with no independent replication yet, closer to the commercial tier than to a cheap DIY device. Converting low-fidelity DIY oligos into a functional gene depends on an error-correction, verification and (beyond ~7–10 kb) host-system pipeline that remains expertise- and equipment-intensive. The near-term concern is proliferation of capable *benchtop* devices and their resale, not a homebrew synthesizer.

**4. Screening works against known threats; the open problem is functional and jurisdictional.** Tested screening tools already clear >95% sensitivity and >97% accuracy on a blinded NIST dataset (Laird et al., 2025). The demonstrated vulnerability is to AI-designed protein variants: after coordinated patching by three of four providers, ~3% of the more-probably-functional variants still escaped similarity-based detection (a ~97% flag rate; Wittmann et al., 2025). This is precisely what the October 2026 functional-SOC provision targets.

**5. Forensic attribution is a feasible backstop — now demonstrated, not just proposed.** Reprocessing four deposited datasets reproduces published per-method error signatures to within ~±20%, and a co-processed reference atlas separates four synthesis chemistries at 100% balanced accuracy under leakage-safe validation. Within-chemistry vendor attribution is hard (near-neighbour vendors ~72%, borderline), so the defensible near-term output is **exclusion** — ruling out a commercial-provider origin, which redirects an investigation from order records toward equipment.

**Table 2. Findings summary.**

| # | Finding | Core evidence | Confidence |
|---|---|---|---|
| 1 | Supply-chain restriction is not durable | ~45–60 suppliers; GRAS solvent substitute; DMD/CMOS are access barriers, not chokepoints | HIGH |
| 2 | A US mandate reaches under ¼ of manufacturers | 8/34 US-bound; 14 outside; 5 of 9 firms since 2019 outside | HIGH |
| 3 | Residual DIY gap is narrow and lab-scale | OpenIDS usable ~15–30 nt; MAS 2.0 ~€200–300K; ~7–10 kb assembly ceiling | HIGH / MED |
| 4 | Screening works vs known threats; the gap is functional | Laird 2025 >95% sens / >97% acc; Wittmann ~3% miss | HIGH |
| 5 | Forensic attribution is a feasible backstop (exclusion-first) | 100% cross-chemistry; vendor-level ~72% (borderline) | HIGH / MED |

## Recommendations by stakeholder

### For regulators (OSTP, HHS/ASPR, IGSC)

Issue the OSTP framework revision and implement the October 2026 provisions — the 50-nt window, functional SOC definitions, six-frame translation, and on-device/manufacturer expectations — rather than allowing the pause to become a lapse. Recognise explicitly that a US mandate binds under a quarter of known manufacturers, and make international harmonisation a first-order objective, not an add-on. Do not rely on supply-chain restriction as a primary lever; direct oversight to the synthesis order and the device. Resolve the classification of DIY and open-source synthesizers explicitly — define whether they fall under a device mandate or establish an alternative oversight pathway — and address low-signature electrochemical platforms in the framework before they mature (a post-2028 concern on current TRL). Invest in forensic and attribution capability as a complement to prevention, prioritising the device classes where the reference population is small enough for attribution to be informative.

### For manufacturers and providers

Integrate screening ahead of the mandate rather than at the deadline, and treat proprietary-reagent sales as a control point that already exists in enzymatic and some array systems — the licensed consumable is the most durable benchtop lever available. Publish adopted-screening status: the benchtop layer is currently unauditable from outside, and transparency is itself a low-cost trust and governance measure. Recognise that resale and export leakage — documented in this sector, including screened-by-design instruments reaching embargoed destinations via resellers — undermines point-of-sale know-your-customer, and design retention and device-registration practices accordingly.

### For researchers (IBBIS, academia)

Front-load forensics research: attribution capability has a long lead time, and the binding constraint is a single co-processed, labelled reference library spanning method classes, built from deposited and collaborator-provided data under infohazard review — with no in-house synthesis. Develop functional SOC detection, since sequence-similarity screening alone will not catch AI-designed variants. Follow responsible-disclosure practice, coordinating with providers before publication, as the coordinated "zero-day" patching of the AI-evasion vulnerability demonstrated. Physical-signature and supply-chain forensics should remain in compartmented operational-security work developed with agencies and manufacturers, not open research.

### For funders and policymakers

Fund implementation, not just requirements — including device-level screening R&D for manufacturers who need integration help, which the Institute for Progress estimates is a modest fraction of instrument cost. Support the international coordination bodies (the IBBIS Common Mechanism, IGSC, ISO 20688-2) that alone can raise the jurisdictional ceiling. Plan for the legacy and secondary-market installed base, where on-device screening cannot reach and forensic attribution is the only available control layer. Keep the two policy instruments distinct in legislative and budgetary design: S. 3741 supplies a mandate mechanism; the OSTP framework supplies the technical specification — each needs the other to constitute an effective regime.

**Table 3. Recommendations — what, who, and by when.**

| Recommendation | Who | By when |
|---|---|---|
| Issue the OSTP framework revision; implement the 50-nt window, functional SOC, on-device expectations | OSTP; HHS/ASPR | Oct 2026 milestone — before the pause becomes a lapse |
| Resolve DIY / open-source device classification (or an alternative oversight pathway) | OSTP (framework revision) | With the revision |
| Make international harmonisation a first-order objective | OSTP; State; IBBIS; allied governments | 2026–2028 |
| Integrate screening ahead of the mandate; publish adopted-screening status | Benchtop manufacturers; IGSC | 2026–2027 |
| Track proprietary-reagent sales as a control point; design for resale/legacy leakage | Manufacturers; providers | Ongoing |
| Build the co-processed forensic reference library; develop functional SOC detection | IBBIS; academia | 2026–2028 (long lead time) |
| Fund implementation and device-screening R&D; plan for the legacy/secondary-market base | Funders; Congress | FY2026–2030 |

## The durable architecture

A resilient 2026–2030 governance architecture is layered and regime-conditional. Its high-durability core (Tier 1) is mandatory on-device screening for benchtop devices, mandatory provider screening at a 50-nt window with functional SOC detection, enforced through Commerce regulation and/or funding-and-procurement conditions. Its medium-durability layer (Tier 2) is mandatory record retention, which enables attribution. Its emerging layer (Tier 3) is international coordination. Explicitly *not* recommended as a primary control (Tier 4, low durability) is supply-chain restriction on phosphoramidites, solvents, or device components — substitutable, commodity, and swamped by legitimate demand. Forensic attribution sits across these layers as the backstop for the devices and residual DIY routes the preventive levers cannot reach.

**Table 4. The layered control architecture (2026–2030).**

| Tier | Mechanism | Durability | Primary lever? |
|---|---|---|---|
| Tier 1 | On-device screening + mandatory provider screening (50-nt, functional SOC) | High (for regulated devices) | Yes |
| Tier 2 | Mandatory record retention | Medium (post-hoc attribution) | Supporting |
| Tier 3 | International coordination (IBBIS Common Mechanism, IGSC, ISO 20688-2) | Low–Medium (incomplete) | Load-bearing |
| Tier 4 | Supply-chain restriction (reagents, solvents, components) | Very low | Not recommended |

## Confidence and caveats

Two conclusions are stated at different confidence levels, honestly. It is HIGH-confidence and structural that supply-chain restriction is not a durable control point. It is MEDIUM/conditional that R1 device-level control will prove effective — this depends on the OSTP framework revision being issued and implemented substantially as projected, on S. 3741 (or an equivalent) being enacted, and on the DIY-classification question being resolved. This brief does not claim the mandatory/on-device regime already exists or that it will certainly work; it claims the regime is aimed at the right levers, and identifies where it must reach further to succeed.

## Key sources

Executive Order 14292 (2025), *Federal Register* 90 FR 19611. · OSTP (2024), *Framework for Nucleic Acid Synthesis Screening*, ASPR S3. · S. 3741, 119th Congress (Cotton, Klobuchar, 2026), congress.gov. · IGSC (2024), *Harmonized Screening Protocol v3.0*. · BIOSECURE Act, §851 of the FY2026 NDAA (P.L. 119-60, 18 Dec 2025). · Wittmann, B. J., et al. (2025), *Science* 390(6768):82–87, https://doi.org/10.1126/science.adu8578. · Laird, T. S., et al. (2025), *Applied Biosafety*, https://doi.org/10.1177/15356760251401228. · Kane, A., & Parker, M. T. (2024), *Applied Biosafety* 29(2):85–95. · Rose, S., et al. (2024), Practical Questions for Securing Nucleic Acid Synthesis, *Applied Biosafety*, https://doi.org/10.1089/apb.2023.0028. · Institute for Progress / Langenkamp (2024), *Securing Benchtop DNA Synthesizers*. · NTI | bio (2023), *Benchtop DNA Synthesis Devices*. · Kim, Kim & Bang (2024), *Scientific Reports* 14:3773. · Masaki, Onishi & Seio (2022), *Scientific Reports* 12:12095. · Lietard et al. (2021), *Nucleic Acids Research* 49(12):6687. · Gimpel et al. (2023), *Nature Communications* 14:6026. · Crook et al. (2022), *Nature Communications* 13:7374. · Helices Biological Photolithography GmbH (2026), helicesbio.com (MAS 2.0 capital/specs, developer interview, Jul 2026). *(Full citations in the companion Technical Review.)*
