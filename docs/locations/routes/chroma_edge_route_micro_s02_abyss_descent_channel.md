# Deep Lane Micro-Map: S02 — Abyss Descent Channel

## Route Overview

| Property | Value |
|----------|-------|
| **Deep Lane Name** | Abyss Descent Channel (S02 Micro) |
| **Theme** | Submersible slipway → kelp-dark trench mouth → pressure gate |
| **Encounter Level Band** | 50–60 |
| **Mounts** | N/A |
| **Map Size** | 80 × 44 (x 0–79, y 0–43) |
| **Purpose** | "You're going down" connector; introduces pressure/currents + ballast gate |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Abyss Entry Pier (sub dock)** | (10, 38) | Entry point |
| **To Abyssal Trench (D5) entrance** | (70, 6) | Dungeon door |

---

## Gating (Hard Requirement)

| Requirement | Message if Not Met |
|-------------|-------------------|
| `SUBMERSIBLE_UNLOCKED = TRUE` | `DEPTH CLEARANCE REQUIRED.` |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Sub Dock Control Panel | (14, 36) | Departure terminal |
| Ballast Gate (pressure seal) | (40, 18) | Puzzle gate |
| Trench Mouth Arch | x 60–74, y 6–14 | D5 entrance frame |
| Emergency air pocket alcove | (52, 28) | Safe nook |

---

## Hazards

### A) Current Jets (Push Lanes)

| Jet | Zone | Direction |
|-----|------|-----------|
| **Jet A** | x 22–26, y 20–34 | Down-angle |
| **Jet B** | x 46–50, y 12–26 | Down-angle |

#### Current Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 12s |
| **Telegraph** | 1.3s bubbles |
| **Active** | 4.0s |
| **Effect** | Shove 2 tiles along lane + minor chip (optional) |

### B) Pressure Pulse (Teach "Don't Stall")

| Property | Value |
|----------|-------|
| **Frequency** | Every 16s |
| **Telegraph** | 1.6s low thrum |
| **Danger zone** | x 30–58, y 10–26 (open center) |
| **Effect** | Apply Pressure Mark (warning debuff) |
| **3 stacks** | Small damage tick (urgency without unfairness) |

---

## Micro Puzzle: Ballast Gate

### Components

| Object | Coordinates |
|--------|-------------|
| **Valve 1** | (32, 22) |
| **Valve 2** | (40, 26) |
| **Valve 3** | (48, 22) |
| **Gate** | (40, 18) |

### Rule

| Condition | Result |
|-----------|--------|
| Toggle all 3 within 10 seconds | Gate opens |
| Fail (timer expires) | Valves reset (no damage) |

---

## Encounter Pockets (2, Tuned)

### Pocket A (Pre-Gate)

| Property | Value |
|----------|-------|
| **Location** | (26, 30) |
| **Composition** | 2× Kelp Stalker + 1× Brine Caster |

### Pocket B (Post-Gate Trench Mouth)

| Property | Value |
|----------|-------|
| **Location** | (62, 12) |
| **Composition** | 1× "Abyss Lampjaw" (mini-elite) + 2× Tide Scuttler |
| **Tier 8+** | Add 1 more stalker |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 14) | Consumables |
| Chest (small) | (54, 10) | Risk/reward (near trench mouth) |
| Gather: Abyss Kelp | (28, 10) | Crafting |
| Gather: Paradox Shell | (58, 30) | Rare mat seed |

---

## Post-D5 Shortcut (QoL)

| Condition | Effect |
|-----------|--------|
| `D5_CLEARED = TRUE` | Unlock one-way ascent vent at (58, 18) |
| **Benefit** | Returns near (18, 34) — faster back to pier |

---

## Quick Reference Coordinates

```
Sub dock entry: (10, 38)      Control panel: (14, 36)
D5 entrance: (70, 6)          Trench arch: x 60–74, y 6–14
Air pocket: (52, 28)          Shortcut vent: (58, 18) [locked]

--- Puzzle ---
Valve 1: (32, 22)             Valve 2: (40, 26)
Valve 3: (48, 22)             Gate: (40, 18)

--- Pockets ---
A: (26, 30)                   B: (62, 12)

--- Hazards ---
Jet A: x 22–26, y 20–34       Jet B: x 46–50, y 12–26
Pressure zone: x 30–58, y 10–26

--- Gather ---
Abyss Kelp: (28, 10)          Paradox Shell: (58, 30)
```

---

## Implementation Notes

- **Hard gate:** Submersible requirement blocks D5 until story milestone
- **Pressure system:** Warning debuff creates urgency without unfair deaths
- **Ballast puzzle:** 3-valve timed toggle — moderate pressure
- **Air pocket:** Safe zone teaches players to find refuge
- **Abyss Lampjaw:** Mini-elite feel before D5 proper
- **Ascent vent:** One-way shortcut respects player time post-clear
