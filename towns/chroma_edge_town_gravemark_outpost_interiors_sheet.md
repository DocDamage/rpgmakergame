# Chroma's Edge - Gravemark Outpost Interiors Sheet (v1)
## Build-Ready Interior Layouts + Mass Economy Operations

---

## 0) Global Interior Rules (All Gravemark Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Industrial density with two clear movement lanes minimum |
| **Lighting (Day)** | Warm lamp pools + dusty neutral fill |
| **Lighting (Night)** | Lower ambient with deeper shadow pockets and amber rails |
| **Audio Bed** | Chain clinks, distant crane rumble, soft gravity hum |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear spawn pocket |

---

## 1) THE HEAVY BLANKET (Inn/Bunkhouse)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 20 tiles |
| **Exterior Door** | Town door `(52, 78)` |
| **Interior Entry Pad** | `(16, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(16, 12)` | Rest + save |
| **Stew board** | `(8, 12)` | Rumor and bounty hints |
| **Bunk ledger** | `(24, 8)` | Flavor interaction |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Gravemark** | `(16, 19)` |

---

## 2) ANVIL & ANCHOR (Forge)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 42 x 26 tiles |
| **Exterior Door** | Town door `(18, 62)` |
| **Interior Entry Pad** | `(21, 24)` |

### B) Key Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Main anvil lane** | x 17-25, y 10-13 | Upgrade anchor |
| **Temper station** | x 30-38, y 9-15 | Heavy upgrade tier |
| **Mass plate rack** | x 4-12, y 8-17 | Material storage |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Forge upgrade menu** | `(21, 12)` | Heavy-tier weapon/armor upgrades |
| **Anchor accessory bench** | `(33, 11)` | Anchor Step line (post-D6) |
| **Mass patch crate** | `(8, 11)` | Limited consumables |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Gravemark** | `(21, 25)` |

---

## 3) PLATE & PINION (Pressworks)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 20 tiles |
| **Exterior Door** | Town door `(28, 70)` |
| **Interior Entry Pad** | `(17, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Pressworks menu** | `(17, 12)` | Plating mods and belt gear |
| **Countermass bench** | `(26, 10)` | Knockback support line |
| **Press control panel** | `(6, 9)` | Flavor and sidequest hook |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Gravemark** | `(17, 19)` |

---

## 4) RATIONS & RIVETS (General Goods)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(66, 72)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **General shop menu** | `(15, 12)` | Consumables and basic gear |
| **Freight board** | `(6, 6)` | Route and shipment notes |
| **Store crate** | `(24, 12)` | Sidequest dependency |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Gravemark** | `(15, 19)` |

---

## 5) DUSTWARD AID (Clinic)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 18 tiles |
| **Exterior Door** | Town door `(62, 80)` |
| **Interior Entry Pad** | `(15, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(15, 11)` | Mass and bleed/burn support |
| **Aid cabinet** | `(5, 4)` | 1/day cure item |
| **Triage board** | `(23, 10)` | Quest flavor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Gravemark** | `(15, 17)` |

---

## 6) COUNTERWEIGHT STATION (Stabilizer Office)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(24, 30)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Stabilizer tutorial console** | `(14, 10)` | Mass lane and anchor-plate tutorial |
| **Calibration dial** | `(20, 8)` | Story gate interaction |
| **Rig log shelf** | `(6, 8)` | Sidequest text |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Gravemark** | `(14, 17)` |

---

## 7) Dominion Ledger Booth + Terminal Nook

### A) Dominion Ledger Booth

| Parameter | Value |
|-----------|-------|
| **Map Size** | 20 x 14 tiles |
| **Exterior Door** | Town door `(10, 78)` |
| **Interior Entry Pad** | `(10, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Ledger desk** | `(10, 7)` | Permit/bribe branch hooks |
| **Records cabinet** | `(15, 8)` | Sidequest target |
| **Compliance notice** | `(5, 6)` | Dominion pressure flavor |

| Exit | Coordinates |
|------|-------------|
| **Return to Gravemark** | `(10, 13)` |

### B) Terminal Nook

| Parameter | Value |
|-----------|-------|
| **Map Size** | 20 x 14 tiles |
| **Exterior Access** | Prompt at terminal tile `(26, 22)` |
| **Interior Entry Pad** | `(10, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Terminal interface** | `(10, 6)` | Route and gravity lane diagnostics |
| **Dragon route panel** | `(5, 8)` | Post-D6 hidden-route cue |

---

## 8) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Core services available, low Dominion pressure |
| **PHASE 1** | Ledger interactions and permit friction increase |
| **PHASE 2** (`D6_CLEARED`) | Forge/Pressworks high-tier unlocks activate |
| **PHASE 3+** | Hidden-route signals and gravity materials become prominent |

| Interior | Main Hook |
|----------|-----------|
| **Heavy Blanket** | Rest loop and worker rumor pacing |
| **Anvil & Anchor** | Mass-tier upgrade center |
| **Counterweight Station** | Mass mechanic explanation and gate support |
| **Ledger Booth** | Bureaucratic tension branch |
| **Terminal Nook** | Dragon's Graveyard breadcrumb |

---

## Quick Reference

```text
HEAVY BLANKET        32x20  door (52,78)  pad (16,18)
ANVIL & ANCHOR       42x26  door (18,62)  pad (21,24)
PLATE & PINION       34x20  door (28,70)  pad (17,18)
RATIONS & RIVETS     30x20  door (66,72)  pad (15,18)
DUSTWARD AID         30x18  door (62,80)  pad (15,16)
COUNTERWEIGHT STN    28x18  door (24,30)  pad (14,16)
LEDGER BOOTH         20x14  door (10,78)  pad (10,12)
TERMINAL NOOK        20x14  access (26,22) pad (10,12)
```
