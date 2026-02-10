# Stabilizer Interaction VO/UI — Remnant Vault

## 1) Wing Stabilizer Station (Repeatable)

### A) Approach / Hover

| Element | Text |
|---------|------|
| **Prompt** | `STABILIZER STATION` |
| **Subtext** | `Reduce Echo Pressure. Create a Stabilization Field.` |

---

### B) Interact Prompt

| Source | Line |
|--------|------|
| **SYSTEM** | *"ACTIVATE STABILIZER?"* |

**Buttons:** `ACTIVATE` / `CANCEL`

---

### C) Channel Start

| Source | Line | Condition |
|--------|------|-----------|
| **SYSTEM** | *"STABILIZER — PRIMING…"* | Short interact channel begins |

---

### D) Channel Interrupted

| Source | Line |
|--------|------|
| **SYSTEM** | *"PRIMING INTERRUPTED."* |
| **SYSTEM** | *"TRY AGAIN."* |

---

### E) Activation Success (Field Begins)

| Source | Line |
|--------|------|
| **SYSTEM** | *"STABILIZATION FIELD — ACTIVE."* |
| **SYSTEM** | *"ECHO PRESSURE REDUCED."* |
| **SYSTEM** | *"ENEMIES SYNCED."* |

---

### F) Field Active Status (HUD Line)

```
STABILIZATION FIELD: {10…0}s
```

---

### G) Field Ending Warnings

| Timing | Source | Line |
|--------|--------|------|
| At 3s remaining | **SYSTEM** | *"STABILIZATION FIELD — ENDING."* |
| At 0s | **SYSTEM** | *"FIELD OFFLINE."* |

---

### H) Cooldown / Unavailable States

#### On Cooldown

| Source | Line |
|--------|------|
| **SYSTEM** | *"STABILIZER RECHARGING."* |

**UI Display:** `COOLDOWN: {Xs}`

#### Disabled in Room (Scripted)

| Source | Line |
|--------|------|
| **SYSTEM** | *"STABILIZER LOCKED IN THIS AREA."* |

---

## 2) Core Vault Stabilizer (Single-Use, Boss Room)

### A) Approach / Hover

| Element | Text |
|---------|------|
| **Prompt** | `CORE STABILIZER` |
| **Subtext** | `Single-use. Cancels CORE UNRAVEL.` |

---

### B) Interact Prompt (Shows Charges Remaining)

| Source | Line |
|--------|------|
| **SYSTEM** | *"DEPLOY CORE STABILIZER?"* |
| **SYSTEM** | *"USES REMAINING: {2/2, 1/2, 0/2}"* |

**Buttons:** `DEPLOY` / `CANCEL`

---

### C) Deploy Start

| Source | Line |
|--------|------|
| **SYSTEM** | *"CORE STABILIZER — ARMING…"* |

---

### D) Deploy Interrupted

| Source | Line |
|--------|------|
| **SYSTEM** | *"DEPLOYMENT INTERRUPTED."* |

---

### E) Deploy Success (Field Begins)

| Source | Line |
|--------|------|
| **SYSTEM** | *"CORE STABILIZATION FIELD — ACTIVE."* |
| **SYSTEM** | *"HAZARDS SUPPRESSED."* |
| **SYSTEM** | *"TARGET SYNCED: DAMAGE WINDOW."* |

---

### F) Integrity Interaction (Callouts)

#### When It Reduces Integrity

| Source | Line |
|--------|------|
| **SYSTEM** | *"INTEGRITY REDUCED."* |

**Optional (if meter shown):** `INTEGRITY: {X}/6`

---

### G) CORE UNRAVEL Cancel (The Big Moment)

#### When Stabilizer Deployed During Unravel Charge

| Source | Line |
|--------|------|
| **SYSTEM** | *"UNRAVEL CANCELLED."* |
| **SYSTEM** | *"TARGET STUNNED."* |
| **SYSTEM** | *"EXPOSED WINDOW — GO."* |

#### Optional Boss Grunt

| Source | Line |
|--------|------|
| **BOSS** | *"—Denied."* |

---

### H) Field Ending (Boss Room)

| Source | Line |
|--------|------|
| **SYSTEM** | *"FIELD ENDING."* |
| **SYSTEM** | *"HAZARDS RETURNING."* |
| **SYSTEM** | *"FIELD OFFLINE."* |

---

### I) Used Up / No Charges

| Source | Line |
|--------|------|
| **SYSTEM** | *"CORE STABILIZER DEPLETED."* |
| **SYSTEM** | *"NO USES REMAINING."* |

---

### J) Can't Deploy (Edge Cases)

#### If Another Field Is Active

| Source | Line |
|--------|------|
| **SYSTEM** | *"FIELD ALREADY ACTIVE."* |

#### If Player Tries After Boss Death / Reward State

| Source | Line |
|--------|------|
| **SYSTEM** | *"SYSTEM IDLE."* |

---

## 3) Optional: Minimal "Teach the Player" Callouts

**Usage:** Once per run (non-spammy)

| Source | Line | Context |
|--------|------|---------|
| **SYSTEM** | *"TIP: STABILIZERS REDUCE PRESSURE AND CREATE BURST WINDOWS."* | First Stabilizer use in wing |
| **SYSTEM** | *"TIP: SAVE ONE CORE STABILIZER FOR THE 20% UNRAVEL."* | First Core Stabilizer use in boss room |

---

## 4) Short SFX Tags (Implementation Labels)

**Note:** Not voice lines—audio implementation references only.

| Event | SFX Tag | Description |
|-------|---------|-------------|
| **PRIMING** | `sfx_stabilizer_priming` | Soft rising hum |
| **ACTIVE** | `sfx_stabilizer_active` | Clean "lock-in" chime |
| **ENDING** | `sfx_stabilizer_ending` | Triple warning tick |
| **CANCEL UNRAVEL** | `sfx_stabilizer_cancel` | Deep snap + release whoosh |

---

## Quick Reference — Wing vs Core Stabilizer Differences

| Feature | Wing Stabilizer | Core Vault Stabilizer |
|---------|-----------------|----------------------|
| **Uses** | Repeatable (cooldown 30s) | Single-use (2 total) |
| **Effect** | -2 Pressure, +SYNCED enemies | -2 Integrity, hazard suppression, can cancel Unravel |
| **Interact Time** | 1.0s channel | 1.0s deploy |
| **Key Verb** | ACTIVATE | DEPLOY |
| **Cooldown UI** | Yes (timer display) | No (charges only) |
| **Cancel Unravel** | No | Yes (primary purpose) |
| **Stun/Expose Boss** | No | Yes (on successful Unravel cancel) |

---

## Implementation Priority Notes

1. **Core Vault Stabilizer VO takes precedence** over Wing VO if both could play simultaneously (edge case: extremely fast speedrun)
2. **"Teach the Player" callouts** should trigger once per account or once per run max—never spam
3. **Field ending warnings** at 3s give players time to reposition before hazards resume
4. **Unravel cancel sequence** is highest priority VO in the fight—can interrupt lower priority barks
5. **SFX tags** should be distinct and consistent across all Stabilizer uses for audio learnability
