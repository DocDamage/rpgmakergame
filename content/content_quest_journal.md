# Chroma's Edge - Quest Journal + Objectives System
## Quest Tracking, Map Markers, and Player Guidance

---

# QUEST JOURNAL STRUCTURE

## Journal Categories

| Category | Icon | Description |
|----------|------|-------------|
| **Main Scenario** | ★ | Critical path story quests |
| **Character** | 👤 | Party member personal quests |
| **Side Quests** | ◆ | Optional quests by region |
| **Bounties** | ⚔️ | Combat/hunting quests |
| **Delivery** | 📦 | Item fetch quests |
| **Exploration** | 🗺️ | Discovery-based quests |

---

# QUEST DISPLAY FORMAT

## Active Quest Entry

```
┌─────────────────────────────────────────────────────────────┐
│  ★ THE RUINS OF ASHVEIL                          [Track]    │
│  Main Scenario • Act I • Recommended: Level 8-12            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  The Sanctuary Keeper believes the source of the Growth     │
│  corruption lies in the ancient ruins to the west. The      │
│  Dominion has already sent scouts—none returned.            │
│                                                             │
│  OBJECTIVES:                                                │
│  [✓] Speak to the Sanctuary Keeper                        │
│  [✓] Travel to the Ruins of Ashveil                       │
│  [►] Explore the ruins and find the source                │
│  [  ] Defeat the source of corruption                     │
│  [  ] Report back to the Sanctuary Keeper                │
│                                                             │
│  HINT:                                                      │
│  Look for paths that aren't completely overgrown.          │
│  The Growth seems to avoid certain ancient symbols.        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Rewards: 1500 XP • 500 G • Growth Relic                   │
│  Unlocks: Prime Pedestal Access • Mount System             │
└─────────────────────────────────────────────────────────────┘
```

## Completed Quest Entry

```
┌─────────────────────────────────────────────────────────────┐
│  ★ THE RUINS OF ASHVEIL                          [Replay]   │
│  Main Scenario • Act I • Completed: [Date]                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  You defeated The Bloom and claimed the Growth Relic.      │
│  The Sanctuary Keeper directed you to the Prime Pedestal   │
│  beneath the town, where the Relic now rests.              │
│                                                             │
│  COMPLETION NOTES:                                         │
│  • The Bloom was a Lieutenant of Growth Foundation         │
│  • First of eight Relics secured                           │
│  • Korr, a Dominion Marshal, has offered to join you       │
│                                                             │
│  Rewards Received:                                         │
│  ✓ 1500 XP • ✓ 500 G • ✓ Growth Relic                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# MAP MARKER SYSTEM

## Marker Types

| Marker | Icon | Color | Meaning |
|--------|------|-------|---------|
| Main Objective | ★ | Gold | Critical path target |
| Side Quest | ◆ | Blue | Optional objective |
| Bounty Target | ⚔️ | Red | Hunt/kill target |
| Delivery Point | 📍 | Green | Turn-in location |
| Search Area | ⭕ | Yellow | Investigation zone |
| Exit/Entry | 🚪 | White | Dungeon entrance |
| Fast Travel | ⚡ | Cyan | Unlocked warp point |

## Marker Behavior

### Distance-Based Display

```
If distance < 50m:    Marker visible on compass + world
If distance < 200m:   Marker visible on compass only
If distance > 200m:   Marker visible on map only
If in different zone: Marker hidden (quest text hints direction)
```

### Dynamic Markers

```
SEARCH AREA Behavior:
- Yellow circle pulses on map
- As player nears target, circle shrinks
- At 10m range, marker becomes precise point
- Text update: "You're close. Look carefully."

MULTI-TARGET Behavior:
- Show "3/5 remaining" on marker
- Update as targets completed
- Final target gets gold star overlay
```

---

# QUEST TRACKING LOGIC

## Auto-Track Rules

1. **Main Scenario** quests auto-track when accepted
2. **Only one** quest can be actively tracked at a time
3. **Character quests** auto-track when in correct zone
4. **Time-sensitive** quests override others
5. Player can manually track any active quest

## Contextual Hints

### Stuck Detection

```
If quest active for > 30 minutes with no progress:
  Show hint button in journal
  
If player in wrong zone:
  Hint: "This objective is in [Zone Name]. Try checking your map."
  
If player near but missed interaction:
  Hint: "Look for glowing objects or unusual features nearby."
  
