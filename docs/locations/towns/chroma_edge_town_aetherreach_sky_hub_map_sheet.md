# Town Map Sheet: Aetherreach — True Ending Sky Hub

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Town Name** | Aetherreach |
| **Type** | Endgame hub (skyborne) + epilogue trigger space |
| **Theme** | Quiet, clean air, "the world after the edit"—a breath before the final truth |
| **Recommended Level** | 220–240 (scales) |
| **Map Size** | 112 × 72 tiles |
| **Tile Scale** | 16×16 px |
| **Encounters** | OFF |
| **Mounts** | Allowed (optional; looks cool on sky-bridges) |

---

## 2. Unlock + Access

### Primary Unlock (True Ending Route)

| Flag | Condition |
|------|-----------|
| `FINAL_PALACE_CLEARED` | Complete Final Palace |
| `PROGENITOR_ENGINE_DEFEATED` | Defeat Progenitor Engine |
| `ECLIPSE_CONFLUENCE_STABILIZED` | World stabilized (post-Eclipse) |

### Travel Nodes

#### A) From Chronowake Pier (Recommended)

| Feature | Details |
|---------|---------|
| Location | Phase-Lane terminal |
| New Option | "ASCEND: AETHERREACH" |
| Flag Set | `AETHERREACH_ROUTE_OPEN = TRUE` |

#### B) From Eclipse Confluence (Optional)

| Feature | Details |
|---------|---------|
| Method | Aetherlift platform |
| Message | "AETHERLIFT: SKYBOUND VECTOR ONLINE" |

### First Arrival One-liner

```
[SYSTEM] "AETHERREACH COORDINATES LOCKED. ALTITUDE STABLE."
```

---

## 3. Town Structure

### 3 Terraces + 1 Central Spire

| Terrace | Name | Function |
|---------|------|----------|
| 1 | **Aether Docks** | Arrival, warp, NG+ kiosk |
| 2 | **Cloudmarket Walk** | Shops, inn, crafting |
| 3 | **Quietward Gardens** | Memorial, lore, party barks |
| Central | **Skybound Spire** | True Ending terminal + final record chamber |

---

## 4. Anchors & Coordinates (local 0–111, 0–71)

### A) Terrace 1 — Aether Docks (South Band)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Arrival spawn (Phase-Lane) | (56, 66) | Player entry point |
| Return pad (to Chronowake/Confluence) | (56, 68) | Exit to overworld |
| **Warp Sigil (Aetherreach)** | (44, 62) | Fast travel unlock |
| **Save Crystal** | (68, 62) | Town save point |
| **Protocol Kiosk** (Eclipse modifiers/NG+) | (56, 60) | Post-game settings |
| Dockmaster NPC | (56, 64) | Welcome dialogue |
| **Bridge to Cloudmarket** | (56, 56) | Northbound connection |

### B) Terrace 2 — Cloudmarket Walk (Mid Band)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Market spine path | x 20–92, y 40–46 | Main walkway |
| **Inn entrance** — "Featherrest" | (28, 44) | Rest + memory snippets |
| **Item shop entrance** — "Windmere Supplies" | (44, 44) | Late-game consumables |
| **Smith/Forge entrance** — "Aurumwright" | (56, 44) | Origin-tier upgrades |
| **Exchange/Token shop** — "Origin Ledger Booth" | (68, 44) | Token exchanges |
| **Relic/Curio shop** — "Starglass Cabinet" | (84, 44) | Rare accessories |
| **Notice board** | (56, 46) | Postgame hunts / dungeon hooks |
| **Cooking/Rest fountain** | (28, 40) | Inn side amenity |
| **Bridge to Quietward Gardens** | (56, 34) | Northbound connection |

### C) Terrace 3 — Quietward Gardens (North Band)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Garden entry | (56, 32) | From Cloudmarket bridge |
| **Memorial dais** | (56, 22) | Token placement interaction |
| **Lore obelisk** | (40, 22) | World history archive |
| **Hidden puzzle ring** (optional) | (72, 20) | Secret relic puzzle |
| **Skyview bench** (party barks) | (56, 18) | Character interactions |
| **Spire approach stair** | (56, 14) | Bridge to central spire |

### D) Central — Skybound Spire (True Ending Chamber)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Spire entry door | (56, 10) | Exterior threshold |
| **Spire interior trigger** | (56, 8) | Loads "Final Record" submap |

---

## 5. Interiors List

| Interior Name | Location Coords | Purpose |
|---------------|-----------------|---------|
| **Featherrest** (Inn) | (28, 44) | Rest, party memory snippets |
| **Windmere Supplies** (Item Shop) | (44, 44) | Late-game consumables, remnant keys |
| **Aurumwright** (Smith) | (56, 44) | Origin-tier upgrades, core conversions |
| **Origin Ledger Booth** (Exchange) | (68, 44) | Token exchanges, protocol unlocks |
| **Starglass Cabinet** (Curio Shop) | (84, 44) | Rare accessories, anti-dispel gear |
| **Final Record** (Spire Interior) | (56, 8) | True Ending trigger room |

---

## 6. Interior Submap: Skybound Spire — "Final Record"

| Property | Value |
|----------|-------|
| **Size** | 48 × 48 tiles |
| **Purpose** | True Ending trigger room + lore + optional "refuse/return" safety |
| **Encounters** | OFF |

### Anchors (local 0–47, 0–47)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry spawn | (24, 44) | From Aetherreach main map |
| **True Ending Terminal** | (24, 16) | Final choice interface |
| **Record Plinth 1** — "THE EDIT" | (16, 24) | How reality was rewritten |
| **Record Plinth 2** — "THE COST" | (24, 24) | What was lost/flattened |
| **Record Plinth 3** — "THE CHOICE" | (32, 24) | What remains unresolved |
| **Save Crystal** | (10, 40) | Pre-ending save |
| Exit door | (24, 46) | Return to Aetherreach |

