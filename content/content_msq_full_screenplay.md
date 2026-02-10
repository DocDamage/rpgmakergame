# Chroma's Edge - Main Scenario Quest (MSQ) Full Screenplay
## Complete Scene-by-Scene Breakdown with Staging, Beats, Choices, and Event Flags

---

# ACT I: THE HUNT (Dungeons 1-4)

---

## SCENE 000: "THE LATTICE DREAM" (Prologue)
**Location:** Nowhere - The Lattice (Abstract Space)  
**Time:** Night (Timeless)

### Staging
- Total darkness with faint geometric lines forming a planetary circuit map
- Eight Foundation symbols flicker like failing neon
- The Progenitor voice emanates from everywhere and nowhere

### Characters Present
- Progenitor (V.O. only)
- Brief flashes of 8 silhouettes (the future party, unrecognized)

### Scene Beats

| Beat | Action | Dialogue/V.O. | VFX/SFX |
|------|--------|---------------|---------|
| 1 | Black screen | PROGENITOR: "Orion is unstable." | Lattice lines pulse |
| 2 | 8 symbols appear | PROGENITOR: "Mass. Motion. Heat. Tide. Growth. Light. Shadow. Time. Pieces of reality... mis-seated." | Each symbol flickers |
| 3 | Symbols spiral inward | PROGENITOR: "A reset is not cruelty. It is... maintenance." | Symbols shatter |
| 4 | Single point of light | PROGENITOR: "But you will try to stop it. You always do." | Light expands to whiteout |
| 5 | Hard cut to | [SFX: Dusthawk engine sputtering] | Crash sound |

### Event Flags Set
- `GAME_START = TRUE`
- `PROLOGUE_WATCHED = TRUE`
- `LATTICE_DREAM_SEEN = TRUE`

### Transition
Cut to Scene 001: Ashveil crash site

---

## SCENE 001: "ASH AND KADE" (Tutorial Opening)
**Location:** Ruins of Ashveil - Crash Site  
**Time:** Pre-Dawn

### Staging
- Smoke, scattered debris from dusthawk crash
- Distant torchlight from Dominion patrols
- Kade waking up, checking injuries

### Characters Present
- Kade (player character)
- Twist (unconscious nearby)
- [Optional: Tutorial combat with Dominion scout]

### Scene Beats

| Beat | Action | Dialogue | Gameplay |
|------|--------|----------|----------|
| 1 | Kade wakes | "...Still alive. That's irritating." | Movement tutorial begins |
| 2 | Finds Twist | "Twist. Hey. If you're dead, I'm taking your boots." | Party system unlock |
| 3 | Twist groans awake | "They're... already yours. You stole them... in Meridian." | Twist joins party |
| 4 | Spot patrol | "Dominion. Already? They were waiting for us." | Stealth/combat tutorial |
| 5 | Post-combat | "We need to find shelter. And answers." | Objective: Reach Ashveil Sanctuary |

### Event Flags
- `SCENE_001_COMPLETE = TRUE`
- `TWIST_JOINED = TRUE`
- `PARTY_SYSTEM_UNLOCKED = TRUE`

### Player Choices
None (linear tutorial) - Choice system introduced in Scene 003

---

## SCENE 002: "THE FIRST SANCTUARY"
**Location:** Ashveil Sanctuary - Heartroot Hall  
**Time:** Dawn

### Staging
- Refugees, wounded, nervous energy
- Sanctuary Keeper at central hearth
- Quest board newly posted with bounties

### Characters Present
- Kade, Twist
- Sanctuary Keeper (NPC)
- Various refugees (ambient)

### Scene Beats

| Beat | Action | Dialogue | Flags |
|------|--------|----------|-------|
| 1 | Enter sanctuary | Keeper: "More survivors? We're nearly at capacity." | `ASHVEIL_SANCTUARY_REACHED = TRUE` |
| 2 | Explain crash | Keeper: "Dominion patrols have doubled. Something's happening at the old ruins." | Lore hint |
| 3 | Quest board seen | "Bounty: Ruins of Ashveil - Disturbance Source" | `D1_QUEST_AVAILABLE = TRUE` |
| 4 | First rest | Tutorial: Inns and rest mechanics | `REST_TUTORIAL_COMPLETE = TRUE` |
| 5 | Exit prompt | "We should check those ruins. Or do some work around here first." | Free exploration begins |

