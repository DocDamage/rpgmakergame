# Shrine Map Sheet: Prismwrit Chapel (Light Shrine)

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Shrine Name** | Prismwrit Chapel |
| **Element** | Light |
| **Role** | Optional shrine that grants a Light Blessing + a Light craft core |
| **Theme** | Truth and refraction—light as judgement, clarity as a weapon |
| **Recommended Level** | 140–195 (scales if entered late) |
| **Total Footprint** | 1 exterior micro-map + 1 interior map + 1 trial chamber submap |
| **Tile Scale** | 16×16 px |

---

## 2. World Placement + Access

### Overworld Location
- **Position**: On a high ridge spur near Prismridge
- **Description**: Visible from the overworld, reached via a short switchback path
- **Node Label**: `Light Shrine — Prismwrit Chapel`
- **Map Icon**: Prism star

### Access Rule
- Door is sealed by **Prism Lock**
- Open by aligning **3 reflector stones** on the exterior approach to bounce a beam into the door crest

---

## 3. Exterior Micro-Map — "Gleamstep Ascent"

| Property | Value |
|----------|-------|
| **Size** | 40 × 28 tiles |
| **Purpose** | Short beam-bounce unlock |
| **Encounters** | OFF |

### Key Anchors (local 0–39, 0–27)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry from overworld | (20, 26) | Player spawn point |
| Shrine door (Prism Lock) | (20, 4) | Opens when beam hits door crest |
| Save lantern (optional) | (6, 20) | Pre-shrine save point |
| **Beam Emitter Stone** | (20, 22) | Fires steady beam when interacted |
| **Reflector Stone A** | (12, 16) | Rotatable (4 directions) |
| **Reflector Stone B** | (28, 16) | Rotatable (4 directions) |
| **Reflector Stone C** | (20, 10) | Rotatable (4 directions) |
| Flavor plaque | (20, 8) | *"Light does not lie. It only reveals."* |

### Door Puzzle Mechanics

1. Interact emitter → it fires a steady beam
2. Rotate each reflector (4 directions) so the beam reaches the door crest
3. **Success telegraph**: Door crest flares white → lock dissolves

---

## 4. Interior Map — "Chapel of Angles"

| Property | Value |
|----------|-------|
| **Size** | 64 × 48 tiles |
| **Lighting** | Clean white-blue, prismatic glints on floor |
| **Encounters** | OFF |

### Layout Overview

| Room | Name | Type |
|------|------|------|
| Room 1 | Vestibule | Safe zone |
| Room 2 | Mirror Gallery | Main puzzle area |
| Room 3 | Lumen Cloister | Save + warp |
| Room 4 | Truth Seal Door | Portal to Trial Chamber |

### Anchors & Coordinates (local 0–63, 0–47)

#### Entry / Flow

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Interior entry spawn | (32, 44) | From exterior door |
| Return door to overworld | (32, 46) | Exit to Gleamstep Ascent |
| Trial Door (Truth Seal) | (32, 6) | Locked until puzzle solved |

#### Safe Utilities

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Save Crystal | (12, 38) | Standard save point |
| Warp Sigil | (52, 38) | Unlocks after clear |
| Keeper / lectern spot | (32, 38) | Optional NPC location |

#### Mirror Gallery Puzzle Props

**Beam Emitter Pedestal**

| Object | Coordinates |
|--------|-------------|
| Beam Emitter Pedestal | (32, 30) |

**Rotating Mirrors (4)** — 90° rotation steps

| Mirror | Coordinates |
|--------|-------------|
| Mirror 1 | (18, 26) |
| Mirror 2 | (46, 26) |
| Mirror 3 | (18, 18) |
| Mirror 4 | (46, 18) |

**Prism Lens** — Splits beam into 2

| Object | Coordinates |
|--------|-------------|
| Prism Lens | (32, 22) |

**Truth Sigils (targets, 2)**

| Sigil | Coordinates |
|-------|-------------|
| Sigil A | (14, 14) |
| Sigil B | (50, 14) |

#### Locked Door

| Object | Coordinates | Unlock Condition |
|--------|-------------|------------------|
| Truth Seal Door | (32, 6) | Both Truth Sigils lit simultaneously for 4 seconds |

---

## 5. Chapel Puzzle — "Two Truths"

### Goal
Split one beam into two and route both to the two Truth Sigils.

### Rules

| Element | Details |
|---------|---------|
| **Emitter** | Activating the Emitter Pedestal fires a beam upward |
| **Prism Lens** | Splits beam into Left/Right beams at (32, 22) |
| **Mirrors** | Rotate in 90° steps to route beams to Sigils |
| **Shadowed Tiles** | If a beam crosses a "shadowed tile" (gallery dark strip), it weakens and fails |

### Shadowed Tile Strips (prevent brute force)

| Strip | Coordinates |
|-------|-------------|
| Left strip | x 24–28 for y 14–28 |
| Right strip | x 36–40 for y 14–28 |

> Players must route beams around these zones.

### Telegraphs

| State | Visual | Audio |
|-------|--------|-------|
| Correct hit on Sigil | Bright hum + glyph lights | Success tone |
| Beam weakened | Beam flickers | Soft "glass sigh" |

### Fail State
No damage. Just reset beam when deactivated/reactivated.

---

## 6. Trial Chamber Submap — "Lumen Verdict Crucible"

| Property | Value |
|----------|-------|
| **Size** | 48 × 48 tiles |
| **Purpose** | Safe-wedge positioning + "real vs false" check with a mini-boss |
| **Encounters** | ON (scripted boss fight only) |

