# Technology Readiness Index (TRI) for DIY DNA Synthesis
## Framework, Scoring Methodology & Data Collection Plan

**Status:** Phase 1 (Week 1-2) — Framework development & data gathering  
**Target Completion:** TRI spreadsheet + interactive visualization (end of Week 2)

---

## PART 1: TRI FRAMEWORK DESIGN

### 1.1 Core Scoring Dimensions (9 Axes)

Each DIY synthesis approach will be scored on these 9 independent dimensions (0-10 scale unless noted):

| # | Dimension | Scale | Definition | Why It Matters |
|---|-----------|-------|-----------|-----------------|
| 1 | **Technical Readiness Level (TRL)** | 1-9 (NASA) | Stage of maturity from concept to demonstrated system | Predicts deployment risk; determines if approach is "ready now" vs "future" |
| 2 | **Capital Cost** | $0-100K | Total upfront equipment investment | Accessibility barrier; determines who can afford it |
| 3 | **Per-Sequence Cost** | $0-1000 | Reagent+consumable cost per synthesis | Determines if economics favor DIY vs commercial |
| 4 | **Expertise Required** | 1-10 | Minimum technical background needed (1=no training, 10=PhD in chemistry) | Accessibility to non-expert biohackers |
| 5 | **Time-to-First-Synthesis** | Days/weeks | How long from "I bought this" to "I have DNA" | Practical speed; determines adoption rate |
| 6 | **Max Sequence Length** | bp (0-1000000) | Longest oligo producible in one synthesis cycle | Determines whether post-synthesis assembly needed |
| 7 | **Synthesis Yield/Error Rate** | % (0-100) | Per-cycle coupling efficiency; full-length product % | Determines final DNA quality; impacts downstream use |
| 8 | **Detectability/Oversight Risk** | 1-10 (1=very detectable, 10=invisible) | How easy to identify if someone is using this system | Policy/governance relevance |
| 9 | **Supply Chain Vulnerability** | 1-10 (1=single supplier, 10=fully redundant) | How vulnerable to reagent/component shortages | Control point assessment |

---

### 1.2 Secondary Scoring Dimensions (Derived)

These are **calculated** from primary dimensions; they inform policy recommendations:

| Derived Score | Calculation | Interpretation |
|--------------|-----------|-----------------|
| **Accessibility Index** | (10 - Expertise) × (10 - [Capital Cost/10K]) | Combined measure: how easy is it for a typical biohacker to use? |
| **Economic Parity Point** | Capital Cost ÷ ([Per-Seq Cost] - [Commercial per-bp rate]) | When does DIY break even vs. commercial synthesis? (sequences needed) |
| **Policy Control Score** | Detectability × Supply Chain Vulnerability | How much can policy actually control this approach? |
| **Adoption Velocity** | TRL × (10 - Time-to-First) × (10 - Expertise) | Predicted rate of community adoption |

---

### 1.3 Scoring Rubrics (Detailed)

#### **TRL Scale (NASA, 1-9)**
```
TRL 1: Basic research phase (concept exists, no prototype)
TRL 2: Research to prove feasibility (theory + early lab work)
TRL 3: Experimental proof of concept (bench-top prototype)
TRL 4: Technology validated in lab (small-scale demonstration)
TRL 5: Technology validated in relevant environment (OpenIDS = here)
TRL 6: Technology demonstrated in relevant environment (first commercial)
TRL 7: System prototype demonstration in operational environment
TRL 8: System complete and qualified (large-scale production)
TRL 9: Actual system proven in operational environment (commodity)
```

#### **Expertise Required (1-10 Scale)**
```
1-2:  No formal training; DIY instructions sufficient
3-4:  High school biology; ability to follow detailed protocols
5-6:  Undergraduate biology/chemistry; comfort with bench techniques
7-8:  Bachelor's in chemistry/biology; molecular biology experience
9-10: Master's/PhD in chemistry; custom synthesis/troubleshooting required
```

#### **Time-to-First-Synthesis (Days to Weeks)**
```
Days:
  1-2 days:   "Unbox and run" (minimal assembly)
  3-7 days:   Order components, assemble, calibrate, synthesize
  1-2 weeks:  Iterative assembly + troubleshooting
  3-4 weeks:  Significant custom fabrication or setup required
  1-2 months: Major build/learning curve

Week+:
  2-4 weeks:  Extensive calibration or wet-lab protocol development
  4-8 weeks:  Requires specialized equipment or lengthy training
  8+ weeks:   Pre-commercial; not realistic for DIY
```

