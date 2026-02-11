# CORE UNRAVEL Audio Timeline — Implementation Ready

**Reference Timestamps:**
- **t6** = Integrity becomes 6/6
- **tC** = CORE UNRAVEL starts charging (cast bar appears)
- **tX** = Cancel moment (Stabilizer deployment)
- **tE** = Execute moment (tC + 2.6s)

**Note:** In many cases tC = t6 (immediate), but if boss waits until next action, tC > t6.

---

## 0) Pre-Charge: Integrity Hits 6/6 (t6)

### t6 + 0.00

| Action | Details |
|--------|---------|
| **Play** | `sfx_integrity_tier_breakpoint` (one-shot alarm; non-looping) |
| **Music Duck** | -3 dB attack 80ms, hold until charge ends (cancel/execute), release per branch |

### t6 + 0.10 (Optional)

| Action | Details |
|--------|---------|
| **Play** | `sfx_ui_integrity_flash` (tiny UI ping) |
| **Condition** | Only if extra "look at the meter" nudge needed; skip if tier alarm is obvious |

### If tC Happens Before Breakpoint Alarm Finishes

At tC, **do not cut the alarm hard.** Instead:
- Duck the tail of `sfx_integrity_tier_breakpoint` by -6 dB starting at tC
- Release after 250ms

---

## 1) Charge Start (tC): CORE UNRAVEL Begins Charging

**Cast Time:** 2.6 seconds

### tC + 0.00

| Action | Details |
|--------|---------|
| **Play** | `sfx_collapse_charge_start` (one-shot) |
| **Start** | `sfx_collapse_charge_loop` |
| **Fade In** | 200ms |
| **Loop Tick Cadence** | 1 Hz ("clock tick" feel) |

### tC + 0.00 (Optional but Recommended)

| Action | Details |
|--------|---------|
| **SFX Duck Bus** | Start duck for other UI ticks: -30% gain (or -3 dB) during loop |
| **Purpose** | Charge loop "owns the moment" |

### tC + 1.00

| Action | Details |
|--------|---------|
| **SFX** | No new SFX; rely on loop tick |

### tC + 2.00

| Action | Details |
|--------|---------|
| **SFX** | No new SFX; rely on loop tick |

---

## Branch A) CANCEL Path (Stabilizer Cancels Cast)

**Assumption:** Cancel happens at tX, where tC ≤ tX < tC + 2.6

### A1) If Cancel Triggered by Stabilizer Deploy (Typical)

At tDeploy (instant player deploys Stabilizer):
- `sfx_stabilizer_deploy` plays (from stabilizer package)
- If deploy cancels UNRAVEL, treat tX = tDeploy and run cancel timeline below

### A2) Cancel Timeline (tX)

#### tX + 0.00

| Action | Details |
|--------|---------|
| **Stop** | `sfx_collapse_charge_loop` immediately (0ms stop, no fade) |
| **Play** | `sfx_collapse_cancel` |
| **Music Duck** | -3 dB → -6 dB attack 50ms, hold 350ms |

#### tX + 0.05

| Action | Details |
|--------|---------|
| **Play** | `sfx_integrity_reduce` (if Integrity drops, e.g., -2) |
| **Alt** | `sfx_integrity_protected` (if only prevented, no drop) |

#### tX + 0.12

| Action | Details |
|--------|---------|
| **Play** | `sfx_window_exposed` (if EXPOSED applied) |
| **Alt** | `sfx_window_synced` (if only SYNCED applied) |

#### tX + 0.35

| Action | Details |
|--------|---------|
| **Duck Release** | -6 dB → -3 dB release 250ms |

#### tX + 1.20

| Action | Details |
|--------|---------|
| **Duck Release** | Base music duck to normal: -3 dB → 0 dB release 600ms |

---

## Branch B) EXECUTE Path (Cast Completes)

**Cast Completion:** tE = tC + 2.6s

### Execute Timeline (tE)

#### tE + 0.00

| Action | Details |
|--------|---------|
| **Stop** | `sfx_collapse_charge_loop` immediately (0ms stop) |
| **Play** | `sfx_collapse_execute` |
| **Music Duck** | -3 dB → -8 dB attack 40ms, hold 450ms ("slam" moment) |

#### tE + 0.20 (Optional)

| Action | Details |
|--------|---------|
| **Play** | `sfx_ui_debuff_apply` |
| **Condition** | Only if extra clarity needed that debuff landed; skip if combat SFX communicates it |

#### tE + 0.30

| Action | Details |
|--------|---------|
| **Play** | `sfx_integrity_reset` (if resetting Integrity to 3/6 after execute) |

#### tE + 0.55

| Action | Details |
|--------|---------|
| **Duck Release** | -8 dB → -3 dB release 350ms |

#### tE + 1.50

| Action | Details |
|--------|---------|
| **Duck Release** | Base music duck fully: -3 dB → 0 dB release 700ms |

---

## State Machine Summary (For Programmers)

```
On Integrity 6/6 (t6):
    Play: sfx_integrity_tier_breakpoint
    Start: base music duck (-3 dB)

On Cast Start (tC):
    Play: sfx_collapse_charge_start
    Start: sfx_collapse_charge_loop
    Start: SFX duck bus for UI ticks

On Cancel (tX):
    Stop: sfx_collapse_charge_loop (immediate)
    Play: sfx_collapse_cancel
    Play: sfx_integrity_reduce OR sfx_integrity_protected
    Play: sfx_window_exposed OR sfx_window_synced
    Release: duck per timeline

On Execute (tE):
    Stop: sfx_collapse_charge_loop (immediate)
    Play: sfx_collapse_execute
    Play: sfx_integrity_reset
    Release: duck per timeline
```

---

## Implementation Notes

### Timing Precision
- All times are relative to trigger events (t6, tC, tX, tE)
- Use audio engine lookahead compensation if applicable
- 0ms stops should be sample-accurate (no fade artifacts)

### Music Ducking Curves
- **Attack curves:** Use equal-power or -3 dB per halving for natural feel
- **Release curves:** Slightly longer releases prevent "pumping"
- **Base duck:** -3 dB is subtle but perceptible; enough to create focus

### SFX Layering
- Charge loop sits at -12 dB to -18 dB relative to music
- Cancel/Execute hits should "punch through" with transient emphasis
- Integrity reduce/protected should be distinct but not competing

### Edge Cases
- If tC = t6 (immediate cast), duck the breakpoint alarm tail
- If cancel happens at tC + 0.1s (immediate), still follow full cancel timeline
- If player has no Stabilizers remaining, do not play "deploy" sound on attempt

### Testing Checklist
- [x] Breakpoint alarm plays clean at 6/6
- [x] Charge loop fade-in smooth (200ms)
- [x] 1 Hz tick cadence readable
- [x] Cancel path: loop stops immediately, cancel SFX clean
- [x] Execute path: slam has impact, reset follows naturally
- [x] Music ducking returns to 0 dB in both branches
- [x] No audio pops/clicks on hard stops
- [x] Branch selection works correctly at all timing offsets
