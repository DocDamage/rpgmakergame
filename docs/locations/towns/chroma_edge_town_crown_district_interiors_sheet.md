# Chroma's Edge - Crown District Interiors Sheet (v1)
## Build-Ready Final Capital Interiors + Conduit Routing

---

## 0) Global Interior Rules (All Crown District Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Minimal clutter, high readability, ceremonial geometry |
| **Lighting (Day)** | Cold marble reflection with controlled warm service lights |
| **Lighting (Night)** | Strong wrong-sky bounce and seam accent glow |
| **Audio Bed** | Distant mechanism drones, hush ambience, occasional phase chime |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear spawn pocket |

---

## 1) CANDLE VAULT (Rest Chamber)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(72, 92)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Rest and save prompt** | `(14, 10)` | Rest loop and staging |
| **Stash chest** | `(22, 10)` | Inventory prep |
| **Character beat marker** | `(6, 8)` | Optional story scene |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Crown District** | `(14, 17)` |

---

## 2) QUIET MEND (Clinic Pod)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 24 x 16 tiles |
| **Exterior Door** | Town door `(86, 86)` |
| **Interior Entry Pad** | `(12, 14)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(12, 8)` | Late-game status support |
| **Med cabinet** | `(17, 8)` | 1/day aid item |
| **Prep board** | `(7, 7)` | Boss prep notes |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Crown District** | `(12, 15)` |

---

## 3) LAST SUPPLIES (Vendor Pod)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 26 x 16 tiles |
| **Exterior Door** | Town door `(58, 86)` |
| **Interior Entry Pad** | `(13, 14)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Vendor menu** | `(13, 8)` | Consumables and rare mat bundles |
| **Stock register** | `(18, 8)` | Inventory flavor |
| **Supply crate** | `(7, 7)` | Sidequest hook |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Crown District** | `(13, 15)` |

---

## 4) CROWN CONDUIT NODE ROOM (Terminal Interior)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 24 x 14 tiles |
| **Exterior Door** | Town door `(104, 46)` |
| **Interior Entry Pad** | `(12, 12)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Conduit terminal UI** | `(12, 7)` | Routing and seam intelligence |
| **Authorization feed** | `(17, 7)` | D8 gate prep |
| **Hidden ping panel** | `(7, 7)` | Post-D8 cache reveals |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Crown District** | `(12, 13)` |

---

## 5) RECORD GATE ANNEX (Authorization Room)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 14 tiles |
| **Exterior Door** | Town door `(112, 56)` |
| **Interior Entry Pad** | `(11, 12)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Authorization console** | `(11, 7)` | Archive key validation |
| **Record-state selector** | `(16, 7)` | OFFICIAL/ORIGINAL/REDACTED puzzle flavor |
| **Readout plaque** | `(6, 7)` | Lore text |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Crown District** | `(11, 13)` |

---

## 6) PALACE ANTECHAMBER (Optional Staging)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 22 tiles |
| **Exterior Door** | Town door `(88, 2)` |
| **Interior Entry Pad** | `(16, 20)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Final staging prompt** | `(16, 12)` | Palace readiness check |
| **Loadout shrine** | `(24, 10)` | Last prep interaction |
| **Regent inscription** | `(8, 9)` | Tone/lore anchor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Crown District** | `(16, 21)` |

---

## 7) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Core safe services active, conduit largely advisory |
| **PHASE 1** (`CROWN_ARCHIVE_KEY_ACQUIRED`) | Gate annex and conduit authorization flow active |
| **PHASE 2** (`D8_CLEARED`) | Terminal reveals eclipse routes and unseen cache pings |
| **PHASE 3** (`FINAL_ACT_OPEN`) | Palace antechamber staging fully active |

| Interior | Main Hook |
|----------|-----------|
| **Candle Vault** | Rest and character staging |
| **Quiet Mend** | Late-game hazard prep |
| **Conduit Node Room** | D8 and eclipse route control |
| **Record Gate Annex** | Key authorization and state logic |
| **Palace Antechamber** | Final-act commit corridor |

---

## Quick Reference

```text
CANDLE VAULT         28x18  door (72,92)  pad (14,16)
QUIET MEND           24x16  door (86,86)  pad (12,14)
LAST SUPPLIES        26x16  door (58,86)  pad (13,14)
CONDUIT NODE ROOM    24x14  door (104,46) pad (12,12)
RECORD GATE ANNEX    22x14  door (112,56) pad (11,12)
PALACE ANTECHAMBER   32x22  door (88,2)   pad (16,20)
```
