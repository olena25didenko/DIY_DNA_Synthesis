# DropSynth developer interview — Calin Plesa (transcript and findings)

**Interviewee:** Calin Plesa (identity inferred from context; DropSynth co-inventor, University of Oregon; author on Plesa et al. 2018 Science and Sidore et al. 2020 NAR). Confirm before citing by name.
**Interviewer:** Olena Didenko (ERA/IBBIS fellowship).
**Date:** 2026 (audio: "Calin.m4a"). **Topic:** DropSynth input requirements, oligo quality, cost, expertise, and biosecurity relevance.
**Standing constraint:** detection/characterisation only; no synthesis performed or guided.

---

## Key findings

**Input-oligo quality is the binding constraint.** DropSynth only stitches oligos together, so input errors propagate through. Error rate is roughly constant with length, but percent-perfect compounds down: 50% perfect oligos give ~25% at two oligos, ~12% at three, and so on (X^N). The effective length cap is set by what you need downstream and by how deep you can sequence to recover perfects, not by a hard chemistry wall.

**Three high-fidelity vendors only:** Dynegene (China), Twist (USA), Agilent (USA), all inkjet phosphoramidite, reaching ≥230 nt at ≤1-in-500 error. Electrode-protection (electrochemical) and photolithographic array oligos are much more error-prone; photolithography is nearly abandoned commercially (LC Sciences in Texas; a Michigan successor to Roche NimbleGen; "nobody really uses it anymore").

**A ~70 nt process floor.** Standard DropSynth consumes ~70 nt of every input oligo for barcodes and assembly overlaps before any payload. A 150-mer leaves ~80 nt of payload. Sub-70-nt DIY oligos (OpenIDS 15–30 nt, electrochemical 13–17 nt) cannot feed the process at all, independent of error rate.

