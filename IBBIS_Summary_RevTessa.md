# DNA Synthesis Screening Under Device Proliferation

**Can open synthesis routes produce and assemble sequences of concern? A measured characterisation of seven routes**

Open protocols and open-hardware designs for DNA synthesis are publicly available, and a builder who follows them places no order with a provider. Nothing about that synthesis passes through the channel where sequence screening happens. The concern is therefore concrete: a DIY or benchtop route is a potential path to producing oligonucleotides and assembling them into sequences of concern (SOCs) outside the screening perimeter entirely.

Whether that concern is warranted turns on facts that can be measured rather than assumed: how long and how accurate the oligos actually are, what a build costs and what expertise and laboratory infrastructure it demands, and whether the resulting product can be attributed after synthesis.

**Why now.** The OSTP Framework for Nucleic Acid Synthesis Screening (April 2024) took first effect on 26 April 2025, requiring recipients of federal life-sciences funding to procure synthetic nucleic acids, and benchtop synthesis devices, only from providers and manufacturers that screen, initially at a ≥200 nt window (OSTP, 2024). A second stage scheduled for 13 October 2026 would tighten that window to 50 nt and add a functional "sequence of concern" (SOC) definition. Executive Order 14292 (May 2025) then directed OSTP to revise or replace the Framework, and that revision is unpublished (Executive Order 14292, 2025). The IGSC protocol operates voluntarily and there's no on-device mandate (IGSC, 2024).

**The screening perimeter and what lies outside it.** Two scenarios frame the analysis. In the current situation (no on-device screening mandate, IGSC protocol voluntary), the only control point that touches an order is the provider's own screening, and only if the provider participates and the order is placed with them. In the projected scenario (mandatory provider and on-device benchtop screening at a 50-nt window with functional detection), most of what the current arrangement leaves open would be closed. That second scenario is doubly conditional: the OSTP framework revision must issue substantially as scheduled, and S. 3741 (Cotton-Klobuchar, January 2026) or equivalent legislation must be enacted. As of October 2026, neither has occurred.

Every finding below is weighted toward the residual gap: the synthesis capability that sits outside the perimeter even after commercial providers and benchtop manufacturers are screened. The tables separate commercial and purchasable approaches (what a device mandate can reach) from DIY and open-source approaches (what remains outside regardless).

### Summary table 1 — Commercial and purchasable synthesis routes

