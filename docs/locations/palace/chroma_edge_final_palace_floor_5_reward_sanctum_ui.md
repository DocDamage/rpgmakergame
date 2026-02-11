# Chroma's Edge — Final Palace Floor 5: Post-Clear Reward Sanctum UI (v1)
## Apex Sanctum — Origin Seal

---

## 0) Defeat → Transition Toasts

### Toast 1 (Instant)

```
═══════════════════════════════════════
   PROGENITOR ENGINE: SHUTDOWN CONFIRMED.
═══════════════════════════════════════
```

### Toast 2 (After 1.5s)

```
═══════════════════════════════════════
        ORIGIN STABILITY RESTORED.
═══════════════════════════════════════
```

### Toast 3 (On Door Unlock)

```
═══════════════════════════════════════
       SANCTUM ACCESS GRANTED.
═══════════════════════════════════════
```

---

## 1) Sanctum Main Screen

### Screen Title

```
APEX SANCTUM — ORIGIN SEAL
```

### Subheader

```
You have completed the Final Palace.
Claim your Origin Reward.
```

### Primary Options (Big Buttons)

| Button | Function |
|--------|----------|
| **BIND ORIGIN ARMAMENT** | Choose 1 of 12 best-in-slot weapons |
| **FORGE ENGINE CORE SCHEMA** | Unlock a permanent crafting branch |
| **CLAIM CLEAR CHEST** | Materials + currency + guaranteed drops |
| **SAVE / EXIT / EPILOGUE** | Terminal access |

### Guidance Text (Small Panel)

```
Armament = immediate best-in-slot weapon choice.
Engine Core Schema = unlocks a permanent crafting branch (late endgame progression).

You may choose only one: Armament or Schema.
```

---

## 2) Choice Gate (Prevents Player Confusion)

### Trigger
When player selects "Bind Armament" OR "Forge Schema"

### Modal: ORIGIN CHOICE

```
╔══════════════════════════════════════════════╗
║            ORIGIN CHOICE                     ║
╠══════════════════════════════════════════════╣
║                                              ║
║  You may claim one Origin Choice Reward.     ║
║                                              ║
║  Binding an Armament locks out the Core      ║
║  Schema.                                     ║
║                                              ║
║  Forging a Core Schema locks out the         ║
║  Armament.                                   ║
║                                              ║
║  [ CONTINUE ]           [ CANCEL ]           ║
║                                              ║
╚══════════════════════════════════════════════╝
```

---

## 3) Armament Binding Screen (12 Pedestals)

### Screen Title

```
BIND ORIGIN ARMAMENT
```

### Subheader

```
Twelve armaments. One vow.
Pick one to bind to your clear.
```

### Pedestal Hover Panel (Right Side)

| Field | Description |
|-------|-------------|
| **{WEAPON NAME}** | Weapon name |
| **Type** | {Weapon Class} |
| **Resonance** | {Foundation/Composite} |
| **Origin Trait** | {Unique passive} |
| **Signature Bonus** | {What it excels at} |
| **Binding** | {Who can equip / restrictions} |

### Interaction Prompts

| Prompt | Action |
|--------|--------|
| **Inspect Details** | View full stat panel |
| **Bind Armament** | Begin binding process |

### Confirmation Modal

```
╔══════════════════════════════════════════════╗
║      CONFIRM ARMAMENT BINDING                ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Bind {WEAPON NAME} to your ascent?          ║
║                                              ║
║  All other pedestals will dim and lock.      ║
║  This cannot be undone for this clear.       ║
║                                              ║
║  [ CONFIRM BINDING ]    [ CANCEL ]           ║
║                                              ║
╚══════════════════════════════════════════════╝
```

### Post-Selection Stamp

```
═══════════════════════════════════════
         ORIGIN SEALED.
      ARMAMENT BOUND.
═══════════════════════════════════════
```

### Smart UX: Tower 100 Duplicate Handling

If player already claimed same pedestal in Tower 100:

| Change | Implementation |
|--------|----------------|
| **Button** | "Bind" → "Ascend/Upgrade" |
| **New Button** | "UPGRADE TO ORIGIN TIER" |
| **Modal Text** | "Convert your existing {Weapon Name} into its Origin Tier variant?" |

---

## 4) Engine Core Schema Screen (Craft Line Unlock)

### Screen Title

```
FORGE ENGINE CORE SCHEMA
```

### Subheader

```
Choose a schema to unlock permanent endgame crafting.
```

### Core List (8 + Eclipse)

Display as tiles with icons:

| Schema | Foundation |
|--------|------------|
| **Heat Core Schema** | Heat |
| **Tide Core Schema** | Tide |
| **Growth Core Schema** | Growth |
| **Light Core Schema** | Light |
| **Motion Core Schema** | Motion |
| **Mass Core Schema** | Mass |
| **Time Core Schema** | Time |
| **Shadow Core Schema** | Shadow |
| **Eclipse Core Schema** | Eclipse |

*Note: Eclipse Core unlocks after all 8 cores, or available now as premium pick.*

### Hover/Inspect Panel

| Field | Description |
|-------|-------------|
| **Schema** | {Core Name} |
| **Unlocks** | {2–3 recipe lines} (e.g., anti-dispel gear / phase resist / conduit cooldown trims) |
| **Best For** | {playstyle} |
| **Material Focus** | {what it consumes / produces} |

### Confirmation Modal

```
╔══════════════════════════════════════════════╗
║         CONFIRM CORE FORGE                   ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Forge {Core Schema}?                        ║
║                                              ║
║  This unlocks new crafting at:               ║
║  • Tower Lobby → Hundredfold Exchange        ║
║  • Old Lumencrest / Endgame Forge            ║
║                                              ║
║  Armament binding will be locked             ║
║  for this clear.                             ║
║                                              ║
║  [ FORGE SCHEMA ]       [ CANCEL ]           ║
║                                              ║
╚══════════════════════════════════════════════╝
```

### Post-Selection Stamp

```
═══════════════════════════════════════
         SCHEMA ETCHED.
   CRAFTING BRANCH UNLOCKED.
═══════════════════════════════════════
```

---

## 5) Clear Chest Screen (Guaranteed Loot Delivery)

### Screen Title

```
CLEAR CHEST — ORIGIN SPOILS
```

### Contents Panel (No RNG Ambiguity)

| Reward | Amount/Details |
|--------|----------------|
| **Duckets** | {large fixed amount} |
| **Eclipse Mats** | {X rolls / fixed bundle} |
| **Legendary Craft Components** | {fixed} |
| **Unique Drop** | Progenitor Lattice (craft key item) |
| **Completion Token** | Origin Sigil ×1 (upgrades / cosmetics / tower modifiers) |

### Claim Button

```
CLAIM SPOILS
```

### Toast

```
═══════════════════════════════════════
         SPOILS CLAIMED.
═══════════════════════════════════════
```

---

## 6) Sanctuary Terminal (Save / Ending / Return)

### Screen Title

```
SANCTUARY TERMINAL — FINAL PALACE CLEAR
```

### Options

| Option | Function |
|--------|----------|
| **Save Clear State** | Log completion |
| **View Unlocks** | See what was unlocked |
| **Begin Epilogue** | Story scene |
| **Watch Credits** | Optional credits roll |
| **Return to Tower Lobby** | Exit to Hundredfold Vestibule |
| **Return to Eclipse Confluence** | Exit to post-D8 hub |
| **Stay in Sanctum** | Remain in reward room |

### Save Toast

```
═══════════════════════════════════════
       CLEAR STATE SAVED.
    FINAL PALACE: COMPLETE.
═══════════════════════════════════════
```

---

## 7) Unlock Summary Screen

### Screen Title

```
UNLOCKS — ORIGIN CLEAR
```

### Checklist (Green Stamps)