### Branch Options
- **Option A:** Go directly to D1 (main path)
- **Option B:** Complete sidequests in Ashveil (optional)
- **Option C:** Explore and gather (optional)

### Event Flags
- `SCENE_002_COMPLETE = TRUE`
- `WORLD_MAP_UNLOCKED = TRUE`

---

## SCENE 003: "D1 ENTRY - THE RUINS CALL"
**Location:** Ruins of Ashveil - Entrance  
**Time:** Day

### Staging
- Overgrown ancient structure
- Growth Foundation corruption visible
- Dead Dominion soldiers at entrance (warning)

### Characters Present
- Kade, Twist
- [First appearance of Growth corruption]

### Scene Beats

| Beat | Action | Dialogue | Mechanics |
|------|--------|----------|-----------|
| 1 | Approach ruins | Twist: "That's... growing. The stone is growing." | Foundation tutorial |
| 2 | Examine bodies | "Dominion. Dead a week. But the blood looks... fresh?" | Time distortion hint |
| 3 | Enter decision | **CHOICE:** "We go in careful" / "We go in fast" / "We're not ready" | Affects first encounter |
| 4 | If "careful": | Stealth advantage in first combat | `D1_STEALTH_BONUS = TRUE` |
| 5 | If "fast": | Initiative bonus in first combat | `D1_INIT_BONUS = TRUE` |
| 6 | If "not ready": | Return to world map, can re-enter anytime | No penalty |

### Event Flags
- `D1_ENTERED = TRUE`
- `SCENE_003_COMPLETE = TRUE`

---

## SCENE 004: "THE BLOOM AWAKENS" (D1 Boss Intro)
**Location:** Ruins of Ashveil - Boss Chamber  
**Time:** Indeterminate (interior)

### Staging
- Massive plant-beast hybrid rooted to ceiling
- Relic pedestal visible behind boss
- Growth energy pulsing through roots

### Characters Present
- Full party (Kade, Twist, any recruits)
- **BOSS:** The Bloom (Lieutenant of Growth)

### Scene Beats

| Beat | Action | Dialogue | Combat |
|------|--------|----------|--------|
| 1 | Enter chamber | [SFX: Organic rumbling, wet growth sounds] | Boss dormant |
| 2 | Approach | The Bloom stirs | Pre-boss checkpoint |
| 3 | Boss awakens | THE BLOOM: "Root. Feed. Spread." | Boss intro animation |
| 4 | Combat start | "It doesn't negotiate. Good." | BATTLE: The Bloom |
| 5 | At 50% HP | THE BLOOM: "Growth... cannot... be... pruned..." | Phase shift - spawns adds |
| 6 | At 10% HP | THE BLOOM: "The... seed... remains..." | Enrage mode |

### Post-Combat

| Beat | Action | Dialogue | Rewards |
|------|--------|----------|---------|
| 7 | Defeat | The Bloom dissolves into spores | EXP, items |
| 8 | Relic revealed | "That's... what we came for?" | Growth Relic visible |
| 9 | Approach pedestal | Twist: "Should we touch it?" | **CHOICE: Touch / Wait / Examine** |
| 10 | Touch relic | Relic bonds to Kade | `RELIC_GROWTH_ACQUIRED = TRUE` |

### Event Flags
- `D1_CLEARED = TRUE`
- `THE_BLOOM_DEFEATED = TRUE`
- `RELIC_GROWTH_ACQUIRED = TRUE`
- `SCENE_004_COMPLETE = TRUE`

---

## SCENE 005: "FIRST SEATING"
**Location:** Ashveil Sanctuary - Hidden Chamber  
**Time:** Evening

### Staging
- Secret basement revealed by Sanctuary Keeper
- Prime Pedestal (inactive, awaiting relic)
- Ancient technology interface

### Characters Present
- Kade, Twist
- Sanctuary Keeper

### Scene Beats

