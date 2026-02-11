# Chroma's Edge — Sunken City Hidden Area Map Sheet (v1)
## Optional Tide Expedition — "Civilization Erased But Not Gone"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Area Type** | Hidden Area (Optional) |
| **Unlock Condition** | `AQUATIC_TRAVEL_UNLOCKED = TRUE` (post-D5 Tide relic seated) |
| **Recommended Level** | Lv 46–70 (scales with story progression) |
| **Theme** | Tide memory + "civilization erased but not gone" |
| **Primary Rewards** | Rare mats, Tide gear, lore keys, optional boss, breadcrumb toward endgame anomalies |
| **Structure** | 4 submaps (expedition feel, not one room) |
| **Encounters** | ON (except safe domes + boss aftermath) |
| **Save Points** | 1 (Drowned Plaza Safe Dome) + autosave before optional boss |
| **Return Loop** | Floodgate Shortcut back to surface dock after clearing vault (QoL) |

---

## 1) Macro Flow (How it Plays)

**Flow:** Surface Dock → Kelp Streets → Drowned Plaza (Safe Dome) → Vault of Bells (Puzzle + Optional Boss) → Floodgate Shortcut → Exit

### Macro ASCII

```
[MAP 1 Surface Dock]
        |
        v
[MAP 2 Kelp Streets] --(tide sigils)-> (opens)
        |
        v
[MAP 3 Drowned Plaza] (SAFE DOME + SAVE)
        |
        v
[MAP 4 Vault of Bells]
  Puzzle + Optional Boss + Relics
        |
   Floodgate Shortcut
        v
Back to Surface Dock (fast return)
```

---

## CORE MECHANICS (Sunken City-wide)

### A) Oxygen Gauge (Soft Timer)

Oxygen drains in submerged zones.

**Refilled by:**
- Air Domes (safe bubbles)
- Kelp Filters (consumable found here)
- Tide Breath Nodes (interactable vents)

**Threshold Effects:**

| Level | Effect |
|-------|--------|
| **Low O2** | Accuracy down + slower movement |
| **Critical** | Periodic chip damage + "panic" debuff (reduced healing) |
| **Fail-safe** | At 0: warped to last safe dome with penalty (no hard game-over) |

### B) Current Lanes

- Gentle and fast current tiles push 1–2 tiles
- Some currents only stabilize after solving Tide Sigils

### C) Tide Sigils (3-key Puzzle Language)

- Small floor glyphs that must be activated in the correct order
- Order is hinted by bell chimes and Marinus's Sanctum (payoff if player visited shrine)

---

## SUBMAP 1 — SURFACE DOCK ("DIVE GATE")

**Purpose:** Entry framing + oxygen tutorial + gear check.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 64 tiles |
| **Entry** | From Brinegate boat launch / sea node |
| **Exit** | Into Kelp Streets |
| **Encounters** | OFF in dock area; ON after passing dive frame |

### B) Visual / Tone

Broken stone pier, half-submerged arches, rope lines down into green-black water.

### C) Anchors (Local Coords)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** (boat/sea node) | (48, 6) | — |
| **Dive Frame Gate** (oxygen tutorial) | (48, 18) | Triggers UI tip |
| **Exit to Map 2** | (48, 62) | — |
| **Oxygen Cache Crate** (1st-time) | (18, 14) | Kelp Filter ×2 |
| **Tide Breath Node** (refill) | (78, 16) | — |

### D) One-Time Script Beat

| Property | Value |
|----------|-------|
| **Trigger** | (48, 18) |
| **Event** | Bell sound from below |
| **UI Tip** | "Oxygen drains. Find domes and vents." |

---

## SUBMAP 2 — KELP STREETS

**Purpose:** Exploration maze-lite + first Tide Sigil puzzle + current hazards.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 96 tiles |
| **Encounter Band** | Lv 46–60 |
| **Entry** | From Surface Dock |
| **Exit** | To Drowned Plaza (locked by 3 Sigils) |

### B) Layout Concept

A grid of collapsed streets:
- **Upper street:** Safer, longer
- **Lower canal:** Faster, current-heavy
- **Collapsed library nook:** Optional loot + lore

### C) Puzzle — "Three Sigils of Return"

**Goal:** Activate 3 Tide Sigils to open the Plaza Dome door.

