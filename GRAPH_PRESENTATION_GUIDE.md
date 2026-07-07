# TRI Visualization Guide: How to Use These Graphs

**Created:** July 7, 2026  
**For:** Phase 1 Research Presentation & Policy Briefing

---

## 📊 GRAPH 1: TRI Dashboard (6-Panel Overview)
**File:** `TRI_Dashboard_6Charts.png`

### Purpose
Comprehensive single-page overview of all key TRI metrics in one view. **Use this to open presentations or print as a poster.**

### What Each Panel Shows

**Panel 1 (Top-Left): Radar Chart - Multi-Dimensional Profile**
- 9 axes: TRL, Affordability, Cost per Sequence, Ease of Use, Speed, Sequence Length, Yield, Invisibility, Supply Chain Robustness
- **Interpretation:** 
  - OpenIDS (blue) = well-rounded, balanced profile; weak on invisibility (detectable)
  - Electrochemical (red) = DANGEROUS profile (nearly invisible, moderate cost), weak on TRL
  - Commercial (gray dashed) = high TRL but low accessibility
- **Use for:** Explaining why different approaches have different risk profiles

**Panel 2 (Top-Middle): Cost vs Accessibility (Bubble Chart)**
- X-axis: How accessible to biohackers (0-100 scale)
- Y-axis: Capital cost ($)
- Bubble size: Adoption velocity (larger = faster adoption predicted)
- Color: Risk level (red = high risk, green = low risk)
- **Key Finding:** Electrochemical (red bubble, top-right) = highest risk (easy + invisible)
- **Use for:** Showing why electrochemical is the "canary in coal mine"

**Panel 3 (Top-Right): Policy Control Quadrant**
- X-axis: Detectability (1-10, left = invisible, right = detectable)
- Y-axis: Supply Chain Vulnerability (bottom = robust, top = fragile)
- **Green zone (bottom-left):** Controllable via regulation
- **Red zone (top-right):** Uncontrollable; can't stop it
- **Key Finding:** Electrochemical in red zone = policy has no leverage
- **Use for:** Explaining to regulators which approaches are worth controlling

**Panel 4 (Bottom-Left): TRL Timeline 2024-2028**
- Lines show Technology Readiness Level progression over 4 years
- Dashed reference lines at TRL 5, 6, 7 (important milestones)
- **Key Finding:** Electrochemical and enzymatic will reach TRL 4-5 by 2028
- **Use for:** Addressing "this is hypothetical" objections (it's not; it's coming)

**Panel 5 (Bottom-Middle): Capital Cost Bar Chart**
- Shows total upfront investment needed
- Color-coded bars; labels show exact costs
- Horizontal reference lines at $10K (accessible), $20K (moderate), $50K (expensive)
- **Key Finding:** Electrochemical is cheapest; enzymatic is most expensive
- **Use for:** Explaining cost barriers and inflection points

**Panel 6 (Bottom-Right): Biosecurity Risk Matrix**
- X-axis: Detectability (invisible to detectable)
- Y-axis: Accessibility (hard to easy for biohackers)
- Bubble size: Policy control score (smaller = easier to control)
- Color: Risk level
- **Key Finding:** Electrochemical (top-right, huge bubble) = uncontrollable risk
- **Use for:** Presenting biosecurity risk in plain language

---

## 🎯 GRAPH 2: Individual Radar Profiles
**File:** `TRI_Individual_Radars.png`

### Purpose
**Deep dive into each approach.** Use this when presenting to specialists or for technical documentation.

### What It Shows
6 separate radar charts (one per approach):
- Each has 9 dimensions rated 0-10
- Inner circle = weaker; outer circle = stronger

### How to Read Each Profile

**OpenIDS (Top-Left, Blue)**
- Strong: TRL, cost, yield, availability
- Weak: Invisibility (score ~4; detectable)
- **Message:** "This is ready now, but detectable"