If combat difficulty blocking progress:
  Hint: "This area may be dangerous. Consider leveling up or upgrading equipment."
```

### Proactive Guidance

```
On entering new zone with active quest:
  "[Quest Name] has objectives in this area."
  
On acquiring item needed for quest:
  "[Item Name] is needed for [Quest Name]."
  
On approaching quest NPC:
  "[NPC Name] is nearby and may have information about your current quest."
```

---

# MAIN SCENARIO QUEST JOURNAL

## ACT I: THE HUNT

### Quest: PROLOGUE - THE LATTICE DREAM
**Type:** Main Scenario (Unskippable)  
**Location:** N/A  
**Level:** 1

**Journal Entry:**
```
You saw... something. A voice speaking of Orion's instability.
Eight symbols. Eight Foundations. A warning, or a threat?

Then you woke up in the wreckage of a dusthawk, with no memory
of how you got there. Twist is nearby, unconscious. The Dominion
will be looking for survivors.

OBJECTIVES:
[►] Check on Twist
[  ] Find shelter from Dominion patrols
[  ] Reach Ashveil Sanctuary
```

---

### Quest: ASH AND KADE
**Type:** Main Scenario  
**Location:** Ashveil Region  
**Level:** 1-3

**Journal Entry:**
```
You and Twist survived the crash, but you're not safe yet.
Dominion patrols are sweeping the area. You need to find
shelter and figure out what's happening.

The Sanctuary Keeper at Ashveil might help—if you can reach it.

OBJECTIVES:
[✓] Wake Twist
[✓] Deal with Dominion scout
[►] Travel to Ashveil Sanctuary
[  ] Speak to the Sanctuary Keeper

HINT:
Stick to the low ground. The patrols' dusthawks have trouble
seeing through the ravines.

REWARDS:
• Twist joins party
• Access to Ashveil Sanctuary
• First equipment upgrade
```

---

### Quest: THE RUINS OF ASHVEIL (D1)
**Type:** Main Scenario • Dungeon  
**Location:** D1 - Ruins of Ashveil  
**Level:** 8-12

**Journal Entry:**
```
The Sanctuary Keeper believes something in the ancient ruins
is causing the Growth corruption spreading through the region.
Dominion scouts went in and never came out.

You'll need to be careful—the ruins are unstable, and whatever's
down there killed trained soldiers.

OBJECTIVES:
[✓] Learn of the ruins from the Keeper
[►] Enter the Ruins of Ashveil [Map Marker: West of Sanctuary]
[  ] Navigate to the deepest chamber
[  ] Defeat the source of corruption
[  ] Claim the Relic
[  ] Return to the Sanctuary

HINT:
The Growth seems to pulse with energy. Watch for patterns in
its movement—you might find safe paths through the overgrowth.

REWARDS:
• 1500 XP
• 500 G
• Growth Relic (Key Item)
• Access to Prime Pedestal
• Korr recruitment opportunity

UNLOCKS:
• Prime Pedestal system
• Next main quest: The Fungal Depths
```

---

### Quest: FIRST SEATING
**Type:** Main Scenario  
**Location:** Ashveil Sanctuary (Basement)  
**Level:** 12

**Journal Entry:**
```
You claimed the Growth Relic from The Bloom. Now the Sanctuary
Keeper reveals a secret beneath the town—a Prime Pedestal,
ancient technology that can "seat" the Relic and stabilize
its power.

This is only the first of eight. But it's a start.

OBJECTIVES:
[✓] Obtain Growth Relic
[►] Follow the Keeper to the basement
[  ] Place the Relic on the Prime Pedestal
[  ] Witness the Seating

HINT:
The Keeper seems nervous. Ask her what she's not telling you.

REWARDS:
• Growth Relic seated
• World map updates
• Korr offers to join party

UNLOCKS:
• D2: The Fungal Depths
• Mount system (post-D3)
```

---

### Quest: THE FUNGAL DEPTHS (D2)
**Type:** Main Scenario • Dungeon  
**Location:** D2 - Fungal Depths  
**Level:** 15-20

**Journal Entry:**
```
Korr's information points to the Fungal Depths—a swamp where
the Motion Foundation has gone unstable. Gravity itself is
wrong there. 

The second Relic awaits. So does something that used to be
a Dominion expedition team.

OBJECTIVES:
[✓] Learn D2 location from Korr
[►] Travel to Fungal Depths [Map Marker: Southeast marsh]
[  ] Navigate the gravity-shifting swamp
[  ] Defeat the Sporocyte
[  ] Claim the Motion Relic
[  ] Seat the Relic at a Prime Pedestal

