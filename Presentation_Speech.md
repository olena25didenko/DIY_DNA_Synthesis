# Presentation — speaker notes / speech

## Title

Good morning. My thesis asks a single question: as DNA-synthesis screening becomes mandatory and moves onto the synthesis device itself, and as do-it-yourself and benchtop synthesis proliferate, where does control stay robust, where does it erode, and where must policy move to keep pace through 2030. I characterise the whole governance architecture as a function of the policy regime, and I back it with original forensic results. I'll walk through four workstreams: a technology-readiness index, cost trajectories, control robustness, and a forensic attribution framework.

## Why now

Three US policy instruments define this moment. The OSTP Framework for Nucleic Acid Synthesis Screening took first effect in April 2025 at a 200-nucleotide window; a second stage scheduled for October 2026 would tighten that to 50 nucleotides and add a functional sequence-of-concern definition. Executive Order 14292 then paused the Framework pending revision, so that milestone's survival is genuinely uncertain. And Senate bill S. 3741 would make screening statutory. The BIOSECURE Act became law in December 2025. So screening is being strengthened deliberately — the question is whether it reaches far enough as devices proliferate.

## Two regimes

I anchor everything in two regimes. R0 is the status quo as of October 2026 — voluntary, no device mandate. R1 is the projected regime with mandatory provider and on-device screening at a 50-nucleotide window with functional detection. Crucially, R1 is a composite projection, doubly conditional on the Framework revision being issued and on S. 3741 being enacted. The analytically interesting object is not whether screening works — it's the residual DIY gap: the synthesis capability that remains outside the perimeter once commercial providers and benchtop manufacturers are covered. Everything is scored under both regimes and weighted toward that gap.

## Four workstreams

The work has four parts. First, a regime-conditional technology-readiness index across the synthesis chemistries, weighted toward DIY. Second, cost and accessibility trajectories to 2030. Third, a control-robustness assessment — which levers stay durable and how far a US mandate actually reaches. And fourth, the forensic contribution: a method to attribute the synthesis route from error signatures in the sequenced product. The contribution overall is to move the conversation from ranking which sequences are dangerous toward designing the control architecture itself.

## Section 1

First, the readiness index — how accessible and how governable each synthesis route actually is.

## TRL landscape

I score seven routes by technology-readiness level, which here means how close a route is to a working, assembly-ready capability a non-expert could stand up. The analytical weight sits in the TRL 3–6 band. OpenIDS and MAS 2.0 are the genuine open-source DIY builds at TRL 5. DropSynth is DIY gene assembly at TRL 4. Electrochemical is TRL 3 with no independent build. Commercial systems sit at 9 but are reached only by purchase — they're a baseline, not the object of concern.

## Usable length

A methodological point that keeps the assessment honest: I score capability by usable length at high fidelity, not advertised maximum. At 98% per-step coupling a 30-mer is full-length only about 55% of the time, and OpenIDS has only ever demonstrated a short poly-dT homopolymer. Gene assembly needs upwards of 90% full-length product. So the honest usable length for these DIY routes is tens of nucleotides — well short of a defined-sequence gene. Advertised numbers overstate the threat.

## Capital cost

On capital cost: OpenIDS is about twenty thousand dollars, MAS 2.0 tens of thousands, and DropSynth just a thirty-four-hundred-dollar bead pool. The enzymatic benchtop — DNA Script's SYNTAX — is around $292,000, verified against a vendor quote. The key nuance is DropSynth: its low cost buys you assembly of a commercial oligo pool, which is already screenable. Cheapness there doesn't translate into unscreened capability.

## Expertise

When you plot the expertise required, the picture inverts the cost story. The cheap DIY routes — MAS 2.0, DropSynth, electrochemical — demand the most skill, scoring 7 to 8 out of 10 across multiple specialist domains. The easy, push-button options are the commercial ones you simply buy. So accessibility isn't really about price; it's gated by know-how.

## Section 2

Second, where these costs are heading — and where the true barrier actually sits.

## Cost trajectory

I model cost as conditional annual-decline scenarios with explicit TRL gating — not mechanical curve fits. OpenIDS, the only DIY route with a real anchor, projects from its nineteen-thousand-nine-hundred-dollar build to about twelve thousand by 2030 in the base case. But the load-bearing conclusion is that commercial cost-per-base has plateaued, so the DIY barrier is capital cost, not per-base cost — and even where OpenIDS undercuts a provider at volume, it yields raw short oligos, not a finished product.

## 2030 matrix

Across accelerate, continue, and stall scenarios, OpenIDS stays the only genuinely low-cost DIY route. Electrochemical cost is undefined at TRL 3 — I refuse to itemise parts for a system that doesn't exist. And the enzymatic benchtop stays six-figure, tracking the Institute for Progress 2030 forecast of roughly a hundred-and-twelve to two-hundred-and-ninety-eight thousand dollars.

## Assembly cost

A practitioner benchmark sharpens the whole argument. Commercial oligo pools cost about a dollar-fifty per kilobase — nearly free. Clonal, sequence-perfect DNA from the same provider is about a hundred and twenty-five. That eighty-fold markup is entirely assembly and sequence validation — which Keoni Gandall has shown can be done for about six dollars per kilobase with enough know-how. So the barrier isn't a hard cost floor; it's tacit knowledge — two years of specialisation. That reframes the residual DIY gap as expertise-gated, downstream of synthesis.

