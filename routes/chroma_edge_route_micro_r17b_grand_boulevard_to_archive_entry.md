# Route Micro-Map: R17b - Grand Boulevard to Archive Entry

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Grand Boulevard to Archive Entry (R17b) |
| **Theme** | Bureaucratic boulevard branch into archive intake |
| **Encounter Level Band** | 88-102 |
| **Mounts** | ON at entry, OFF in archive intake lane |
| **Map Size** | 112 x 56 (x 0-111, y 0-55) |
| **Purpose** | Branch connector that cleanly hands players into Archive District access |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Grand Boulevard archive spur** | (4, 48) | Incoming from boulevard branch |
| **To Archive approach gate** | (108, 8) | Hands into R17c |
| **Back to Grand Boulevard main lane** | (4, 40) | Two-way return |
| **Maintenance catwalk to Outer Wards** | (56, 55) | One-way shortcut after unlock |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Route marker pillar | (16, 44) | "Archive Intake" signage |
| Permit dais ruin | (54, 30) | Mid-map landmark |
| Intake seal gate | (96, 12) | Final threshold visual |

---

## Terrain / Hazards

### A) Redaction Haze Corridor

| Property | Value |
|----------|-------|
| **Zone** | x 42-84, y 16-34 |
| **Telegraph** | 1.3s text smear shimmer |
| **Active** | 3.2s |
| **Effect** | Vision softening + small Confounded buildup |
| **Cooldown** | 9.0s |

### B) Chrono Chime Emitters

| Emitter | Coordinates | Size |
|---------|-------------|------|
| **Emitter A** | (62, 22) | 2x2 |
| **Emitter B** | (74, 26) | 2x2 |

| Property | Value |
|----------|-------|
| **Telegraph** | 1.0s bell chime + floor ring |
| **Active** | 2.5s |
| **Effect** | Brief slow + turn-delay pressure |
| **Cooldown** | 12.0s |

---

## Encounter Pockets

### Pocket A - Intake Road

| Property | Value |
|----------|-------|
| **Location** | (24, 42) |
| **Composition** | 2x Crownshard Sentinel + 1x Chrono Wisp |

### Pocket B - Permit Dais

| Property | Value |
|----------|-------|
| **Location** | (54, 30) |
| **Composition** | 1x Seal Leech elite + 2x Phase Skulker |

### Pocket C - Haze Corridor

| Property | Value |
|----------|-------|
| **Location** | (70, 24) |
| **Composition** | 1x Null Caster + 2x Refraction Image |

### Pocket D - Gate Ramp

| Property | Value |
|----------|-------|
| **Location** | (94, 14) |
| **Composition** | 1x Wardbreaker + 2x Rift Skirmisher |

---

## Interactables

| Type | Coordinates | Contents / Function |
|------|-------------|---------------------|
| Chest (small) | (20, 10) | Credits + consumables |
| Chest (medium) | (84, 42) | Seal Wax + Paradox mat |
| Gather node | (66, 6) | Clocksteel filings |
| Archive notice kiosk | (58, 32) | Key hint text |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R17b open** | `CROWN_CHAIN_STARTED = TRUE` |
| **Archive gate active** | `ARCHIVE_DISTRICT_ACCESS_GRANTED = TRUE` |
| **Catwalk shortcut open** | `CROWN_ARCHIVE_KEY_ACQUIRED = TRUE` |

---

## Quick Reference Coordinates

```text
Grand Boulevard entry: (4, 48)      Grand Boulevard return: (4, 40)
Archive gate: (108, 8)              Catwalk shortcut: (56, 55)

Redaction Haze: x 42-84, y 16-34
Emitter A: (62, 22)                 Emitter B: (74, 26)

Pocket A: (24, 42)                  Pocket B: (54, 30)
Pocket C: (70, 24)                  Pocket D: (94, 14)

Chest S: (20, 10)                   Chest M: (84, 42)
Clocksteel node: (66, 6)            Kiosk: (58, 32)
```

---

## Implementation Notes

- This segment is the short branch between `chroma_edge_submap_grand_boulevard_map_sheet.md` and the Archive chain.
- Use the kiosk text as a clear reminder that Archive completion unlocks Crown gate progression.