| Beat | Action | Dialogue | VFX |
|------|--------|----------|-----|
| 1 | Descend stairs | Keeper: "We wondered when someone worthy would come." | Ancient lights activate |
| 2 | See pedestal | "This is older than the ruins. Older than Dominion." | Prime technology reveal |
| 3 | Insert relic | **CHOICE: Seat the relic / Ask more questions / Refuse** | |
| 4 | If "seat": | Relic glows, locks into place | Foundation energy surge |
| 5 | Seating complete | "One of eight. The Lattice acknowledges." | `RELIC_GROWTH_SEATED = TRUE` |
| 6 | World shift | [SFX: Deep harmonic resonance] | Brief world tremor |

### Event Flags
- `FIRST_RELIC_SEATED = TRUE`
- `RELIC_GROWTH_SEATED = TRUE`
- `SCENE_005_COMPLETE = TRUE`
- `ACT1_PROGRESS = 1`

### Transition
Korr tracks Kade to Ashveil - Sets up Scene 006

---

## SCENE 006: "THE MARSHAL ARRIVES"
**Location:** Ashveil Sanctuary - Entrance  
**Time:** Night

### Staging
- Dominion airship overhead (not attacking, observing)
- Korr approaches alone, hands visible, weapon sheathed
- Tense standoff with Kade

### Characters Present
- Kade, Twist
- **Korr** (first appearance)

### Scene Beats

| Beat | Action | Dialogue | Tension |
|------|--------|----------|---------|
| 1 | Airship arrives | [SFX: Airship engines, spotlight] | High alert |
| 2 | Korr descends | "Marshal Nadia Korr. I'm not here to arrest you." | Unexpected approach |
| 3 | **CHOICE POINT:** | **"Then why are you here?" / "I don't believe you" / "Leave us alone"** | |
| 4 | Korr responds | "I'm here because my superiors are wrong. About the relics. About everything." | Character reveal |
| 5 | Proposal | "I know where the next one is. You need a guide. I need... redemption." | Recruitment offer |
| 6 | **CHOICE:** | **Accept her help / Reject her / Demand proof** | |

### Branch: Accept
- Korr joins party
- `KORR_JOINED = TRUE`
- Access to Dominion intel

### Branch: Reject
- Korr leaves but follows at distance
- `KORR_WATCHING = TRUE`
- Re-recruitment opportunity later

### Branch: Proof
- Korr shares D2 location info
- `D2_LOCATION_REVEALED = TRUE`
- Trust +1 with Korr

### Event Flags
- `SCENE_006_COMPLETE = TRUE`
- `KORR_INTRODUCED = TRUE`

---

## SCENE 007: "D2 ENTRY - THE FUNGAL DEPTHS"
**Location:** Fungal Depths - Entrance  
**Time:** Day

### Staging
- Swamp atmosphere, spore clouds
- Motion Foundation instability (gravity fluctuations)
- Previous expedition corpses visible

### Characters Present
- Party (Kade, Twist, [Korr])
- [Ambient: Dead adventurers]

### Scene Beats

| Beat | Action | Dialogue | Mechanics |
|------|--------|----------|-----------|
| 1 | Arrival | Renna: "Swamps. The planet's armpit." | If Renna recruited |
| 2 | Gravity shift | Nix: "Motion frequency unstable." | If Nix recruited |
| 3 | See bodies | "Another salvage team. Dead." | Warning |
| 4 | **CHOICE:** | **Search bodies / Press on / Return** | |
| 5 | If search: | Find map fragment revealing D2 shortcut | `D2_SHORTCUT_UNLOCKED = TRUE` |
| 6 | Entry | [SFX: Wet, organic sounds, gravity shifts] | Dungeon begins |

### Event Flags
- `D2_ENTERED = TRUE`
- `SCENE_007_COMPLETE = TRUE`

---

## SCENE 008: "THE SPOROCYTE UNVEILED" (D2 Boss)
**Location:** Fungal Depths - Boss Chamber  
**Time:** Interior

### Staging
- Massive fungal colony with central nervous structure
- Spore clouds thick as fog
- Relic pedestal embedded in central mass

### Characters Present
- Full party
- **BOSS:** The Sporocyte (Lieutenant of Motion)

### Scene Beats

