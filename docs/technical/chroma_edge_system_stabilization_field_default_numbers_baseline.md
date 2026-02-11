# Stabilization Field — Final Default Numbers (Recommended Baseline)

## Core Values

### Stabilization Field (Area Effect)

| Property | Value |
|----------|-------|
| **Duration** | 10s |
| **Hazard damage reduction** | 70% |
| **Pull/knockback reduction** | 70% |
| **Hard control downgrade** | STOP/FREEZE → SLOW while inside (where applicable) |

### SYNCED (Enemy Debuff — Standard Burst Window)

| Property | Value |
|----------|-------|
| **Duration** | 8s |
| **Damage taken increase** | +30% |

### EXPOSED (Enemy Debuff — Earned Window)

| Property | Value |
|----------|-------|
| **Duration** | 10s |
| **Damage taken increase** | +45% |
| **Rule** | Overrides SYNCED (no stacking confusion) |

### PINNED (Enemy State)

| Property | Value |
|----------|-------|
| **Duration** | 8s |
| **Effect** | Reposition/teleport disabled |
| **Optional** | Movement speed reduced: 50% |

### STUNNED (Enemy State)

| Property | Value |
|----------|-------|
| **Duration** | 2s |
| **Effect** | Unable to act |

---

## On-Screen HUD Text Package (Numbers Filled)

### 1) Area Effect Banner

| Element | Value |
|---------|-------|
| **Type** | AREA EFFECT |
| **Name** | `STABILIZATION FIELD` |
| **Icon ID** | `icon_field_stabilization` |
| **HUD Banner** | `STABILIZATION FIELD: {SEC}s` (counts down from 10) |
| **Mini line** | `Hazards suppressed • Forced movement weakened` |

#### Tooltip

```
Title: STABILIZATION FIELD

Body:
Reduces environmental hazard damage by 70%.
Reduces pull/knockback strength by 70%.
Stop/Freeze effects become Slow while inside (where applicable).

Source: Stabilizer
```

---

### 2) Player Buff (While Inside)

| Element | Value |
|---------|-------|
| **Type** | BUFF |
| **Name** | `STABILIZED` |
| **Icon ID** | `icon_buff_stabilized` |
| **Label** | `STABILIZED ({SEC}s)` |

#### Tooltip

```
Title: STABILIZED

Body:
Hazard damage taken reduced by 70%.
Pull/knockback reduced by 70%.
Stop/Freeze becomes Slow while inside (where applicable).

Note: Only active while inside the Stabilization Field.
Source: Stabilization Field
```

---

### 3) Enemy Debuff (Standard Burst Window)

| Element | Value |
|---------|-------|
| **Type** | DEBUFF |
| **Name** | `SYNCED` |
| **Icon ID** | `icon_debuff_synced` |
| **Label** | `SYNCED ({SEC}s)` (counts down from 8) |

#### Tooltip

```
Title: SYNCED

Body:
Damage taken increased by 30%.
Applied when caught in a Stabilization Field.

Source: Stabilization Field
```

---

### 4) Enemy Debuff (Big Earned Window)

| Element | Value |
|---------|-------|
| **Type** | DEBUFF |
| **Name** | `EXPOSED` |
| **Icon ID** | `icon_debuff_exposed` |
| **Label** | `EXPOSED ({SEC}s)` (counts down from 10) |

#### Tooltip

```
Title: EXPOSED

Body:
Damage taken increased by 45%.
Triggered when a major collapse cast is cancelled.

Overrides SYNCED.
Source: Stabilizer Counter
```

---

### 5) Enemy States (Control Feedback)

#### PINNED

| Element | Value |
|---------|-------|
| **Type** | STATE |
| **Name** | `PINNED` |
| **Icon ID** | `icon_state_pinned` |
| **Label** | `PINNED ({SEC}s)` (counts down from 8) |

**Tooltip:**
```
Title: PINNED

Body:
Reposition and teleport effects disabled.
Movement speed reduced by 50%.

Source: Stabilizer / Clamp
```

#### STUNNED

