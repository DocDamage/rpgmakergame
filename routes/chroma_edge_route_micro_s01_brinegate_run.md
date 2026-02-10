# Sea Lane Micro-Map: S01 — Brinegate Run

## Route Overview

| Property | Value |
|----------|-------|
| **Sea Lane Name** | Brinegate Run (S01 Micro) |
| **Theme** | Dock departure → open chop → fog pier approach |
| **Encounter Level Band** | 45–55 |
| **Mounts** | N/A |
| **Map Size** | 72 × 40 (x 0–71, y 0–39) |
| **Purpose** | "Travel" as short playable micro with terminal at each end |

---

## Design Note

Treat as **"ship deck + pier approach"** rather than full ocean map. Short, readable, feels like travel happened.

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Brinegate (Dock Gate)** | (8, 34) | Departure |
| **To Abyss Entry Pier micro** | (64, 10) | Arrival trigger |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Boarding Terminal (Brinegate side) | (12, 32) | Departure point |
| Mid-Deck safe zone (cover) | (36, 22) | Crate stack blocks shove |
| Fog bell buoy (visual landmark) | (54, 16) | Navigation marker |
| Arrival gangplank | (62, 12) | Pier access |

---

## Hazards

### Wave Pitch (Positional Drift, No Damage)

| Property | Value |
|----------|-------|
| **Cycle** | 10s |
| **Telegraph** | 1.0s creak + sway |
| **Active** | 3.0s |
| **Effect** | Shove 1 tile sideways (alternating L/R each cycle) |
| **Blockable** | Crates/rails block shove (use cover geometry) |

### Spray Burst (Tiny Chip + Wet Marker Optional)

| Property | Value |
|----------|-------|
| **Cycle** | 14s |
| **Telegraph** | 1.2s mist |
| **Active** | 2.5s |
| **Zone** | x 44–60, y 12–20 |
| **Effect** | Tiny chip + optional Wet marker |

---

## Encounter Pockets (2, Controlled)

### Pocket A (Mid Deck)

| Property | Value |
|----------|-------|
| **Location** | (30, 26) |
| **Composition** | 2× Tide Scuttler + 1× Brine Caster |

### Pocket B (Fog Approach)

| Property | Value |
|----------|-------|
| **Location** | (56, 14) |
| **Composition** | 1× "Rope-Eel" ambush + 2× Tide Scuttler |
| **Tier 7+** | Add 1 more eel |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (20, 14) | Consumables |
| Gather: Sea Barnacle | (48, 28) | Crafting |

---

## Travel UI Prompt at Terminal

```
Title: SEA RUN
Body: Depart for Abyss Entry Pier?
Buttons: [DEPART] [NOT YET]
```

---

## Scripting Notes

| Option | Implementation |
|--------|----------------|
| **Cutscene travel** | Skip Pocket A, keep only Pocket B as "boarding event" |
| **Full micro** | Both pockets active |
| **Same map** | Works for either approach |

---

## Quick Reference Coordinates

```
Brinegate dock: (8, 34)       Terminal: (12, 32)
Mid-deck cover: (36, 22)      Fog bell: (54, 16)
Abyss Pier: (64, 10)          Gangplank: (62, 12)

--- Pockets ---
A: (30, 26)                   B: (56, 14)

--- Hazards ---
Wave pitch: alternating shove (10s cycle)
Spray zone: x 44–60, y 12–20 (14s cycle)
```

---

## Implementation Notes

- **Compact design:** Feels like travel without empty ocean
- **Wave pitch:** Alternating direction creates rhythm
- **Cover mechanics:** Crates teach positioning on moving deck
- **Fog approach:** Pocket B creates tension before arrival
- **Optional cutscene:** Can reduce to single encounter if preferred
