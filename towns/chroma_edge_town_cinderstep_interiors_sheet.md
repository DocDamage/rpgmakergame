# Chroma's Edge - Cinderstep Interiors Sheet (v1)
## Build-Ready Interior Layouts + Heat Route Operations

---

## 0) Global Interior Rules (All Cinderstep Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Dense industrial props with 2 clear movement lanes minimum |
| **Lighting (Day)** | Warm forge glow + neutral fill light |
| **Lighting (Night)** | High contrast vent light + lower ambient fill |
| **Audio Bed** | Low forge rumble, steam hiss, chain creak |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear spawn pocket |

---

## 1) THE VENTGATE REST (Inn)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(58, 78)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(15, 12)` | Rest + save |
| **Route rumor board** | `(7, 12)` | D4 ascent hints |
| **Heat flask stand** | `(22, 9)` | Flavor interaction |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Cinderstep** | `(15, 19)` |

---

## 2) TONGS & THUNDER (Forge)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 40 x 26 tiles |
| **Exterior Door** | Town door `(22, 62)` |
| **Interior Entry Pad** | `(20, 24)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Main Anvil Line** | x 15-25, y 10-13 | Upgrade anchor |
| **Coolant Troughs** | x 4-10, y 9-16 | Visual and quest props |
| **Parts Rack** | x 30-37, y 8-18 | Material storage |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Forge upgrade menu** | `(20, 12)` | Mid-tier upgrades |
| **Tempering station** | `(32, 11)` | Heatguard tier (`D4_CLEARED`) |
| **Tack module bench** | `(8, 12)` | Mount heat modules post-D4 |

### D) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Cinderstep** | `(20, 25)` |

---

## 3) HEATSHIELD OUTFITTERS (Gear Shop)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 20 tiles |
| **Exterior Door** | Town door `(36, 68)` |
| **Interior Entry Pad** | `(16, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Shop menu** | `(16, 12)` | Burn and overheat mitigation items |
| **Coolant display** | `(6, 8)` | Item flavor + sidequest hook |
| **Field kit locker** | `(25, 11)` | PHASE 2+ unlock crate |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Cinderstep** | `(16, 19)` |

---

## 4) EMBERWELL AID (Clinic)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(68, 78)` |
| **Interior Entry Pad** | `(15, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic menu** | `(15, 12)` | Burn and overheat cures |
| **Aid cabinet** | `(5, 4)` | 1/day heal item |
| **Treatment ledger** | `(23, 11)` | Quest text hooks |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Cinderstep** | `(15, 19)` |

---

## 5) ASH & SALT SUPPLY (General Goods)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(74, 66)` |
| **Interior Entry Pad** | `(14, 16)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **General shop menu** | `(14, 11)` | Core consumables |
| **Stock list board** | `(5, 6)` | Economy hints |
| **Reserve bin** | `(23, 11)` | Sidequest dependency |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Cinderstep** | `(14, 17)` |

---

## 6) SPIRE PERMIT HALL + INSPECTOR OFFICE

### A) Spire Permit Hall

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(92, 44)` |
| **Interior Entry Pad** | `(14, 16)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Permit desk** | `(14, 10)` | D4 progression gating |
| **Ascent board** | `(20, 7)` | Route hints |
| **Rope manifest shelf** | `(6, 8)` | Flavor and sidequest text |

| Exit | Coordinates |
|------|-------------|
| **Return to Cinderstep** | `(14, 17)` |

### B) Dominion Inspector Office

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 16 tiles |
| **Exterior Door** | Town door `(100, 72)` |
| **Interior Entry Pad** | `(11, 14)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inspection desk** | `(11, 8)` | Branching paperwork sidequest |
| **Confiscation locker** | `(16, 8)` | Quest objective marker |
| **Notice wall** | `(5, 6)` | Dominion pressure flavor |

| Exit | Coordinates |
|------|-------------|
| **Return to Cinderstep** | `(11, 15)` |

---

## 7) Terminal Nook + Optional Tack Stall

### A) Terminal Nook

| Parameter | Value |
|-----------|-------|
| **Map Size** | 20 x 14 tiles |
| **Exterior Access** | Prompt at terminal tile `(28, 30)` |
| **Interior Entry Pad** | `(10, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Terminal interface** | `(10, 6)` | Heat route diagnostics |
| **Vent lane monitor** | `(5, 8)` | Post-D4 stabilized lane readout |

### B) Tack Stall (Optional)

| Parameter | Value |
|-----------|-------|
| **Map Size** | 18 x 14 tiles |
| **Exterior Access** | Prompt at mount hitch post `(40, 74)` |
| **Interior Entry Pad** | `(9, 12)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Tack menu** | `(9, 6)` | Heat modules and mount gear |
| **Trial board** | `(5, 8)` | Mount heat tack trial hook |

---

## 8) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Standard services, low Dominion pressure |
| **PHASE 1** | Inspector office line density increases |
| **PHASE 2** (`D4_CLEARED`) | Forge and clinic full heat-tier support |
| **PHASE 3+** | Curfew tone at night, permit hall remains active |

| Interior | Main Hook |
|----------|-----------|
| **Ventgate Rest** | Rest loop and route setup |
| **Tongs & Thunder** | Heat upgrade center |
| **Spire Permit Hall** | D4 route gate |
| **Inspector Office** | Bureaucratic tension branch |
| **Emberwell Aid** | Burn and overheat support |

---

## Quick Reference

```text
VENTGATE REST        30x20  door (58,78)  pad (15,18)
TONGS & THUNDER      40x26  door (22,62)  pad (20,24)
HEATSHIELD SHOP      32x20  door (36,68)  pad (16,18)
EMBERWELL AID        30x20  door (68,78)  pad (15,18)
ASH & SALT SUPPLY    28x18  door (74,66)  pad (14,16)
SPIRE PERMIT HALL    28x18  door (92,44)  pad (14,16)
INSPECTOR OFFICE     22x16  door (100,72) pad (11,14)
TERMINAL NOOK        20x14  access (28,30) pad (10,12)
TACK STALL           18x14  access (40,74) pad (9,12)
```
