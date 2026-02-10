# Chroma's Edge - UI Microcopy Polish
## Error Messages, Confirmations, Warnings, and Tutorials

---

# ERROR MESSAGES

## General Errors

```
┌─────────────────────────────────────────────────────────┐
│  ⚠ ERROR                                                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Unable to perform action.                              │
│                                                         │
│  [OK]                                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Connection/Loading Errors

**Code:** NETWORK_ERROR  
**Message:**
```
Connection lost.

Unable to reach game servers. 
Your progress has been saved locally.

[Retry] [Continue Offline] [Exit to Title]
```

**Code:** SAVE_CORRUPTED  
**Message:**
```
Save data issue detected.

We found a problem with your save file.
Don't worry—we've loaded your most recent backup.

If problems persist, contact support.

[Continue] [Report Issue]
```

---

## Gameplay Errors

### Cannot Use Item
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ CANNOT USE                                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Item Name] cannot be used right now.                  │
│                                                         │
│  Possible reasons:                                      │
│  • Target is at full HP/MP                              │
│  • Status effect is not present                         │
│  • Item has no effect in this context                   │
│                                                         │
│  [OK]                                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Cannot Equip
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ CANNOT EQUIP                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Character] cannot equip [Item].                       │
│                                                         │
│  Requirements not met:                                  │
│  • Level required: 25 (current: 18)                     │
│  • Class restriction: [Class] only                      │
│                                                         │
│  [OK]                                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Cannot Enter Dungeon
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ AREA LOCKED                                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You cannot enter [Dungeon Name] yet.                   │
│                                                         │
│  Required:                                              │
│  • Complete [Previous Quest]                            │
│  • Recommended level: 35                                │
│                                                         │
│  Current status:                                        │
│  • [Previous Quest]: Incomplete                         │
│  • Current level: 28                                    │
│                                                         │
│  [OK] [Track Quest]                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Inventory Full
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ INVENTORY FULL                                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You cannot carry any more items.                       │
│                                                         │
│  Current: 99/99 items                                   │
│                                                         │
│  Options:                                               │
│  • Discard items                                        │
│  • Use consumables                                      │
│  • Store at camp                                        │
│                                                         │
│  [Manage Inventory] [Cancel]                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Not Enough Gil
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ INSUFFICIENT FUNDS                                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You don't have enough Gil for this purchase.           │
│                                                         │
│  Cost: 2,500 G                                          │
│  Current: 1,840 G                                       │
│  Shortfall: 660 G                                       │
│                                                         │
│  [Sell Items] [Cancel]                                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# CONFIRMATION DIALOGS

## High-Stakes Confirmations

### Overwrite Save
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ OVERWRITE SAVE?                                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  This will overwrite your existing save file.           │
│                                                         │
│  Save details:                                          │
│  • Play time: 45:32                                     │
│  • Level: 38                                            │
│  • Location: Ashveil Sanctuary                          │
│  • Date: 2026/02/07                                     │
│                                                         │
│  This action cannot be undone.                          │
│                                                         │
│  [Cancel] [Overwrite]                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Discard Item
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ DISCARD ITEM?                                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You are about to discard:                              │
│                                                         │
│  [ELIXIR] ×1                                            │
│  ★★★★☆ Epic Consumable                                  │
│  Fully restore HP and MP                                │
│                                                         │
│  This item will be permanently lost.                    │
│                                                         │
│  [Cancel] [Discard]                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Major Choice Warning
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ IMPORTANT CHOICE                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Your next decision will have significant consequences. │
│                                                         │
│  Choice: [Spare the Colossus / End its suffering]      │
│                                                         │
│  Consequences:                                          │
│  • Affects Grit's character development                 │
│  • Unlocks different content                            │
│  • Cannot be changed without reloading                  │
│                                                         │
│  [Cancel] [Make Choice]                                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Standard Confirmations

### Use Rare Item
```
┌─────────────────────────────────────────────────────────┐
│  Use [MEGA PHOENIX]?                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Revive all KO'd allies with full HP.                   │
│                                                         │
│  Party status:                                          │
│  • Kade: KO                                             │
│  • Twist: KO                                            │
│  • Renna: 45% HP                                        │
│                                                         │
│  [Cancel] [Use]                                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Fast Travel
```
┌─────────────────────────────────────────────────────────┐
│  Fast Travel to [ASHVEIL SANCTUARY]?                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Cost: 100 G                                            │
│                                                         │
│  [Cancel] [Travel]                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Rest at Inn
```
┌─────────────────────────────────────────────────────────┐
│  Rest at [Mira's Rest]?                                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Cost: 150 G                                            │
│                                                         │
│  Effects:                                               │
│  • Fully restore HP and MP                              │
│  • Remove all status ailments                           │
│  • Advance time (day → night or night → day)           │
│  • Save game                                            │
│                                                         │
│  [Cancel] [Rest]                                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# WARNINGS

## Combat Warnings

### Low HP Warning (Ally)
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ [RENNA] IS IN DANGER                                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Renna's HP is critically low (12%).                    │
│                                                         │
│  Suggested actions:                                     │
│  • Use healing item                                     │
│  • Cast healing spell                                   │
│  • Use Defend command                                   │
│                                                         │
│  [Don't warn again for this battle]                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Boss Warning
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ DANGEROUS FOE AHEAD                                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You are approaching a powerful boss enemy.             │
│                                                         │
│  Recommended:                                           │
│  • Level 45+                                            │
│  • Stocked healing items                                │
│  • Saved recently                                       │
│                                                         │
│  Your status:                                           │
│  • Average level: 38 ⚠                                  │
│  • Healing items: 12 Potions, 3 Hi-Potions ✓            │
│  • Last save: 23 minutes ago ⚠                          │
│                                                         │
│  [Save Now] [Proceed Anyway] [Turn Back]                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Integrity Critical
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ SYSTEM CRITICAL                                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Integrity: 6/6                                         │
│                                                         │
│  CORE UNRAVEL IMMINENT                                  │
│                                                         │
│  USE STABILIZER NOW                                     │
│                                                         │
│  Available stabilizers: 2                               │
│                                                         │
│  [Use Stabilizer] [Deploy Field]                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Exploration Warnings

### Leaving Area with Active Quest
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ ACTIVE QUEST IN AREA                                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You have an active quest that can be completed here:   │
│                                                         │
│  ◆ The Cartographer's Legacy                            │
│    Objective: Search D3 for Master Varnis              │
│                                                         │
│  Are you sure you want to leave?                        │
│                                                         │
│  [Stay] [Leave Anyway] [Track Quest]                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Unsaved Progress Warning
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ UNSAVED PROGRESS                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You haven't saved for 45 minutes.                      │
│                                                         │
│  Progress at risk:                                      │
│  • 2 quests completed                                   │
│  • Level gained (38 → 39)                               │
│  • Rare item acquired: Mithril Blade                    │
│                                                         │
│  [Save Now] [Save & Continue] [Dismiss]                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# SAVE/LOAD TEXT

## Save Menu

```
┌─────────────────────────────────────────────────────────┐
│  SAVE GAME                                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Select a save slot:                                    │
│                                                         │
│  [Slot 1]  Kade Lv.38  45:32  Ashveil    2026/02/07   │
│  [Slot 2]  Kade Lv.25  22:15  Prismridge 2026/02/05   │
│  [Slot 3]  Empty                                      │
│  [Slot 4]  Empty                                      │
│                                                         │
│  [Auto-Save]  Kade Lv.38  44:55  Ashveil  2026/02/07   │
│                                                         │
│  [Save] [Cancel] [Delete Save]                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Save Success
```
┌─────────────────────────────────────────────────────────┐
│  ✓ GAME SAVED                                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Your progress has been saved.                          │
│                                                         │
│  Location: Ashveil Sanctuary                            │
│  Time: 45:32                                            │
│  Level: 38                                              │
│                                                         │
│  [OK]                                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Load Game
```
┌─────────────────────────────────────────────────────────┐
│  LOAD GAME                                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Select a save to load:                                 │
│                                                         │
│  [Slot 1]  Kade Lv.38  45:32  Ashveil    2026/02/07   │
│           ⭐ Current save                               │
│  [Slot 2]  Kade Lv.25  22:15  Prismridge 2026/02/05   │
│           (2 hours 17 minutes earlier)                  │
│                                                         │
│  [Load] [Cancel] [Show Details] [Delete]                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# FAST TRAVEL TEXT

## Fast Travel Menu

```
┌─────────────────────────────────────────────────────────┐
│  FAST TRAVEL                                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Select destination:                                    │
│                                                         │
│  ASHVEIL REGION                                         │
│  [Ashveil Sanctuary]           ✓ Unlocked               │
│                                                         │
│  PRISMRIDGE REGION                                      │
│  [Prismridge]                  ✓ Unlocked               │
│  [Crystal Caverns Entrance]    ✓ Unlocked               │
│                                                         │
│  CAPITAL CHAIN                                          │
│  [Meridian Junction]           ✓ Unlocked               │
│  [Old Lumencrest]              ✓ Unlocked               │
│  [Crown District]              ✓ Unlocked               │
│                                                         │
│  ─────────────────────────────────────────────────     │
│  Current location: Dusthaven                            │
│  Destination: Ashveil Sanctuary                         │
│  Cost: 100 G                                            │
│  ─────────────────────────────────────────────────     │
│                                                         │
│  [Travel] [Cancel]                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Fast Travel Unavailable
```
┌─────────────────────────────────────────────────────────┐
│  ⚠ CANNOT FAST TRAVEL                                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You cannot fast travel right now.                      │
│                                                         │
│  Reason: Inside dungeon (Ruins of Ashveil)              │
│                                                         │
│  Fast travel is available:                              │
│  • In towns and settlements                             │
│  • At discovered campsites                              │
│  • On the world map                                     │
│                                                         │
│  [OK]                                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# SETTINGS TEXT

## Settings Menu Categories

```
┌─────────────────────────────────────────────────────────┐
│  SETTINGS                                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Gameplay]                                             │
│    Difficulty, Autosave, Tutorials...                   │
│                                                         │
│  [Controls]                                             │
│    Key bindings, Controller, Vibration...               │
│                                                         │
│  [Video]                                                │
│    Resolution, Graphics quality, Fullscreen...          │
│                                                         │
│  [Audio]                                                │
│    Master, Music, SFX, Voice...                         │
│                                                         │
│  [Accessibility]                                        │
│    Colorblind, Text size, High contrast...              │
│                                                         │
│  [Language]                                             │
│    Text language, Voice language, Subtitles...          │
│                                                         │
│  [System]                                               │
│    Brightness, HDR, Performance metrics...              │
│                                                         │
│  [Restore Defaults]  [Back]                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Difficulty Selection
```
┌─────────────────────────────────────────────────────────┐
│  DIFFICULTY                                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Select your preferred challenge level:                 │
│                                                         │
│  [STORY]                                                │
│   Combat is easier. Focus on narrative.                │
│   Enemy damage: -40%  Enemy HP: -30%                   │
│                                                         │
│  [NORMAL] ★ Current                                     │
│   Balanced experience.                                 │
│   Standard difficulty.                                  │
│                                                         │
│  [HARD]                                                 │
│   Enemies are smarter and tougher.                     │
│   Enemy damage: +25%  Enemy HP: +50%                   │
│   Better loot drops.                                    │
│                                                         │
│  [CHAOS]                                                │
│   Maximum challenge. No mercy.                         │
│   Enemy damage: +75%  Enemy HP: +100%                  │
│   Permanent death. Unique rewards.                      │
│   Unlocks after completing Normal.                      │
│                                                         │
│  [Confirm] [Cancel]                                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# TUTORIAL POPUPS

## First-Time Tutorials

### First Warp (Fast Travel)
```
┌─────────────────────────────────────────────────────────┐
│  🎓 TUTORIAL: FAST TRAVEL                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You've unlocked a FAST TRAVEL point!                   │
│                                                         │
│  Fast Travel allows you to instantly move between       │
│  discovered locations for a small fee.                  │
│                                                         │
│  How to use:                                            │
│  1. Open the World Map                                  │
│  2. Select a discovered location                        │
│  3. Confirm travel and pay the fee                      │
│                                                         │
│  💡 Tip: You can only fast travel from the world map    │
│     or towns—not inside dungeons!                       │
│                                                         │
│  [Don't show again]  [Got it!]                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### First Shrine
```
┌─────────────────────────────────────────────────────────┐
│  🎓 TUTORIAL: FOUNDATION SHRINES                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You've discovered a Foundation Shrine!                 │
│                                                         │
│  Shrines are sacred places attuned to one of the        │
│  Eight Foundations. Each offers:                        │
│                                                         │
│  • Blessings (temporary buffs)                          │
│  • Spell learning (unique magic)                        │
│  • Lore (codex entries)                                 │
│  • Fast travel points                                   │
│                                                         │
│  💡 Tip: Visit all 8 shrines to unlock a special        │
│     reward and deepen your understanding of Orion.      │
│                                                         │
│  [Don't show again]  [Got it!]                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### First Tower Entry
```
┌─────────────────────────────────────────────────────────┐
│  🎓 TUTORIAL: CHROMA TOWER                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Welcome to the Chroma Tower.                           │
│                                                         │
│  Tower Rules:                                           │
│  • 100 floors of increasing difficulty                  │
│  • Save points every 20 floors                          │
│  • Boss battles at floors 10, 25, 50, 75, 90, 100      │
│  • You can exit and resume from save points             │
│  • No mounts permitted inside                           │
│  • Party switching allowed at save points               │
│                                                         │
│  💡 Tip: The Tower adapts to your strategies.           │
│     Vary your tactics to keep it off-balance.           │
│                                                         │
│  [Don't show again]  [Got it!]                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### First Remnant Vault Entry
```
┌─────────────────────────────────────────────────────────┐
│  🎓 TUTORIAL: REMNANT VAULT                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  You've unlocked the Remnant Vault!                     │
│                                                         │
│  Vault Features:                                        │
│  • Post-game challenge content                          │
│  • Superboss encounters                                 │
│  • Ultimate equipment rewards                           │
│  • Modifier system (customize difficulty)               │
│                                                         │
│  Vault Structure:                                       │
│  • Wing A: Cinder Scar Gallery (combat focus)           │
│  • Wing B: Archive Annex (puzzle focus)                 │
│  • Wing C: Veilroot Catacombs (exploration focus)       │
│  • Core: Ultimate challenge (all wings cleared)         │
│                                                         │
│  💡 Tip: Complete all three wings to unlock the Core    │
│     and face the ultimate test of your party.           │
│                                                         │
│  [Don't show again]  [Got it!]                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

# LOADING SCREEN TEXT

## Tips Rotation

```
Loading...

═══════════════════════════════════════════════════════════

💡 TIP: Stuck on a puzzle? Try looking at it from a 
   different angle—literally. Camera rotation can reveal
   hidden patterns.

═══════════════════════════════════════════════════════════

[Loading bar: ████████░░ 80%]
```

### Tip Pool (Rotating)

1. "Stuck on a puzzle? Try looking at it from a different angle—literally."
2. "Save often. The world is dangerous, and not all choices can be undone."
3. "Talk to NPCs multiple times. They might have new information after events."
4. "Different enemies are weak to different elements. Experiment!"
5. "Character quests unlock powerful abilities. Don't ignore them."
6. "The Tower saves your progress every 20 floors. Pace yourself."
7. "Fast travel costs Gil. Sometimes walking is worth the savings."
8. "Night and day affect enemy spawns and NPC locations."
9. "Party banter triggers during travel. Different pairs have unique conversations."
10. "The Progenitor Engine can be defeated multiple ways. Your choice matters."

---

# IMPLEMENTATION CHECKLIST

- [ ] All error messages have clear solutions
- [ ] High-stakes confirmations prevent accidental loss
- [ ] Warning thresholds configurable in settings
- [ ] Tutorial triggers only once (unless reset)
- [ ] "Don't show again" option on all tutorials
- [ ] Loading tips rotate and remain relevant
- [ ] Save/load UI shows meaningful info
- [ ] Fast travel clearly shows cost and destination
- [ ] Settings changes apply immediately or confirm
- [ ] All text accessible (screen reader compatible)
- [ ] Text size options don't break layout
- [ ] Color coding supplemented with icons/text
