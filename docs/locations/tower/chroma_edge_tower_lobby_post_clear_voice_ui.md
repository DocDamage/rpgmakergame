# Chroma's Edge — Tower Lobby: Post-Clear Voice & UI Lines (v1)
## Trigger: First Load and Subsequent Returns After `FINAL_PALACE_CLEARED = TRUE`

---

## 1) Lobby System Announcer (UI Voice)

### Trigger: First Load into Tower Lobby After Clear

```
[LOBBY SYSTEM] "CLEAR STATE VERIFIED: ORIGIN SEAL ACTIVE."

[LOBBY SYSTEM] "NEW PROTOCOLS AVAILABLE."

[LOBBY SYSTEM] "HUNDREDFOLD EXCHANGE: ORIGIN INVENTORY UNLOCKED."
```

### Trigger: Subsequent Returns

```
[LOBBY SYSTEM] "ORIGIN SEAL STATUS: STABLE."
```

---

## 2) The Attendant (Tower Steward)

### First Return

```
[ATTENDANT] "You did it. The summit is quiet now."
```

### Conditional: Player Chose Origin Armament

```
[ATTENDANT] "That weapon… it's not a prize. It's a responsibility."
```

### Conditional: Player Forged Core Schema

```
[ATTENDANT] "Schema confirmed. The tower will recognize your craft."
```

### Rotation (Random on Talk)

```
[ATTENDANT] "No more tests. Only choices."

[ATTENDANT] "The tower has stopped watching you. For now."

[ATTENDANT] "If you want harder climbs—toggle the Eclipse Protocols."
```

---

## 3) Archivist Echo (Records / Hundred Marks Wall)

### First Return

```
[ARCHIVIST ECHO] "The record tried to erase itself. It failed."
```

### Rotation

```
[ARCHIVIST ECHO] "Floor 100 is no longer the end. It's the proof."

[ARCHIVIST ECHO] "Origin entries have been inked. Permanently."

[ARCHIVIST ECHO] "Your name survived the edit."
```

### Conditional: Epilogue Not Yet Watched

*Optional flag check: `EPILOGUE_WATCHED = FALSE`*

```
[ARCHIVIST ECHO] "There's an ending waiting. When you're ready."
```

---

## 4) Quartermaster (Vendor)

### First Return

```
[QUARTERMASTER] "New stock just unlocked. Don't ask where it came from."
```

### Rotation

```
[QUARTERMASTER] "Origin-grade materials. Pricey. Worth it."

[QUARTERMASTER] "If you're farming now, do it smart. Don't get sloppy."

[QUARTERMASTER] "You broke the ceiling. So the shelves got taller."
```

---

## 5) Hundredfold Exchange Clerk (Token / Craft Exchange)

### First Return

```
[EXCHANGE] "Origin inventory is live. Trades updated."
```

### Conditional: Core Schema Forged

```
[EXCHANGE] "Schema recognized. New recipes are now admissible."
```

### Rotation

```
[EXCHANGE] "Tokens in, power out. Same deal—higher stakes."

[EXCHANGE] "If you're short one component, don't grind blind. Convert."

[EXCHANGE] "Origin Sigils accepted."
```

---

## 6) Aurora Crucible (Summon / Evolution Station Voice)

### Conditional: Alexander Unlocked

```
[CRUCIBLE] "CONTRACT REGISTERED: ALEXANDER."
```

### Rotation

```
[CRUCIBLE] "Evolution paths expanded."

[CRUCIBLE] "Accord resonance detected."
```

---

## 7) Eclipse Protocol Panel (Modifier UI Voice)

### First Approach After Clear

```
[PROTOCOL PANEL] "ECLIPSE PROTOCOLS: EXPANDED TIER UNLOCKED."
```

### Rotation

```
[PROTOCOL PANEL] "Select one modifier. Earn more. Suffer more."
```

---

## 8) Seam Router / Lift Core Console (Start/Resume UI)

### First Interaction After Clear

```
[LIFT CORE] "ORIGIN CLEAR REGISTERED. NEW ROUTES AUTHORIZED."
```

### Rotation

```
[LIFT CORE] "Resume at last save floor."

[LIFT CORE] "Modifiers active."
```

---

## Quick Reference: NPC Response Matrix

| NPC | First Return | Armament Chosen | Schema Forged | Epilogue Pending | Standard Rotation |
|-----|--------------|-----------------|---------------|------------------|-------------------|
| **Lobby System** | 3 lines | — | — | — | 1 line |
| **Attendant** | 1 line | 1 line | 1 line | — | 3 lines |
| **Archivist Echo** | 1 line | — | — | 1 line | 3 lines |
| **Quartermaster** | 1 line | — | — | — | 3 lines |
| **Exchange Clerk** | 1 line | — | 1 line | — | 3 lines |
| **Aurora Crucible** | — | — | — | — | 2 lines + Alexander |
| **Protocol Panel** | 1 line | — | — | — | 1 line |
| **Lift Core** | 1 line | — | — | — | 2 lines |

---

## Flag Dependencies

| Line | Required Flag |
|------|---------------|
| All Lobby System post-clear lines | `FINAL_PALACE_CLEARED = TRUE` |
| Armament-specific lines | `ORIGIN_ARMAMENT_BOUND = TRUE` |
| Schema-specific lines | `ORIGIN_CORE_SCHEMA_FORGED = TRUE` |
| Epilogue reminder | `EPILOGUE_WATCHED = FALSE` |
| Alexander contract line | `SUMMON_ALEXANDER_UNLOCKED = TRUE` |
| Expanded Protocols line | `ECLIPSE_PROTOCOLS_EXPANDED = TRUE` |
| Origin Inventory line | `ORIGIN_INVENTORY_UNLOCKED = TRUE` |

---

## Atmosphere Notes

**Post-Clear Lobby Tone:**
- **System voices**: Mechanical, precise, acknowledging achievement
- **Attendant**: Respectful, slightly ominous about the responsibility
- **Archivist Echo**: Meta-aware of the "record" and permanence
- **Quartermaster**: Practical, gruff, acknowledging power ceiling broken
- **Exchange Clerk**: Transactional but impressed
- **Crucible**: Cold, technical, recognizing new resonance
- **Protocol Panel**: Inviting challenge, promising risk/reward
- **Lift Core**: Functional, noting new authorizations

**Overall**: The lobby shifts from "testing ground" to "veteran's hall" — NPCs acknowledge the player's accomplishment while offering new challenges (Eclipse Protocols) and endgame systems (Origin crafting, rematches).
