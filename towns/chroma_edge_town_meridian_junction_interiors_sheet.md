# Chroma's Edge - Meridian Junction Interiors Sheet (v1)
## Build-Ready Interior Layouts + Route Hub Operations

---

## 0) Global Interior Rules (All Meridian Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Open civic lanes; dense props only at edges |
| **Lighting (Day)** | Neutral daylight with relay cyan accents |
| **Lighting (Night)** | Lower ambient with stronger relay and inspection lights |
| **Audio Bed** | Relay hum, cargo crane movement, market chatter |
| **Door Warp Rule** | 1-tile entry pad with 2-tile clear spawn lane |

---

## 1) CROSSWIND LODGE (Inn)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 36 x 24 tiles |
| **Exterior Door** | Town door `(68, 96)` |
| **Interior Entry Pad** | `(18, 22)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(18, 14)` | Rest + save |
| **Rumor wall** | `(8, 13)` | Route status updates |
| **Caravan board** | `(27, 10)` | Flavor interaction |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(18, 23)` |

---

## 2) WAYFARER AID (Clinic)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 20 tiles |
| **Exterior Door** | Town door `(84, 96)` |
| **Interior Entry Pad** | `(16, 18)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic service menu** | `(16, 12)` | Broad status support by progression |
| **Aid cabinet** | `(6, 4)` | 1/day cure item |
| **Treatment log** | `(24, 11)` | Sidequest hooks |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(16, 19)` |

---

## 3) ROUTE & RATION + JUNCTION CHARMS

### A) Route & Ration (General Goods)

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 x 20 tiles |
| **Exterior Door** | Town door `(112, 76)` |
| **Interior Entry Pad** | `(15, 18)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **General shop menu** | `(15, 12)` | Core consumables |
| **Freight board** | `(6, 6)` | Route economy hints |
| **Supply crate** | `(24, 12)` | Sidequest dependency |

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(15, 19)` |

### B) Junction Charms (Accessories)

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 18 tiles |
| **Exterior Door** | Town door `(124, 66)` |
| **Interior Entry Pad** | `(14, 16)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Accessory shop menu** | `(14, 11)` | Route-resistant charms |
| **Charm rack** | `(23, 10)` | Flavor interaction |
| **Counter display** | `(6, 7)` | Quest flavor |

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(14, 17)` |

---

## 4) BOLT & BALE (Repair/Smith)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 40 x 24 tiles |
| **Exterior Door** | Town door `(34, 86)` |
| **Interior Entry Pad** | `(20, 22)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Upgrade bench** | `(20, 13)` | Mid/late upgrades |
| **Conversion rig** | `(31, 11)` | Material conversion |
| **Mount module rack** | `(9, 11)` | Tack module support |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(20, 23)` |

---

## 5) HITCH & HARNESS (Stable Office)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 22 tiles |
| **Exterior Door** | Town door `(18, 86)` |
| **Interior Entry Pad** | `(17, 20)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Stable menu** | `(17, 13)` | Storage, tack swap, bond support |
| **Travel feed bin** | `(8, 10)` | Consumable support |
| **Tack rack** | `(26, 10)` | Gear interaction |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(17, 21)` |

---

## 6) MERIDIAN LEDGER (Contract Hall)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 34 x 22 tiles |
| **Exterior Door** | Town door `(52, 66)` |
| **Interior Entry Pad** | `(17, 20)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Contract board UI** | `(17, 13)` | Bounties and shipment contracts |
| **Faction ledger** | `(26, 10)` | Reputation tracking |
| **Dispatch map** | `(8, 10)` | Route planning flavor |

### C) Exit

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(17, 21)` |

---

## 7) Relay Control + Permit Booth

### A) Meridian Relay Control

| Parameter | Value |
|-----------|-------|
| **Map Size** | 26 x 18 tiles |
| **Exterior Access** | Prompt at terminal tile `(72, 32)` |
| **Interior Entry Pad** | `(13, 16)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Relay terminal UI** | `(13, 10)` | Route status and phase markers |
| **Stabilization console** | `(19, 8)` | Routing quest interactions |
| **Signal panel** | `(7, 8)` | Flavor and hidden pings |

### B) Dominion Permit Booth

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 16 tiles |
| **Exterior Door** | Town door `(12, 34)` |
| **Interior Entry Pad** | `(11, 14)` |

| Interactable | Location | Function |
|--------------|----------|----------|
| **Permit desk** | `(11, 8)` | Branching permit quest flow |
| **Inspection locker** | `(16, 8)` | Sidequest objective |
| **Compliance board** | `(5, 6)` | Pressure flavor |

| Exit | Coordinates |
|------|-------------|
| **Return to Meridian** | `(11, 15)` |

---

## 8) Phase and Hook Mapping

| Phase | Interior Impact |
|-------|------------------|
| **PHASE 0** | Standard hub operations and baseline contracts |
| **PHASE 1** | Permit friction and inspection dialogue increase |
| **PHASE 2** (`D5_CLEARED`) | Coastal contract paths expand |
| **PHASE 3** (`D6_CLEARED`) | Freight contracts and heavy upgrades expand |
| **PHASE 4** (`D7_CLEARED`) | Phase marker routing and time-lane tasks unlock |

| Interior | Main Hook |
|----------|-----------|
| **Crosswind Lodge** | Rest and rumor cadence |
| **Meridian Ledger** | Contract system center |
| **Bolt & Bale** | Upgrade and conversion center |
| **Relay Control** | Routing brain and phase diagnostics |
| **Permit Booth** | Bureaucratic tension branch |

---

## Quick Reference

```text
CROSSWIND LODGE      36x24  door (68,96)  pad (18,22)
WAYFARER AID         32x20  door (84,96)  pad (16,18)
ROUTE & RATION       30x20  door (112,76) pad (15,18)
JUNCTION CHARMS      28x18  door (124,66) pad (14,16)
BOLT & BALE          40x24  door (34,86)  pad (20,22)
HITCH & HARNESS      34x22  door (18,86)  pad (17,20)
MERIDIAN LEDGER      34x22  door (52,66)  pad (17,20)
RELAY CONTROL        26x18  access (72,32) pad (13,16)
PERMIT BOOTH         22x16  door (12,34)  pad (11,14)
```
