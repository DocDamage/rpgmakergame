# Full Integrity + Stabilizer State Machine Table

**Purpose:** Zero edge-case weirdness—every event maps to exact UI, SFX, and widget animation

---

## State Definitions

### Integrity States (0–6)

| State | Range | Tier Name | Visual | Audio Base |
|-------|-------|-----------|--------|------------|
| **I0** | 0 | STABLE | No cracks | idle_stable |
| **I1** | 1 | STABLE | No cracks | idle_stable |
| **I2** | 2 | STRAINED | Faint cracks | pulse_strained |
| **I3** | 3 | FRACTURED | Visible cracks | flicker_fractured |
| **I4** | 4 | CRITICAL | Heavy cracks, edge vignette low | flash_critical |
| **I5** | 5 | CRITICAL HI | Heavy cracks, "!" badge, edge med | flash_critical_fast |
| **I6** | 6 | BREAKPOINT | Max cracks, shake, edge high | alarm_breakpoint |

### Stabilizer States

| State | Description |
|-------|-------------|
| **S_OFF** | No field active |
| **S_ON** | Stabilization Field active (10s) |
| **S_ENDING** | Field ending (3s warning) |

### Collapse States

| State | Description |
|-------|-------------|
| **C_IDLE** | No collapse active |
| **C_CHARGING** | Collapse charging (2.6s) |
| **C_CANCELLED** | Collapse cancelled |
| **C_EXECUTED** | Collapse executed |

---

## Event → Response Matrix

### Event: Signature Hazard Hit (Integrity Would Increase)

| Condition | Integrity | Stabilizer | Collapse | UI Toast | SFX | Widget Animation |
|-----------|-----------|------------|----------|----------|-----|------------------|
| Standard hit, no throttle | N → N+1 | S_OFF | C_IDLE | `INTEGRITY COMPROMISED.` `INTEGRITY: {N+1}/6` | `sfx_integrity_gain` | Crack appears on new segment |
| Standard hit, throttled (<6s) | N → N+1 | S_OFF | C_IDLE | *(none)* | *(none)* | Crack appears only (silent) |
| Tier boundary crossed | N → N+1 | S_OFF | C_IDLE | `INTEGRITY {TIER} ({N+1}/6).` | `sfx_integrity_tier_{TIER}` | Full tier transition animation |
| Hit at 5/6 → 6/6 | 5 → 6 | S_OFF | C_IDLE | `INTEGRITY CRITICAL (6/6).` `COLLAPSE PROTOCOL IMMINENT.` | `sfx_integrity_tier_breakpoint` | BREAKPOINT state + edge strobe |
| Hit inside field | N (no change) | S_ON | C_IDLE | *(none)* OR `SIGNATURE IMPACT SUPPRESSED.` (throttle) | `sfx_integrity_protected` (throttle) | Shield ripple on meter |
| Hit would push 6/6, field negates | 5 (no change) | S_ON | C_IDLE | `INTEGRITY PROTECTED.` | `sfx_integrity_protected` | Shield flash + "6/6" ghost fade |

### Event: Stabilizer Deployed

| Condition | Integrity | Stabilizer | Collapse | UI Toast | SFX | Widget Animation |
|-----------|-----------|------------|----------|----------|-----|------------------|
| Deploy success, no collapse | N → N-2 (min 0) | S_OFF→S_ON | C_IDLE | `INTEGRITY REDUCED.` `INTEGRITY: {N-2}/6` | `sfx_stabilizer_deploy` + `sfx_integrity_reduce` | Reverse sweep + crack reknit |
| Deploy during charge, cancels | 6 → 4 | S_OFF→S_ON | C_CHARGING→C_CANCELLED | `UNRAVEL CANCELLED.` `TARGET STUNNED.` | `sfx_collapse_cancel` + `sfx_integrity_reduce` + `sfx_window_exposed` | Snap-shut flash, calm drop |
| Deploy, Integrity already 0 | 0 (no change) | S_OFF→S_ON | C_IDLE | `STABILIZATION FIELD — ACTIVE.` | `sfx_stabilizer_deploy` | Halo ring appears |
| Deploy but other field active | N (no change) | S_ON (blocked) | C_IDLE | `FIELD ALREADY ACTIVE.` | `sfx_ui_error_soft` | Red pulse on meter |
| Deploy interrupted | N (no change) | S_OFF | C_IDLE | *(none)* | `sfx_stabilizer_prime_interrupt` | Interrupted anim only |

### Event: Collapse Charge Begins (Organic 6/6 or Forced 20%)

| Condition | Integrity | Stabilizer | Collapse | UI Toast | SFX | Widget Animation |
|-----------|-----------|------------|----------|----------|-----|------------------|
| Organic 6/6 charge start | 6 | S_OFF | C_IDLE→C_CHARGING | `COLLAPSE PROTOCOL — CHARGING.` `STABILIZER REQUIRED.` | `sfx_collapse_charge_start` + loop (1 Hz) | Freeze at 6/6, cast_warning icon |
| Forced 20% charge start | 6 | S_OFF | C_IDLE→C_CHARGING | `CORE UNRAVEL — CHARGING.` | `sfx_forced_unravel_trigger` + lead-in + charge (1.5 Hz) | FORCED overlay, then charge |
| Charge with field active | 6 | S_ON | C_IDLE→C_CHARGING | `COLLAPSE PROTOCOL — CHARGING.` | `sfx_collapse_charge_start` + loop | Cast_warning icon, field halo remains |

