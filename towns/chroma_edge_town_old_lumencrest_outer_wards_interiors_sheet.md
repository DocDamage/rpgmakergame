# Chroma's Edge - Old Lumencrest Outer Wards Interiors Sheet (v1)
## Build-Ready Capital Camp Interiors + Routing Support

---

## 0) Global Interior Rules (All Outer Wards Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Compact shelters with clear central navigation line |
| **Lighting (Day)** | Cold daylight bleed + warm tent lamps |
| **Lighting (Night)** | Lower fill, stronger cyan relay and wrong-sky bounce |
| **Audio Bed** | Wind through broken rails, tarp flutter, distant city hum |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear spawn lane |

---

## 1) RELAY CAMP TENT (Vendor and Contracts)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 22 tiles |
| **Exterior Door** | Town door `(66, 78)` |
| **Interior Entry Pad** | `(17, 20)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Vendor menu (Kett)** | `(17, 13)` | Main camp shop |
| **Contract board UI** | `(8, 12)` | Contracts and turn-ins |
| **Rumor map** | `(26, 10)` | Route hints |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Outer Wards** | `(17, 21)` |

---

## 2) PATCHHOUSE CLINIC

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 18 tiles |
| **Exterior Door** | Town door `(80, 78)` |
| **Interior Entry Pad** | `(15, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(15, 11)` | Pressure/Stasis/Overheat support |
| **Med cabinet** | `(5, 4)` | 1/day aid item |
| **Triage ledger** | `(23, 10)` | Story and sidequest hooks |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Outer Wards** | `(15, 17)` |

---

## 3) CANDLECELL SHELTER (Rest)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(74, 84)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Rest and save prompt** | `(14, 10)` | Rest loop support |
| **Stash chest** | `(22, 10)` | Optional stash |
| **Memory wall** | `(6, 8)` | Character beat trigger |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Outer Wards** | `(14, 17)` |

---

## 4) RELAY BUNKER (Terminal Room)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 24 x 16 tiles |
| **Exterior Door** | Town door `(70, 62)` |
| **Interior Entry Pad** | `(12, 14)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Relay terminal UI** | `(12, 8)` | Route pings and advisories |
| **Signal monitor** | `(17, 8)` | Hidden marker cues |
| **Warning panel** | `(7, 7)` | Flavor and safety text |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Outer Wards** | `(12, 15)` |

---

## 5) BOLT & BIND WORKSHOP

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 18 tiles |
| **Exterior Door** | Town door `(92, 80)` |
| **Interior Entry Pad** | `(15, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Workshop menu** | `(15, 11)` | Basic upgrades and conversion |
| **Seal-cutter bench** | `(23, 10)` | Utility unlock support |
| **Parts shelf** | `(6, 8)` | Craft flavor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Outer Wards** | `(15, 17)` |

---

## 6) QUARANTINE OFFICE RUIN (Optional)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 16 tiles |
| **Exterior Door** | Town door `(16, 72)` |
| **Interior Entry Pad** | `(11, 14)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Ruined desk** | `(11, 8)` | Lore and sidequest hook |
| **Locked locker** | `(16, 8)` | Key-gated reward |
| **Compliance wall** | `(5, 6)` | Dominion echo flavor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Outer Wards** | `(11, 15)` |

---

## 7) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Camp baseline services active |
| **PHASE 1** | Quarantine office questlines become active |
| **PHASE 2** (`RELIC_TIDE_SEATED`) | Underworks support and supplies improve |
| **PHASE 3** (`RELIC_MASS_SEATED`) | Workshop utility items expand |
| **PHASE 4** (`RELIC_TIME_SEATED`) | Relay bunker route intelligence deepens |

| Interior | Main Hook |
|----------|-----------|
| **Relay Camp Tent** | Contracts and local economy |
| **Patchhouse Clinic** | Hazard prep before capital chain routes |
| **Candlecell Shelter** | Rest and character beats |
| **Relay Bunker** | Capital route guidance |
| **Quarantine Office** | Dominion history and optional branch |

---

## Quick Reference

```text
RELAY CAMP TENT      34x22  door (66,78)  pad (17,20)
PATCHHOUSE CLINIC    30x18  door (80,78)  pad (15,16)
CANDLECELL SHELTER   28x18  door (74,84)  pad (14,16)
RELAY BUNKER         24x16  door (70,62)  pad (12,14)
BOLT & BIND          30x18  door (92,80)  pad (15,16)
QUARANTINE OFFICE    22x16  door (16,72)  pad (11,14)
```