| Element | Value |
|---------|-------|
| **Type** | STATE |
| **Name** | `STUNNED` |
| **Icon ID** | `icon_state_stunned` |
| **Label** | `STUNNED ({SEC}s)` (counts down from 2) |

**Tooltip:**
```
Title: STUNNED

Body: Unable to act until the effect ends.

Source: Stabilizer Counter
```

---

### 6) Threat / Cast UI (Core Vault + "Collapse" Fights)

| Element | Value |
|---------|-------|
| **Type** | THREAT |
| **Name** | `CORE UNRAVEL` |
| **Icon ID** | `icon_threat_unravel` |
| **Cast Bar Text** | `CORE UNRAVEL — {SEC}s` |

**Tooltip:**
```
A catastrophic collapse is imminent.
Deploy a Stabilizer to cancel this cast.
```

---

### 7) System Toasts (Consistent Everywhere)

#### Field Lifecycle

| Trigger | Toast |
|---------|-------|
| Field begins | `STABILIZATION FIELD — ACTIVE.` |
| Field ending | `STABILIZATION FIELD — ENDING.` |
| Field ends | `STABILIZATION FIELD — OFFLINE.` |

#### Burst Window

| Trigger | Toast |
|---------|-------|
| Standard window | `TARGET SYNCED — DAMAGE WINDOW.` |
| Extended window | `EXPOSED — DAMAGE WINDOW EXTENDED.` |

#### Counter Moment

| Trigger | Toast |
|---------|-------|
| Unravel cancelled | `UNRAVEL CANCELLED.` |
| Boss stunned | `TARGET STUNNED.` |
| Boss pinned | `TARGET PINNED.` |
| Integrity reduced | `INTEGRITY REDUCED.` |

---

## Quick Reference Table

| Effect | Duration | Numeric Value | Override Rule |
|--------|----------|---------------|---------------|
| **Stabilization Field** | 10s | 70% hazard/pull reduction | — |
| **SYNCED** | 8s | +30% damage taken | — |
| **EXPOSED** | 10s | +45% damage taken | Overrides SYNCED |
| **PINNED** | 8s | 50% move speed | — |
| **STUNNED** | 2s | Cannot act | — |

---

## Tiny Tuning Knobs (Playtest Adjustments)

> No new design needed—just nudge numbers:

### If Stabilizer Trivializes Hazards

| Adjustment | Change |
|------------|--------|
| Hazard reduction | 70% → 60% |
| Pull reduction | 70% → 60% |

### If Burst Windows Melt Bosses Too Fast

| Adjustment | Change |
|------------|--------|
| SYNCED damage | +30% → +25% |
| EXPOSED damage | +45% → +35% |
| EXPOSED duration | 10s → 8s |

### If Cancel Feels Mandatory

| Adjustment | Solution |
|------------|----------|
| Keep cancel mechanic | It's intentional |
| Shorten reward window | EXPOSED 10s → 8s |

---

## Implementation Summary

```
FIELD DEPLOYED (10s)
├── Banner: STABILIZATION FIELD — ACTIVE
├── Player inside → BUFF: STABILIZED (70% reduction)
├── Enemy inside → DEBUFF: SYNCED (+30% damage, 8s)
│
├── [If cancels major cast]
│   ├── STATE: STUNNED (2s)
│   ├── STATE: PINNED (8s) [optional]
│   └── DEBUFF: EXPOSED (+45% damage, 10s, overrides SYNCED)
│
├── 7s remaining
│   └── [Continue]
│
├── 3s remaining
│   └── TOAST: STABILIZATION FIELD — ENDING
│
└── 0s
    ├── TOAST: STABILIZATION FIELD — OFFLINE
    └── All buffs/debuffs clear
```

---

## Notes for QA/Balance

- **70% reduction** creates meaningful protection without total immunity
- **30% damage boost (SYNCED)** is a solid but not overwhelming DPS window
- **45% damage boost (EXPOSED)** is the "earned" reward for skilled counterplay
- **10s field duration** gives time to reposition and burst, but not infinite safety
- **2s stun** is long enough to punish, short enough to not feel oppressive
- **EXPOSED overrides SYNCED** prevents confusion—players see the bigger number