**Electrochemical (Top-Middle, Red)**
- Strong: Low cost, speed, invisibility, supply chain robustness
- Weak: TRL (only 3), yield (88%)
- **Message:** "This is the threat - it's becoming ready and impossible to detect"

**Enzymatic (Top-Right, Green)**
- Strong: TRL, high yield, long sequences
- Weak: High cost ($80K), requires expertise
- **Message:** "This is commercial soon, but expensive barrier limits DIY"

**DropSynth (Bottom-Left, Orange)**
- Weak across the board: low accessibility, high cost, high expertise
- **Message:** "This is NOT an imminent DIY threat due to complexity"

**Commercial Benchtop (Bottom-Middle, Purple)**
- Strong everything EXCEPT subject to screening
- **Message:** "This is the current regulated baseline"

**Commercial Provider (Bottom-Right, Gray)**
- Perfect radar except hidden detectability (score 0.2)
- Reason: Already screened by IGSC/OSTP
- **Message:** "This is the current regulated system"

### Use Cases for This Graph
- **For scientists/engineers:** "Here's the technical depth you need"
- **For investors:** "Here's market readiness across all dimensions"
- **For policy:** "Here's why electrochemical needs different regulation than OpenIDS"

---

## ⚖️ GRAPH 3: Accessibility vs Risk Trade-Off
**File:** `TRI_AccessibilityVsRisk.png`

### Purpose
**Simple, side-by-side comparison for non-technical audiences.** Use in executive presentations, policy briefs, media.

### What It Shows

**Left Panel: Accessibility Index (0-100)**
- Higher = easier for biohackers to use without formal training
- OpenIDS (32): Requires moderate expertise + patience
- Electrochemical (45): More accessible (lower expertise needed)
- DropSynth (8): Very hard (chip fabrication barrier)
- **Key message:** "Electrochemical is most accessible"

**Right Panel: Biosecurity Risk Score (0-10)**
- Higher = more dangerous from biosecurity perspective
- Electrochemical (7.8): Nearly invisible, commodity materials, portable
- OpenIDS (3.2): Detectable, traceable equipment supply
- **Key message:** "Electrochemical is highest risk"

### Why This Matters
**The paradox:** The EASIEST approach to build (Electrochemical) is also the HARDEST to detect and control. This is the central policy challenge.

### Use Cases
- **One-slide executive summary:** "This shows the fundamental problem"
- **Policy brief:** "Why current screening strategy is inadequate"
- **Media/public:** "Simple visualization of the challenge"

---

## 🎤 How to Present These Graphs in a Meeting

### 5-Minute Version (Use Just One Graph)
**Graph 1, Panel 6 (Risk Matrix)** 
- "Here's where every approach sits on Accessibility vs Invisibility"
- "Electrochemical (top-right) = most concerning: easy AND undetectable"
- "OpenIDS (bottom-left) = manageable: detectable AND controllable"

### 15-Minute Version (Use Graphs 1 & 3)
1. **Start with Graph 3 (Accessibility vs Risk)**
   - "Here's the core problem: the easiest approaches are the hardest to detect"
   - Point to Electrochemical: "This one."
2. **Show Graph 1, Panel 4 (Timeline)**
   - "This isn't hypothetical. Here's when each technology matures."
   - "Electrochemical reaches TRL 4-5 by 2028."
3. **Show Graph 1, Panel 3 (Control Quadrant)**
   - "Policy levers only work in the green zone (bottom-left)."
   - "Electrochemical is in the red zone (top-right). We have no control."

### 30-Minute Deep Dive (Use All Graphs)
1. **Graph 1 Dashboard (10 min):** Walk through all 6 panels
2. **Graph 2 Individual Radars (10 min):** Spotlight OpenIDS vs Electrochemical
3. **Graph 3 Trade-Off (5 min):** "Here's what this means for policy"
4. **Conclusion (5 min):** "Our research identifies where control is still possible"

---

## 💾 File Specifications