**Hint:** Bell chimes: low → mid → high

| Sigil | Coordinates | Notes |
|-------|-------------|-------|
| **Sigil A** (low chime) | (26, 30) | — |
| **Sigil B** (mid chime) | (92, 40) | — |
| **Sigil C** (high chime) | (60, 72) | Fast-current zone |
| **Plaza Gate** (locked) | (120, 84) | Opens after 3 sigils |

### D) Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (64, 6) |
| **Exit Gate to Map 3** | (124, 84) |
| **Air Pocket #1** | (18, 58) |
| **Tide Breath Node** | (108, 22) |

### E) Optional Side Nook — "Collapsed Library"

| Property | Value |
|----------|-------|
| **Entrance crack** | (10, 24) |
| **Loot chest** | (8, 36) → "Sea-Glass Lens" (rare craft mat) |
| **Lore note** | "They rang the bells when the water came." |

---

## SUBMAP 3 — DROWNED PLAZA (SAFE DOME + HUB)

**Purpose:** Safe hub + save + tiny shops + route to vault.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Encounters** | OFF inside dome; ON at edges in rubble pockets |
| **Save Point** | Yes |
| **Entry** | From Kelp Streets |
| **Exit** | To Vault of Bells corridor |

### B) Visual / Tone

A huge shimmering air dome over a plaza. Statues are half-silted. A bell tower lies sideways.

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (56, 6) | — |
| **SAVE CRYSTAL** | (56, 38) | — |
| **Rest/Refill Vent** | (30, 42) | Refills oxygen, 1/day free |
| **Relic Cache Pedestal** (lore) | (78, 30) | Reads Tide memory logs |
| **Exit to Map 4 corridor** | (56, 74) | — |

### D) Optional "Deepwright Cache" (Mini Vendor)

| Property | Value |
|----------|-------|
| **NPC / Cache box** | (84, 44) |
| **Inventory** | Kelp Filters, Pressure Patches, Tide Veil charges |
| **UI** | Simple list menu (no full shop UI) |

---

## SUBMAP 4 — VAULT OF BELLS (PUZZLE + OPTIONAL BOSS)

**Purpose:** Climax room(s) with bell logic, big loot, and optional boss.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 96 tiles |
| **Encounter Band** | Lv 55–70 (elite chance) |
| **Pre-boss antechamber** | No encounters + oxygen refill |

### B) Core Puzzle — "Bell Sequence Lock"

**Goal:** Ring 3 bell mechanisms in correct order to open vault core.

**Hint:** Marinus's Sanctum chime pattern (payoff) OR wall mural showing bell sizes.

| Bell | Coordinates | Tone |
|------|-------------|------|
| **Bell 1** | (28, 28) | Low |
| **Bell 2** | (64, 22) | Mid |
| **Bell 3** | (98, 30) | High |
| **Vault Core Door** (locked) | (64, 58) | Opens after correct sequence |

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | — |
| **Oxygen Refill Vent** (antechamber) | (64, 18) | — |
| **Chest A** | (18, 70) | "Brineguard Charm" upgrade mat |
| **Chest B** | (110, 70) | "Pearl Dust" (rare Tide craft mat) |

### D) Optional Boss — "The Drowned Archivist"

| Property | Value |
|----------|-------|
| **Trigger** | When Vault Core opens OR when player loots core chest |
| **Arena** | Vault interior with rotating current ring + falling "memory shards" |

#### Mechanics

| Mechanic | Description |
|----------|-------------|
| **Memory Current** | Current direction flips every few turns |
| **Silence Wave** | Periodic silence; Tide Veil counters it |
| **Summons** | 2 Glowjellies at 60% HP |

#### Rewards

| Reward | Description |
|--------|-------------|
| **Accessory: ARCHIVIST'S SEAL** | Oxygen drain -20%, Silence resist +25%, reveals "sea secrets" on minimap in water zones |
| **Key Item: TIDE LOG: BELLKEEPERS** | Unlocks lore + small benefit (extra sea node marker) |

### E) Vault Core Loot (Always Available)

| Chest | Coordinates | Loot |
|-------|-------------|------|
| **Core Chest** | (64, 74) | High-tier Tide weapon/armor mat + Sea-Glass Lens + credits |

---

