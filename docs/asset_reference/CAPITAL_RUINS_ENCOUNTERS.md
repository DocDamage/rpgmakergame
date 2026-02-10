# Capital Ruins Encounter Design
## Using Terranigma Louran Ruins

The Capital Ruins zone represents the fallen capital city of the Kingdom, corrupted by the Extinguisher's influence. This document designs encounters using the 40+ ruined interior sections from Terranigma's Louran.

---

## 🏚️ ZONE OVERVIEW

**Theme:** Fallen metropolis, decayed opulence, haunted streets
**Tone:** Melancholy, dangerous, mysterious
**Visual:** Gray stone, broken architecture, overgrown with dark vines
**Enemies:** Corrupted citizens, void creatures, architectural hazards

---

## 🗺️ MAP LAYOUT

### Zone Structure:
```
[Entry Plaza] → [Merchant District] → [Residential Quarter]
      ↓               ↓                      ↓
[Memorial   ← [Town Square] ←→ [Destroyed   → [Palace
 Hall]            ☠️             Market]        Gate]
      ↑               ↑                      ↑
[Underground] → [Sewer System] → [Secret Passage]
```

---

## ⚔️ ENCOUNTERS BY AREA

### 1. ENTRY PLAZA
**Asset:** Louran Ruins - Row 1, Column 1 (Large ruined hall)

**Battle Background:**
- Extract: (0, 0) to (428, 320)
- Features: Collapsed ceiling, debris, broken columns

**Encounters:**

#### Encounter 1A: "Welcome to Ruins" (Tutorial)
- **Enemies:** 2x Void Leech, 1x Corrupted Rat
- **Level:** Easy
- **Purpose:** Introduce zone mechanics
- **Dialogue:** 
  - Kade: "The Capital... it's worse than I remembered."
  - Nix-7: "Sensors detecting multiple hostiles."

#### Encounter 1B: "The Memorial Guardians"
- **Enemies:** 3x Stone Sentinel (corrupted statues)
- **Level:** Medium
- **Mechanic:** Enemies revive once unless hit with Light damage
- **Twist Reaction:** "Statues that fight back? Now I've seen everything."

---

### 2. MERCHANT DISTRICT
**Assets:** Louran Ruins - Row 1, Columns 2-3 (Shops and stalls)

**Battle Backgrounds:**
- Ruined Shop A: (428, 0) to (856, 320)
- Ruined Shop B: (856, 0) to (1284, 320)
- Collapsed Stall: (1284, 0) to (1712, 320)

**Encounters:**

#### Encounter 2A: "Last Customer"
- **Setting:** Abandoned general store
- **Enemies:** 1x Void Merchant (unique), 2x Void Leech
- **Level:** Medium
- **Special:** Merchant drops unique trinket "Last Sale Receipt"
- **Lore:** Implies the shopkeeper was consumed mid-transaction

#### Encounter 2B: "Market Crash"
- **Setting:** Collapsed marketplace
- **Enemies:** 4x Void Leech, 1x Corrupted Guard Dog
- **Level:** Medium-Hard
- **Mechanic:** Crumbling environment - random debris falls each turn

#### Encounter 2C: "The Hoarder" (Mini-boss)
- **Setting:** Pristine-looking shop (trap)
- **Enemies:** 1x Corrupted Collector (mini-boss)
- **Level:** Hard
- **Mechanic:** Collector steals items during fight, must defeat to recover
- **Drop:** "Collector's Key" (opens locked building in zone)

---

### 3. RESIDENTIAL QUARTER
**Assets:** Louran Ruins - Rows 2-3 (Houses and apartments)

**Battle Backgrounds:**
- Destroyed Home A: (0, 320) to (214, 568)
- Destroyed Home B: (214, 320) to (428, 568)
- Destroyed Home C: (428, 320) to (642, 568)
- Apartment Complex: (642, 320) to (1070, 568)

**Encounters:**