| Beat | Action | Dialogue | Combat |
|------|--------|----------|--------|
| 1 | Enter | [SFX: Spore release, wet pulse] | Atmosphere thick |
| 2 | Central approach | Spores form patterns - almost intelligent | Puzzle hint |
| 3 | Boss reveals | THE SPOROCYTE: [Telepathic] "Movement... is... change..." | Boss intro |
| 4 | Combat | Gravity shifts throughout fight | Mechanic: Variable gravity |
| 5 | 50% HP | Spore clones split off | Adds phase |
| 6 | 10% HP | "Change... cannot... be... stopped..." | Final attack |
| 7 | Defeat | Colony collapses, revealing relic | `RELIC_MOTION_ACQUIRED = TRUE` |

### Event Flags
- `D2_CLEARED = TRUE`
- `THE_SPOROCYTE_DEFEATED = TRUE`
- `RELIC_MOTION_SEATED = TRUE` (after seating scene)
- `SCENE_008_COMPLETE = TRUE`
- `ACT1_PROGRESS = 2`

---

## SCENE 009-019: [Additional Act I Scenes]
*Note: Following the same structure for D3 (Crystal Caverns - Light) and D4 (Skyspire Temple - Heat)*

### Key Flag Milestones

| Scene | Flag Set | Significance |
|-------|----------|--------------|
| 009 | `D3_ENTERED = TRUE` | Renna recruitment opportunity |
| 010 | `THE_PRISM_DEFEATED = TRUE` | Light Relic acquired |
| 011 | `RELIC_LIGHT_SEATED = TRUE` | Mount system unlock |
| 012 | `D4_ENTERED = TRUE` | Suresh recruitment |
| 013 | `THE_INFERNO_DEFEATED = TRUE` | Heat Relic acquired |
| 014 | `CATASTROPHE_TRIGGER = TRUE` | **WORLD BREAK EVENT** |
| 015 | `RELIC_HEAT_SEATED = TRUE` | Omega Pedestals revealed |
| 016 | `WORLD_BREAK_EVENT = TRUE` | Orion destabilizes |
| 017 | `SKY_WRONG = TRUE` | Visual world shift |
| 018 | `NEW_MONSTERS_APPEAR = TRUE` | Encounter tables change |
| 019 | `ACT1_COMPLETE = TRUE` | Transition to Act II |

---

# ACT II: RECOVERY (Dungeons 5-8)

---

## SCENE 020: "ASH AND ORDERS" (Act II Opener)
**Location:** Shattered Badlands  
**Time:** Pre-Dawn

### Staging
- Post-Catastrophe landscape
- Wrong sky (eclipse-like permanent state)
- Korr and Kade tension

### Characters Present
- Kade, Korr, Twist, [other Act I recruits]

### Scene Beats

| Beat | Action | Dialogue | Impact |
|------|--------|----------|--------|
| 1 | March through ash | Korr: "Four seated. Four still out there." | Mission focus |
| 2 | Kade confronts | "You knew this would happen. The World Break." | Trust test |
| 3 | **CHOICE:** | **"Did you?" / "Doesn't matter now" / "I trusted you"** | Korr affinity |
| 4 | Korr's truth | "I suspected. The Dominion files... they called it 'recalibration.'" | Lore reveal |
| 5 | New goal | "We find the rest. We stabilize Orion. We don't let them reset everything." | Act II motivation |

### Event Flags
- `ACT2_STARTED = TRUE`
- `SCENE_020_COMPLETE = TRUE`
- `PRIME_PEDESTALS_REVEALED = TRUE`

---

## SCENE 021-039: [Act II Dungeon Scenes]

### D5: Abyssal Trench (Tide)
- `D5_ENTERED = TRUE`
- Marinus recruitment
- `THE_DEPTHCALLER_DEFEATED = TRUE`
- `RELIC_TIDE_SEATED = TRUE`
- `AQUATIC_TRAVEL_UNLOCKED = TRUE`
- `SUNKEN_CITY_DISCOVERED = TRUE`

### D6: Obsidian Quarry (Mass)
- `D6_ENTERED = TRUE`
- Grit recruitment
- `THE_COLOSSUS_DEFEATED = TRUE`
- `RELIC_MASS_SEATED = TRUE`
- `DRAGONS_GRAVEYARD_UNLOCKED = TRUE`