| File | Size | Resolution | Format | Best For |
|------|------|-----------|--------|----------|
| TRI_Dashboard_6Charts.png | ~2 MB | 300 DPI | PNG | Posters, printed handouts, presentations |
| TRI_Individual_Radars.png | ~1.5 MB | 300 DPI | PNG | Technical appendices, detailed analysis |
| TRI_AccessibilityVsRisk.png | ~1 MB | 300 DPI | PNG | Executive summaries, policy briefs, media |

All images are high-resolution (300 DPI) suitable for:
- ✓ Printed materials (posters, handouts)
- ✓ Presentations (PowerPoint, Keynote)
- ✓ Reports (PDF embedding)
- ✓ Web/blog posts
- ✓ Printing on A4/US Letter at full size

---

## 🔑 Key Insights Illustrated by These Graphs

### Insight 1: Accessibility-Risk Paradox
The most accessible approaches (Electrochemical) are the hardest to detect. This is the core biosecurity problem these graphs illustrate.

### Insight 2: Policy Control Points Are Collapsing
- OpenIDS: Still controllable via printhead sourcing (Xaar 128 availability)
- Electrochemical: Completely uncontrollable (portable, no distinctive reagents)
- Enzymatic: Partially controllable (enzyme licensing possible)
- **Implication:** Current synthesis screening strategy is increasingly obsolete

### Insight 3: Maturation Is Inevitable
All approaches are advancing on a predictable TRL trajectory. Electrochemical reaches usable status by 2028. Policy must account for this.

### Insight 4: Cost Convergence
DIY costs are approaching commercial costs per-sequence. Economic parity point is approaching (~2000 sequences for OpenIDS; immediate for Electrochemical). At some cost threshold, DIY becomes competitive.

---

## 📋 Suggested Caption Text for Each Graph

### For Graph 1 (Dashboard)
"Figure 1: Technology Readiness Index Dashboard showing comparative assessment of DIY DNA synthesis approaches across nine dimensions (TRL, capital cost, expertise required, detectability, supply chain robustness, etc.). The six panels illustrate cost-accessibility trade-offs, policy control feasibility, maturation timelines, and biosecurity risk. Key finding: Electrochemical synthesis (red) poses highest biosecurity risk due to accessibility combined with invisibility, while remaining largely uncontrollable via current policy mechanisms."

### For Graph 2 (Radars)
"Figure 2: Individual Technology Readiness Profiles for six approaches across nine technical dimensions. OpenIDS shows well-balanced profile with weakness in invisibility (detectable). Electrochemical shows dangerous combination: low cost, ease, speed, and invisibility. DropSynth blocked by high expertise and cost barriers. Commercial approaches (benchtop, provider) shown for reference; note low detectability only because these are already subject to IGSC screening."

### For Graph 3 (Trade-Off)
"Figure 3: Accessibility-Risk Trade-Off Analysis. Left panel shows ease of implementation for non-expert biohackers; right panel shows biosecurity risk level. Electrochemical (red) emerges as critical concern: highest accessibility combined with highest risk. This paradox—that the easiest approaches to build are hardest to detect—illustrates fundamental gap in current synthesis screening strategy."

---

## 💡 Tips for Effective Presentation

1. **Lead with the problem (Graph 3):**
   - "Easier to build = harder to detect"
   - "This is why synthesis screening alone is insufficient"

2. **Show the timeline (Graph 1, Panel 4):**
   - "This is not hypothetical"
   - "These approaches are materializing on schedule"

3. **Explain the control gap (Graph 1, Panel 3):**
   - "Policy can control approaches in the green zone"
   - "Electrochemical is in the red zone: uncontrollable"

4. **Conclude with implications:**
   - "If synthesis democratizes, screening becomes irrelevant"
   - "New governance models are needed; current approach is insufficient"

---

**Next Steps:** Use these graphs in your policy brief (Week 12) and technical report. Consider printing Graph 1 as a poster for your presentation to Rassin (end of Week 2).