#### **Max Sequence Length (bp)**
```
<100 bp:     Oligonucleotides only; assembly required for genes
100-500 bp:  Short sequences; light assembly overhead
500-2000 bp: Medium genes; manageable assembly
2000-10kb:   Full genes; straightforward Gibson/overlap-PCR
10-50kb:     Operons; requires advanced assembly
50+ kb:      Pathway-scale synthesis; rare for DIY
```

#### **Synthesis Yield / Full-Length Product % (Per-Cycle)**
```
<80%:        Low yield; <50% full-length products in multi-cycle synthesis
80-90%:      Moderate; acceptable for research (error correction possible)
90-95%:      High; commercial-grade for most applications
95-98%:      Excellent; industrial standard (OpenIDS = here)
98%+:        Premium; enterprise-grade reliability
```

#### **Detectability (1-10 Scale)**
```
1-2:  Extremely visible (large facility, power consumption, distinctive waste)
3-4:  Detectable with moderate effort (waste chemistry, equipment signatures)
5-6:  Possible to detect but requires investigation (consumable ordering patterns)
7-8:  Difficult to detect; requires sophisticated forensics (error patterns, software)
9-10: Essentially invisible (portable, low-power, uses commodity chemicals)
```

#### **Supply Chain Vulnerability (1-10 Scale)**
```
1-2:  Single supplier; banned/restricted material; easily controlled
3-4:  2-3 suppliers; some regulatory barriers; possible control
5-6:  4-6 suppliers; minimal regulatory barriers; control difficult
7-8:  8+ suppliers; commodity materials; control very difficult
9-10: Fully distributed; multiple substitutes; no control point
```

---

## PART 2: DATA COLLECTION STRATEGY

### 2.1 Data Sources Hierarchy (by Reliability)

**Tier 1 (Highest Confidence):**
- Published peer-reviewed papers (primary data from authors)
- GitHub repos with open data (OpenIDS, others)
- Official manufacturer specs (Xaar printheads, Sigma reagents)
- Market research reports with cited methodology

**Tier 2 (Good Confidence):**
- Preprints (bioRxiv, arXiv) with author contact possible
- Company datasheets & public pricing
- DIYbio community reports (forum posts, build logs)
- Conference talks & presentations

**Tier 3 (Use with Caveats):**
- Social media discussions (Reddit, Twitter)
- Blog posts from experienced practitioners
- Estimates from industry analysts
- Extrapolation from partial data

### 2.2 Specific Data Needed Per Approach

#### **OpenIDS (Inkjet)**
- **TRL:** 5 (demonstrated in relevant environment) — Kim et al. 2024, 2025
- **Capital Cost:** $19,900 (5-printhead system) — Kim et al. 2024; GitHub BOM
- **Per-Sequence Cost:** Estimate from reagent pricing
  - Phosphoramidites: $500-1000 per 100 syntheses (commodity pricing)
  - Solvents (propylene carbonate): <$100
  - CPG, substrates: <$500
  - **Estimate:** $10-50 per sequence at scale
- **Expertise:** Medium (assembly, Arduino programming, protocol optimization)
  - **Score:** ~6 (undergrad bio + patience)
- **Time-to-First:** 4-6 weeks (assembly, calibration, first synthesis)
- **Max Length:** 30nt demonstrated; theoretical up to 50-100nt
- **Yield:** 98% per cycle (Kim et al.)
- **Detectability:** Medium-High (large equipment, distinctive waste stream)
  - **Score:** ~4 (visible to authorities, detectable by forensics)
- **Supply Chain:** Xaar 128 printheads (still manufactured, available via OEM/AliExpress)
  - **Score:** ~7 (multiple suppliers, not restricted)

#### **DropSynth (Microfluidic)**
- **TRL:** 4 (technology validated in lab) — research prototype, not commercial
- **Capital Cost:** $50K-100K (custom microfluidic setup)
  - Requires cleanroom or outsourced chip fab
  - Flow control equipment
  - **Estimate:** $70K minimum
- **Per-Sequence Cost:** Unknown (research only); estimate $5-20 if scaled
- **Expertise:** High (microfluidic design, chip fabrication, flow optimization)
  - **Score:** ~8-9 (requires chemistry + engineering)
- **Time-to-First:** 2-3 months (chip design, fabrication, protocol optimization)
- **Max Length:** Similar to OpenIDS (~50-100nt); massively parallel
- **Yield:** Not fully characterized; likely 90-95%
- **Detectability:** Low-Medium (microfluidic equipment less distinctive)
  - **Score:** ~5-6 (harder to detect than inkjet)
- **Supply Chain:** Microfluidic components are commodity (PDMS, lithography)
  - **Score:** ~8 (multiple sources, not restricted)

