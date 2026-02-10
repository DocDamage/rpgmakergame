# HALCYON FREEPORT - Town Map Sheet

## Map Specifications
- **Map ID:** T_HALCYON_112x72
- **Display Name:** Halcyon Freeport
- **Map Size:** 112×72 tiles (16px/tile) = 1792×1152px
- **Purpose:** Neutral coastal freeport, refugee rebuild hub, postgame market
- **Location:** Eastern Continent, southern coast
- **Level Range:** 80-150 (postgame accessible)
- **Story Phase:** Unlocked after D8 Void Nexus cleared, before Tower access

## Town Overview

Halcyon Freeport is a rebuilt coastal settlement that emerged after the world break. Originally a Dominion military port, it was abandoned and claimed by refugees, merchants, and Ironhawk remnants. Now serves as neutral ground where survivors trade, rebuild, and plan for the future. The town represents hope amid chaos—a space where former enemies can coexist under pragmatic truce.

---

## Layout Zones

### North Docks (Coordinates: 8-32, 8-24)
- **Description:** Main pier with trading vessels, cargo platforms, fishing nets
- **NPCs:** Harbormaster, Dock workers (4), Merchants (3)
- **Services:** None (transition zone)
- **Connections:** North edge to sea routes (overworld fast travel)
- **Atmosphere:** Salty air, creaking ships, gulls, bustling activity

### Market Plaza (Coordinates: 32-72, 24-48)
- **Description:** Open-air market with vendor stalls, fountain centerpiece, merchant tents
- **NPCs:** Vendors (8), Broker Vane (night only), Travelers (3)
- **Services:** Advanced item shop, rare materials vendor
- **Connections:** All major town zones converge here
- **Atmosphere:** Vibrant, colorful, bargaining, trade-focused

### Ironhawk Quarter (Coordinates: 8-40, 48-64)
- **Description:** Former Dominion military safehouse, now neutral syndicate territory
- **NPCs:** Ex-syndicate members (5), Bounty clerks (2)
- **Services:** Bounty board (postgame hunts), black market access, information broker
- **Connections:** Secret passage to hideout interior, hidden from main streets
- **Atmosphere:** Dark, secretive, dangerous edge, shadows and whispered deals

### Refuge District (Coordinates: 40-72, 48-72)
- **Description:** Tent city, temporary housing, medical tents, supply depot
- **NPCs:** Refugee families (8), Medics (2), Aid workers (2)
- **Services:** Free healing point (no purchase needed), rest area, community center
- **Connections:** Inn interior, clinic interior, supply tents
- **Atmosphere:** Hopeful but weary, communal, aid-focused, makeshift but organized

### Lighthouse Point (Coordinates: 88-112, 8-40)
- **Description:** Active lighthouse, lookout tower, signal station, beacon light
- **NPCs:** Lighthouse keeper, Scouts (2)
- **Services:** Fast travel unlock, quest board, hidden staircase to dungeon
- **Connections:** Lighthouse interior (optional challenge dungeon)
- **Atmosphere:** Isolated, elevated, clear views of horizon, peaceful and contemplative

---

## NPC List

### Story-Critical NPCs

**1. Broker Vane** (Ironhawk elder, information dealer)
- **Location (Day):** Ironhawk Quarter hideout interior
- **Location (Night):** Market Plaza (18:00-06:00)
- **Role:** Postgame quest giver, Remnant Vault unlock trigger
- **Dialog Tree:** DT_VANE_HALCYON
- **Quests:** Q_REMNANT_VAULT_UNLOCK
- **Notes:** Appears only after Tower Floor 100 completion

**2. Captain Ressa Vane** (Tower Captain F15, if player allowed her to survive)
- **Location:** Lighthouse Point
- **Appears:** Post-Tower completion only
- **Role:** Optional rematch boss, secret challenge
- **Dialog Tree:** DT_RESSA_POSTGAME
- **Quest:** Q_TOWER_CAPTAIN_REMATCH
- **Notes:** Conditional appearance (only if spared during Tower Floor 15)

**3. Harbormaster "Kellan Frost"** (Port administrator)
- **Location:** North Docks (always available, day and night)
- **Role:** Port services, ship travel information, coastal quests
- **Dialog Tree:** DT_KELLAN_HARBOR
- **Services:** Fast travel by ship, ferry routes information

### Utility NPCs

**4. Innkeeper "Mira Halcyon"** (Refuge District)
- **Services:** Inn rooms (200 Gil), save point, party management
- **Interior:** I_HALCYON_INN
- **Notes:** Named after the town's founding hope

**5. Item Vendor "Salen Korr"** (Market Plaza)
- **Services:** Postgame consumables, rare items
- **Shop ID:** SHOP_HALCYON_ITEMS
- **Stock:** Mega-Potions, Ethers, Phoenix Downs, rare status cure items

**6. Weapon Vendor "Thane Vex"** (Market Plaza)
- **Services:** Legendary weapons, Tower reward integration
- **Shop ID:** SHOP_HALCYON_WEAPONS
- **Stock:** All Tier 5 Legendary weapons (character-specific, 50,000 Gil each)
- **Unlock:** Tower Floor 50+ completion required

