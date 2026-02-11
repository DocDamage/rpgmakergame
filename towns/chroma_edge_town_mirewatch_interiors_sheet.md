# Chroma's Edge - Mirewatch Interiors Sheet (v1)
## Build-Ready Interior Layouts + Services + Phase Behaviors

---

## 0) Global Interior Rules (All Mirewatch Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Narrow, readable lanes with no deadlock corners |
| **Lighting (Day)** | Humid amber lantern wash + soft teal spore accents |
| **Lighting (Night)** | Heavier fog planes + stronger lamp contrast |
| **Ambient Audio** | Drip loops, rope creak, distant fan hum |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear spawn buffer |

---

## 1) THE LANTERN & REED (Inn)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(52, 66)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Front Desk** | x 12-18, y 11-13 | Rest/save service anchor |
| **Common Tables** | x 6-23, y 6-10 | Rumor and flavor seating |
| **Back Hall** | x 23-28, y 12-18 | Decorative room access |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(15, 12)` | Rest + save |
| **Rumor board** | `(7, 12)` | Regional hints |
| **Dry rack** | `(22, 8)` | 1/day minor recovery item |

### D) Exit Trigger

| Exit | Coordinates |
|------|-------------|
| **Return to Mirewatch** | `(15, 19)` |

---

## 2) SPOREHOUSE CLINIC

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 24 tiles |
| **Exterior Door** | Town door `(88, 58)` |
| **Interior Entry Pad** | `(17, 22)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Clinic Counter** | x 14-20, y 14-16 | Core service lane |
| **Triage Bed - Left** | x 5-11, y 7-10 | Treatment prop |
| **Triage Bed - Right** | x 23-29, y 7-10 | Treatment prop |
| **Salt Fan Wall** | x 2-6, y 3-11 | Motion/mechanical foreshadow |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(17, 15)` | Poison/sleep/dizzy cures |
| **Medicine cabinet** | `(4, 4)` | 1/day antidote pickup |
| **Triage ledger** | `(27, 14)` | Quest progress text |

### D) Exit Trigger

| Exit | Coordinates |
|------|-------------|
| **Return to Mirewatch** | `(17, 23)` |

---

## 3) SALT & STITCH (General Goods)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(70, 84)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Vendor Counter** | x 11-17, y 10-12 | Purchase lane |
| **Supply Shelves** | x 3-8, y 4-12 | Consumable props |
| **Bridge Kit Stack** | x 20-26, y 5-13 | Rope/filter stock |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Shop menu** | `(14, 11)` | Potions, rope kits, filters |
| **Route board** | `(5, 6)` | Travel hints |
| **Reserve crate** | `(23, 12)` | PHASE 2 sidequest unlock |

### D) Exit Trigger

| Exit | Coordinates |
|------|-------------|
| **Return to Mirewatch** | `(14, 17)` |

---

## 4) BITTERCAP BENCH (Alchemy Stall Interior)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 24 x 16 tiles |
| **Exterior Door** | Town door `(82, 86)` |
| **Interior Entry Pad** | `(12, 14)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Alchemy Counter** | x 9-15, y 9-11 | Core vendor anchor |
| **Drying Rack Wall** | x 2-6, y 3-11 | Herb prep props |
| **Glass Rack** | x 17-22, y 4-12 | Potion vessel props |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Alchemy menu** | `(12, 10)` | Antidotes and tonics |
| **Formula slate** | `(4, 6)` | Recipe tips |
| **Infusion pot** | `(20, 8)` | Flavor interaction |

### D) Exit Trigger

| Exit | Coordinates |
|------|-------------|
| **Return to Mirewatch** | `(12, 15)` |

---

## 5) FILTERWRIGHT'S SHED (Craft)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 18 tiles |
| **Exterior Door** | Town door `(60, 82)` |
| **Interior Entry Pad** | `(16, 16)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Main Bench** | x 12-20, y 8-10 | Crafting anchor |
| **Tool Wall** | x 3-8, y 3-12 | Mechanical props |
| **Filter Bins** | x 22-30, y 7-13 | Material storage |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Craft menu** | `(16, 9)` | Filters, anti-toxin wraps |
| **Upgrade stand** | `(25, 9)` | PHASE 2+ craft tier |
| **Design board** | `(5, 8)` | Slipstep hints |

### D) Exit Trigger

| Exit | Coordinates |
|------|-------------|
| **Return to Mirewatch** | `(16, 17)` |

---

## 6) FOG CHAPEL (Optional Quiet Hut)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 18 x 14 tiles |
| **Exterior Access** | Prompt near Fog Shanties altar marker `(24, 68)` |
| **Interior Entry Pad** | `(9, 12)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Respect altar** | `(9, 6)` | Character beat trigger |
| **Offering tray** | `(9, 9)` | Sidequest target |
| **Wall inscription** | `(4, 6)` | Lore line |

### C) Exit Trigger

| Exit | Coordinates |
|------|-------------|
| **Return to Mirewatch shanties** | `(9, 13)` |

---

## 7) Terminal + Utility Nook (Optional)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 20 x 14 tiles |
| **Exterior Access** | Prompt at terminal tile `(86, 56)` |
| **Interior Entry Pad** | `(10, 12)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Mirewatch terminal interface** | `(10, 6)` | Route intel and seam status |
| **Wind-reading panel** | `(5, 8)` | Unlocks post-D2 text updates |
| **Maintenance crate** | `(15, 9)` | Small material pickup |

### C) Exit Trigger

| Exit | Coordinates |
|------|-------------|
| **Return to Mirewatch terminal pad** | `(10, 13)` |

---

## 8) Day/Night + Phase Service Changes

| Phase | Change |
|-------|--------|
| **PHASE 0** | Terminal locked; base clinic and craft lists only |
| **PHASE 1** | Broken speaker static lines; suspicious stranger appears at night |
| **PHASE 2** (`D2_CLEARED`) | Clinic/Filterwright expansion + Ventwright availability |
| **PHASE 3** (`D3_CLEARED`) | Stable hitch support and mount cosmetics |
| **PHASE 4** | Reduced civilian night schedule and stronger guard flavor |

---

## 9) Interior-to-Quest Hook Map

| Interior | Main Hook |
|----------|-----------|
| **Lantern & Reed** | Main rest loop + route rumor updates |
| **Sporehouse Clinic** | "Breathing Below" prep and status education |
| **Salt & Stitch** | Early economy + Salt Line Repair support |
| **Bittercap Bench** | Antidote economy and tonic progression |
| **Filterwright's Shed** | D2 craft progression and Slipstep prep |
| **Fog Chapel** | Character reflection and lore |
| **Terminal Nook** | Wind-reading updates and route diagnostics |

---

## Quick Reference

```text
LANTERN & REED      30x20  door (52,66)  pad (15,18)
SPOREHOUSE CLINIC   34x24  door (88,58)  pad (17,22)
SALT & STITCH       28x18  door (70,84)  pad (14,16)
BITTERCAP BENCH     24x16  door (82,86)  pad (12,14)
FILTERWRIGHT SHED   32x18  door (60,82)  pad (16,16)
FOG CHAPEL          18x14  access (24,68) pad (9,12)
TERMINAL NOOK       20x14  access (86,56) pad (10,12)
```