#### **Electrochemical Synthesis**
- **TRL:** 3 (proof of concept) — Wang et al. 2021, pre-commercial
- **Capital Cost:** $5-15K (electrodes, controllers, reagent delivery)
- **Per-Sequence Cost:** $2-5 (no phosphoramidites; just electricity + electrode consumables)
- **Expertise:** Low-Medium (electrochemistry knowledge + control systems)
  - **Score:** ~5-6
- **Time-to-First:** 2-4 weeks (assembly, electrode fabrication, optimization)
- **Max Length:** 100-200nt (demonstrated); theoretical higher
- **Yield:** 85-90% (electrochemical deblocking challenges)
- **Detectability:** Very Low (portable, low power, generic equipment)
  - **Score:** ~8-9 (nearly invisible)
- **Supply Chain:** Electrodes (Au, Pd) commodity; controllers (Arduino) commodity
  - **Score:** ~9 (fully distributed, untracked)

#### **Enzymatic DNA Synthesis (EDS)**
- **TRL:** 5-6 (demonstrated, entering commercial production)
- **Capital Cost:** $50-200K (benchtop enzyme synthesizer)
  - Ansa, Molecular Assemblies, others: commercial products available
  - Lower-cost DIY versions: $10-30K possible (polymerase + flow setup)
- **Per-Sequence Cost:** $1-10 (polymerase, dNTPs, no phosphoramidites)
- **Expertise:** Medium (biochemistry, enzyme handling, flow chemistry)
  - **Score:** ~6-7
- **Time-to-First:** 1-2 weeks (commercial systems are turnkey; DIY setup slower)
- **Max Length:** 400bp (Ansa Clonal, Nov 2024); 5000bp (Elegen, Jan 2025)
- **Yield:** 95%+ (polymerase fidelity improving rapidly)
- **Detectability:** Medium (enzyme reagents orderable, but less suspicious than phosphoramidites)
  - **Score:** ~5 (detectable by reagent tracking, but hard to distinguish from legitimate research)
- **Supply Chain:** Polymerases, nucleotides widely available; no restricted materials
  - **Score:** ~8-9

#### **Commercial Benchtop Synthesizers (For Comparison)**
- **TRL:** 7-8 (system prototype/qualified)
- **Capital Cost:** $50-200K (Tecan, ABI, others)
- **Per-Sequence Cost:** $0.01-0.1 per bp (economies of scale)
- **Expertise:** Low (turnkey; push-button operation)
  - **Score:** ~2
- **Time-to-First:** Days (delivery + setup)
- **Max Length:** 100-1000bp standard
- **Yield:** 98%+
- **Detectability:** **Subject to OSTP/IGSC screening**
  - **Score:** ~1 (orders are monitored)
- **Supply Chain:** Manufacturers (Thermo Fisher, etc.) implement screening
  - **Score:** ~1 (screened/regulated)

---

## PART 3: TRI SPREADSHEET STRUCTURE

### 3.1 Column Organization

**Spreadsheet Tabs:**
1. **TRI_Raw_Data** — All 9 primary scoring dimensions + metadata
2. **TRI_Derived** — Calculated indices (Accessibility, Parity Point, Control Score, Adoption Velocity)
3. **Data_Sources** — Citations, confidence levels, uncertainty ranges for each cell
4. **Comparison_Charts** — Radar charts, scatter plots (generated from tabs 1-2)
5. **Research_Gaps** — Unknown data points; priority for Phase 1 research

### 3.2 TRI_Raw_Data Tab Structure

```
Approach Name | TRL | Capital Cost ($) | Per-Seq Cost ($) | Expertise (1-10) | 
Time-to-First (weeks) | Max Length (bp) | Yield (%) | Detectability (1-10) | 
Supply Chain (1-10) | Data_Source | Confidence | Lower_Bound | Upper_Bound | 
Notes
```

**Example Row (OpenIDS):**
```
OpenIDS | 5 | 19900 | 15 | 6 | 5 | 100 | 98 | 4 | 7 | 
Kim et al. 2024, GitHub BOM | HIGH | 18000 | 22000 | 
98% coupling confirmed; cost estimate from Sigma pricing
```

### 3.3 Derived Indices (TRI_Derived Tab)

```
Approach | Accessibility_Index | Economic_Parity_Point | Policy_Control_Score | 
Adoption_Velocity | Overall_Readiness | Biosecurity_Risk_Level
```

**Formula Examples:**