HINT:
Gravity shifts follow patterns. Watch the spores—they float
in the direction gravity will shift next.

REWARDS:
• 2500 XP
• 800 G
• Motion Relic
• Renna recruitment opportunity

UNLOCKS:
• D3: Crystal Caverns
• Gravity manipulation puzzles
```

---

### Quest: THE CRYSTAL CAVERNS (D3)
**Type:** Main Scenario • Dungeon  
**Location:** D3 - Crystal Caverns  
**Level:** 25-32

**Journal Entry:**
```
The Light Foundation has fractured in the Crystal Caverns.
Prismridge miners reported impossible geometry and colors
that hurt to look at.

Renna insists on joining you—her engineering skills might
unravel the Light Foundation's puzzles. And she knows the
region better than anyone.

OBJECTIVES:
[✓] Recruit Renna (optional but recommended)
[✓] Learn D3 location
[►] Enter Crystal Caverns [Map Marker: Prismridge mines]
[  ] Solve the prism puzzles
[  ] Defeat The Prism
[  ] Claim the Light Relic
[  ] Seat the Relic

HINT:
Light behaves strangely here. Mirrors, prisms, and shadows
are your tools—and your obstacles.

REWARDS:
• 4000 XP
• 1200 G
• Light Relic
• Mount system unlocked
• Nix-7 recruitment opportunity

UNLOCKS:
• Mounts (Drakes, Nightmares, Striders)
• D4: Skyspire Temple
```

---

### Quest: THE SKYSPIRE TEMPLE (D4) - CATASTROPHE
**Type:** Main Scenario • Dungeon  
**Location:** D4 - Skyspire Temple  
**Level:** 38-45

**Journal Entry:**
```
Four Relics seated. Four to go. The Skyspire Temple holds
the Heat Relic—but the Dominion has fortified the area.
They're expecting you.

Suresh knows a back route through the cliffs. But even he
admits this will be the most dangerous ascent yet.

⚠️ WARNING: Quest completion triggers major world event.

OBJECTIVES:
[✓] Recruit Suresh (optional)
[✓] Learn D4 location
[►] Reach Skyspire Temple [Map Marker: Eastern mountains]
[  ] Breach Dominion defenses
[  ] Ascend the temple
[  ] Defeat The Inferno
[  ] Attempt to seat the Heat Relic

HINT:
The Dominion has anti-air cannons. You'll need to approach
on foot or find their blind spots.

⚠️ COMPLETING THIS QUEST WILL TRIGGER THE WORLD BREAK EVENT.
THE SKY WILL CHANGE. NEW ENEMIES WILL APPEAR.
SAVED GAMES CAN CONTINUE AFTER.

REWARDS:
• 6000 XP
• 2000 G
• Heat Relic
• CATASTROPHE TRIGGERED
• Callum and Ashka recruitment

UNLOCKS:
• Act II: Recovery
• Post-Break world state
• Omega Pedestals
```

---

## ACT II: RECOVERY

### Quest: ASH AND ORDERS
**Type:** Main Scenario  
**Location:** Shattered Badlands  
**Level:** 45

**Journal Entry:**
```
The World Break has happened. The sky is wrong—permanently
eclipsed, lit by wrong stars. Orion is destabilizing, and
the Progenitor Engine is preparing a "reset" that would
erase all life.

Four Relics remain, now at Omega Pedestals that have risen
from the earth. The clock is ticking.

OBJECTIVES:
[✓] Survive the World Break
[✓] Gather scattered party members
[►] Locate the first Omega Pedestal
[  ] Decide: D5, D6, D7, or D8 first?

HINT:
The Omega Pedestals appear on your map. Each leads to a
dungeon, but you can choose the order.
Recommended: D5 (Abyssal Trench) for aquatic travel unlock.

REWARDS:
• Act II begins
• New party members available
• World map expanded