#### Encounter 3A: "Family Reunion"
- **Setting:** Crumbled living room
- **Enemies:** 3x Corrupted Family (tragic visual)
- **Level:** Medium
- **Special:** Non-hostile at first, become aggressive if approached
- **Moral Choice:** Put them out of their misery or try to cure them (lore only)
- **Sova Reaction:** "This... this is what we're fighting to prevent."

#### Encounter 3B: "The Neighbor"
- **Setting:** Apartment hallway
- **Enemies:** 1x Corrupted Resident, 2x Void Spawns
- **Level:** Easy-Medium
- **Dialogue:** 
  - Renna: "They were just... normal people."
  - Korr: "The Extinguisher spares no one."

#### Encounter 3C: "Haunted House"
- **Setting:** Large manor (special building)
- **Enemies:** 1x Void Wraith, 4x Void Leech
- **Level:** Hard
- **Mechanic:** Wraith possesses party members temporarily
- **Ashka Reaction:** "Get out of my head!"

---

### 4. TOWN SQUARE
**Asset:** Louran Ruins - Row 4, Large open area

**Battle Background:**
- Town Square: (0, 568) to (856, 820)

**Encounters:**

#### Encounter 4A: "The Siege"
- **Setting:** Open plaza with fountain
- **Enemies:** 6x Corrupted Guard, 1x Elite Captain
- **Level:** Hard
- **Mechanic:** Reinforcements arrive each turn until captain is defeated
- **Story:** Represents the final stand of the Capital Guard