**Accessibility Index (0-100):**
```
= ((10 - Expertise) / 10) × ((100000 - Capital_Cost) / 100000) × 100
```
- Higher = more accessible to average biohacker
- OpenIDS: ((10-6)/10) × ((100k-20k)/100k) × 100 = 32 (moderate)
- Electrochemical: ((10-5)/10) × ((100k-10k)/100k) × 100 = 45 (higher)

**Economic Parity Point (sequences needed to break even):**
```
= Capital_Cost / (Per_Seq_Cost - Commercial_Rate)
Assume Commercial_Rate = $0.05 per bp (conservative)
If max_length = 100bp, commercial cost ≈ $5 per sequence

OpenIDS: 19900 / (15 - 5) = 1990 sequences
Electrochemical: 10000 / (5 - 5) = ∞ (never breaks even on cost alone)
```

**Policy Control Score (1-100):**
```
= (Detectability × Supply_Chain_Vulnerability) / 10
1 = fully controllable; 100 = uncontrollable

OpenIDS: (4 × 7) / 10 = 2.8 (controllable via printhead sourcing)
Electrochemical: (9 × 9) / 10 = 8.1 (very difficult to control)
```

**Adoption Velocity (0-100):**
```
= TRL × ((10 - Time_to_First_weeks) / 10) × ((10 - Expertise) / 10) × 10
Higher = faster predicted adoption

OpenIDS: 5 × ((10-5)/10) × ((10-6)/10) × 10 = 12 (moderate)
Electrochemical: 3 × ((10-3)/10) × ((10-5)/10) × 10 = 10.5 (slower due to TRL)
```

---

## PART 4: RESEARCH GAPS & DATA COLLECTION PRIORITY

### 4.1 Priority 1: Fill Immediately (Literature + Direct Contact)

**For OpenIDS:**
- [ ] Confirm per-sequence reagent cost with Sigma/ChemGenes pricing (1 email)
- [ ] Verify printhead sourcing options (check AliExpress/OEM distributors) (2 hours)
- [ ] Contact Kim/Bang lab for OpenIDS2 updates (email)

**For Electrochemical:**
- [ ] Locate latest preprints on ElectroWayve Sciences / other EDS startups
- [ ] Confirm electrode cost & availability (supplier research, 2 hours)
- [ ] Model time-to-first for DIY electrochemical setup (estimate from literature)

**For DropSynth:**
- [ ] Contact Castellanos lab (bioRxiv) for TRL/timeline update
- [ ] Estimate microfluidic chip fab cost (reach out to academic cleanroom providers)

**For Enzymatic:**
- [ ] Collect pricing from Ansa, Molecular Assemblies, Ribbon Bio (public websites)
- [ ] Locate TRL assessments from company product announcements (2024-2026)

### 4.2 Priority 2: Follow-Up Outreach (Week 2)

**DIYbio community:**
- [ ] Post survey on DIYbio.org forums: "Have you built OpenIDS? What was the actual cost & timeline?"
- [ ] Contact 2-3 BioCurious members for testimonials (Slack/email)

**Academic partners:**
- [ ] Reach out to UCL colleagues with printhead access for compatibility assessment
- [ ] Ask Rassin for any IBBIS contacts working on DIY synthesis

**Industry:**
- [ ] Email Thermo Fisher/IDT for benchtop synthesizer pricing (for comparison baseline)
- [ ] Request data sheets from Xaar Corporation (printhead specs)

### 4.3 Priority 3: Estimation & Modeling (Week 2-3)

**If data unavailable:**
- Use published cost structures (e.g., phosphoramidite synthesis papers)
- Build sensitivity models (e.g., "if per-seq cost is $10 vs $50, adoption changes by X")
- Scenario modeling (e.g., "in 2028, if China clones OpenIDS for $5K, accessibility jumps to Y")

---

## PART 5: VISUALIZATION & DELIVERABLES

### 5.1 Chart Types (to Generate from TRI Data)

**1. Radar Chart (TRL Landscape)**
- 9 axes: TRL, Capital, Per-Seq Cost, Expertise, Time, Length, Yield, Detectability, Supply Chain
- Each approach = polygon overlay
- Shows at-a-glance readiness profile

**2. Scatter Plot: Cost vs. Accessibility**
- X-axis: Accessibility Index (0-100)
- Y-axis: Capital Cost ($)
- Bubble size: Adoption Velocity
- Color: Detectability (red=detectable, green=invisible)

**3. Timeline Chart: Parity Point vs. Detectability**
- X-axis: Economic Parity Point (sequences to break even)
- Y-axis: Detectability (1-10)
- Shows trade-off: cheaper DIY vs. harder to detect

