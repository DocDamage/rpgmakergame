# Stabilization Field — HUD Text Package (Unified)

**Usage:** Tower / Palace / Remnant Vault / Any future content

**Note:** Token placeholders ({PCT}, {SEC}, etc.) allow string reuse across modes (Wing vs Core Vault vs Tower boss).

---

## 1) Area Effect (Global HUD Banner)

### AREA EFFECT: Stabilization Field

| Property | Value |
|----------|-------|
| **Display Name** | `STABILIZATION FIELD` |
| **Icon ID** | `icon_field_stabilization` |
| **HUD Banner** (top-center) | `STABILIZATION FIELD: {SEC}s` |
| **Mini HUD** (optional, under banner) | `Hazards suppressed • Integrity stabilized` |

### Tooltip (Banner Hover)

```
Title: STABILIZATION FIELD

Body:
Reduces environmental hazard intensity by {PCT}%.
Reduces pull/knockback strength by {PCT_PULL}%.
Severe control effects are downgraded while inside.

Source: Stabilizer Station
```

---

## 2) Player Buff (Inside Field)

### BUFF: Stabilized

| Property | Value |
|----------|-------|
| **Display Name** | `STABILIZED` |
| **Icon ID** | `icon_buff_stabilized` |
| **Buff Bar Label** | `STABILIZED ({SEC}s)` |
| **Short Tooltip** | Hazards reduced. Forced movement weakened. Control effects softened. |

### Full Tooltip

```
Title: STABILIZED

Body:
Incoming hazard damage reduced by {PCT}%.
Pull/knockback reduced by {PCT_PULL}%.
Stop/Freeze effects become Slow (where applicable).

Notes: Only active while inside the Stabilization Field.
Source: Stabilization Field
```

---

## 3) Enemy Debuff (Burst Window — Normal)

### DEBUFF: Synced

| Property | Value |
|----------|-------|
| **Display Name** | `SYNCED` |
| **Icon ID** | `icon_debuff_synced` |
| **Debuff Bar Label** | `SYNCED ({SEC}s)` |
| **Short Tooltip** | Takes increased damage. |

### Full Tooltip

```
Title: SYNCED

Body:
Damage taken increased by {PCT_DMG_TAKEN}%.
Applied when enemies are caught in a Stabilization Field.

Source: Stabilization Field
```

---

## 4) Enemy Debuff (Burst Window — Hard Counter)

### DEBUFF: Exposed

| Property | Value |
|----------|-------|
| **Display Name** | `EXPOSED` |
| **Icon ID** | `icon_debuff_exposed` |
| **Debuff Bar Label** | `EXPOSED ({SEC}s)` |
| **Short Tooltip** | Takes greatly increased damage. |

### Full Tooltip

```
Title: EXPOSED

Body:
Damage taken increased by {PCT_DMG_TAKEN}%.
Triggered when a major cast is cancelled (e.g., CORE UNRAVEL).

Source: Stabilizer Counter
```

---

## 5) Enemy States (Cast Cancellation)

### STATE: Pinned

| Property | Value |
|----------|-------|
| **Display Name** | `PINNED` |
| **Icon ID** | `icon_state_pinned` |
| **State Label** | `PINNED ({SEC}s)` |
| **Short Tooltip** | Cannot reposition. |

### Full Tooltip

```
Title: PINNED

Body:
Reposition and teleport effects disabled.
Movement speed reduced by {PCT_MOVE}%. (optional)

Source: Stabilizer / Clamp
```

### STATE: Stunned

| Property | Value |
|----------|-------|
| **Display Name** | `STUNNED` |
| **Icon ID** | `icon_state_stunned` |
| **State Label** | `STUNNED ({SEC}s)` |
| **Short Tooltip** | Cannot act. |

### Full Tooltip

```
Title: STUNNED

Body: Unable to act until the effect ends.

Source: Stabilizer Counter
```

---

## 6) Cast/Threat Callouts

### THREAT: Core Unravel (Cast Banner)

| Property | Value |
|----------|-------|
| **Display Name** | `CORE UNRAVEL` |
| **Icon ID** | `icon_threat_unravel` |
| **Cast Bar Text** | `CORE UNRAVEL — {SEC}s` |

### Cast Tooltip

```
A catastrophic collapse is imminent.
Deploy a Core Stabilizer to cancel this cast.
```

### Integrity Meter (HUD Widget)

| Property | Value |
|----------|-------|
| **Widget Label** | `INTEGRITY` |
| **Icon ID** | `icon_meter_integrity` |
| **Meter Text** | `INTEGRITY: {N}/6` |

### Tooltip

```
Increases when you are hit by signature hazards.
At 6/6, CORE UNRAVEL will trigger.
```

---

## 7) Standardized System Toast Strings

### Field Lifecycle