### D7: Frozen Citadel (Time)
- `D7_ENTERED = TRUE`
- `ELDER_MORDAI_DEFEATED = TRUE`
- `RELIC_TIME_SEATED = TRUE`
- `CHRONOWAKE_UNLOCKED = TRUE`

### D8: Void Nexus (Shadow)
- `D8_ENTERED = TRUE`
- Vex/Sova recruitment resolution
- `THE_VOIDHOUND_DEFEATED = TRUE`
- `RELIC_SHADOW_SEATED = TRUE`
- `ECLIPSE_CONFLUENCE_DISCOVERED = TRUE`
- `TOWER_UNLOCKED = TRUE`

---

## SCENE 040: "ALL EIGHT"
**Location:** Eclipse Confluence - Central Platform  
**Time:** Eclipse Peak

### Staging
- All eight relics seated in Prime Pedestals
- The Tower visible, door opening
- Party assembled (up to 13 characters)

### Characters Present
- **ALL 13 PARTY MEMBERS** (if recruited)
- Full assembly

### Scene Beats

| Beat | Action | Dialogue | VFX |
|------|--------|----------|-----|
| 1 | Final seating | [SFX: All eight harmonics resonating] | Light pillars converge |
| 2 | Tower opens | "It's... inviting us." | Tower door animation |
| 3 | Pre-ascent | Each present character gets one line | Character moments |
| 4 | Kade speech | **CHOICE: "We end this" / "We save Orion" / "We fight together"** | Motive declaration |
| 5 | Approach | Party walks toward Tower | Epic shot setup |

### Event Flags
- `ALL_RELICS_SEATED = TRUE`
- `TOWER_GATE_OPEN = TRUE`
- `ACT2_COMPLETE = TRUE`
- `ACT3_AVAILABLE = TRUE`
- `SCENE_040_COMPLETE = TRUE`

---

# ACT III: ASCENSION (Tower + Final Palace)

---

## SCENE 041-093: [Tower Floors 1-99]

### Structure
- Every 10 floors: Major scene
- Boss floors (10, 25, 50, 75, 90, 100): Extended scenes
- Captain floors (15, 35, 55, 65, 85, 95): Character development

### Key Flags

| Floor | Flag | Content |
|-------|------|---------|
| 10 | `DAX_KAINE_DEFEATED = TRUE` | First boss |
| 25 | `YAKOV_THORNE_DEFEATED = TRUE` | Second boss |
| 50 | `MERCER_DEFEATED = TRUE` | Triumvirate confrontation |
| 75 | `SENTINEL_DEFEATED = TRUE` | Third boss |
| 90 | `VOID_ARCHITECT_DEFEATED = TRUE` | Fourth boss |
| 95 | `SEAM_WARDEN_PRIME_DEFEATED = TRUE` | Final captain |
| 100 | `ALEXANDER_GATE_DEFEATED = TRUE` | Gate guardian |

---

## SCENE 094: "THE PROGENITOR ENGINE"
**Location:** Final Palace - Floor 5  
**Time:** The Final Moment

### Staging
- Massive ancient machine
- The Engine at center
- All eight Foundation energies converging

### Characters Present
- Full party (all 13 if recruited)

### Scene Beats

| Beat | Action | Dialogue | Combat |
|------|--------|----------|--------|
| 1 | Enter chamber | [SFX: Machine hum at cosmic scale] | Atmosphere |
| 2 | Engine speaks | PROGENITOR ENGINE: "You have seated the Foundations. The reset can proceed." | Boss intro |
| 3 | Kade refuses | "We're not letting you erase everything." | |
| 4 | Engine explains | "I do not erase. I maintain. Orion will decay without reset." | Moral complexity |
| 5 | **CHOICE:** | **"We fight" / "Is there another way?" / "What if we stabilize instead?"** | Affects ending |
| 6 | Combat begins | 8-phase final battle | Final boss fight |
| 7 | Phase 8 | Engine weakens | Collapse mechanic |
| 8 | Final blow | "Perhaps... a new path... is possible..." | Victory |

### Ending Branches

| Choice | Ending | Flag |
|--------|--------|------|
| Fight | ENDING_FREE_PRIME | Prime is freed, Orion stabilizes organically |
| Alternative | ENDING_NEGOTIATE | Partial reset, preserved memories |
| Stabilize | ENDING_ANCHOR | Party becomes new Progenitors |