| Approach | TRL | Capital | Usable length @ fidelity | Per-unit cost | Evasion (no on-device screening → on-device screening) | Screening reach & governance note |
|---|---|---|---|---|---|---|
| Commercial phosphoramidite benchtop (column) | 9 | ~$60K (~$15–150K; used ~$15–30K) | ~100–150+ nt | ~$0.30/bp | Medium → Low | On-device screening applies under projected mandatory regime; provider screening covers purchased sequences. Standard capped column (G→A). Active resale market means used units escape on-device controls |
| Enzymatic benchtop (SYNTAX) | 5 | ~$270–303K | 80–120 nt | €0.11–0.26/base | Medium → Low | On-device screening applies under projected mandatory regime. Deletion/insertion-dominated error profile, sub <0.1% (aqueous). Closed proprietary cartridge = first-sale control point; aftermarket circumvents it |
| Commercial provider (mail-order) | 9 | none | genes/genomes (benchmark) | $0.07–0.10/bp | Medium → Low | The screened channel under both scenarios: voluntary now, mandatory in the projected regime. IGSC members self-report ~80% of global commercial synthesis capacity by volume (a claim from the consortium's 2009 founding; refers to centralized service providers; compliance within membership unverified). Estimated screening compliance across all providers: 40–60% (GHSC estimate; no reliable public dataset; IBBIS Global Synthesis Map identifies 700+ synthesis companies across 81 countries, most unverified screeners). SecureDNA provides an additional screening layer |
| DropSynth (emulsion assembly) | 4 | ~$3.4K bead pool (~200 rxns) | ~1–3 kb assembled; ~25% perfect | ~$1–2/gene | Medium → Low | Inherits provider screening through its commercial oligo-pool input; the assembly step is untracked. Screening depends on the input oligos being ordered through a participating provider |

*Evasion is scored as the change from no on-device screening mandate to projected mandatory on-device screening (higher = more able to evade). Costs and lengths are the corrected values used across Chapters 1–4.*

### Summary table 2 — DIY and open-source synthesis routes (outside the device mandate perimeter)

These routes sit outside any device mandate under either scenario. Provider screening applies only where purchased reagents or oligos pass through a participating provider; the synthesis step itself is untracked.

| Approach | TRL | Capital | Usable length @ fidelity | Per-unit cost | What screening can reach | Forensic signature & governance note |
|---|---|---|---|---|---|---|
| OpenIDS / OpenIDS2 (inkjet) | 5 | ~$19.9K (v1); cheaper 2025 v2 | ~15–30 nt | ~$1–5/seq | Provider screening on any purchased reagents or oligos only | Column phosphoramidite; capping omitted → predicted suppressed G→A + elevated n−1. Core residual DIY route; not gene-assembly-ready |
| MAS 2.0 / AMS (photolithographic) | 5 | ~€150–170K instrument (~€200–300K loaded; optics ~€150K); sourced from developer interview, 2026 | library-grade (error-prone) | n/a | Provider screening on reagent/oligo purchases; specialty photolabile amidites and single-source DMD (Texas Instruments, sold openly) are partial supply signatures | Photolithographic G→T + array spatial gradient (Lietard class). Open build; optics + photolabile-amidite barrier; no independent build outside originating lab |
| Electrochemical | 3 | undefined (~$10–12K est) | 13–17 nt (demo only) | ~$1–5 est | No device mandate; custom CMOS array not monitorable | High deletion + 5′ gradient (18.8× deposition, measured). Conditional-future; no independent build exists |
| Enzymatic (Church DIY route) | ~3 | low | data-storage only (not defined-sequence) | n/a | Off-the-shelf reagents (TdT, dNTPs, apyrase); not monitorable | Produces stochastic homopolymers, not defined sequences; not gene-capable |

*DIY routes sit outside any device mandate under either scenario. Whether open-source synthesizers fall within the scope of a mandate is unresolved and would need to be addressed explicitly in any framework revision.*

**The reproducible open synthesizers produce short, low-fidelity oligonucleotides**

Two open synthesizers are reproducible, and both are academic instruments with limited output. OpenIDS, an open-source inkjet system costing approximately $19,900, produces usable oligonucleotides of roughly 15 to 30 nucleotides (Kim, Kim & Bang, 2024). At 98% per-step coupling efficiency a 30-mer is full-length only about 55% of the time, and the second-generation build measured approximately 56% full-length for a 15-mer (Kim, Kim & Bang, 2025).

MAS 2.0, the open photolithographic platform (Somoza et al., 2024), proved on investigation to be considerably more expensive than earlier estimates suggested. A 2026 interview with its developer put the instrument at €150,000 to €170,000, rising to between €200,000 and €300,000 for a complete working installation, with the optics alone accounting for around €150,000 (Helices Biological Photolithography, 2026). Optical alignment is the practical barrier to building one, no independent build exists outside the originating laboratory, and the output is library-grade, meaning it's usable in aggregate but not accurate at the level of individual strands.

None of the remaining routes alters this picture. Electrochemical synthesis rests on a single data-storage proof-of-concept at technology readiness level 3, with no independent build and no commercial instance among the 34 manufacturers inventoried (Xu et al., 2021). Enzymatic synthesis is available in DIY form only for data storage, where it produces stochastic homopolymers (Lee et al., 2019); the defined-sequence route depends on an engineered enzyme and bespoke nucleotides that are proprietary and take years to develop (Palluk et al., 2018). DropSynth does offer inexpensive gene assembly at around $3,400 for the bead pool, but it consumes a commercial microarray oligonucleotide pool and therefore inherits the screening perimeter through its own input (Sidore et al., 2020; Plesa et al., 2018). A 2026 survey identified no working homebrew synthesizer beyond these academic platforms.

**Fidelity, and the pipeline that follows synthesis, is the binding constraint**

Assembling short oligonucleotides into genes is a standard method: the 901 base pair GFP gene has been assembled from 16-mers (US Patent 12,018,316). The constraint lies in fidelity. Standard practice for gene assembly targets above 90% full-length building blocks, and below roughly 70% a redesign or a different synthesis route is indicated, so DIY output at around 56% falls well short of what assembly requires.

The effect compounds through assembly (Kosuri & Church, 2014). Even with good-quality oligonucleotides, polymerase cycling assembly of a 1 kilobase fragment yielded only about 4% correct product before error correction (Int. J. Mol. Sci., 2024, 25:11514). Recovering a correct functional gene from DIY-grade material therefore requires mismatch cleavage, clonal selection and sequence verification, none of which forms part of the synthesizer. Above approximately 7,000 to 10,000 base pairs, reliable assembly requires bacterial or yeast host systems, and many viral sequences are toxic to those hosts (NTI, 2023). These considerations are the reason the analysis is scoped to the synthesis step and treats assembly and pathogen rescue as lying outside it.

**Commercial benchtop devices, and their jurisdictional distribution, present the larger exposure**

If the garage doesn't present the main concern, the mature commercial layer does. Commercial column benchtop instruments reach 100 to 150 nucleotides and beyond at high fidelity, which makes their output directly usable for assembly, and they sell for around $60,000 new and between $15,000 and $30,000 second-hand (Institute for Progress / Langenkamp, 2024).

The most consequential finding in the project concerns jurisdictional reach. Of the 34 benchtop manufacturers inventoried within the ERA/IBBIS group, 8 are headquartered in the United States and directly bound by a US mandate, 12 sit in allied jurisdictions where they can be reached only through harmonisation, and 14 fall outside both categories (ERA/IBBIS manufacturer inventory; Alexanian, 2026). Five of the nine firms founded since 2019 lie outside US jurisdiction, and they include the highest-throughput, array-based class. About 35% of the inventory predates 2010, a legacy installed base that can't be retrofitted with know-your-customer checks or secure boot.

A secondary market compounds the problem. Working instruments are listed openly with no buyer verification and, in the cases observed, with cross-border shipping. A Codex DNA and Telesis Bio 10-Q disclosure documents BioXp units reaching embargoed destinations through resellers. An instrument sold second-hand carries none of the controls attached to its original sale, and its screening state cannot be verified by the next buyer.

A US mandate consequently reaches fewer than a quarter of known manufacturers, while the newest and most capable capacity concentrates where it does not. International harmonisation therefore carries substantial weight in any workable architecture. A further finding compounds this: adopted-screening status couldn't be verified from public sources for any of the 34 firms, which leaves the benchtop layer effectively unauditable from outside.

**Controls on inputs cannot close the gap**

Across all routes assessed, covering DIY and benchtop synthesis and both chemical and enzymatic approaches, almost no input functions as a durable control point. Of 34 inputs assessed, the large majority are commodity items available from many suppliers, substitutable, and subject to legitimate demand that overwhelms any synthesis-specific signal. Phosphoramidites are supplied by some 45 to 60 firms worldwide (Grand View Research; Mordor Intelligence) and can be produced on demand from more stable precursors (Sandahl et al., 2021). Acetonitrile can be replaced in DIY synthesis by propylene carbonate, an unregulated food additive (Kim, Kim & Bang, 2024).

Only one input is genuinely difficult to obtain: the custom CMOS electrode array an electrochemical system would need, which is not an off-the-shelf part but a chip that must be designed and fabricated at a semiconductor foundry. The digital micromirror device used in photolithographic synthesis is made by a single manufacturer, Texas Instruments, but it's sold openly (GMInsights, 2024); the practical barrier for a photolithographic build is the optics and alignment around it, not the chip. Neither can serve as a monitoring point, because their markets in semiconductors and projectors make any attempt to track sales impractical.

The few real control points sit on the ordering and benchtop side, and they work in different ways. The commercial oligonucleotide pool that DropSynth consumes is a screening handle rather than a scarce input: it's easy to order, but because it comes from a provider it passes through that provider's sequence screening (Sidore et al., 2020). Among the closed enzymatic benchtops, DNA Script SYNTAX and Ansa both use proprietary reagent cartridges; the majority of the installed benchtop base uses commodity phosphoramidites from the global suppliers noted above. The proprietary cartridge and the device manufacturer are first-sale control points, and the aftermarket circumvents both. Restriction of the supply chain therefore doesn't provide a durable control point under either scenario, and this is the project's highest-confidence conclusion, one that survives worst-case testing.

**Screening performs well against known sequences of concern, and less well against designed variants**

Screening tools perform well against the sequences they're designed to catch. An inter-tool analysis against a blinded NIST dataset found sensitivity above 95% and accuracy above 97%, with most tools already screening to 50 nucleotides (Laird et al., 2025).

The demonstrated vulnerability is of a different kind. Protein variants designed with generative models can retain predicted function while diverging enough in sequence to evade similarity-based screening. Following coordinated disclosure and patching by three of the four providers involved, about 3% of the more-probably-functional variants continued to escape detection, a flag rate of roughly 97% (Wittmann et al., 2025). This is the gap that the functional sequence-of-concern provision scheduled for October 2026 is intended to address, and it's why functional detection, as distinct from sequence similarity alone, is the frontier problem.

**Synthesis route can be inferred from the product after the event**

Since prevention is imperfect by design, the project developed a capability for identifying synthesis route retrospectively, inferring it from characteristic error signatures in the sequence of the product, using reads alone and without any cooperation from the device that made it.

The framework has since been tested against real data. When the deposited reads for four chemistries were reprocessed independently through the project pipeline, the per-method error rates recovered matched the originally published rates to within about 20%, which is close agreement for an independent reanalysis with a different pipeline rather than a synthesis error rate. Column phosphoramidite synthesis shows a capping-driven G→A bias, which reproduced at 12.2 fold against the paper's approximate 13 fold and proved independent of the polymerase used (Masaki, Onishi & Seio, 2022). Photolithographic synthesis shows a G→T bias together with a spatial gradient across the array (Lietard et al., 2021). Electrochemical synthesis shows a deletion rate 18.8 times that of material deposition (Gimpel et al., 2023). On a single co-processed reference atlas of 65 runs, the four chemistries separate at 100% balanced accuracy under leakage-safe, leave-one-run-out validation.

Attribution within a chemistry, to a particular vendor, is much harder (Filges, Mouhanna & Ståhlberg, 2021). Under leave-one-lot-out validation, vendors whose profiles sit close together reach only around 72%. The defensible output is therefore exclusion: ruling out a commercial-provider origin from an anomalous error profile, which redirects an investigation away from subpoenaing order records and towards searching for equipment. This mirrors the genetic-engineering-attribution literature, where exclusion has been the most successful output (Nielsen & Voigt, 2018; Alley et al., 2020; Crook et al., 2022). One specific discriminator between DIY and commercial synthesis has been identified: OpenIDS omits the capping step (Kim, Kim & Bang, 2024), so its product should show suppressed G→A substitution together with elevated n−1 deletions, anchored mechanistically in the reproduced capping result (Masaki, Onishi & Seio, 2022). That prediction awaits product data from a collaborator, subject to IBBIS infohazard review. No synthesis is performed in-house.

**Overall assessment**

The DIY frontier is narrower than surrounding discussion tends to assume. The two reproducible open-source synthesizers are both laboratory instruments that require substantial expertise, and both produce short or library-grade oligonucleotides that aren't ready for assembly. The binding constraint sits downstream, in error correction, verification and host systems, not in the synthesis step itself. There's no evidence of a home-buildable synthesizer that works outside a lab.

The exposure of greater consequence lies in the mature commercial benchtop layer, whose output is assembly-ready, proliferating, largely unscreened and actively resold, together with the jurisdictional position in which a US mandate reaches only 8 of 34 manufacturers. That exposure can't be closed at the input. Reagents and components are commodity and substitutable, and the few harder-to-source items (the custom electrode array and the single-source but openly sold micromirror device) aren't monitorable in any case, because their real markets lie in semiconductors and projectors.

It follows that a single control at the point of sale isn't enough, and the architecture has to be layered. Provider and on-device screening can be mandated by regulation. International harmonisation then determines how much of the world that screening actually covers. Post-hoc attribution, now demonstrated on real data, is the layer that acts after synthesis rather than before it, so it's the one that reaches the places prevention cannot: legacy devices, the resale market, and the residual DIY routes.

---

## References

**Peer-reviewed literature**

Alley, E. C., et al. (2020). A machine learning toolkit for genetic engineering attribution to facilitate biosecurity. *Nature Communications*, 11, 6293. https://doi.org/10.1038/s41467-020-19612-0

Crook, O. M., et al. (2022). Analysis of the first Genetic Engineering Attribution Challenge. *Nature Communications*, 13, 7374. https://doi.org/10.1038/s41467-022-35032-8

Filges, S., Mouhanna, P., & Ståhlberg, A. (2021). Digital quantification of chemical oligonucleotide synthesis errors. *Clinical Chemistry*, 67(10), 1384–1394.

Gimpel, A. L., Stark, W. J., Heckel, R., & Grass, R. N. (2023). A digital twin for DNA data storage based on comprehensive quantification of errors and biases. *Nature Communications*, 14, 6026. https://doi.org/10.1038/s41467-023-41729-1

Kim, J., Kim, H., & Bang, D. (2024). An open-source, 3D printed inkjet DNA synthesizer. *Scientific Reports*, 14, 3773. https://doi.org/10.1038/s41598-024-53944-x

Kim, J., Kim, H., & Bang, D. (2025). OpenIDS2: a low-cost, 3D-printed, open-source platform for reproducible construction of DNA microarray synthesizers. *PLOS ONE*, 20, e0338478. https://doi.org/10.1371/journal.pone.0338478

Kosuri, S., & Church, G. M. (2014). Large-scale de novo DNA synthesis: technologies and applications. *Nature Methods*, 11(5), 499–507. https://doi.org/10.1038/nmeth.2918

Laird, T. S., et al. (2025). Inter-tool analysis of a NIST dataset for assessing baseline nucleic acid sequence screening. *Applied Biosafety*. https://doi.org/10.1177/15356760251401228

Lee, H. H., Kalhor, R., Goela, N., Bolot, J., & Church, G. M. (2019). Terminator-free template-independent enzymatic DNA synthesis for digital information storage. *Nature Communications*, 10, 2383. https://doi.org/10.1038/s41467-019-10258-1

Lietard, J., et al. (2021). Chemical and photochemical error rates in light-directed synthesis of complex DNA libraries. *Nucleic Acids Research*, 49(12), 6687–6701. https://doi.org/10.1093/nar/gkab505

Masaki, Y., Onishi, Y., & Seio, K. (2022). Quantification of synthetic errors during chemical synthesis of DNA and its suppression by non-canonical nucleosides. *Scientific Reports*, 12, 12095. https://doi.org/10.1038/s41598-022-16222-2

Nielsen, A. A. K., & Voigt, C. A. (2018). Deep learning to predict the lab-of-origin of engineered DNA. *Nature Communications*, 9, 3135. https://doi.org/10.1038/s41467-018-05378-z

Palluk, S., Arlow, D. H., de Rond, T., et al. (2018). De novo DNA synthesis using polymerase–nucleotide conjugates. *Nature Biotechnology*, 36(7), 645–650. https://doi.org/10.1038/nbt.4173

Plesa, C., Sidore, A. M., Lubock, N. B., Zhang, D., & Kosuri, S. (2018). Multiplexed gene synthesis in emulsions for exploring protein functional landscapes. *Science*, 359(6373), 343–347. https://doi.org/10.1126/science.aao5167

Rose, S., Alexanian, T., Langenkamp, M., Cozzarini, H., & Diggans, J. (2024). Practical Questions for Securing Nucleic Acid Synthesis. *Applied Biosafety*. https://doi.org/10.1089/apb.2023.0028

Sandahl, A. F., Nguyen, T. J. D., Hansen, R. A., Johansen, M. B., Skrydstrup, T., & Gothelf, K. V. (2021). On-demand synthesis of phosphoramidites. *Nature Communications*, 12, 2760. https://doi.org/10.1038/s41467-021-22945-z

Sidore, A. M., Plesa, C., Samson, J. A., Lubock, N. B., & Kosuri, S. (2020). DropSynth 2.0: high-fidelity multiplexed gene synthesis in emulsions. *Nucleic Acids Research*, 48(16), e95. https://doi.org/10.1093/nar/gkaa600

Somoza, M. M., et al. (2024). An open-source advanced maskless synthesizer for light-directed chemical synthesis of large nucleic acid libraries and microarrays. *ChemRxiv*. https://doi.org/10.26434/chemrxiv-2024-j4c90

Optimization of PCA Error Correction Conditions to Improve Efficiency of Virus Genome De Novo Synthesis (2024). *International Journal of Molecular Sciences*, 25(21), 11514. https://doi.org/10.3390/ijms252111514

Wittmann, B. J., et al. (2025). Strengthening nucleic acid biosecurity screening against generative protein design tools. *Science*, 390(6768), 82–87. https://doi.org/10.1126/science.adu8578

**Policy, legal and institutional**

Executive Order 14292 (2025). Improving the Safety and Security of Biological Research. *Federal Register*, 90 FR 19611 (May 8, 2025).

Institute for Progress / Langenkamp, M. (2024). Securing Benchtop DNA Synthesizers. https://ifp.org/securing-benchtop-dna-synthesizers/

International Gene Synthesis Consortium (2024). Harmonized Screening Protocol v3.0. https://genesynthesisconsortium.org/

Nuclear Threat Initiative | bio (2023). Benchtop DNA Synthesis Devices: Capabilities, Biosecurity Implications, and Governance.

Office of Science and Technology Policy (2024). Framework for Nucleic Acid Synthesis Screening. ASPR S3. https://aspr.hhs.gov/S3/

Telesis Bio Inc. (formerly Codex DNA, Inc.). Form 10-Q, U.S. Securities and Exchange Commission (EDGAR CIK 1850079) — export-compliance / BioXp reseller disclosure.

US Patent 12,018,316. Methods for assembling nucleic acids — assembly of a 901 bp GFP gene from 16-mers (Example 2).

**Industry, company and market sources**

Grand View Research; Mordor Intelligence. Phosphoramidite market (supplier count and market size).

GMInsights (2024). Digital Micromirror Device Market — Texas Instruments as the sole commercial DMD manufacturer.

Helices Biological Photolithography GmbH (2026). MAS 2.0. https://helicesbio.com/ (instrument cost and specifications; developer interview, July 2026).

IBBIS Global DNA Synthesis Map (2025). https://globalsynthesismap.bio/ (700+ synthesis companies across 81 countries; launched December 2025).

ERA/IBBIS benchtop-manufacturer inventory (Alexanian, 2026) — 34-firm jurisdictional census (internal working-group source).