### Anchors & Coordinates (local 0–47, 0–47)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry portal spawn | (24, 44) | From Truth Seal Door |
| Boss spawn | (24, 18) | Chapel Adjudicator: Seraph Glass |
| Exit portal | (24, 6) | Spawns after clear |
| Reward pedestal | (24, 10) | Light Blessing + loot |
| **Prism Beacon A** | (12, 26) | Reveals "true target" / shrinks hazards |
| **Prism Beacon B** | (36, 26) | Reveals "true target" / shrinks hazards |
| **Cover Plinth 1** | (14, 18) | 2×2 collision cover |
| **Cover Plinth 2** | (34, 18) | 2×2 collision cover |
| **Cover Plinth 3** | (14, 34) | 2×2 collision cover |
| **Cover Plinth 4** | (34, 34) | 2×2 collision cover |

---

## 7. Trial Script — "Vow of Clarity"

### Phase 0: Start
- Portal locks when player crosses y ≤ 40

### Phase 1: Prism Wedge Drill (30 seconds)

**Hazard: "Prism Verdict"**

| Property | Value |
|----------|-------|
| Cycle | Every 12 seconds |
| Telegraph | 1.5s wedge outline + chime |
| Active | 8.0s |
| Effect | Outside wedge: chip damage + Dazzled buildup |

### Phase 2: Mini-Boss — Chapel Adjudicator: Seraph Glass

#### Boss Identity
Creates false images and fires beams; players must reveal the real one with beacons.

#### Move List

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Radiant Spear** | Fast line | 0.7s | Damage |
| **Split Verdict** | Spawns 2 images | 1.1s prism burst | Creates decoys |
| **Refraction Lines** | 2 lanes | 1.3s thin lines | Lane damage |
| **Flash Seal** | Blind-lite | 1.0s flare | Vision debuff |

#### Prism Beacons (Counterplay)

| Property | Value |
|----------|-------|
| Interact time | 1.0s |
| Cooldown | 20s |
| Effect | 8s reveal pulse: real boss outline + images become brittle / expire fast |

### Clear Condition
Defeat Seraph Glass → Exit portal spawns + Reward pedestal unlocks.

---

## 8. Rewards + Flags

### Reward Pedestal Contents

#### Blessing: Benediction of Truth

| Property | Value |
|----------|-------|
| **Type** | Light Blessing |
| **Effect** | +Light resistance; Your first miss each turn becomes a glancing hit (reduced damage), and illusions/stealth are revealed briefly when you land a crit |

#### Unique Item Drops

| Item | Type |
|------|------|
| Light Core Shard | Craft component / resonance upgrade |
| Prism Sigil | Optional: unlocks Light-aligned node / summon enhancement |

#### Optional Treasure Chest

| Property | Value |
|----------|-------|
| Location | (40, 12) in Trial Chamber |
| Contents | Materials + currency + 1 Light-leaning accessory roll |

### Game Flags

| Flag | Trigger |
|------|---------|
| `SHRINE_LIGHT_FOUND` | Entering Gleamstep Ascent |
| `SHRINE_LIGHT_CLEARED` | Defeating Seraph Glass |
| `BLESSING_LIGHT_UNLOCKED` | Collecting from reward pedestal |
| `WARP_LIGHT_SHRINE_UNLOCKED` | Clearing the shrine |

---

## 9. NPC/Voice Lines

### Chapel Keeper (Lumen Cloister, at 32, 38)

| Context | Line |
|---------|------|
| Greeting | *"Two beams. Two truths."* |
| Puzzle Hint | *"If it flickers, your path is wrong."* |
| After Clear | *"Clarity suits you."* |

---

## 10. Quick Reference

### Coordinate Summary

#### Exterior (Gleamstep Ascent) — 40×28
```
Entry: (20, 26)      Door: (20, 4)
Emitter: (20, 22)
Reflector A: (12, 16)    Reflector B: (28, 16)    Reflector C: (20, 10)
Save: (6, 20)            Plaque: (20, 8)
```

#### Interior (Chapel of Angles) — 64×48
```
Entry: (32, 44)           Exit: (32, 46)
Save: (12, 38)            Warp: (52, 38)
Keeper: (32, 38)          Trial Door: (32, 6)

--- Puzzle ---
Emitter: (32, 30)             Prism Lens: (32, 22)
Mirror 1: (18, 26)            Mirror 2: (46, 26)
Mirror 3: (18, 18)            Mirror 4: (46, 18)
Sigil A: (14, 14)             Sigil B: (50, 14)

--- Shadowed Strips ---
Left: x 24–28, y 14–28
Right: x 36–40, y 14–28
```

#### Trial Chamber (Lumen Verdict Crucible) — 48×48
```
Entry: (24, 44)           Boss: (24, 18)
Exit: (24, 6)             Reward: (24, 10)
Beacon A: (12, 26)        Beacon B: (36, 26)
Plinths: (14,18) (34,18) (14,34) (34,34)
```

---

## 11. Implementation Notes

- **Beam routing**: Real-time visual feedback as mirrors are rotated
- **Shadowed tile detection**: Beam weakens if path intersects shadowed zones
- **Prism wedge hazard**: Safe zone rotates/changes position each cycle
- **Seraph Glass images**: Decoys expire or become brittle when beacon is active
- **Prism Beacon cooldown**: 20s per beacon, track independently