## 2) Floodgate Shortcut (QoL Return)

**After opening Vault Core (boss optional):**

| Feature | Coordinates | Effect |
|---------|-------------|--------|
| **Floodgate Lever** | (10, 84) | Activates tunnel to Surface Dock |
| **Exit trigger** | (2, 90) | Returns to Map 1 near (72, 54) |

---

## 3) Enemies (Area Table)

| Enemy | Traits |
|-------|--------|
| **Glowjellies** | Silence |
| **Silt Skitters** | Fast |
| **Brine Leeches** | Poison |
| **Kelp Wraiths** | Drain oxygen slightly on hit |
| **Sonar Drone (Stolen)** | Rare elite, drops high-tier brine mats |

---

## 4) Rewards Summary

| Category | Reward |
|----------|--------|
| **Consumables** | Kelp Filters (oxygen), Pressure Patches |
| **Craft Mats** | Sea-Glass Lens, Pearl Dust (Tide crafting gating) |
| **Accessory** | Archivist's Seal (optional boss) |
| **Navigation** | Sea node breadcrumbs for later hidden areas (Glass Tribunal Ruins / Choir Vaults) |
| **Lore** | Tide Log: Bellkeepers |

---

## 5) Completion Flags

| Flag | Condition |
|------|-----------|
| `SUNKEN_CITY_DISCOVERED` | TRUE on first entry |
| `SUNKEN_CITY_VAULT_OPENED` | TRUE after Bell Sequence Lock solved |
| `SUNKEN_CITY_BOSS_DEFEATED` | TRUE after Drowned Archivist defeated (optional) |
| `SUNKEN_CITY_FLOODGATE_UNLOCKED` | TRUE after Vault Core opened |

---

## Quick Reference: Area Overview

```
BRINEGATE BOAT LAUNCH
       |
       v
[SUBMAP 1: SURFACE DOCK]
   Size: 96×64 | Tutorial: Oxygen Gauge
   Entry: (48, 6) | Dive Frame: (48, 18)
   Exit: (48, 62) | Oxygen Cache: (18, 14)
       |
       v
[SUBMAP 2: KELP STREETS]
   Size: 128×96 | Lv 46–60
   Sigils: A (26,30) / B (92,40) / C (60,72)
   Plaza Gate: (120, 84)
   Side Nook: Collapsed Library (10,24) → Sea-Glass Lens
       |
       v
[SUBMAP 3: DROWNED PLAZA]
   Size: 112×80 | Safe Dome
   Save: (56, 38) | Refill Vent: (30, 42)
   Lore Pedestal: (78, 30) | Mini Vendor: (84, 44)
   Exit: (56, 74)
       |
       v
[SUBMAP 4: VAULT OF BELLS]
   Size: 128×96 | Lv 55–70
   Bells: 1 (28,28), 2 (64,22), 3 (98,30)
   Vault Door: (64, 58)
   Optional Boss: DROWNED ARCHIVIST → Archivist's Seal
   Core Loot: (64, 74)
   
   FLOODGATE SHORTCUT: (10, 84)
       |
       v
SURFACE DOCK RETURN
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Submap 1 Entry** | (48, 6) |
| **Dive Frame Gate** | (48, 18) |
| **Submap 1 Exit** | (48, 62) |
| **Submap 2 Entry** | (64, 6) |
| **Sigil A** | (26, 30) |
| **Sigil B** | (92, 40) |
| **Sigil C** | (60, 72) |
| **Plaza Gate** | (120, 84) |
| **Collapsed Library** | (10, 24) |
| **Submap 3 Entry** | (56, 6) |
| **Save Crystal** | (56, 38) |
| **Refill Vent** | (30, 42) |
| **Lore Pedestal** | (78, 30) |
| **Vendor Cache** | (84, 44) |
| **Submap 3 Exit** | (56, 74) |
| **Submap 4 Entry** | (64, 6) |
| **Antechamber Vent** | (64, 18) |
| **Bell 1** | (28, 28) |
| **Bell 2** | (64, 22) |
| **Bell 3** | (98, 30) |
| **Vault Door** | (64, 58) |
| **Chest A** | (18, 70) |
| **Chest B** | (110, 70) |
| **Core Chest** | (64, 74) |
| **Floodgate Lever** | (10, 84) |