### Terminal UI Options

```
┌─────────────────────────────────┐
│     TRUE ENDING TERMINAL        │
├─────────────────────────────────┤
│  [BEGIN TRUE ENDING]            │
│  [REVIEW THE RECORD]            │
│  [LEAVE (NOT YET)]              │
└─────────────────────────────────┘
```

### True Ending Safety Modal

```
"Beginning the True Ending will advance the world state. 
You can still return to postgame afterward."

[BEGIN]    [NOT YET]
```

---

## 7. Town Services

### Shops

| Shop | Location | Inventory |
|------|----------|-----------|
| **Windmere Supplies** | (44, 44) | Late-game consumables, remnant keys |
| **Aurumwright** | (56, 44) | Origin-tier upgrades, core shard conversions |
| **Origin Ledger Booth** | (68, 44) | Token exchanges, protocol unlock materials |
| **Starglass Cabinet** | (84, 44) | Rare accessories, prism/shadow anti-dispel gear |
| **Featherrest Inn** | (28, 44) | Rest, optional "party memory" snippet selector |

### Save/Warp
- Save + warp available immediately on arrival (player-friendly endgame hub)

---

## 8. True Ending Content Hooks

### A) "Review the Record" — Three Plinths

| Plinth | Title | Content |
|--------|-------|---------|
| 1 | **THE EDIT** | How reality was rewritten |
| 2 | **THE COST** | What was lost/flattened |
| 3 | **THE CHOICE** | What remains unresolved |

#### Completion Flag (Optional)

| Flag | Unlock Condition | Reward |
|------|------------------|--------|
| `AETHERREACH_RECORD_REVIEWED` | Read all 3 plinths | 1 cosmetic OR small passive buff |

### B) Memorial Dais Interaction (Quietward Gardens)

| Feature | Details |
|---------|---------|
| Prompt | "PLACE A TOKEN" |
| Cost | Origin Sigil OR cheap token |
| Reward | Small buff for next run / title / mural change |

---

## 9. NPC/Voice One-Liners

### Dockmaster (Aether Docks, 56, 64)
> *"Sky's stable. That means you did your job."*

### Attendant (Near Save Crystal, post-clear)
> *"No alarms. No countdowns. Just… air."*

### Archivist Echo (Near Lore Obelisk, Quietward)
> *"For once, the record isn't fighting back."*

### Smith (Aurumwright, Cloudmarket)
> *"If it broke the ceiling, I can reinforce it."*

### Innkeeper (Featherrest)
> *"Sleep here. Even heroes need one quiet night."*

---

## 10. True Ending World-State Change

### Activation Trigger
When player selects **BEGIN TRUE ENDING**:

### Flags Set

| Flag | Value |
|------|-------|
| `TRUE_ENDING_STARTED` | TRUE |
| `AETHERREACH_POST_CREDITS` | TRUE (optional post-credits teleport) |

### Visual Updates

| Element | Before | After |
|---------|--------|-------|
| Sky color | Cool blue/violet | Warm gold/amber |
| Prisms | Jittering | Still/calm |
| Wind effects | Active | Gentle/barely perceptible |

### New System Line
```
[SYSTEM] "WORLD STATE: RECONCILED."
```

---

## 11. Quick Reference

### Aetherreach Coordinate Summary

```
=== TERRACE 1: AETHER DOCKS (South) ===
Arrival: (56, 66)          Return pad: (56, 68)
Warp: (44, 62)             Save: (68, 62)
Protocol Kiosk: (56, 60)   Dockmaster: (56, 64)
Bridge to Cloudmarket: (56, 56)

=== TERRACE 2: CLOUDMARKET WALK (Mid) ===
Market spine: x 20–92, y 40–46

Inn (Featherrest): (28, 44)
Item Shop (Windmere): (44, 44)
Smith (Aurumwright): (56, 44)
Exchange (Ledger): (68, 44)
Curio (Starglass): (84, 44)

Notice board: (56, 46)
Fountain: (28, 40)
Bridge to Gardens: (56, 34)

=== TERRACE 3: QUIETWARD GARDENS (North) ===
Entry: (56, 32)
Memorial dais: (56, 22)      Lore obelisk: (40, 22)
Hidden puzzle: (72, 20)      Skyview bench: (56, 18)
Spire approach: (56, 14)

=== CENTRAL: SKYBOUND SPIRE ===
Entry door: (56, 10)         Interior trigger: (56, 8)

=== SPIRE INTERIOR (48×48) ===
Entry: (24, 44)              Terminal: (24, 16)
Plinth 1: (16, 24)           Plinth 2: (24, 24)
Plinth 3: (32, 24)           Save: (10, 40)
Exit: (24, 46)
```

---

## 12. Implementation Notes

- **Access validation**: Check all three flags before displaying Aetherreach travel options
- **Visual polish**: Skybox gradient shift on `TRUE_ENDING_STARTED` flag
- **Spire terminal**: Modal confirmation prevents accidental true ending trigger
- **Record plinths**: Lore entries should be concise (2–3 paragraphs max each)
- **Party barks**: Skyview bench triggers contextual dialogue based on active party composition
- **Hidden puzzle ring**: Optional collectible hunt; reward can be cosmetic or small mechanical bonus
- **Post-credits return**: If `AETHERREACH_POST_CREDITS` is TRUE, player respawns in Aetherreach after credits instead of title screen
