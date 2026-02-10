# Chroma's Edge - Brinegate Port Interiors Sheet (v1)
## Build-Ready Interior Layouts + Dive/Ferry Service Flow

---

## 0) Global Interior Rules (All Brinegate Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Wide dock-adjacent entries, clear lanes around props |
| **Lighting (Day)** | Diffuse overcast + warm storm lamps |
| **Lighting (Night)** | Strong lamp pools, low ambient, reflective wet surfaces |
| **Audio Bed** | Surf impact, rigging creak, buoy bell pulses |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear landing zone |

---

## 1) THE BREAKWATER LANTERN (Inn)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 22 tiles |
| **Exterior Door** | Town door `(74, 74)` |
| **Interior Entry Pad** | `(16, 20)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(16, 13)` | Rest + save |
| **Rumor wall** | `(7, 12)` | D5 and ferry hints |
| **Storm map** | `(24, 9)` | Flavor interaction |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(16, 21)` |

---

## 2) DEEPWRIGHT OUTFITTERS (Dive Shop)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 36 x 24 tiles |
| **Exterior Door** | Town door `(28, 66)` |
| **Interior Entry Pad** | `(18, 22)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Dive Counter** | x 15-21, y 13-15 | Main service lane |
| **Pressure Rack** | x 3-9, y 6-15 | Pressure gear display |
| **Chart Wall** | x 25-33, y 6-15 | Route map and sea-node props |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Dive shop menu** | `(18, 14)` | Pressure patches and equalizers |
| **Chart table** | `(29, 9)` | Post-D5 sea route hooks |
| **Prep locker** | `(6, 10)` | Sidequest item source |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(18, 23)` |

---

## 3) BRINE MEDIC STATION (Clinic)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(20, 58)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(15, 12)` | Poison/silence/pressure cures |
| **Salt cabinet** | `(5, 4)` | 1/day cure item |
| **Triage ledger** | `(23, 11)` | Quest text and flavor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(15, 19)` |

---

## 4) ROPE & RATION (General Goods)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(90, 58)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **General shop menu** | `(15, 12)` | Core consumables |
| **Supply board** | `(6, 6)` | Trade and route notes |
| **Dock crate** | `(24, 12)` | Sidequest dependency |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(15, 19)` |

---

## 5) HARBOR OFFICE / FERRY TICKETS

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(104, 78)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Ferry route desk** | `(14, 10)` | Route UI and ticketing |
| **Weather board** | `(20, 7)` | Delay and timing flavor |
| **Manifest shelf** | `(6, 8)` | Story and sidequest hooks |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(14, 17)` |

---

## 6) HULL & HOOK (Shipwright Bench)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 20 tiles |
| **Exterior Door** | Town door `(44, 58)` |
| **Interior Entry Pad** | `(17, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Shipwright craft menu** | `(17, 12)` | Rope, sealant, storm lamp crafts |
| **Hull table** | `(27, 10)` | Upgrade and mat conversion anchor |
| **Dock plans rack** | `(6, 8)` | Sea-node prep hints |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(17, 19)` |

---

## 7) QUIET TIDE CHAPEL + CUSTOMS OFFICE

### A) Quiet Tide Chapel

| Parameter | Value |
|-----------|-------|
| **Map Size** | 24 x 18 tiles |
| **Exterior Door** | Town door `(34, 34)` |
| **Interior Entry Pad** | `(12, 16)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Rite prompt** | `(12, 8)` | Character beat and blessing hook |
| **Offering tray** | `(12, 11)` | Sidequest interaction |
| **Tide inscription** | `(5, 7)` | Lore text |

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(12, 17)` |

### B) Customs Office

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 16 tiles |
| **Exterior Door** | Town door `(10, 78)` |
| **Interior Entry Pad** | `(11, 14)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inspection desk** | `(11, 8)` | Permit pressure branch |
| **Confiscation locker** | `(16, 8)` | Sidequest objective |
| **Posted rules wall** | `(5, 6)` | Dominion pressure flavor |

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate** | `(11, 15)` |

---

## 8) Terminal Alcove (Optional Tech Nook)

| Parameter | Value |
|-----------|-------|
| **Map Size** | 18 x 14 tiles |
| **Exterior Access** | Prompt at terminal tile `(88, 44)` |
| **Interior Entry Pad** | `(9, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Terminal interface** | `(9, 6)` | Sea-node and route diagnostics |
| **Sonar panel** | `(4, 8)` | Post-D5 node ping tutorial |

| Exit | Coordinates |
|------|-------------|
| **Return to Brinegate terminal pad** | `(9, 13)` |

---

## 9) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Core services active, minimal customs pressure |
| **PHASE 1** | Customs lines and permit friction increase |
| **PHASE 2** (`D5_CLEARED`) | Dive shop and terminal unlock sea-node features |
| **PHASE 3+** | Ferry economy expands and route services improve |

| Interior | Main Hook |
|----------|-----------|
| **Breakwater Lantern** | Rest loop and D5 rumor cadence |
| **Deepwright Outfitters** | Dive prep and aquatic progression |
| **Harbor Office** | Ferry route unlock path |
| **Hull & Hook** | Shipwright crafting and upgrade flow |
| **Customs Office** | Dominion pressure branch |

---

## Quick Reference

```text
BREAKWATER LANTERN  32x22  door (74,74)  pad (16,20)
DEEPWRIGHT SHOP     36x24  door (28,66)  pad (18,22)
BRINE MEDIC         30x20  door (20,58)  pad (15,18)
ROPE & RATION       30x20  door (90,58)  pad (15,18)
HARBOR OFFICE       28x18  door (104,78) pad (14,16)
HULL & HOOK         34x20  door (44,58)  pad (17,18)
QUIET TIDE CHAPEL   24x18  door (34,34)  pad (12,16)
CUSTOMS OFFICE      22x16  door (10,78)  pad (11,14)
TERMINAL ALCOVE     18x14  access (88,44) pad (9,12)
```