### Event: Collapse Resolves (Execute)

| Condition | Integrity | Stabilizer | Collapse | UI Toast | SFX | Widget Animation |
|-----------|-----------|------------|----------|----------|-----|------------------|
| Execute, no field protection | 6 → 3 | S_OFF | C_CHARGING→C_EXECUTED | `COLLAPSE EXECUTED.` `INTEGRITY RESET: 3/6.` | `sfx_collapse_execute` + `sfx_integrity_reset` | Fracture flash, reset sweep |
| Execute, hit inside field | 6 → 3 | S_ON→S_OFF | C_CHARGING→C_EXECUTED | `COLLAPSE EXECUTED.` `FIELD BROKEN.` | `sfx_collapse_execute` + `sfx_stabilizer_field_off` | Field shatter, reset sweep |

### Event: Collapse Cancelled (Stabilizer Counter)

| Condition | Integrity | Stabilizer | Collapse | UI Toast | SFX | Widget Animation |
|-----------|-----------|------------|----------|----------|-----|------------------|
| Cancel organic 6/6 | 6 → 4 | S_OFF→S_ON | C_CHARGING→C_CANCELLED | `UNRAVEL CANCELLED.` `TARGET STUNNED.` `EXPOSED WINDOW.` | `sfx_collapse_cancel` + `sfx_integrity_reduce` + `sfx_window_exposed` | Snap-shut, drop to FRACTURED |
| Cancel forced 20% | 6 → 4 | S_OFF→S_ON | C_CHARGING→C_CANCELLED | `UNRAVEL CANCELLED.` `TARGET STUNNED.` `EXPOSED — GO.` | `sfx_forced_unravel_cancel` + `sfx_integrity_reduce` + `sfx_window_exposed` | Sharper snap-shut, EXPOSED guaranteed |

### Event: Field Lifecycle

| Condition | Integrity | Stabilizer | Collapse | UI Toast | SFX | Widget Animation |
|-----------|-----------|------------|----------|----------|-----|------------------|
| Field starts | N | S_ON | C_IDLE | *(none, or show in widget)* | `sfx_stabilizer_field_loop` starts | Halo ring steady |
| Field 3s warning | N | S_ENDING | C_IDLE | `STABILIZATION FIELD — ENDING.` | `sfx_stabilizer_field_ending` | Halo ring pulse fast |
| Field expires | N | S_OFF | C_IDLE | `FIELD OFFLINE.` | `sfx_stabilizer_field_off` | Halo ring fade |

---

## Priority Override Rules

### When Multiple Events Fire on Same Frame

1. **Collapse state changes** (charge/cancel/execute) override all other audio
2. **Tier entry sounds** override standard gain sounds
3. **Stabilizer deploy** overrides field lifecycle sounds
4. **Integrity gain** lowest priority (can be throttled silently)

### Visual Stack Order (Z-Depth)

```
Top:    Collapse cast overlay (CHARGING)
        ↓
        Breakpoint shake animation (if 6/6)
        ↓
        Stabilizer halo ring (if S_ON)
        ↓
        "!" badge (if 5/6)
        ↓
        Crack overlay (by tier)
        ↓
Base:   Integrity bar fill
```

---

## Edge Case Resolutions

### Edge Case: Hit at 6/6 with Field Active

**Resolution:**
- Integrity stays 6 (field prevents gain)
- No "breakpoint" re-trigger (already at max)
- Field absorbs hit: `sfx_integrity_protected` (throttled)
- If field expires while at 6/6, remain at 6/6 (no auto-collapse)

### Edge Case: Stabilizer Deployed at 5/6

**Resolution:**
- Integrity: 5 → 3
- Tier: CRITICAL → STRAINED
- Toast: `INTEGRITY REDUCED.` `INTEGRITY: 3/6`
- SFX: `sfx_integrity_reduce` + tier transition (STRAINED)
- Widget: Reverse sweep, drop to STRAINED visuals

### Edge Case: Two Stabilizers Deployed Simultaneously

**Resolution:**
- First deploy: succeeds, starts field
- Second deploy: blocked with `FIELD ALREADY ACTIVE`
- No charges consumed on second attempt

### Edge Case: Collapse Charge Starts as Field Expires

**Resolution:**
- Field expires first (frame order)
- Then collapse charge begins
- Player at 6/6 with no field protection
- Full organic collapse sequence plays

### Edge Case: Boss Dies During Charge

**Resolution:**
- Charge immediately cancelled (no execute/cancel SFX)
- Stop `sfx_collapse_charge_loop`
- Play `sfx_collapse_cancel` (short version)
- Victory sequence overrides all Integrity UI

---

## Testing Checklist

- [x] All 6 tier transitions work correctly
- [x] Stabilizer reduces Integrity by exactly 2 (min 0)
- [x] Field prevents Integrity gain while active
- [x] Organic 6/6 collapse: full sequence
- [x] Forced 20% collapse: lead-in + faster tick
- [x] Cancel at any point in charge: stops loop, plays cancel
- [x] Execute: plays slam, resets Integrity
- [x] No audio pops on hard stops
- [x] Visual tier readable without color
- [x] Simultaneous events resolve by priority
- [x] All edge cases handled gracefully