**7. Material Trader "Nessa Quill"** (Market Plaza)
- **Services:** Crafting materials, rare dungeon drops
- **Shop ID:** SHOP_HALCYON_MATERIALS
- **Stock:** Void Shards, Progenitor Fragments, Relic Dust, Foundation Essences

### Flavor NPCs (12 ambient population)
- 4× Dock workers (North Docks) - varied animation sets
- 5× Market vendors (Market Plaza) - selling various goods
- 3× Refugees (Refuge District) - sitting, conversing, grateful

---

## Shop Contents & Economy

### SHOP_HALCYON_ITEMS (Salen Korr)
**Tier:** Postgame (high prices, premium quality)

| Item | Cost | Effect |
|------|------|--------|
| Mega-Potion | 500 Gil | Restore 100% HP to single ally |
| Mega-Ether | 500 Gil | Restore 100% MP to single ally |
| Elixir | 1000 Gil | Restore 100% HP and MP to single ally |
| Phoenix Down | 300 Gil | Revive KO'd ally with 50% HP |
| Remedy Plus | 200 Gil | Cure all status effects on one ally |
| Smoke Bomb | 150 Gil | Guaranteed escape from battle |

### SHOP_HALCYON_WEAPONS (Thane Vex)
**Tier:** Legendary (Tier 5 - Maximum progression)
**Unlock Requirement:** Tower Floor 50+ completion

| Character | Weapon | Cost | Special Effect |
|-----------|--------|------|-----------------|
| Kade | Sovereign Edge (Gunblade) | 50,000 Gil | Drain 10% damage as HP |
| Nix-7 | Lattice Resonator (Arm-Caster) | 50,000 Gil | +30% spell damage |
| Renna | Vortex Cannon (Rifle) | 50,000 Gil | Chain lightning on hit |
| Suresh | Vitalis Staff | 50,000 Gil | +25% healing output |
| Twist | Void Dagger | 50,000 Gil | 50% crit chance |
| Sova | Prism Rod | 50,000 Gil | +50% elemental damage |
| Grit | Earthbreaker (Greatsword) | 50,000 Gil | Heavy armor penetration |
| Ashka | Starbow | 50,000 Gil | Infinite ammo, multi-hit |
| Senna | Transcendent Fists (Claws) | 50,000 Gil | 3x combo on basic attack |
| Callum | Draconic Scepter | 50,000 Gil | Summons cost 50% less MP |
| Petra | Incarnate Axe | 50,000 Gil | Scales with mutations |
| Vex | Holy Judgment (Sword) | 50,000 Gil | Heals on hit |

### SHOP_HALCYON_MATERIALS (Nessa Quill)
**Tier:** Rare crafting materials for postgame synthesis

| Material | Cost | Source/Use |
|----------|------|-----------|
| Void Shard | 5,000 Gil | Progenitor Engine battle reward; crafts shadow items |
| Progenitor Fragment | 10,000 Gil | Final Palace; crafts ultimate armor |
| Relic Dust | 2,000 Gil | All Prime Pedestal locations; general upgrades |
| Foundation Essence (set of 8) | 2,000 Gil each | One per Foundation; specialized crafting |
| Celestial Thread | 8,000 Gil | Remnant Vault; rare equipment enhancement |

---

## Interiors

### I_HALCYON_INN (40x28)
- **Innkeeper:** Mira Halcyon
- **Features:**
  - Save point (dialogue option)
  - Rest (500 Gil per room)
  - Party management terminal (resync party, change equipment)
  - Bar area (barkeep NPC with rumors/hints)
  - Private rooms upstairs (implied, not explorable)
- **Atmosphere:** Warm lanterns, comfortable despite makeshift construction
- **Connections:** Main town square

### I_HALCYON_HIDEOUT (32x24)
- **Location:** Accessed from Ironhawk Quarter secret passage
- **Key NPCs:** Broker Vane (office), Syndicate members
- **Features:**
  - Broker's office (quest giver, information)
  - Quest board (postgame hunt jobs)
  - Black market merchant (illegal items for sidequests)
  - Map wall (showing Remnant Vault location hint)
- **Atmosphere:** Dark, secretive, conspiracy-like
- **Connections:** Hidden entrance from Ironhawk Quarter

### I_HALCYON_LIGHTHOUSE (24x48, vertical tower)
- **Keeper:** Lighthouse keeper (optional quest giver)
- **Features:**
  - Lower level: Keeper's quarters, equipment storage
  - Mid level: Lens mechanism, light control (interactive)
  - Upper level: Lookout point (reveals overworld secrets when examined)
  - Basement: Hidden staircase to optional Lighthouse Dungeon
- **Atmosphere:** Isolated, peaceful, commanding view
- **Connections:** Descends to optional challenge dungeon below

---

## Quest Triggers

### Q_REMNANT_VAULT_UNLOCK
- **Quest Giver:** Broker Vane (Ironhawk hideout)
- **Trigger Condition:** Player completes Tower Floor 100
- **Reward:** Remnant Vault location unlocked, fast travel added
- **Narrative:** Vane explains the Vault exists and offers to mark the location
- **Significance:** Postgame endgame content unlock