| Trigger | Toast |
|---------|-------|
| Field begins | `STABILIZATION FIELD — ACTIVE.` |
| Field ending | `STABILIZATION FIELD — ENDING.` |
| Field ends | `STABILIZATION FIELD — OFFLINE.` |

### Burst Window Feedback

| Trigger | Toast |
|---------|-------|
| Normal damage window | `TARGET SYNCED — DAMAGE WINDOW.` |
| Extended damage window | `EXPOSED — DAMAGE WINDOW EXTENDED.` |

### Unravel Interaction (Core Vault)

| Trigger | Toast |
|---------|-------|
| Cast begins | `CORE UNRAVEL — CHARGING.` |
| Successfully cancelled | `UNRAVEL CANCELLED.` |
| Boss stunned | `TARGET STUNNED.` |
| Integrity reduced | `INTEGRITY REDUCED.` |

---

## 8) UI Rules (Consistency)

### Display Hierarchy

1. **Global banner timer** — Shows for all Stabilization Fields
2. **STABILIZED buff** — Applied to units inside field
3. **SYNCED debuff** — "Normal" damage window (enemy caught in field)
4. **EXPOSED debuff** — "Earned" damage window (cancelled something big)

### Priority Rule

> If both SYNCED and EXPOSED are present, **show EXPOSED first** and let it override damage-taken math (no stacking confusion).

### State Transitions

```
Field Deployed
    ↓
Banner: STABILIZATION FIELD — ACTIVE
    ↓
Player inside → BUFF: STABILIZED
Enemy inside → DEBUFF: SYNCED
    ↓
[If cancels major cast]
    ↓
STATE: STUNNED (boss)
DEBUFF: EXPOSED (replaces/augments SYNCED)
TOAST: UNRAVEL CANCELLED / TARGET STUNNED / EXPOSED
    ↓
Field ending (3s warning)
    ↓
TOAST: STABILIZATION FIELD — ENDING
    ↓
Field ends
    ↓
TOAST: STABILIZATION FIELD — OFFLINE
All buffs/debuffs clear
```

---

## 9) Token Reference

| Token | Description | Example Values |
|-------|-------------|----------------|
| `{SEC}` | Duration in seconds | `10`, `8`, `2` |
| `{PCT}` | Hazard reduction percentage | `70`, `50` |
| `{PCT_PULL}` | Pull/knockback reduction | `70`, `50` |
| `{PCT_DMG_TAKEN}` | Damage increase percentage | `30`, `20` |
| `{PCT_MOVE}` | Movement speed reduction | `50`, `0` |
| `{N}` | Current integrity value | `0`–`6` |

---

## 10) Icon Asset Summary

| Icon ID | Usage |
|---------|-------|
| `icon_field_stabilization` | Area effect banner, field visualization |
| `icon_buff_stabilized` | Player buff bar |
| `icon_debuff_synced` | Enemy debuff bar (standard damage window) |
| `icon_debuff_exposed` | Enemy debuff bar (earned damage window) |
| `icon_state_pinned` | Enemy state (reposition disabled) |
| `icon_state_stunned` | Enemy state (action disabled) |
| `icon_threat_unravel` | Cast bar, threat indicator |
| `icon_meter_integrity` | Integrity meter widget |

---

## 11) Mode-Specific Value Examples

### Wing Stabilizer (Remnant Vault)

| Token | Value |
|-------|-------|
| `{SEC}` | `10` |
| `{PCT}` | `70` |
| `{PCT_PULL}` | `70` |
| `{PCT_DMG_TAKEN}` (SYNCED) | `30` |

### Core Vault Stabilizer (Remnant Custodian)

| Token | Value |
|-------|-------|
| `{SEC}` | `10` |
| `{PCT}` | `70` |
| `{PCT_PULL}` | `70` |
| `{PCT_DMG_TAKEN}` (SYNCED) | `30` |
| `{PCT_DMG_TAKEN}` (EXPOSED) | `50` or `20` additive |
| `{PCT_MOVE}` (PINNED) | `0` or `50` |
| `{SEC}` (STUNNED) | `2` |
| `{SEC}` (EXPOSED) | `10` |

### Tower / Palace Boss (Future Use)

| Token | Suggested Value |
|-------|-----------------|
| `{SEC}` | `8`–`12` (mode dependent) |
| `{PCT}` | `50`–`70` |
| `{PCT_DMG_TAKEN}` | `20`–`30` |

---

## 12) Implementation Checklist

- [x] All icon assets created and linked to IDs
- [x] Token replacement system implemented
- [x] Toast queue prioritization (Unravel > Field states > Synced/Exposed)
- [x] Buff/debuff stacking rules (EXPOSED overrides SYNCED display)
- [x] Localization strings exported with tokens preserved
- [x] SFX hooks tied to toast triggers
- [x] Visual field effect matches banner timer
