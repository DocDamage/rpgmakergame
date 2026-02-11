# Chroma's Edge — Endgame Overworld "Eclipse State" Design Doc (v1)
## Post-D8 World Changes — "The World Stopped Agreeing With Itself"

---

## Implementation Reference

For final trigger and flag wiring plus post-R17 integration, use:
`chroma_edge_endgame_overworld_overlay_finalization.md`

---

## 0) World State Overview

| Parameter | Value |
|-----------|-------|
| **World State Name** | ECLIPSE ROUTES |
| **Trigger Flag** | `RELIC_SHADOW_SEATED = TRUE` |
| **Primary New Field Tech** | SHADOWWALK (plus "Unseen" detection) |
| **Tone Shift** | The world feels "edited" — seams in reality, hidden layers exposed |

---

## 1) Global Overworld Rules (Post-D8)

### A) Eclipse Seams (New Traversal Layer)

| Property | Description |
|----------|-------------|
| **Visual** | Thin black "stitch lines" on overworld |
| **Access** | Crossable **only** with Shadowwalk |
| **Function** | Shortcuts + hidden access gates (not random portals) |
| **Placement** | Strategic connections between regions, not everywhere |

### B) Unseen Caches (Hidden Pickups)

| Property | Description |
|----------|-------------|
| **Visual** | Dark glint nodes |
| **Locations** | Cliff bases, behind old barricades, "wrong-shadow" tiles near ruins |
| **Type** | Quick interact nodes (not chests — keeps pacing tight) |
| **Contents** | High-tier mats, consumables, lore fragments |

### C) Encounter Tier Shift (Endgame Tuning)

| Aspect | Change |
|--------|--------|
| **Eclipse Zones** | +1 tier (new enemy variants) |
| **Towns** | Remain safe |
| **Fringe Edges** | Non-combat tension props (fog, watchers) near town exits |

### D) Eclipse Cycle (Recommended)

**Simple 3-state rotation** (triggers on rest OR after X battles):

| State | Visual | Encounter Effect |
|-------|--------|------------------|
| **Clear** | Normal visibility | Normal encounters |
| **Veil** | Heavier fog | Higher ambush chance |
| **Eclipse** | Seams glow | Elite chances up; Unseen caches more likely to spawn |

---

## 2) New Overworld Nodes (Post-D8)

### A) Eclipse Confluence (Endgame Hub)

| Property | Value |
|----------|-------|
| **Visual** | Black "knot" where multiple seams intersect |
| **Function** | Late-game connector + optional boss gate |
| **Unlock** | First time you Shadowwalk through any seam, it pings on map |
| **Terminal Access** | Yes — full seam routing network |

### B) Unseen Vaults (Mini-Dungeons ×3)

**Small 1–2 submap challenge rooms (20–30 minutes each)**

| Vault | Theme | Location | Reward |
|-------|-------|----------|--------|
| **Vault of Quiet Glass** | Time-leaning | Near Rimehold seam endpoint | Relic amplifier / endgame mats |
| **Vault of Boneweight** | Mass-leaning | Near Gravemark seam endpoint | Relic amplifier / endgame mats |
| **Vault of Deep Salt** | Tide-leaning | Near Brinegate seam endpoint | Relic amplifier / endgame mats |

**Gating:** Each vault gated by Shadow seam

### C) Final Route Gate (To True Finale)

| Requirement | Description |
|-------------|-------------|
| **Shadow seated** | TRUE |
| **Other foundations** | Seated (if enforcing) |
| **Crown Sigil/Core** | One final key (optional gating) |
| **Visual** | Stabilized "world gate" seam |

---

## 3) Region-by-Region Changes

### Chronowake / Time Coast

| Change | Description |
|--------|-------------|
| **New Seam** | Chronowake Pier → Eclipse Confluence (short hop) |
| **Night Effect** | Buoys ping in "wrong rhythm" (flavor) |
| **Hidden Cache Lane** | Along sea wall walk (Unseen glints) |

### Old Lumencrest (Ruined Capital)

| Change | Description |
|--------|-------------|
| **Crown District Overlay** | "Shadow channel stabilized" visual update |
| **New Seam** | Mirror Plaza (Outer Wards) → Spire Shadow Line (leads to vault) |
| **Grand Boulevard** | Elites spawn during Eclipse cycle only |

### Rimehold / Frozen Fields

| Change | Description |
|--------|-------------|
| **New Seam** | Rime Causeway cliffside → Vault of Quiet Glass |
| **Eclipse Effect** | "Time-snow falling upward" more frequent (tone payoff) |

### Gravemark / Sable Expanse

| Change | Description |
|--------|-------------|
| **New Seam** | Near Gravemark stabilizer rigs → Vault of Boneweight |
| **Dragon's Graveyard** | One post-D8 Unseen pocket (short hallway, not full map) |

### Brinegate / Coast

| Change | Description |
|--------|-------------|
| **New Seam** | Brinegate harbor edge → Vault of Deep Salt |
| **Sea Nodes** | Show "black current lines" (visual only unless functional) |

### Early Game Regions (Dusthaven / Ashveil / Mirewatch / Prismridge / Cinderstep)

**Simple, non-invasive changes:**

| Change | Description |
|--------|-------------|
| **1 Small Seam Each** | Leads to cache pocket OR shortcut connector to midgame road |
| **Purpose** | Late-game traversal QoL + makes revisits feel rewarded |

