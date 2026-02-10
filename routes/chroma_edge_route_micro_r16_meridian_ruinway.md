# Route Micro-Map: R16 — Meridian Ruinway

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Meridian Ruinway (R16) |
| **Theme** | Clean junction → broken arterial road → rift-stitched outskirts → Lumencrest outer wards |
| **Encounter Level Band** | 84–100 |
| **Mounts** | ON until ruin choke, then OFF (recommended) |
| **Map Size** | 136 × 56 (x 0–135, y 0–55) |
| **Purpose** | Endgame corridor on-boarding; introduces edited reality + null hazards |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Meridian gate** | (10, 46) | Route start |
| **To Old Lumencrest (Outer Wards) entry** | (126, 18) | Hub entrance |
| **Optional spur to Shadow Shrine undercroft** | (112, 44) | Unlocks once Lumencrest discovered |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Junction pylons fade-out | x 16–28, y 36–46 | Clean tech ends |
| Ruin boulevard crack | x 52–90, y 14–30 | Broken road |
| Outer Wards campfire silhouette | (118, 22) | First sight of destination |

---

## Terrain / Hazards (Endgame Feel, Fair)

### A) Edited Record Zones (Loop-Feel)

| Zone | x 60–80, y 22–34 |
|------|------------------|
| **Effect** | Minor visual "page smear"; enemies gain small evasion OR player accuracy down |
| **Counter** | Truth Beacon suppresses debuff |

### Truth Beacon (Required Interactable)

| Property | Value |
|----------|-------|
| **Location** | (72, 18) |
| **Interact** | 1.0s |
| **Effect** | Suppress Edited Zone debuff in radius for 12s |
| **Teaching** | Capital's "edited records" theme |

### B) Null Pulse Vents

| Vent | Coordinates | Size |
|------|-------------|------|
| **Vent A** | (92, 26) | 3×3 |
| **Vent B** | (102, 20) | 3×3 |

#### Null Pulse Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 16s |
| **Telegraph** | 1.6s violet hum |
| **Active** | 4.0s |
| **Effect** | Strip 1 buff (max 1) + small chip |

---

## Encounter Pockets (4, Corridor Escalation)

### Pocket A (Clean Road Break)

| Property | Value |
|----------|-------|
| **Location** | (26, 40) |
| **Composition** | 2× Phase Scuttler + 1× Chrono Scriber |

### Pocket B (Ruin Boulevard)

| Property | Value |
|----------|-------|
| **Location** | (62, 26) |
| **Composition** | 1× Elite "Record Sentry" + 2× Rift Skirmisher |
| **Notes** | Tier scaling |

### Pocket C (Edited Zone Pressure)

| Property | Value |
|----------|-------|
| **Location** | (74, 28) |
| **Composition** | 1× Null Caster + 2× "Refraction Image" adds |
| **Notes** | Die fast; encourages Truth Beacon use |

### Pocket D (Outer Wards Approach)

| Property | Value |
|----------|-------|
| **Location** | (116, 20) |
| **Composition** | 1× Elite "Wardbreaker" + 2× adds |
| **Notes** | Final check before hub |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 12) | Consumables |
| Chest (medium) | (84, 44) | Side rubble path |
| Chest (small) | (108, 12) | Materials |
| Gather: Paradox Glass shard node | (98, 36) | Capital craft mat seed |
| Lore slab | (54, 12) | *"Someone rewrote the street signs. The street obeyed."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R16 opens** | `MERIDIAN_UNLOCKED = TRUE` AND `ACT2_RIFT_OVERLAY = TRUE` |
| **Early approach message** | `ROUTE UNSTABLE. VECTOR REFUSED.` |

---

## Post-Route QoL

| Condition | Effect |
|-----------|--------|
| First reach to Old Lumencrest | Meridian Return Vector warps to Meridian gate from Outer Wards |

---

## Quick Reference Coordinates

```
Meridian entry: (10, 46)      Lumencrest entry: (126, 18)
Shadow Shrine spur: (112, 44)
Pylons fade: x 16–28, y 36–46
Ruin crack: x 52–90, y 14–30
Campfire silhouette: (118, 22)

--- Pockets ---
A: (26, 40)                   B: (62, 26)
C: (74, 28)                   D: (116, 20)

--- Hazards ---
Edited Zone: x 60–80, y 22–34
Truth Beacon: (72, 18)
Null Vent A: (92, 26)         Null Vent B: (102, 20)

--- Gather ---
Paradox Glass: (98, 36)
```

---

## Implementation Notes

- **Edited Zones:** Visual distortion + gameplay effect; Truth Beacon counterplay
- **Null Vents:** Buff-stripping hazard foreshadows Palace content
- **Record Sentry:** Elite representing "edited reality" theme
- **Refraction Images:** Fast-dying adds create priority challenge
- **Wardbreaker:** Final gatekeeper before capital hub
- **Return Vector:** Prevents corridor fatigue on repeat visits