**4. TRL Trajectory (2024-2028 Projection)**
- Each approach on separate line
- X-axis: Year (2024-2028)
- Y-axis: Projected TRL (conservative, optimistic bounds)
- Shows which approaches mature fastest

**5. Policy Control Assessment**
- X-axis: Detectability (1-10)
- Y-axis: Supply Chain Vulnerability (1-10)
- Quadrants: Controllable / Detectable / Vulnerable / Invisible
- Policy recommendations by quadrant

### 5.2 Final Deliverable Format

**Main:** Interactive Excel workbook
- TRI_Raw_Data (sortable, filterable)
- TRI_Derived (auto-calculated indices)
- Data_Sources (citeable; includes uncertainty)
- Comparison_Charts (pivot tables + embedded charts)

**Secondary:** PDF summary report
- Executive summary (1 page)
- TRI table + key findings (2 pages)
- Radar charts + scatter plots (3 pages)
- Research gaps & priorities (1 page)

**Tertiary:** GitHub repo
- Spreadsheet (xlsx)
- Python script to regenerate charts
- Citation list (BibTeX format)
- Methodology document (this file, plus code comments)

---

## PART 6: IMPLEMENTATION TIMELINE (Week 1-2)

### **Week 1 (July 8-14)**

**Monday-Tuesday:**
- [ ] Finalize TRI framework & scoring rubrics (you are here)
- [ ] Create blank Excel template with formulas
- [ ] Set up Data_Sources tab with citation format

**Wednesday-Thursday:**
- [ ] Populate OpenIDS data (highest confidence; published papers + GitHub)
- [ ] Populate Electrochemical data (from literature; estimate unknowns)
- [ ] Populate Enzymatic data (market research + company websites)

**Friday:**
- [ ] Draft 5-8 data collection outreach emails (to Kim/Bang, Castellanos, DIYbio forums, etc.)
- [ ] Send Priority 1 emails
- [ ] Review TRI for internal consistency (e.g., does high TRL + low expertise = realistic?)

### **Week 2 (July 15-21)**

**Monday-Wednesday:**
- [ ] Populate DropSynth data (follow-up from outreach or estimation)
- [ ] Populate Commercial benchtop baseline (for comparison)
- [ ] Calculate all derived indices (Accessibility, Parity Point, Control Score, Adoption Velocity)

**Thursday:**
- [ ] Generate comparison charts (radar, scatter, timeline)
- [ ] Sensitivity analysis: "What if electrochemical cost drops to $5K? Adoption jumps to X%"
- [ ] Draft Data_Sources documentation for each cell

**Friday:**
- [ ] Final review & audit of spreadsheet
- [ ] Write 1-page summary of TRI findings
- [ ] Prepare for presentation to Rassin (end of Week 2)

---

## NOTES FOR IMPLEMENTATION

### Key Assumptions to Document

1. **Commercial synthesis baseline:** Assume $0.05/bp cost (conservative middle estimate)
2. **"DIY feasible" threshold:** Score approaches with TRL ≥ 4 and Accessibility ≥ 20 as "accessible now"
3. **Detectability metric:** Assumes regulatory interest (forensics, supply chain tracking)
4. **Supply Chain Vulnerability:** Assumes no deliberate restrictions; scores reflect realistic sourcing friction

### Uncertainty Handling

- **Confidence levels:** HIGH (published, verified), MEDIUM (expert consensus, multiple sources), LOW (single source, extrapolated)
- **Ranges:** Report (Lower, Best Estimate, Upper) for each cell
- **Sensitivity thresholds:** Flag cells where ±20% change would alter conclusions

### Red Flags to Watch

- **OpenIDS cost creep:** If actual builds exceed $25K, accessibility drops significantly
- **Electrochemical yield:** If <85%, feasibility drops; >95%, it's game-changing
- **Supply chain disruption:** If Xaar stops making 128 printheads, OpenIDS becomes harder
- **Regulatory tightening:** If propylene carbonate is regulated, solvent substitution needed

---

## APPENDIX: QUICK REFERENCE — TRI SCORING SCALE

```
TRL Readiness:        | Accessibility Index:  | Policy Control Score:
1-3 = Concept only    | 0-20 = Inaccessible   | 0-2 = Fully controllable
4-5 = Demonstrated    | 20-40 = Difficult     | 3-5 = Largely controllable  
6-7 = Production      | 40-60 = Moderate      | 6-7 = Difficult to control
8-9 = Commodity       | 60-80 = Accessible    | 8-10 = Uncontrollable
                      | 80-100 = Very easy    |
```

---

**Next Step:** Build the Excel workbook with this framework. Ready?