#### Encounter 4B: "Monument to Failure"
- **Setting:** Around destroyed statue
- **Enemies:** 1x Corrupted Statue (golem-type), 3x Void Leech
- **Level:** Medium
- **Lore:** Statue was of the previous King (Kade's father)
- **Kade Reaction:** [Silent, clenched fists]

---

### 5. MEMORIAL HALL
**Assets:** Louran Ruins - Row 5, Columns 1-2 (Large ceremonial building)

**Battle Background:**
- Memorial Hall: (0, 820) to (428, 1070)

**Encounters:**

#### Encounter 5A: "The Honored Dead"
- **Setting:** Hall of statues/trophies
- **Enemies:** 4x Animated Armor, 1x Void Commander
- **Level:** Hard
- **Mechanic:** Armor pieces reform if not all destroyed same turn
- **Lore:** These were the kingdom's greatest heroes, now corrupted

#### Encounter 5B: "Echoes of Victory" (Hidden)
- **Setting:** Secret chamber behind broken wall
- **Enemies:** None (puzzle only)
- **Reward:** "Medal of Valor" - permanent +5% damage vs Void enemies
- **Twist Reaction:** "Shiny! I mean... historically significant."

---

### 6. UNDERGROUND / SEWERS
**Assets:** Louran Ruins - Row 6+ (Dark underground sections)

**Battle Backgrounds:**
- Sewer Tunnel: (428, 1070) to (856, 1320)
- Underground Chamber: (856, 1070) to (1284, 1320)

**Encounters:**

#### Encounter 6A: "Down the Drain"
- **Setting:** Flooded sewer tunnel
- **Enemies:** 3x Sewer Horror, 2x Void Leech
- **Level:** Medium
- **Mechanic:** Water slows movement, electrical attacks dangerous

#### Encounter 6B: "The Dweller" (Optional Boss)
- **Setting:** Large underground cavern
- **Enemies:** 1x Capital Dweller (unique boss)
- **Level:** Very Hard
- **Description:** Massive creature that has made the sewers its home
- **Drop:** "Dweller's Heart" - crafting material for best armor
- **Grit Reaction:** "Now THAT'S what I call a target!"

---

### 7. PALACE GATE
**Asset:** Louran Ruins - Final row sections (Large gate structure)

**Battle Background:**
- Palace Gate: (bottom row, wide section)

**Encounters:**

#### Encounter 7A: "The Final Stand"
- **Setting:** Before the Palace entrance
- **Enemies:** 8x Elite Guard, 2x Void Knight
- **Level:** Very Hard
- **Story:** Last guardians before the Palace dungeon
- **Dialogue:**
  - Suresh: "The corruption is strongest here. Be ready."
  - Kade: "I'm going to end this. For all of us."

---

## 🎭 SPECIAL EVENTS

### Event 1: "The Survivor"
**Location:** Residential Quarter
- Find a living citizen hiding in a ruined house
- Quest: "The Last Resident" - escort to zone exit
- Reward: Unique information about Palace secret entrance

### Event 2: "Memory Echo"
**Location:** Town Square
- Activate to see ghostly replay of the Capital's fall
- Lore-heavy, no combat
- Unlocks backstory about the Extinguisher's rise

### Event 3: "The Collector's Vault"
**Location:** Merchant District (requires Collector's Key)
- Unique shop with rare items
- Sells end-game consumables and materials

---

## 📊 ENCOUNTER DIFFICULTY CURVE

| Area | Easy | Medium | Hard | Boss |
|------|------|--------|------|------|
| Entry Plaza | 1 | 1 | 0 | 0 |
| Merchant District | 0 | 2 | 1 | 0 |
| Residential | 1 | 2 | 1 | 0 |
| Town Square | 0 | 1 | 1 | 0 |
| Memorial Hall | 0 | 0 | 1 | 0 |
| Underground | 0 | 1 | 0 | 1 |
| Palace Gate | 0 | 0 | 0 | 1 |

**Total:** 2 Easy, 7 Medium, 4 Hard, 2 Boss encounters

---

## 🎨 ASSET EXTRACTION LIST

### Priority 1 (Battle Backgrounds):
1. `louran_entry_plaza.png` - Row 1, Col 1
2. `louran_shop_a.png` - Row 1, Col 2
3. `louran_shop_b.png` - Row 1, Col 3
4. `louran_home_a.png` - Row 2, Col 1
5. `louran_home_b.png` - Row 2, Col 2
6. `louran_town_square.png` - Row 4, wide section
7. `louran_memorial.png` - Row 5, Col 1
8. `louran_sewer.png` - Row 6, Col 2
9. `louran_palace_gate.png` - Final row

### Priority 2 (Environmental Details):
10. `louran_apartment.png` - Row 3
11. `louran_underground.png` - Row 6-7
12. `louran_rubble_a.png` - Various debris sections

---

## 💀 ENEMY ROSTER

### Common:
- **Void Leech** - Basic grunts, fast but weak
- **Corrupted Rat** - Swarm enemy
- **Void Spawn** - Ranged magic user

### Uncommon:
- **Corrupted Guard** - Medium melee
- **Stone Sentinel** - Tanky, slow
- **Void Spawns** - Support caster
- **Sewer Horror** - Aquatic, poison attacks

### Rare:
- **Void Knight** - Elite melee
- **Corrupted Collector** - Mini-boss, item theft
- **Void Wraith** - Possession mechanic
- **Void Commander** - Buffs other enemies

### Bosses:
- **Capital Dweller** - Optional sewer boss
- **Elite Captain** - Gate guardian (before Palace)

---

## 📝 DESIGN NOTES

### Visual Consistency:
- All backgrounds share gray stone palette
- Corruption elements: purple/black vines, dark mist
- Lighting: Dim, flickering, ominous

### Audio Design:
- Ambient: Wind howling through ruins, distant screams
- Combat: Heavy, industrial sounds (concrete breaking)
- Music: Melancholic strings, occasional discordant notes

### Pacing:
- Start slow (Entry Plaza) - exploration
- Build intensity (Town Square) - major battle
- Climax (Palace Gate) - epic finale to zone
- Secret area (Underground) - optional challenge

---

*"They say the Capital fell in a single day. Looking at these ruins... I believe it." - Korr*