| Unlock | Description |
|--------|-------------|
| ✓ **Tower Lobby: "Eclipse Protocols" Expanded** | New modifier tier on Eclipse Protocol Panel |
| ✓ **Hundredfold Exchange: Origin Inventory** | New recipes (from chosen Core Schema) |
| ✓ **Progenitor Rematch** | Final Palace replayable for mats (reduced story gating) |
| ✓ **Eclipse Hunts** | New endgame hunt board targets (Confluence / Crown District) |

### Button

```
CONTINUE
```

### Post-Unlock Toast (On Returning to Lobby)

```
═══════════════════════════════════════
       TOWER LOBBY UPDATED.
    NEW PROTOCOLS AVAILABLE.
═══════════════════════════════════════
```

---

## 8) Epilogue / Credits Prompts

### Epilogue Prompt

```
╔══════════════════════════════════════════════╗
║         BEGIN EPILOGUE                       ║
╠══════════════════════════════════════════════╣
║                                              ║
║  You can return later to finish side         ║
║  content and tower modifiers.                ║
║                                              ║
║  Begin the epilogue now?                     ║
║                                              ║
║  [ BEGIN ]              [ NOT YET ]          ║
║                                              ║
╚══════════════════════════════════════════════╝
```

### Credits Prompt

```
╔══════════════════════════════════════════════╗
║         WATCH CREDITS                        ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Credits will return you to the Tower        ║
║  Lobby afterward.                            ║
║                                              ║
║  [ WATCH ]              [ CANCEL ]           ║
║                                              ║
╚══════════════════════════════════════════════╝
```

---

## Flag Summary

| Flag | Trigger |
|------|---------|
| `FINAL_PALACE_CLEARED` | Defeat Progenitor Engine |
| `PROGENITOR_ENGINE_DEFEATED` | Defeat Progenitor Engine |
| `ORIGIN_ARMAMENT_BOUND` | Chose armament reward |
| `ORIGIN_CORE_SCHEMA_FORGED` | Chose schema reward |
| `{CORE_NAME}_SCHEMA_UNLOCKED` | Specific core schema chosen |
| `CLEAR_CHEST_CLAIMED` | Claimed origin spoils |
| `EPILOGUE_AVAILABLE` | Post-clear unlock |
| `NG_PLUS_UNLOCKED` | After credits/epilogue |

---

## Quick Reference: Reward Flow

```
DEFEAT PROGENITOR ENGINE
        ↓
[Transition Toasts] → Sanctum Access Granted
        ↓
┌─────────────────────────────────────┐
│   APEX SANCTUM — ORIGIN SEAL        │
├─────────────────────────────────────┤
│  • Bind Origin Armament (12)        │
│  • Forge Engine Core Schema (9)     │
│  • Claim Clear Chest                │
│  • Save / Exit / Epilogue           │
└─────────────────────────────────────┘
        ↓
CHOOSE ONE:
┌─────────────────┐   ┌─────────────────┐
│   ARMAMENT      │   │  CORE SCHEMA    │
│  (1 of 12 BIS)  │   │ (craft branch)  │
└─────────────────┘   └─────────────────┘
        ↓                   ↓
   [BINDING MODAL]    [FORGE MODAL]
        ↓                   ↓
   "Origin Sealed"    "Schema Etched"
        ↓                   ↓
┌─────────────────────────────────────┐
│   CLEAR CHEST — ORIGIN SPOILS       │
│   • Duckets • Eclipse Mats          │
│   • Progenitor Lattice              │
│   • Origin Sigil ×1                 │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│   SANCTUARY TERMINAL                │
│   • Save • Epilogue • Credits       │
│   • Return to Lobby/Confluence      │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│   UNLOCKS — ORIGIN CLEAR            │
│   ✓ Eclipse Protocols Expanded      │
│   ✓ Origin Inventory (crafting)     │
│   ✓ Progenitor Rematch              │
│   ✓ Eclipse Hunts                   │
└─────────────────────────────────────┘
        ↓
   Return to Tower Lobby
   "New Protocols Available"
```
