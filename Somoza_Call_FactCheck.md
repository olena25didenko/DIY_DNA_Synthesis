# Fact-check of the Mark Somoza call — claims, verdicts, and links

*Every substantive claim from the 28 Jul 2026 call, checked against published sources. Verdicts: ✅ Verified · 🟢 Consistent with literature · 🟡 Plausible, not independently verifiable · ⚪ Private/unverifiable.*

## Papers he mentioned

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | The open-source **MAS 2.0** device exists and is published (CAD, protocols, software) | ✅ | Holz, Somoza et al., *"An open-source advanced maskless synthesizer for light-directed chemical synthesis of large nucleic acid libraries and microarrays,"* **ChemRxiv, 21 Feb 2024**, DOI [10.26434/chemrxiv-2024-j4c90](https://doi.org/10.26434/chemrxiv-2024-j4c90) · [article page](https://chemrxiv.org/engage/chemrxiv/article-details/65ba15e39138d231611ab534) |
| 2 | The published error-rate work is in **Nucleic Acids Research** ("the only thing we have") | ✅ | Lietard et al. (2021), *"Chemical and photochemical error rates in light-directed synthesis of complex DNA libraries,"* **NAR 49(12):6687**, [10.1093/nar/gkab505](https://academic.oup.com/nar/article/49/12/6687/6307908) — the paper already in your Ch.1/Ch.4 refs. Foundational error study: Agbavwe et al. (2011), *J. Nanobiotechnol.* 9:57, [10.1186/1477-3155-9-57](https://jnanobiotechnology.biomedcentral.com/articles/10.1186/1477-3155-9-57) |
| 3 | **Lloyd Smith (Wisconsin)**, "RNA-mediated gene assembly from microarrays" — postdoc-era, converted DNA→RNA, expressed a gene | ✅ Exactly right | Wu, Lockett & Smith (2012), *"RNA-Mediated Gene Assembly from DNA Arrays,"* **Angew. Chem. Int. Ed.** — assembled the ZsGreen1 GFP gene. [PubMed 22473711](https://pubmed.ncbi.nlm.nih.gov/22473711/) · [PMC3422211](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3422211/) |

## The company

| # | Claim | Verdict | Detail |
|---|---|---|---|
| 4 | They sell the device commercially through a company (heard as "Helicis Bio") | ✅ name resolved | The company is **Helices Biological Photolithography** (Vienna) — co-founded by Somoza, manufactures photolithographic nucleic-acid-synthesis equipment. I could **not** locate an official website/URL in public search — worth asking Mark directly for the site, or checking the affiliations/conflict-of-interest note in the ChemRxiv paper (which typically names the spin-out). |

## Technical claims

| # | Claim | Verdict | Basis |
|---|---|---|---|
| 5 | Error rate **~5% deletion per nucleotide**, highest of the high-throughput methods | 🟢 | Consistent: Lietard 2021 reports deletion-dominated errors ~4.65% for a 67-mer library; Agbavwe 2011 similar. Optimized MAS chemistry can reach 0.3–0.6%/bp, but ~5% is the honest *un-optimized / library-grade* figure — matches what you already have in Ch.1 ("library-grade, error-prone"). |
| 6 | Yield falls exponentially with length; make short (~30-mers) at ~5% correct yield, filter, then concatenate/assemble to gene length | 🟢 | Standard stepwise-yield arithmetic; consistent with the field. Supports your "not gene-assembly-ready" scoring. |
| 7 | **Lower depurination** because they use **no acidic deblock** (light-based deprotection instead of acid) | ✅ | Chemically correct and literature-supported: photolithographic MAS removes the 5′ group by **NPPOC photocleavage**, avoiding the acidic detritylation (TCA/DCA) that drives depurination in standard column chemistry. Sources note MAS "does not use acidic conditions… which helps reduce depurination." This is a genuine **forensic discriminator** for your Ch.4. |
| 8 | Likely **photo-induced (UV) damage** as a signature; low rate, still characterising via mass spec | 🟡 | Mechanistically plausible (light-directed synthesis can cause photodamage) but not yet published as a fingerprint — his own ongoing work. Good to cite as "developer's hypothesis," not established fact. |
| 9 | Forensics: manufacturers have distinct error rates; buy pools, sequence + mass-spec for base damage (guanine oxidation, depurination) | 🟢 | Sound and directly aligned with your Chapter 4 error-signature approach — he independently endorsed your method. |
| 10 | **Twist only makes DNA** — not large-scale modified/RNA pools; you'd have to negotiate specially and they likely won't | 🟢 | Accurate: Twist's oligo pools are DNA; they don't offer large modified-RNA library pools as a catalog product. |
| 11 | Value prop = **flexibility**: large-scale RNA + non-natural modifications (2′-F, 2′-OMe, phosphorothioate, 5-methyl-C, 5-hydroxymethyl-C, abasic, dU), not available commercially | 🟢 | Accurate. These are standard therapeutic-oligo/guide-RNA modifications, and large-scale *modified* array/pool synthesis is exactly the MAS niche (Somoza lab has extensive RNA-microarray work, e.g. *Sci. Adv.* 2024 [10.1126/sciadv.ado6762](https://www.science.org/doi/10.1126/sciadv.ado6762)). |

## Customers & commercial details

| # | Claim | Verdict | Detail |
|---|---|---|---|
| 12 | A **Ghent University** group uses it for spatial transcriptomics (error-tolerant barcodes) | 🟡 | Plausible and consistent with MAS 2.0 being used for spatial-transcriptomics barcodes, but I found **no public paper** tying a Ghent group to the device. (Note: the well-known Nat. Biotech. 2026 spatial-reconstruction paper is from the **Broad Institute**, not Ghent — don't conflate them.) Treat as an unverified private-customer account. |
| 13 | **GSK** bought one for therapeutic-RNA modification work | ⚪ | Private commercial sale — no public record; can't be verified. Fine as an anecdote, not citable. |
| 14 | Nobody has independently built the open-source device yet; a **Korean group** may attempt it | ⚪ | His own account; plausible given the Feb-2024 release. Not independently verifiable. |
| 15 | **Cost: optics ~€150K + system/synthesizer ~€20K → realistic end-to-end ~€200–300K** | ⚪ direct account | Not independently verifiable, but the ChemRxiv paper includes a costed component list you can cross-check. **This is the load-bearing correction** — see below. |

## The one number that changes your thesis

Your Chapter 1 lists MAS 2.0 capital at **~$30K ("tens of $K, est")**. The developer says **optics alone ≈ €150K** and a realistic **end-to-end build ≈ €200–300K** — roughly a **10× correction**, and now a *sourced* figure (developer interview + the paper's component list) rather than an estimate. It moves MAS 2.0 out of the cheap-DIY tier toward the enzymatic-benchtop capital range, and strengthens your "photolithographic is a lab, not a garage, capability" point. Update: Ch.1 §2.2 + §8 table, the cost chapter, and the IBBIS summary.

## Confirmed from the company website (helicesbio.com)

**Company:** Helices Biological Photolithography GmbH — UZA II, Josef-Holaubek-Platz 2, 1090 Vienna, Austria · contact **helices.bio@gmail.com** · [helicesbio.com](https://helicesbio.com/). So "Helicis Bio" from the call = **Helices**. ✅ fully resolved.

**Founders (note the third one):** Erika Schaudy (CEO), **Mark Somoza**, and **Jory Lietard**. ⚠️ Jory Lietard is the lead author of **Lietard et al. 2021 (NAR)** — the photolithographic error-signature paper you reproduce in Chapter 4. Worth a one-line disclosure footnote when you cite it: the reference characterising the photolithographic error signature is co-authored by a co-founder of the company selling the instrument. Not a problem, just scholarly transparency.

**MAS 2.0 specs (citable):**
- Texas Instruments **DMD** (confirms the "TI DMD" point in your supply-chain matrix — it's on the vendor's own page).
- Capacity: **786,432** unique sequences (XGA DMD) or **2,073,600** (1080p DMD) — good throughput figures for your Ch.1 table.
- **365 nm UV LED** source; fully **open-source** hardware + software.
- Coupling ~**15 s**; photodeprotection **60 s (NPPOC) / 30 s (Bz-NPPOC) / 6 s (SPh-NPPOC)** — three generations of photolabile groups.
- **Reverse 5′→3′ synthesis** available (3′-photolabile amidites) — the mechanism behind the "spatial transcriptomics" customer use he described. ✅
- Explicitly confirms the modification range he claimed: **RNA, 2′-O-methyl, 2′-fluoro RNA, 2′-fluoro-arabino (FANA), phosphorothioate, epigenetic/epitranscriptomic** modifications. ✅
- **"No acidic deblock" confirmed in writing:** the site states the photolabile group "directly replaces the acid-labile dimethoxytrityl (DMTr)" — i.e. light replaces acid, supporting his lower-depurination forensic point. ✅

**Two refinements for your other docs:**
- *Supply-chain matrix (photolabile amidites):* the site says "**several suppliers** provide" NPPOC/Bz-NPPOC/SPh-NPPOC amidites — so soften "few specialty suppliers" to "specialty but multi-sourced, three generations." The DMD (TI) remains the tighter point.
- No price is listed on the site, and the spec brochure is an image-only PDF — so the **€150K optics / €200–300K end-to-end** figure still rests on his verbal account plus the ChemRxiv component list.

## Bottom line

Nothing he said was wrong. The two concrete papers (MAS 2.0 ChemRxiv; Lloyd Smith RNA-mediated gene assembly) are exactly as described, the chemistry (no-acid-deblock → lower depurination) is correct and useful for your forensics chapter, and the company is real (**Helices Biological Photolithography**). The only items you can't cite are the private-customer anecdotes (Ghent, GSK) and the build cost — and the cost is the one worth acting on because it corrects a number already in your draft.

---
### Sources
- MAS 2.0 (ChemRxiv 2024): https://chemrxiv.org/engage/chemrxiv/article-details/65ba15e39138d231611ab534
- Lietard et al. 2021, NAR: https://academic.oup.com/nar/article/49/12/6687/6307908
- Agbavwe et al. 2011, J. Nanobiotechnol.: https://jnanobiotechnology.biomedcentral.com/articles/10.1186/1477-3155-9-57
- Wu, Lockett & Smith 2012 (RNA-mediated gene assembly): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3422211/ · https://pubmed.ncbi.nlm.nih.gov/22473711/
- Somoza lab, University of Vienna: https://www.researchgate.net/lab/Mark-Manuel-Somoza-Lab-2
- Somoza RNA-microarray chemistry (Sci. Adv. 2024): https://www.science.org/doi/10.1126/sciadv.ado6762
- Broad Institute spatial-transcriptomics paper (NOT Ghent — for disambiguation): https://pubmed.ncbi.nlm.nih.gov/40181168/
- Helices Biological Photolithography GmbH (company website): https://helicesbio.com/
