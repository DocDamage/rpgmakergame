# Chroma's Edge - Chronowake Pier Interiors Sheet (v1)
## Build-Ready Interior Layouts + Time-Lane Ferry Hub

---

## 0) Global Interior Rules (All Chronowake Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Open concourse-adjacent entries, narrow service lanes only where intentional |
| **Lighting (Day)** | Cool dock ambient + warm lamp accents |
| **Lighting (Night)** | Heavy fog overlays with bright chrono buoy highlights |
| **Audio Bed** | Buoy pings, surf, wood creak, intermittent time-skip stutter |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear spawn lane |

---

## 1) THE WAKE & WICKER (Inn)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 22 tiles |
| **Exterior Door** | Town door `(26, 74)` |
| **Interior Entry Pad** | `(17, 20)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(17, 13)` | Rest + save |
| **Story board** | `(8, 12)` | Time-route rumor lines |
| **Wet coat rack** | `(26, 9)` | Flavor interaction |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake** | `(17, 21)` |

---

## 2) SALTCLOCK SUPPLY (General Goods)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(54, 74)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **General shop menu** | `(14, 11)` | Consumables and Clockseal items |
| **Route stock board** | `(6, 6)` | Travel hints |
| **Reserve crate** | `(23, 11)` | Sidequest target |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake** | `(14, 17)` |

---

## 3) TIDE & TIME AID (Clinic)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(40, 74)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(15, 12)` | Stasis and pressure support |
| **Aid cabinet** | `(5, 4)` | 1/day cure item |
| **Patient board** | `(23, 11)` | Sidequest flavor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake** | `(15, 19)` |

---

## 4) BUOY & BELL WORKSHOP (Timewright)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 36 x 24 tiles |
| **Exterior Door** | Town door `(24, 36)` |
| **Interior Entry Pad** | `(18, 22)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Timewright menu** | `(18, 14)` | Stasis balms and phase keys |
| **Calibration rig** | `(28, 10)` | Post-D7 upgrade anchor |
| **Buoy core rack** | `(6, 10)` | Quest hooks |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake** | `(18, 23)` |

---

## 5) HARBOR OFFICE / TICKET HALL

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(68, 34)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Ferry schedule desk** | `(15, 12)` | Route and ticket UI |
| **Arrival board** | `(24, 9)` | Wrong-time flavor + quest hooks |
| **Lane map** | `(7, 8)` | Phase-lane explanation |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake** | `(15, 19)` |

---

## 6) CHRONO COMPLIANCE OFFICE + KEEL & KNOT

### A) Chrono Compliance Office

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 16 tiles |
| **Exterior Door** | Town door `(84, 34)` |
| **Interior Entry Pad** | `(11, 14)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Compliance desk** | `(11, 8)` | Audit/permit branch |
| **Records locker** | `(16, 8)` | Sidequest marker |
| **Notice wall** | `(5, 6)` | Pressure flavor |

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake** | `(11, 15)` |

### B) Keel & Knot (Boat Repair)

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(14, 60)` |
| **Interior Entry Pad** | `(14, 16)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Repair bench menu** | `(14, 10)` | Nautical craft and utility gear |
| **Hull rack** | `(20, 8)` | Material conversion flavor |
| **Dock plans shelf** | `(6, 8)` | Sidequest hints |

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake** | `(14, 17)` |

---

## 7) Major Terminal Nook (Optional)

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 14 tiles |
| **Exterior Access** | Prompt at terminal tile `(64, 62)` |
| **Interior Entry Pad** | `(11, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Terminal interface** | `(11, 6)` | Full route diagnostics post-D7 |
| **Phase marker panel** | `(6, 8)` | Barrier marker tutorial |
| **Lane schedule strip** | `(16, 8)` | Time-lane unlock cues |

| Exit | Coordinates |
|------|-------------|
| **Return to Chronowake terminal pad** | `(11, 13)` |

---

## 8) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Core services active, terminal features limited |
| **PHASE 1** | Compliance pressure increases in customs interiors |
| **PHASE 2** (`D7_CLEARED`) | Terminal and Timewright systems fully expand |
| **PHASE 3+** | Time-lane ferry routes and hidden marker cues deepen |

| Interior | Main Hook |
|----------|-----------|
| **Wake & Wicker** | Rest loop and narrative pacing |
| **Buoy & Bell Workshop** | Timecraft upgrade center |
| **Harbor Office** | Ferry and lane routing UI |
| **Compliance Office** | Bureaucratic tension branch |
| **Terminal Nook** | Post-D7 route visualization |

---

## Quick Reference

```text
WAKE & WICKER        34x22  door (26,74)  pad (17,20)
SALTCLOCK SUPPLY     28x18  door (54,74)  pad (14,16)
TIDE & TIME AID      30x20  door (40,74)  pad (15,18)
BUOY & BELL SHOP     36x24  door (24,36)  pad (18,22)
HARBOR OFFICE        30x20  door (68,34)  pad (15,18)
COMPLIANCE OFFICE    22x16  door (84,34)  pad (11,14)
KEEL & KNOT          28x18  door (14,60)  pad (14,16)
TERMINAL NOOK        22x14  access (64,62) pad (11,12)
```