## Section 3

Third, which control levers actually hold as the regime changes.

## Durability ladder

Under R0, every lever is fragile — voluntary screening, and reagent or component restrictions that are trivially routed around. Under R1, mandatory provider and on-device screening plus functional detection and retention are substantially more durable — but only for regulated commercial devices. Open firmware makes on-device screening weak for DIY systems, and legacy and secondhand devices escape it entirely. So the durable tier is real, but it has holes exactly where the DIY gap lives.

## Sensitivity

My highest-confidence, worst-case-surviving finding is that supply-chain restriction is not a durable control point under either regime. The inputs are commodity or substitutable — propylene carbonate, a food additive, replaces the regulated solvent; phosphoramidites are made on demand from stable precursors. Control belongs at the device and the provider, not the input.

## Phosphoramidites

I make this concrete with the phosphoramidite supply chain. As a misuse-control lever the risk is low — a dozen suppliers, no purchase controls, chemically substitutable, and a billion-dollar legitimate market that swamps any signal. There is a real concentration upstream, in bulk and GMP grade, with a growing Chinese role — but that's an economic and drug-security issue, addressed by the BIOSECURE Act, not a misuse chokepoint. The one-line takeaway: control belongs at the sequence and the device, not the reagent.

## Reach

The single most consequential result is about reach, not manufacturing. Of thirty-four benchtop manufacturers inventoried, only eight are US-headquartered and directly bound by a mandate; fourteen sit outside US and allied reach; and five of the nine firms founded since 2019 are outside reach, including the highest-throughput array class. So a US mandate directly reaches under a quarter of known makers, and the frontier is drifting away from it. International harmonisation isn't optional — it's load-bearing.

## Section 4

Fourth — and this is the original scientific core — when prevention leaks, can we attribute after the fact.

## Forensic idea

Prevention is imperfect by design, so a mature architecture pairs it with post-hoc detection and attribution — Esvelt's delay, detect, defend. My contribution is the detect leg: infer the synthesis route from characteristic error signatures in the sequenced product, using reads alone. The scope is honest — this is class-level attribution, not a serial number — and following the genetic-engineering-attribution literature, exclusion is the primary value: ruling out a commercial origin redirects an investigation from subpoenaing order records toward searching for equipment.

## Four fingerprints

The premise is no longer just cited — I reprocessed four deposited datasets from raw reads and reproduced each method's published error signature to within about twenty percent. Column phosphoramidite is deletion-dominated with a G-to-A substitution bias; photolithographic is deletion-dominated with a G-to-T bias. The substitution direction is the fine discriminator. Deletion burden alone spans about eighty-fold across methods.

## Gimpel

From the Gimpel data I reproduced the electrochemical-versus-deposition distinction: the electrochemical pool shows roughly nineteen times the deletion rate of material deposition, plus a distinctive five-prime-ward gradient, while deposition is essentially error-free. That's exactly the kind of order-of-magnitude, class-level signature my classifier relies on.

## Measured attribution

And I built the binding-constraint artifact: a single co-processed reference atlas — all four datasets through one pipeline, sixty-five runs. On it, cross-chemistry attribution is essentially perfect: a hundred percent balanced accuracy, permutation p around point-oh-one. Within-chemistry vendor attribution, by contrast, is hard: under leakage-safe validation the four-vendor task isn't supported and near-neighbour vendors reach only about seventy-two percent. That's an honest, rigor-improving result — it corrected an earlier number that had been inflated by replicate leakage.

## OpenIDS prediction

Finally, a concrete, mechanistically-anchored prediction. OpenIDS uses standard column chemistry but omits the capping step. I reproduced that the G-to-A signature is capping-driven — a twelve-point-two-fold shift. So OpenIDS product should show a suppressed G-to-A signature and elevated single-base internal deletions — a distinguishable DIY-versus-commercial phenotype. It's a hypothesis, not yet a measurement, because Kim deposited no sequencing data; testing it needs collaborator OpenIDS reads, infohazard-reviewed through IBBIS. That's the single highest-value next step.

## Implications

Pulling it together: the durable levers, conditional on R1, are on-device screening, mandatory provider compliance, functional detection, international coordination, and forensic attribution as the backstop. The illusory ones are supply-chain restrictions of every kind. And the live frontier problem is function-based screening: the Paraphrase Project showed that even after coordinated patching, about three percent of AI-designed functional protein variants still escape similarity-based screening — which is exactly what the October 2026 functional-sequence-of-concern provision is meant to close.

## Conclusion

So, to conclude. Screening is being strengthened for good reason, but a single point-of-sale control is insufficient. My work maps which levers hold, shows that supply-chain restriction is not one of them, quantifies how far a US mandate reaches — under a quarter of makers — and delivers a forensic backstop that is now demonstrated, not just proposed: four reproduced chemistries and a real, one-hundred-percent cross-chemistry classifier. The problem shifts from preventing DIY synthesis to governing a proliferating-device world with a layered, mandatory, regime-conditional architecture — backstopped by attribution for the devices and residual routes it cannot reach. Thank you.