UNLOCKS:
• D5-D8 dungeons
• Hidden areas (Sunken City, Dragon's Graveyard)
```

---

### Quest: THE ABYSSAL TRENCH (D5)
**Type:** Main Scenario • Dungeon  
**Location:** D5 - Abyssal Trench  
**Level:** 55-62

**Journal Entry:**
```
The Tide Foundation has collapsed beneath the ocean floor.
To reach it, you'll need submersible transport from Brinegate
Port—and nerves of steel.

Marinus, a strange being who claims to BE the tide, offers
to guide you. But his help comes with questions about the
nature of water, memory, and sacrifice.

OBJECTIVES:
[✓] Reach Brinegate Port
[✓] Acquire submersible
[►] Dive to Abyssal Trench [Map Marker: Offshore trench]
[  ] Navigate crushing depths
[  ] Defeat The Depthcaller
[  ] Claim and seat the Tide Relic

HINT:
Pressure is as much an enemy as monsters. Watch your
oxygen and depth gauges carefully.

REWARDS:
• 8000 XP
• 3000 G
• Tide Relic
• Aquatic travel unlocked
• Marinus joins party
• Sunken City discovered

UNLOCKS:
• Underwater exploration
• Sunken City (hidden area)
```

---

### Quest: THE OBSIDIAN QUARRY (D6)
**Type:** Main Scenario • Dungeon  
**Location:** D6 - Obsidian Quarry  
**Level:** 70-78

**Journal Entry:**
```
The Mass Foundation has created a gravity well in the
Obsidian Quarry—an entire mountain compressed into a space
the size of a village. Grit survived the collapse that
killed her crew. She'll guide you through, if you can
handle her guilt.

OBJECTIVES:
[✓] Reach Cinderstep
[✓] Recruit Grit
[►] Enter Obsidian Quarry [Map Marker: Cinderstep mines]
[  ] Navigate zero-gravity zones
[  ] Defeat The Colossus
[  ] CLAIM: Mercy kill or spare?
[  ] Claim and seat the Mass Relic

MORAL CHOICE:
The Colossus was once a person. Grit knew them.
Mercy: Quick death, Grit respects you
Spare: Colossus becomes hidden ally, Grit struggles

REWARDS:
• 10000 XP
• 4000 G
• Mass Relic
• Grit joins party
• Dragon's Graveyard unlocked

UNLOCKS:
• D7: Frozen Citadel
• Dragon's Graveyard (hidden area)
```

---

### Quest: THE FROZEN CITADEL (D7)
**Type:** Main Scenario • Dungeon  
**Location:** D7 - Frozen Citadel  
**Level:** 90-98

**Journal Entry:**
```
Time itself has frozen in the northern citadel. Elder Mordai,
keeper of the Time Foundation, has stopped his own death by
stopping time itself. To claim the Time Relic, you'll need
to convince him to start living again—or end his eternity.

Senna has family ties to the Citadel. Her knowledge may be
the key.

OBJECTIVES:
[✓] Reach Rimehold
[✓] Recruit Senna (optional but recommended)
[►] Enter Frozen Citadel [Map Marker: Northern peak]
[  ] Navigate time-frozen zones
[  ] Confront Elder Mordai
[  ] Defeat the Time Warden
[  ] Claim and seat the Time Relic

HINT:
Time flows differently in different rooms. Some doors lead
to the past. Some to possible futures. Pay attention to details.

REWARDS:
• 12000 XP
• 5000 G
• Time Relic
• Senna joins party (if not recruited)
• Chronowake Pier access

UNLOCKS:
• D8: Void Nexus
• Time manipulation mechanics
```

---

### Quest: THE VOID NEXUS (D8)
**Type:** Main Scenario • Dungeon  
**Location:** D8 - Void Nexus  
**Level:** 115-125

**Journal Entry:**
```
The final Relic. The Shadow Foundation has collapsed into
the Void Nexus, a place where light goes to die. Vex and
Sova both feel the pull of this place—one to seal it, one
to understand it.

The Tower has been visible for days, growing closer. After
this, there will be nowhere else to go but up.

OBJECTIVES:
[✓] Reach Eclipse Confluence
[✓] Resolve Vex/Sova tension (story scene)
[►] Enter Void Nexus [Map Marker: Convergence point]
[  ] Navigate absolute darkness
[  ] Defeat The Voidhound
[  ] Claim the Shadow Relic
[  ] Seat all eight Relics at the Confluence

HINT:
Light sources attract shadows here. Sometimes darkness is
safer than light. Trust your non-visual senses.

REWARDS:
• 15000 XP
• 6000 G
• Shadow Relic
• Vex and Sova join party
• Tower gate opens

UNLOCKS:
• Chroma Tower (Act III)
• Eclipse Confluence hub
```

---

## ACT III: ASCENSION

### Quest: THE CHROMA TOWER
**Type:** Main Scenario • Tower  
**Location:** Chroma Tower  
**Level:** 125+

**Journal Entry:**
```
All eight Relics are seated. The Tower has opened its gates.

One hundred floors stand between you and the Final Palace.
The Dominion Triumvirate has their own champions climbing
from the other side. Mercer waits at Floor 50, preaching
the end of all things.

This is it. The final climb.

OBJECTIVES:
[✓] Open the Tower gate
[►] Ascend Chroma Tower [Map Marker: Center of Confluence]
[  ] Defeat Floor 10 Boss: Dax Kaine
[  ] Defeat Floor 25 Boss: Yakov Thorne
[  ] Defeat Floor 50 Boss: Mercer (Triumvirate)
[  ] Defeat Floor 75 Boss: Sentinel
[  ] Defeat Floor 90 Boss: Void Architect
[  ] Defeat Floor 100: Alexander the Gate
[  ] Enter the Final Palace

HINT:
Save points at Floors 20, 40, 60, 80, 100. Use them.
The Tower remembers your failures and adapts.

REWARDS:
• Progressively increasing per floor
• Floor 100: 50000 XP
• Access to Final Palace
• True ending path unlocked

UNLOCKS:
• Final Palace
• Post-game content (after completion)
```

---

### Quest: THE FINAL PALACE
**Type:** Main Scenario • Final Dungeon  
**Location:** Final Palace  
**Level:** 200+

**Journal Entry:**
```
The Progenitor Engine awaits. Five floors. Five challenges.
One final choice.

The Engine believes reset is mercy. You believe survival
is possible. One of you is wrong—or maybe you're both right,
and there's a third path no one has considered.

Whatever happens, this is the end.

OBJECTIVES:
[✓] Enter Final Palace
[►] Defeat Floor 1: Elemental Lords
[  ] Defeat Floor 2: Chronowarden
[  ] Defeat Floor 3: Void Empress
[  ] Defeat Floor 4: Ancient Drake
[  ] Confront Progenitor Engine (Floor 5)
[  ] MAKE YOUR CHOICE

HINT:
The Engine isn't evil. It's desperate. Remember that when
you make your choice.

REWARDS:
• 100000 XP
• Ending determined by choice
• Post-game unlocked
• Credits

UNLOCKS:
• New Game+
• Remnant Vault
• Superbosses
```

---

# SIDE QUEST JOURNAL EXAMPLES

## Example: "The Cartographer's Legacy"

```
┌─────────────────────────────────────────────────────────────┐
│  ◆ THE CARTOGRAPHER'S LEGACY (Part 2 of 3)       [Track]    │
│  Side Quest • Prismridge • Recommended: Level 25            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Old Kell's mentor, Master Varnis, disappeared in the      │
│  Crystal Caverns years ago. Kell believes he found          │
│  something the Dominion didn't want mapped.                │
│                                                             │
│  Find Varnis—or what remains of him.                       │
│                                                             │
│  OBJECTIVES:                                                │
│  [✓] Speak to Old Kell in Prismridge                      │
│  [✓] Complete "Incomplete Maps" (Part 1)                  │
│  [►] Search D3 for Master Varnis                          │
│  [  ] Recover Varnis's final map                          │
│  [  ] Return to Kell                                       │
│                                                             │
│  HINT:                                                      │
│  Varnis was last seen in the eastern tunnels of D3,        │
│  near a formation he called "The Cartographer's Eye."      │
│                                                             │
│  PREREQUISITE: D3 accessible, "Incomplete Maps" complete   │
├─────────────────────────────────────────────────────────────┤
│  Rewards: 2000 XP • 800 G • Master Cartographer's Lens     │
│  Unlocks: Part 3 "The Legacy Complete"                      │
└─────────────────────────────────────────────────────────────┘
```

---

# IMPLEMENTATION CHECKLIST

- [ ] Journal UI mockup approved
- [ ] Quest database schema defined
- [ ] All 95 main scenario quests entered
- [ ] All side quests categorized and entered
- [ ] Map marker system implemented
- [ ] Compass integration for nearby markers
- [ ] Stuck detection algorithm
- [ ] Hint system with contextual triggers
- [ ] Quest completion tracking (achievements)
- [ ] Failed/abandoned quest states
- [ ] Time-sensitive quest warnings
- [ ] Multi-step objective chaining
- [ ] Optional objective tracking
- [ ] Choice consequence logging