### Event Flags
- `FINAL_PALACE_CLEARED = TRUE`
- `PROGENITOR_ENGINE_DEFEATED = TRUE`
- `GAME_COMPLETE = TRUE`
- `ENDING_[TYPE]_ACHIEVED = TRUE`

---

## SCENE 095: "EPILOGUE"
**Location:** Varies by ending  
**Time:** "Tomorrow"

### Event Flags Set
- `EPILOGUE_ACTIVE = TRUE`
- `POSTGAME_UNLOCKED = TRUE`
- `NEW_GAME_PLUS_AVAILABLE = TRUE`

---

# FLAG REFERENCE MASTER LIST

## Progression Flags

| Flag | Set When | Used For |
|------|----------|----------|
| `GAME_START` | Scene 000 | Tutorial triggers |
| `PROLOGUE_WATCHED` | Scene 000 | Skip option on NG+ |
| `ACT1_STARTED` | Scene 001 | Chapter display |
| `ACT2_STARTED` | Scene 020 | Chapter display, world state |
| `ACT3_STARTED` | Scene 041 | Chapter display |
| `GAME_COMPLETE` | Scene 094 | Credits, postgame, NG+ |

## Relic Flags

| Flag | Set When | Significance |
|------|----------|--------------|
| `RELIC_GROWTH_ACQUIRED` | D1 Boss | Inventory |
| `RELIC_GROWTH_SEATED` | Scene 005 | First Prime Pedestal |
| `RELIC_MOTION_ACQUIRED` | D2 Boss | Inventory |
| `RELIC_MOTION_SEATED` | D2 Post | World state |
| `RELIC_LIGHT_ACQUIRED` | D3 Boss | Inventory, mount unlock |
| `RELIC_LIGHT_SEATED` | D3 Post | Mount system |
| `RELIC_HEAT_ACQUIRED` | D4 Boss | Inventory |
| `RELIC_HEAT_SEATED` | D4 Post | Catastrophe trigger |
| `RELIC_TIDE_ACQUIRED` | D5 Boss | Inventory |
| `RELIC_TIDE_SEATED` | D5 Post | Aquatic travel |
| `RELIC_MASS_ACQUIRED` | D6 Boss | Inventory |
| `RELIC_MASS_SEATED` | D6 Post | Dragon's Graveyard |
| `RELIC_TIME_ACQUIRED` | D7 Boss | Inventory |
| `RELIC_TIME_SEATED` | D7 Post | Chronowake |
| `RELIC_SHADOW_ACQUIRED` | D8 Boss | Inventory |
| `RELIC_SHADOW_SEATED` | D8 Post | Tower unlock |

## Dungeon Clear Flags

| Flag | Set When | Unlocks |
|------|----------|---------|
| `D1_CLEARED` | Scene 004 | Korr recruitment, sidequests |
| `D2_CLEARED` | Scene 008 | Renna recruitment |
| `D3_CLEARED` | Scene 011 | Mounts, Nix recruitment |
| `D4_CLEARED` | Scene 014 | Catastrophe, Suresh recruitment |
| `D5_CLEARED` | Scene 025 | Aquatic travel, Marinus |
| `D6_CLEARED` | Scene 028 | Grit recruitment |
| `D7_CLEARED` | Scene 032 | Time travel elements |
| `D8_CLEARED` | Scene 036 | Tower access |

## Party Recruitment Flags

| Flag | Character | Recruitment Scene |
|------|-----------|-------------------|
| `TWIST_JOINED` | Twist | Scene 001 |
| `KORR_JOINED` | Korr | Scene 006 |
| `RENNA_JOINED` | Renna | Scene 009 |
| `NIX_JOINED` | Nix-7 | Scene 011 |
| `SURESH_JOINED` | Suresh | Scene 012 |
| `CALLUM_JOINED` | Callum | Scene 015 |
| `ASHKA_JOINED` | Ashka | Scene 018 |
| `MARINUS_JOINED` | Marinus | Scene 025 |
| `GRIT_JOINED` | Grit | Scene 028 |
| `SENNA_JOINED` | Senna | Scene 031 |
| `PETRA_JOINED` | Petra | Scene 033 |
| `VEX_JOINED` | Vex | Scene 036 |
| `SOVA_JOINED` | Sova | Scene 037 |

