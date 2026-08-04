# The Benchtop DNA Synthesizer Supply Chain — A Biosecurity Monitorability & Control-Point Assessment

*Companion to the DIY and Phosphoramidite supply-chain assessments. Monitorability framing only; no operational build detail. Characterises **what running a commercial benchtop synthesizer requires and where a durable control point actually exists** — deliberately contrasted with the DIY chain.*

## 1. Bottom line

The benchtop ("buy") path is the mirror image of DIY: unlike the DIY chain, it **does contain genuine chokepoints** — but they are being eroded by a resale and spare-parts market that no point-of-sale control reaches. The two real levers are (1) the **proprietary reagent cartridge/consumable** that closed instruments run on (a licensed, trackable input, unlike DIY's commodity reagents), and (2) the **device manufacturer** itself, which is where on-device screening attaches. Both are legitimate control points in principle. Both are undermined in practice: the secondary/used-device market moves screened-by-design instruments into unscreened hands, and standing webshops sell the spare parts and à-la-carte reagents to keep an out-of-warranty or self-built instrument running.

The governance line: **benchtop has controllable inputs where DIY has none — but "controllable at first sale" is not "controllable," because resale bypasses the manufacturer and the consumable lock alike.**

## 2. Scope

"Benchtop" here means commercially manufactured instruments a user buys rather than builds: column phosphoramidite benchtops (e.g. MerMade/LGC, Dr Oligo/Biolytic, Kilobaser) and enzymatic benchtops (DNA Script SYNTAX), plus gene-assembly workstations acquired the same way (Telesis Bio / Codex DNA BioXP). The supply chain is the instrument, the consumables it depends on, and the aftermarket that keeps it alive.

## 3. The benchtop input categories

### 3.1 Proprietary reagent cartridges / consumables — the real chokepoint

The distinguishing feature of modern benchtops is that many run on **closed, licensed consumables** rather than open-cart reagents:

- **DNA Script SYNTAX** — proprietary enzymatic reagent kits/cartridges under licensing; the consumable, not the instrument, is the recurring gate
- **Kilobaser** — cartridge/chip-based column synthesis
- **Telesis Bio BioXP** — proprietary assembly kits
- Column benchtops more broadly — often sold with vendor amidite/reagent kits, though the underlying chemistry is open (§3.3)

**Chokepoint status: YES — this is the strongest benchtop lever.** A licensed consumable is trackable in a way commodity reagents are not: the vendor knows who buys cartridges and how often, enabling know-your-customer (KYC) at the consumable level. This is a real, existing control point (noted in Ch. 2 as "proprietary-reagent KYC") and is exactly what DIY lacks.

**But its reach is bounded** by (a) instruments whose chemistry is open and can be run on generic reagents, and (b) any secondary market in the consumables themselves.

### 3.2 The instrument and its manufacturer — the on-device screening point

The device is where an on-device screening mandate would live: a compliant manufacturer can bake sequence screening and record-retention into firmware at the point of manufacture.

**Chokepoint status: YES in principle, LEAKY in practice.** Two structural limits, both documented in the companion analyses:

- **Jurisdictional reach.** Of the 34 benchtop manufacturers inventoried in the ERA/IBBIS group, only ~8 are US-headquartered (directly bound), ~12 allied, ~14 outside reach — and the newest, highest-throughput capacity concentrates outside. A US device mandate binds under a quarter of makers.
- **Legacy base.** ~35% of firms predate 2010; pre-mandate instruments cannot be retrofitted with KYC, secure boot, or on-device screening.

So manufacturer-level control is real for *new, in-jurisdiction* devices and absent for the rest.

### 3.3 GMP/standard phosphoramidites + ancillary reagent kits

Column benchtops consume the same phosphoramidites, activator, oxidiser, deblock and capping reagents as any phosphoramidite process — covered in full by the **Phosphoramidite Supply-Chain Assessment**.

**Chokepoint status: NONE** (commodity, multi-sourced, substitutable) — cross-reference that document; not repeated here.

### 3.4 The secondary / used-device market — the chokepoint solvent

This is what dissolves the two real levers above. Documented in the "Secondary Market for Benchtop DNA Synthesizers" brief:

- Working instruments (incl. a Telesis Bio BioXP gene-assembly workstation ~US$13.5K, and column synthesizers from ~£670 to ~$25K) list openly on eBay, LabX, EquipNet, Machinio, and via mainstream shopping ads — **no buyer verification, cross-border shipping observed.**
- A resold device carries **none** of its point-of-sale controls, and its on-device screening state (if any) is unverifiable to the next buyer.
- The Codex DNA / Telesis Bio 10-Q disclosure of BioXp units reaching embargoed destinations via resellers shows even screened-by-design hardware ends up in unscreened hands.

**Chokepoint status: this is the anti-chokepoint** — the channel that routes around both the consumable lock and the manufacturer.

### 3.5 Spare parts and à-la-carte reagents

A standing webshop (OligoMaker CPH) sells the components to build/repair a synthesizer — PEEK manifolds, reagent valves, seals, deprotection-box parts — **and** a dedicated amidite/consumables category, open cart-and-checkout, no visible gating. Whole instruments are enquiry-only (a logistics gate, not a screening gate).

**Chokepoint status: NONE** — the parts-and-reagents aftermarket means even a cartridge-locked or out-of-warranty instrument can be kept running outside the vendor relationship, further eroding the consumable lever.

## 4. Chokepoint summary (benchtop)

| Input category | Durable standalone control? |
|---|---|
| **Proprietary reagent cartridges/consumables** | **Yes** — licensed, KYC-able (the strongest benchtop lever) |
| **Device manufacturer (on-device screening)** | **Yes for new in-jurisdiction devices** — but ~8/34 reach + ~35% legacy base |
| GMP/standard phosphoramidites + kits | No (commodity; see phosphoramidite doc) |
| **Secondary / used-device market** | **No — actively erodes the two levers above** |
| Spare parts + à-la-carte reagents | No — sustains instruments outside the vendor relationship |

## 5. Governance verdict — and the DIY contrast

Benchtop is the **only** part of the synthesis landscape with real input-level chokepoints: a proprietary consumable that can be tracked, and a manufacturer that can screen at source. That makes benchtop *more* governable than DIY at first sale — the enzymatic and closed-column instruments genuinely can be gated at the cartridge and the firmware.

But the levers are **first-sale levers**, and the market is not a first-sale market. Resale, cross-border shipping, the legacy installed base, and an open spare-parts/reagent aftermarket together mean a determined actor reaches benchtop capability *without* touching the controllable inputs. The consumable lock assumes the vendor stays in the loop; the used market and parts webshops remove the vendor from the loop.

**The clean cross-document finding:**

- **DIY chain:** no durable input chokepoint (commodity chemistry + commodity hardware, save two narrow method-specific exceptions).
- **Benchtop chain:** two real input chokepoints (proprietary consumable + manufacturer) — **leaked by resale and aftermarket.**
- **Therefore:** input/supply control is a dead end for DIY and only a *partial, first-sale* lever for benchtop. Durable control belongs at on-device screening (for compliant new devices), record-retention, and post-hoc attribution — with international harmonisation load-bearing because the manufacturer lever is jurisdictionally capped.

## 6. Open items to verify before finalising

- Confirm which current benchtops are genuinely cartridge-locked vs open-reagent (SYNTAX and Kilobaser are cartridge/chip-based; verify the column-benchtop reagent-kit lock-in claim per vendor).
- Whether any secondary market exists for the proprietary *cartridges themselves* (would further weaken the consumable lever) — currently unassessed.
- The 34-firm / 8-of-34 reach figures are carried from the ERA/IBBIS inventory — cite that inventory as the source, consistent with your updated Chapter 1 and IBBIS summary.

*References carried from Chapter 2, the Secondary-Market brief, and the Phosphoramidite assessment: IFP/Langenkamp 2024 (Securing Benchtop DNA Synthesizers); NTI 2023; DNA Script SYNTAX; Telesis Bio / Codex DNA disclosures; OligoMaker CPH listings.*