### Q_TOWER_CAPTAIN_REMATCH (Conditional)
- **Quest Giver:** Captain Ressa Vane (Lighthouse Point)
- **Trigger Condition:** Tower Floor 15 defeat (player spared her), then visit Lighthouse
- **Reward:** Unique Accessory: "Captain's Insignia" (+10% all stats)
- **Battle:** Full rematch with upgraded stats and new moves
- **Narrative:** Ressa seeks honorable combat, proves she's changed sides

### Q_LIGHTHOUSE_SECRETS
- **Quest Giver:** Lighthouse keeper
- **Trigger Condition:** Investigate lighthouse at night, examine lens mechanism
- **Objective:** Discover hidden signal pattern
- **Reward:** Legendary Summon unlock (varies based on player choice earlier)
- **Narrative:** Previous character arcs converge through lighthouse beacon

---

## World Connections

### Map Exits
- **North (Overworld):** Sea routes, fast travel by ship
- **East:** Coastal road connects to Brinegate Port (Lv 80-90 route)
- **South:** Ruins path leads to Remnant Vault entrance (postgame, Lv 150+)
- **West:** Return to mainland overworld

### Fast Travel Integration
- Halcyon Freeport becomes 12th fast-travel point (after other 11 towns)
- Ship-based travel: Ferry to Brinegate Port every 3 in-game hours
- Unlocked after D8 Void Nexus clear

---

## Environmental Notes

### Weather & Atmosphere
- **Morning (6:00-12:00):** Coastal fog, damp air, fresh catch smells
- **Afternoon (12:00-18:00):** Clear skies, merchant bustle peaks, bright sunlight
- **Evening (18:00-22:00):** Golden sunset, lighthouse beam activates
- **Night (22:00-6:00):** Dark except lighthouse, quieter streets, shadow areas

### Music & Soundscape
- **Day Theme:** "Neutral Ground Theme" (peaceful, rebuilding tone)
- **Night Theme:** "Halcyon Dreams" (contemplative, hopeful)
- **Shop Areas:** Merchant chants, trading activity
- **Lighthouse:** Ambient wind, beacon creaking

### Lighting
- **Primary:** Warm lanterns throughout (recovered Dominion infrastructure)
- **Secondary:** Lighthouse beam (sweeps every 10 seconds, interactive light mechanic)
- **Special:** Reflected light on water (docks shimmer)

---

## Story Integration & Significance

### Location Unlock
- **When:** After D8 Void Nexus cleared, before Tower access
- **Why:** Safe haven where party can recover and prepare for final ascent
- **Theme:** Neutral ground representing hope for cooperation after world break

### Postgame Hub Function
- Serves as base of operations for:
  - Remnant Vault quests (3 wings, tower-like structure)
  - Tower progression check-ins with Ressa (if spared)
  - Legendary gear acquisition (completing final progression)
  - Character epilogues (informal scenes in various locations)

### NPC Significance
- **Broker Vane:** Represents syndicate pragmatism and change
- **Ressa Vane:** Second chance/redemption (if player chose mercy)
- **Refugees/Medics:** Show world healing after break
- **Merchants:** Economic recovery symbol

### Thematic Role
- **Symbol:** Phoenix rising from ashes
- **Message:** Cooperation is possible; enemies can become allies
- **Gameplay:** Transition point between main story (urgent, linear) and postgame (optional, exploratory)

---

## Encounters & Level Scaling

### Random Encounters (Field Transitions)
- **Type:** Unlikely in town; possible on coastal approaches
- **Level Range:** 80-120 (postgame scaling active)
- **Monster Types:** Corrupted maritime creatures, Dominion remnants, void-touched wildlife

### No Story Bosses (Town proper is safe)
- **Exception:** Captain Ressa rematch (optional, triggered quest)
- **Safety:** Dominion presence minimal; Lattice stable in this region

---

## Production Status

| Element | Status | Notes |
|---------|--------|-------|
| Map layout | ✅ Defined | 5 major zones, clear connectivity |
| NPC roster | ✅ Complete | 7 story/utility NPCs, 12 ambient NPCs |
| Shop contents | ✅ Balanced | Tier 5 weapons, postgame materials |
| Interior sheets | ⚠️ Pending | I_HALCYON_INN, HIDEOUT, LIGHTHOUSE to be created |
| Dialog trees | ⚠️ Pending | DT_VANE_HALCYON, DT_RESSA_POSTGAME, others |
| Quest scripts | ⚠️ Pending | Q_REMNANT_VAULT_UNLOCK, rematch quest |

---

## Next Steps
1. Create interior map sheets for Inn, Hideout, Lighthouse
2. Write dialog trees for all story NPCs
3. Define quest scripts and triggers
4. Implement ambient NPC schedules (day/night movement)
5. Add weather/time-of-day visual variations
6. Connect to Fast Travel system

---

**Map Sheet Version:** 1.0
**Last Updated:** 2026-02-10
**Status:** Ready for implementation
