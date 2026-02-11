# Chroma's Edge - Prismridge Interiors Sheet (v1)
## Build-Ready Interior Layouts + Mount Hub Integration

---

## 0) Global Interior Rules (All Prismridge Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Clean lanes, low clutter in main route corridors |
| **Lighting (Day)** | Cool white with prismatic highlights |
| **Lighting (Night)** | Reduced ambient light, stronger lamp refraction accents |
| **Audio Bed** | Glass chime loops + distant mining resonance |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear landing space |

---

## 1) THE GLASS LULLABY (Inn)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 22 tiles |
| **Exterior Door** | Town door `(60, 86)` |
| **Interior Entry Pad** | `(16, 20)` |

### B) Key Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Front Desk** | x 13-19, y 12-14 | Rest and save service anchor |
| **Common Seating** | x 6-25, y 7-11 | Rumor and scene staging |
| **Back Corridor** | x 24-30, y 13-20 | Decorative room access |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(16, 13)` | Rest + save |
| **Rumor placard** | `(7, 12)` | D3 and mount hints |
| **Prism lantern stand** | `(24, 9)` | Flavor interaction |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Prismridge** | `(16, 21)` |

---

## 2) STONE & SHINE (General Goods)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(72, 82)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Vendor Counter** | x 12-18, y 11-13 | Main purchase lane |
| **Supply Shelves** | x 3-9, y 4-13 | Consumable stock |
| **Field Kit Rack** | x 20-27, y 6-14 | Rope/filter utility items |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Shop menu** | `(15, 12)` | Consumables and utility gear |
| **Notice board** | `(6, 6)` | Route economy tips |
| **Reserve crate** | `(24, 12)` | PHASE 2+ sidequest unlock |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Prismridge** | `(15, 19)` |

---

## 3) REFRACTION WORKS (Lenswright Shop)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 22 tiles |
| **Exterior Door** | Town door `(22, 40)` |
| **Interior Entry Pad** | `(17, 20)` |

### B) Key Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Calibration Bench** | x 13-21, y 8-10 | Signature tech station |
| **Accessory Counter** | x 12-18, y 12-14 | Sales anchor |
| **Lens Rack Wall** | x 3-8, y 4-13 | Light resist and utility props |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Lenswright menu** | `(17, 13)` | Accessories and light utility items |
| **Calibration UI prompt** | `(17, 9)` | Scene and tutorial anchor |
| **Static monitor** | `(5, 6)` | Lore ping hook |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Prismridge** | `(17, 21)` |

---

## 4) PICK & EDGE (Weapons and Mining Tools)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(84, 76)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Upgrade Bench** | x 12-18, y 8-10 | Upgrade interaction |
| **Tool Wall** | x 3-8, y 4-13 | Mining gear props |
| **Hardened Crate Stack** | x 20-27, y 6-14 | Material storage |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Upgrade menu** | `(15, 9)` | Weapon and tool upgrades |
| **Order ledger** | `(5, 8)` | Craft hints |
| **Sharpening wheel** | `(24, 9)` | Flavor interaction |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Prismridge** | `(15, 19)` |

---

## 5) CLEARWATER STATION (Clinic)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(46, 86)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Clinic Counter** | x 12-18, y 11-13 | Service lane |
| **Triage Cot Left** | x 4-9, y 6-8 | Patient prop |
| **Triage Cot Right** | x 20-25, y 6-8 | Patient prop |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(15, 12)` | Blinded and bleed support |
| **Med shelf** | `(5, 4)` | 1/day recovery item |
| **Patient log** | `(23, 11)` | Flavor + sidequest hook |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Prismridge** | `(15, 19)` |

---

## 6) PRISM CORRAL (Stable HQ)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 36 x 26 tiles |
| **Exterior Door** | Town door `(18, 70)` |
| **Interior Entry Pad** | `(18, 24)` |

### B) Key Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Roster Desk** | x 15-21, y 14-16 | Mount roster interaction |
| **Training Ring** | x 10-26, y 6-13 | Tutorial and bond visuals |
| **Stall Row** | x 2-8 and x 28-34, y 7-19 | Stable props |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Stable UI** | `(18, 15)` | Mount select/rename/cosmetics |
| **Bond board** | `(8, 10)` | Bond upgrade tips |
| **Tack rack** | `(30, 10)` | Mount gear module interaction |

### D) Gate Behavior

| State | Behavior |
|-------|----------|
| **Pre-D3** | Interior available as limited shell with minimal interactions |
| **Post-D3** | Full stable feature set enabled |

### E) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Prismridge** | `(18, 25)` |

---

## 7) FOREMAN OFFICE (Mineworks)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(96, 20)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Permit desk** | `(14, 10)` | D3 progression gate |
| **Route board** | `(20, 7)` | Mineworks hints |
| **Survey file cabinet** | `(6, 8)` | Dominion tension flavor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Prismridge** | `(14, 17)` |

---

## 8) Beast Handler Office + Terminal Nook (Optional Pair)

### A) Beast Handler Office

| Parameter | Value |
|-----------|-------|
| **Map Size** | 20 x 14 tiles |
| **Exterior Door** | Town door `(12, 78)` |
| **Interior Entry Pad** | `(10, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Contract board** | `(10, 6)` | Taming contracts |
| **Capture crate** | `(5, 8)` | Contract reward stash |

### B) Terminal Nook

| Parameter | Value |
|-----------|-------|
| **Map Size** | 20 x 14 tiles |
| **Exterior Access** | Prompt at terminal tile `(24, 28)` |
| **Interior Entry Pad** | `(10, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Terminal interface** | `(10, 6)` | Route intel and anomaly pings |
| **Gleam panel** | `(5, 8)` | Post-D3 secret cue |

---

## 9) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Stable and Beast Handler limited/closed |
| **PHASE 1** | Permit pressure lines added in Foreman Office |
| **PHASE 2** (`D3_CLEARED`) | Stable full unlock + Lenswright expansion |
| **PHASE 3+** | Inspector flavor increases, mine offices tighten |

| Interior | Main Hook |
|----------|-----------|
| **Glass Lullaby** | Rest loop and party rumor pacing |
| **Refraction Works** | Light utility and anomaly flavor |
| **Prism Corral** | Mount system HQ |
| **Foreman Office** | D3 progression and permit tension |
| **Clearwater Station** | Blinded and bleed support |

---

## Quick Reference

```text
GLASS LULLABY        32x22  door (60,86)  pad (16,20)
STONE & SHINE        30x20  door (72,82)  pad (15,18)
REFRACTION WORKS     34x22  door (22,40)  pad (17,20)
PICK & EDGE          30x20  door (84,76)  pad (15,18)
CLEARWATER STATION   30x20  door (46,86)  pad (15,18)
PRISM CORRAL         36x26  door (18,70)  pad (18,24)
FOREMAN OFFICE       28x18  door (96,20)  pad (14,16)
BEAST HANDLER OFFICE 20x14  door (12,78)  pad (10,12)
TERMINAL NOOK        20x14  access (24,28) pad (10,12)
```
