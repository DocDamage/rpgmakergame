# Remnant Custodian — Core Vault VO + UI Barks

## 1. Entry (Arena Seal)

| Source | Line | Trigger |
|--------|------|---------|
| **BOSS** | *"Leftovers belong to the vault."* | Arena seals, fight begins |
| **SYSTEM** | *"CORE VAULT SEALED."* | Arena seal confirmation |
| **SYSTEM** | *"VAULT INTEGRITY: ONLINE."* | Integrity meter activates |

---

## 2. Phase Change VO (HP Gates)

### Phase 1 → Phase 2 (at 70% HP)

| Source | Line | Trigger |
|--------|------|---------|
| **BOSS** | *"Revision begins."* | Phase transition starts |
| **SYSTEM** | *"PHASE SHIFT: ACTIVE REVISION."* | Phase 2 begins |
| **SYSTEM** | *"NEW THREAT: TEAR RINGS DETECTED."* | New hazard introduction |

### Phase 2 → Phase 3 (at 35% HP)

| Source | Line | Trigger |
|--------|------|---------|
| **BOSS** | *"Final redaction."* | Phase transition starts |
| **SYSTEM** | *"PHASE SHIFT: FINAL REDACTION."* | Phase 3 begins |
| **SYSTEM** | *"HAZARD CADENCE INCREASED."* | Frequency warning |

---

## 3. CORE UNRAVEL — Telegraph Callouts

### When Integrity Hits 6 (Warning Ping)

| Source | Line | Trigger |
|--------|------|---------|
| **SYSTEM** | *"INTEGRITY CRITICAL (6/6)."* | Integrity maximum reached |
| **SYSTEM** | *"CORE UNRAVEL IMMINENT."* | Next action will be Unravel |

### When CORE UNRAVEL Begins Charging (2.6s Telegraph Start)

| Source | Line | Trigger |
|--------|------|---------|
| **BOSS** | *"Unstitch."* | Cast begins |
| **SYSTEM** | *"CORE UNRAVEL — CHARGING."* | Telegraph active |
| **SYSTEM** | *"STABILIZER REQUIRED."* | Counterplay hint |

### 20% Scripted UNRAVEL ("You Should've Saved One" Moment)

| Source | Line | Trigger |
|--------|------|---------|
| **BOSS** | *"The record closes."* | Scripted cast begins |
| **SYSTEM** | *"FORCED EVENT: CORE UNRAVEL."* | System warning |
| **SYSTEM** | *"STABILIZE OR SHATTER."* | Urgent counterplay hint |

### If Player Cancels UNRAVEL with Stabilizer (Success)

| Source | Line | Trigger |
|--------|------|---------|
| **SYSTEM** | *"UNRAVEL CANCELLED."* | Stabilizer activation succeeds |
| **SYSTEM** | *"TARGET PINNED: EXPOSED WINDOW."* | Damage window active |
| **BOSS** | *"—Denied."* | Interrupted grunt |

### If UNRAVEL Resolves (Failure)

| Source | Line | Trigger |
|--------|------|---------|
| **SYSTEM** | *"UNRAVEL EXECUTED."* | Cast completes |
| **SYSTEM** | *"INTEGRITY RESET: 3/6."* | Meter reset confirmation |
| **SYSTEM** | *"ECHO DEBUFF APPLIED."* | Debuff notification |

---

## 4. Optional Mid-Fight Barks

**Trigger**: One at random every ~25–35s, max 3 per fight (light touch, not spam)

| # | Source | Line |
|---|--------|------|
| 1 | **BOSS** | *"You don't belong here."* |
| 2 | **BOSS** | *"Stay edited."* |
| 3 | **BOSS** | *"The vault remembers."* |
| 4 | **BOSS** | *"Stop struggling."* |

---

## 5. Death Line + Victory UI

### On Boss Defeat

| Source | Line | Trigger |
|--------|------|---------|
| **BOSS** | *"Returned… to nothing."* | Death animation starts |
| **SYSTEM** | *"CUSTODIAN DISMANTLED."* | Boss HP reaches 0 |
| **SYSTEM** | *"VAULT STABILIZED."* | Hazards stop |

### Cache / Exit Barks

| Source | Line | Trigger |
|--------|------|---------|
| **SYSTEM** | *"REMNANT CACHE: UNLOCKED."* | Reward cache accessible |
| **SYSTEM** | *"EXIT PORTAL: OPEN."* | Return portal spawns |

---

## 6. Quick Reference — Audio Priority Levels

| Priority | Lines | Notes |
|----------|-------|-------|
| **CRITICAL** | Core Unravel callouts, Phase shifts | Must play, can interrupt lower priority |
| **HIGH** | Entry lines, Death lines | Important for pacing |
| **MEDIUM** | Stabilizer success/failure | Feedback for player actions |
| **LOW** | Mid-fight barks (random) | Can be interrupted, fill silence only |

---

## 7. Implementation Notes

- **Overlap Prevention**: Mid-fight barks should not play during Unravel telegraphs or phase transitions
- **Cooldown**: 25–35s random interval for optional barks; max 3 per fight total
- **System Voice**: Consistent mechanical/system tone (think: ship AI, security system)
- **Boss Voice**: Cold, administrative, almost archival—less "angry monster," more "automated librarian"
- **Stinger SFX**: Recommend distinct audio stingers for:
  - Integrity hitting 6 (warning ping)
  - Unravel cancellation success
  - Unravel resolution (failure)
- **Spatial Audio**: System lines can be global/center; Boss lines should originate from boss position