## Boss Defeat Flags

| Flag | Boss | Location |
|------|------|----------|
| `THE_BLOOM_DEFEATED` | The Bloom | D1 |
| `THE_SPOROCYTE_DEFEATED` | The Sporocyte | D2 |
| `THE_PRISM_DEFEATED` | The Prism | D3 |
| `THE_INFERNO_DEFEATED` | The Inferno | D4 |
| `THE_DEPTHCALLER_DEFEATED` | The Depthcaller | D5 |
| `THE_COLOSSUS_DEFEATED` | The Colossus | D6 |
| `ELDER_MORDAI_DEFEATED` | Elder Mordai | D7 |
| `THE_VOIDHOUND_DEFEATED` | The Voidhound | D8 |
| `DAX_KAINE_DEFEATED` | Dax Kaine | Tower F10 |
| `YAKOV_THORNE_DEFEATED` | Yakov Thorne | Tower F25 |
| `MERCER_DEFEATED` | Mercer | Tower F50 |
| `SENTINEL_DEFEATED` | Sentinel | Tower F75 |
| `VOID_ARCHITECT_DEFEATED` | Void Architect | Tower F90 |
| `ALEXANDER_GATE_DEFEATED` | Alexander | Tower F100 |
| `PROGENITOR_ENGINE_DEFEATED` | Progenitor Engine | Final Palace |

## World State Flags

| Flag | Set When | Effect |
|------|----------|--------|
| `WORLD_BREAK_EVENT` | Scene 014 | Sky changes, new enemies |
| `SKY_WRONG` | Scene 014 | Visual overlay active |
| `ECLIPSE_OVERLAY_ACTIVE` | D8 | Eclipse visual state |
| `RIFT_SUPPRESSED` | Post-Palace | Post-game world state |
| `AQUATIC_TRAVEL_UNLOCKED` | D5 | Underwater exploration |
| `SUNKEN_CITY_DISCOVERED` | D5 | Hidden area access |
| `DRAGONS_GRAVEYARD_UNLOCKED` | D6 | Hidden area access |
| `CHRONOWAKE_UNLOCKED` | D7 | Fast travel hub |
| `TOWER_UNLOCKED` | D8 | Endgame content |
| `REMNANT_VAULT_UNLOCKED` | Post-game | Superboss content |

## Choice/Consequence Flags

| Flag | Set When | Affects |
|------|----------|---------|
| `D1_STEALTH_BONUS` | Scene 003 | D1 first encounter |
| `D1_INIT_BONUS` | Scene 003 | D1 first encounter |
| `KORR_TRUST_HIGH` | Scene 006 | Korr loyalty |
| `KORR_WATCHING` | Scene 006 | Re-recruitment |
| `COLOSSUS_MERCY` | D6 | D6 moral choice |
| `ENDING_FREE_PRIME` | Final | Epilogue variant |
| `ENDING_ANCHOR` | Final | Epilogue variant |
| `ENDING_NEGOTIATE` | Final | Epilogue variant |

## Post-Game Flags

| Flag | Set When | Unlocks |
|------|----------|---------|
| `POSTGAME_UNLOCKED` | Scene 095 | Remnant Vault, super bosses |
| `NEW_GAME_PLUS_AVAILABLE` | Scene 095 | NG+ mode |
| `AETHERREACH_ROUTE_OPEN` | Post-Palace | Sky hub access |
| `FINAL_ECLIPSE_GATE_OPEN` | Vault clear | True ending access |

---

# SCENE COUNT SUMMARY

| Act | Scenes | Key Flags |
|-----|--------|-----------|
| Prologue | 1 | 3 |
| Act I | 19 | 35 |
| Act II | 20 | 42 |
| Act III | 55 | 78 |
| **TOTAL** | **95 scenes** | **158 flags** |

---

# NEXT STEPS FOR IMPLEMENTATION

1. Expand each scene with full dialogue
2. Define camera angles and staging markers
3. Implement flag system in game engine
4. Create conditional dialogue trees
5. Build quest journal integration