**No non-commercial oligo source works.** Plesa is aware of no one who has run DropSynth on anything but Twist/Agilent/Dynegene. DIY oligo methods (Doohee Kim's 3D-printed inkjet = OpenIDS; DNA Script enzymatic spotter; others in Georgia and China) are all too short and too error-prone. A Bay Area startup ("Instance Bio," name uncertain) that may synthesise its own oligos gave high-error material.

**Single perfects can be recovered by dial-out PCR at ~70%,** but going from pool to single constructs raises cost ~10×; the most pulled by hand is ~70 constructs; automation to 384 is possible but tedious and expensive. Dial-out was invented by Jay Shendure's lab (Schwartz, Lee & Shendure 2012, Nat. Methods), not "Jason Dury" as auto-transcribed.

**Developer's biosecurity read: DropSynth is low-relevance.** It's a massively-multiplexed library method (roadmap: 12,000 then 100,000+ genes per reaction). For building one specific restricted sequence it's "terrible"; any standard assembly method is better. A bad actor wanting one sequence of concern would not use DropSynth.

**Cost.** Biggest single cost is first-time bead-making capital; beads are cheap per unit volume. A 384 bead set is "a couple thousand," more for 1536. Needs bulk oligos plus a multichannel robot. A forthcoming preprint shows a 12,000-per-reaction bead set with cheaper, fewer-step bead-making.

**Enzymatic is the DIY route to watch,** not chemical. DNA Script SYNTAX already reaches hundreds of nt at low error (but ~96-well throughput), and DNA Script has shown a microarray spotter. Plesa estimates long, low-error enzymatic oligos ~5–10 years out commercially, longer for DIY.

**Expertise.** A complete novice would struggle; an undergrad runs the protocol after one or two demonstrations. Computational design is now simplified. Basic molecular biology is needed, and library-handling experience is the real differentiator: without it, output quality drops sharply.

**Number to reconcile:** Plesa cites ~4% perfect for ~1 kb in the first DropSynth paper (usable data recovered even below 1% perfect). The project's summary table currently states ~25% perfect; confirm the source/condition for that figure.

---

## Implications for the chapters

- **Ch.1 §2.6 (DropSynth):** add the ~70 nt process floor as a length barrier that rules out short DIY oligos independent of fidelity; vendor triple now interview-sourced; soften the expertise read (undergrad-runnable after demonstration; library experience is the differentiator).
- **Ch.2 (control assessment):** DropSynth low-concern now rests on two independent legs — screened-input perimeter, and unsuitability for single-SOC production (developer's own view).
- **Ch.3:** enzymatic-DIY timescale (~5–10 yr commercial, longer DIY) supports the "unlikely before ~2032–2035" forecast; cost figures confirm the ~$3.4K anchor.
- **Ch.4 §4.6:** reinforces the laundering refinement — selection is imperfect (dial-out ~70%), mutants persist, so signal survives incomplete error-correction.
- **IBBIS summary:** add the 70 nt floor and single-SOC point to the DropSynth row and fidelity section; reconcile the ~25% perfect figure.
- **Attribution:** upgrade "Calin, personal communication" to "C. Plesa, interview, 2026" across chapters once identity is confirmed.

---

## Transcript (lightly cleaned; connection preamble trimmed)

**Interviewer (intro):** I'm a researcher, background in neuroscience (electrophysiology and molecular biology), now a fellow in Existential Risk Alliance working with IBBIS (International Biosecurity Initiative for Science). We're landscaping benchtop devices and DIY DNA synthesizers, which aren't regulated, to see whether regulation is needed. We came across DropSynth for gene assembly and wanted to ask about oligo quality, length, whether self-synthesised oligos work, and expertise. First question: what's the minimum oligo quality and length DropSynth requires?

**Plesa:** The issue is that all DropSynth does is stitch oligos together, so any errors in the oligos get propagated through. Oligos have some error rate; typically we don't use below about 1 in 500. The error rate is roughly constant as a function of length, but percent-perfect drops as you increase length. If your oligos are 50% perfect and you stitch two together into, say, 500 bp, you end up with 25%; add another and you're at 12%, and so on. That puts an effective cap on length, based mostly on what you want to do downstream.

For us, we couple it to multiplexed functional assays: clone the constructs in, tag them with UMI barcodes, map them, transform into cells. The critical step is that when we sequence the linkage between barcode and assembled gene, we have to oversample enough to recover a large number of perfects. There's a formula based on library diversity, percent-perfect, and uniformity (skew) that tells you the read depth needed to be, say, 90% sure your coverage is 95%. That usually sets how long you can go and still recover data. We've recovered decent data under 1% perfects; you just have to oversample a lot.

The other interesting thing: the process produces a lot of errors. In our first paper it was ~4% perfect, 96% errors; of those about 50% were frameshifted junk, but the other ~46% were mutants, which are perfectly good data. You feed those into a model and learn your biological question. So mutants aren't a waste.

On oligo quality: there are at the moment three high-quality vendors, Dynegene out of China, Twist out of the USA, and Agilent out of the USA. They produce ≥230 nucleotides at 1 in 500 or better, all using an inkjet phosphoramidite process. Other vendors use other technologies including electrode-protection, which is much more error-prone. Photo-protection is also significantly more error-prone; only one or two vendors still use photolithography (LC Sciences in Texas, and one in Michigan that used to be Roche NimbleGen), and it's so error-prone that nobody really uses it anymore.

It is possible to fish out perfect molecules using dial-out PCR: if everything's barcoded and you know which barcodes are perfect, you synthesise primers for those barcodes and amplify single constructs out of the pool. We do this all the time. Jay Shendure's lab invented it over a decade ago; we and others have published scripts. In our hands it's about a 70% rate. But going from a gene pool to single constructs raises cost ~10×; the most we've pulled from one thing is maybe 70 constructs. You could automate to 384 with a liquid handler, but it gets tedious and costs go way up. For the most part we need long oligos, at least 200 nt, ideally with error better than 1 in 500.

**Interviewer:** We're less concerned about commercial providers because they tend to screen. Do you know labs that reported using DropSynth with a non-commercial (non-screened) oligo source?

**Plesa:** I'm not aware of anybody using an oligo source other than Twist, Agilent, or Dynegene. There was a Bay Area startup ("Instance Bio," unclear) that may synthesise its own oligos; we tried them once and their material had a lot of errors. Most do-it-yourself approaches have two problems: they're short, and they're error-prone, which is a bad combination for DropSynth input. Doohee Kim in South Korea published a 3D-printed homemade oligo inkjet; DNA Script published an enzymatic microarray spotter; there's one from Georgia and at least one from China. All have pretty bad error rates and short length.

One thing I didn't mention: standard DropSynth requires about 70 nucleotides for the process itself, so whatever your oligo length, at least 70 goes to the process, and the rest is payload, part of which is overlap for stitching. Even at 150-mer you'd have ~80 bases for payload, then ~20 on the ends and ~40 in the middle for overlaps. So it takes a lot of oligos to stitch something long. Short answer: it doesn't fit DIY technology as it currently is. Maybe eventually; vendors have shown the chemistry works, but it needs control over temperature, stoichiometry, and other parameters that are hard for a DIY lab right now.

Enzymatic synthesis could be much easier for a DIY person. DNA Script SYNTAX already pushes to hundreds of nucleotides at low error, though limited to ~96-well throughput, and they've shown a microarray spotter. Once enzymatic progresses further, that could enable long, low-error enzymatically synthesised oligos, maybe 5–10 years out commercially, longer for DIY.

**Interviewer:** We're comparing cost across DIY methods (OpenIDS ~$20K, photolithographic DIY ~$200K). If you already had an oligo source and just ran DropSynth, roughly what does that cost?

**Plesa:** The supplementary of the first paper has a detailed cost breakdown. Some costs have risen a little. The biggest single cost is making the beads the first time: beads are cheap per unit volume but there's real capital up front. You can build a 384 or 1536 set for on the order of a couple thousand for the 384, more for the 1536. It's not super involved: order lots of oligos and use a multi-channel robot. We're releasing a preprint soon showing a 12,000-per-reaction bead set with a more optimised, lower-cost bead-making process, and next year hopefully 100,000+ genes per reaction, so we can assemble an entire Twist pool at once.

From a biosecurity perspective, that's my number-one point on why DropSynth isn't that relevant: if someone wants to build a restricted or illegal sequence, they'd want one particular sequence, and DropSynth is terrible for that. Any other assembly method is better to build one thing. For 1,000 things it's great; for one thing there's no reason to use DropSynth.

**Interviewer:** Thoughts on the field, e.g. Omega (Romero lab, 2025)?

**Plesa:** Researchers just want cheap genes; that's why I built DropSynth in the first place. Oligo pools are the cheapest DNA source, so the question is how to assemble them. Omega is one technique; NEB had a paper; there's a preprint from Howard Salis's lab; another coming from a University of Washington group we collaborate with. Lots of ways to assemble, each with pros and cons.

**Interviewer:** Last one, the expertise barrier. Novice, or biology undergrad level?

**Plesa:** A complete novice without training would find it really hard. Undergrads, though, once we've shown them the protocol once or twice, can run it; it's not that difficult, and the computational design is much simpler now. You need some basic molecular biology, and ideally experience working with libraries specifically, because that's the main difference. There are unique things you do or don't do with libraries; without that knowledge, the quality of what you produce drops significantly.