---

## 4) Overworld Map UI Updates

### Toggle Filters

| Toggle | Function |
|--------|----------|
| `[ ] Show Eclipse Seams` | Displays seam gates on map |
| `[ ] Show Unseen Caches` | Appears once Shadowwalk learned |

### Icons

| Icon | Meaning |
|------|---------|
| **Thin black "stitch"** | Seam Gate |
| **Hollow black diamond** | Vault |

---

## 5) Fast Travel / Terminal Network (Post-D8 Payoff)

### A) New Terminal Feature: "Seam Routing"

**Terminals** (Meridian / Chronowake / Crown District) can now:

| Function | Description |
|----------|-------------|
| **Highlight nearest seam gate** | Navigation aid |
| **Show cleared vaults** | Completion tracking |
| **Show Eclipse Cycle state** | Plan travel timing |

### B) New Fast Travel Rule (Optional)

| Property | Description |
|----------|-------------|
| **Unlock** | Once you've stepped through a seam once |
| **Function** | Fast travel between seam gates at terminals |
| **Cost** | Credits OR "Umbral Charge" consumable |

---

## 6) Shadowwalk Mechanics (Overworld Version)

### What Shadowwalk Can Pass Through

| Barrier | Passable? |
|---------|-----------|
| Thin barricades (fences, broken walls) | ✅ Yes |
| Seam gates | ✅ Yes |
| Shadow doors (subtle shimmer mark) | ✅ Yes |
| Solid cliffs | ❌ No |
| Major story gates | ❌ No (unless flagged) |

### Shadowwalk Cost (Pick One)

| Option | Description |
|--------|-------------|
| **A (Simple)** | Cooldown per screen (no resource) |
| **B (RPG)** | Consumes 1 Umbral Charge; recharged by rest or Stillpoint wells |

---

## 7) Endgame Overworld Additions (Optional)

### A) Elite Hunts (3 Roaming Endgame Enemies)

**Spawn only during Eclipse cycle in specific routes:**

| Elite | Location | Reward |
|-------|----------|--------|
| **The Surveyor That Wasn't** | Chronowake coast | Relic amplifier mats + unique accessory |
| **The Crownless Prefect** | Grand Boulevard | Relic amplifier mats + unique accessory |
| **The Boneweight Herald** | Sable Expanse | Relic amplifier mats + unique accessory |

### B) Relic Amplifiers (Endgame Crafting)

**Each vault gives "Amplifier Core" upgrading one Foundation:**

| Foundation | Amplifier Effect |
|------------|------------------|
| **Tide** | Currents calmer / oxygen drain reduced |
| **Mass** | Overworld hazard slow reduced / rubble clears easier |
| **Time** | Phase flicker hazards reduced / extra phase key |
| **Shadow** | More Unseen caches / lower ambush |

---

## 8) Implementation Checklist (10 Concrete Tasks)

| # | Task | Region |
|---|------|--------|
| 1 | Add Eclipse Seam Gate at Chronowake (right edge) | Chronowake |
| 2 | Add Seam Gate at Meridian outskirts (north-west) | Meridian |
| 3 | Add Seam Gate at Gravemark stabilizer ridge | Gravemark |
| 4 | Add Seam Gate at Brinegate breakwater | Brinegate |
| 5 | Add Seam Gate at Rime Causeway cliff | Rimehold |
| 6 | Add Eclipse Confluence node (center-late map) | Overworld |
| 7 | Add Vault of Quiet Glass near Rimehold seam | Rimehold |
| 8 | Add Vault of Boneweight near Gravemark seam | Gravemark |
| 9 | Add Vault of Deep Salt near Brinegate seam | Brinegate |
| 10 | Add Unseen Cache overlay (5–8 caches across older routes) | Global |

---

## Quick Reference: Eclipse State Summary

```
TRIGGER: D8 Complete + Shadow Relic Seated

NEW MECHANICS:
├─ Shadowwalk (pass barriers + seams)
├─ Eclipse Seams (shortcuts + vault access)
├─ Unseen Caches (hidden pickups)
└─ Eclipse Cycle (Clear → Veil → Eclipse)

NEW LOCATIONS:
├─ Eclipse Confluence (endgame hub)
├─ Vault of Quiet Glass (Time)
├─ Vault of Boneweight (Mass)
├─ Vault of Deep Salt (Tide)
└─ Final Route Gate (to finale)

WORLD CHANGES:
├─ Early regions: 1 seam each (QoL)
├─ Mid regions: New shortcuts + caches
├─ Late regions: Vault access + elite hunts
└─ All terminals: Seam routing feature

REPLAY VALUE:
├─ Relic Amplifiers (4 upgrade paths)
├─ Elite Hunts (3 roaming bosses)
├─ Unseen Cache hunting (5–8 nodes)
└─ Eclipse Cycle timing optimization
```

---

## Lore Integration

**Central Theme:** *"The world stopped agreeing with itself."*

- Eclipse Seams are "reality stitches" — places where the Shadow Foundation revealed the world's fragility
- Unseen Caches are "what was always there but hidden"
- The Eclipse Cycle represents the world's unstable attempt to reconcile Shadow with the other Foundations
- Shadowwalk is not "invisibility" — it's "walking in the gaps between agreements"
