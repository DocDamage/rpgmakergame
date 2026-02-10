# Forced 20% UNRAVEL Audio Timeline (Scripted/Stakes Version)

**Context:** Core Vault boss forces CORE UNRAVEL at 20% HP regardless of Integrity value

**Design Goal:** Distinct from organic 6/6 Unravel—players must feel this is **scripted, inevitable, and high-stakes**

---

## Reference Timestamps

| Timestamp | Definition |
|-----------|------------|
| **t20** | Boss HP hits 20% (trigger moment) |
| **tL** | Lead-in starts (audio foreshadowing) |
| **tC** | CORE UNRAVEL begins charging (cast bar appears) |
| **tX** | Cancel moment (Stabilizer deployment) |
| **tE** | Execute moment (tC + 2.6s) |

**Timing Relationship:** t20 → tL (+0.8s) → tC (+1.2s from tL, +2.0s from t20)

---

## Phase 1: Trigger Recognition (t20)

### t20 + 0.00

| Action | Details |
|--------|---------|
| **System Toast** | `FORCED EVENT: CORE UNRAVEL.` |
| **Boss VO** | *"The record closes."* |
| **SFX** | `sfx_forced_unravel_trigger` (low, rising tension tone) |
| **Music** | Begin tension swell: -2 dB → -4 dB over 1.5s |
| **Widget** | Flash "FORCED" overlay on Integrity meter (0.3s) |

### t20 + 0.40

| Action | Details |
|--------|---------|
| **System Toast** | `STABILIZE OR SHATTER.` |
| **SFX** | `sfx_ui_warning_chime` (higher pitch than organic 6/6) |

---

## Phase 2: Lead-In Foreshadowing (tL = t20 + 0.8s)

**Purpose:** Build tension; signal "this is coming whether you're ready or not"

### tL + 0.00

| Action | Details |
|--------|---------|
| **SFX** | `sfx_unravel_leadin_start` (rhythmic pulse, 80 BPM, metallic) |
| **Music** | Lock at -4 dB duck; stinger layer enters |
| **Screen** | Subtle vignette pulse begins (slower than 6/6 breakpoint) |

### tL + 0.40

| Action | Details |
|--------|---------|
| **SFX** | Second pulse hit (layered harmony) |
| **Widget** | Integrity icon begins slow pulse (0.8s cadence) |

### tL + 0.80

| Action | Details |
|--------|---------|
| **SFX** | Third pulse + rising harmonic |

---

## Phase 3: Charge Start (tC = tL + 1.2s = t20 + 2.0s)

### tC + 0.00

| Action | Details |
|--------|---------|
| **SFX** | `sfx_collapse_charge_start` (sharper attack than organic version) |
| **Start** | `sfx_collapse_charge_loop` (modified: faster tick, 1.5 Hz) |
| **Fade In** | 150ms (faster than organic 200ms) |
| **Music** | Aggressive duck: 0 dB → -6 dB attack 60ms |
| **Toast** | `CORE UNRAVEL — CHARGING.` |

**Key Difference:** Faster tick cadence (1.5 Hz vs 1 Hz) = "scripted urgency"

### tC + 0.00 (Simultaneous)

| Action | Details |
|--------|---------|
| **SFX Duck Bus** | -40% (deeper than organic -30%) |
| **Widget** | `CORE UNRAVEL — CHARGING ({SEC}s)` overlay |

---

## Branch A) CANCEL Path (Stabilizer Cancels at tX)

### tX + 0.00

| Action | Details |
|--------|---------|
| **Stop** | `sfx_collapse_charge_loop` + `sfx_unravel_leadin_start` (0ms) |
| **Play** | `sfx_forced_unravel_cancel` (sharper, more "mechanical snap" than organic) |
| **Music** | -6 dB → -8 dB attack 40ms, hold 400ms (deeper slam than organic) |
| **Boss VO** | *"—Denied."* (optional, only if VO budget permits) |

### tX + 0.05

| Action | Details |
|--------|---------|
| **Play** | `sfx_integrity_reduce` OR `sfx_integrity_protected` |
| **Toast** | `UNRAVEL CANCELLED.` |

### tX + 0.10

| Action | Details |
|--------|---------|
| **Play** | `sfx_window_exposed` (guaranteed EXPOSED on forced cancel) |
| **Toast** | `TARGET STUNNED.` / `EXPOSED WINDOW — GO.` |

### tX + 0.50

| Action | Details |
|--------|---------|
| **Music** | -8 dB → -4 dB release 300ms |

### tX + 1.50

| Action | Details |
|--------|---------|
| **Music** | -4 dB → 0 dB release 800ms (slower, more dramatic recovery) |

---

## Branch B) EXECUTE Path (Cast Completes at tE)

### tE + 0.00

| Action | Details |
|--------|---------|
| **Stop** | `sfx_collapse_charge_loop` + `sfx_unravel_leadin_start` (0ms) |
| **Play** | `sfx_forced_unravel_execute` (heavier, more "structural collapse" than organic) |
| **Music** | -6 dB → -10 dB attack 30ms, hold 600ms (maximum impact duck) |
| **Screen** | Full-screen fracture flash (0.15s) |

### tE + 0.15

| Action | Details |
|--------|---------|
| **Toast** | `COLLAPSE EXECUTED.` |
| **SFX** | `sfx_unravel_aftershock` (rumble bed, 2.0s) |

### tE + 0.40

| Action | Details |
|--------|---------|
| **Play** | `sfx_integrity_reset` |
| **Toast** | `INTEGRITY RESET: 3/6.` |
| **Widget** | Crack "heal" animation (slower than organic, 0.8s) |

### tE + 0.80

| Action | Details |
|--------|---------|
| **Music** | -10 dB → -5 dB release 500ms |

### tE + 2.00

| Action | Details |
|--------|---------|
| **Music** | -5 dB → 0 dB release 1000ms (long recovery from failure) |
| **Stop** | `sfx_unravel_aftershock` fade out |

---

## Key Differences: Forced vs Organic Unravel

| Element | Organic (6/6) | Forced (20%) |
|---------|---------------|--------------|
| **Trigger** | Player error (hits) | Scripted boss mechanic |
| **Lead-in** | None (immediate) | 2.0s foreshadowing |
| **Charge tick** | 1.0 Hz | 1.5 Hz (urgent) |
| **Music duck curve** | -3 dB base | -4 dB with swell |
| **Execute duck** | -8 dB | -10 dB |
| **Recovery time** | Fast (0.6s) | Slow (0.8–1.0s) |
| **SFX flavor** | Standard | Heavier, mechanical |
| **Guaranteed EXPOSED** | No (depends on cancel timing) | Yes (if cancelled) |

---

## Quick Reference: Forced Unravel State Machine

```
Boss HP = 20%
    ↓
t20: Trigger
    ├── Toast: FORCED EVENT: CORE UNRAVEL
    ├── Boss VO: "The record closes."
    ├── SFX: sfx_forced_unravel_trigger
    └── Music: Begin tension swell
    ↓
t20 + 0.4s
    └── Toast: STABILIZE OR SHATTER
    ↓
tL (t20 + 0.8s): Lead-in Start
    ├── SFX: sfx_unravel_leadin_start (80 BPM pulse)
    └── Music: Lock at -4 dB
    ↓
tC (tL + 1.2s): Charge Start
    ├── SFX: sfx_collapse_charge_start + loop (1.5 Hz)
    ├── Music: Aggressive duck -6 dB
    └── Toast: CORE UNRAVEL — CHARGING
    ↓
Branch A: Cancel (tX)
    ├── Stop all loops (0ms)
    ├── SFX: sfx_forced_unravel_cancel
    ├── Music: Slam duck -8 dB
    ├── SFX: sfx_integrity_reduce/protected
    ├── SFX: sfx_window_exposed
    └── Music: Slow recovery 1.5s
    ↓
Branch B: Execute (tE = tC + 2.6s)
    ├── Stop all loops (0ms)
    ├── SFX: sfx_forced_unravel_execute + aftershock
    ├── Music: Max duck -10 dB
    ├── Screen: Fracture flash
    ├── SFX: sfx_integrity_reset
    └── Music: Long recovery 2.0s
```

---

## New SFX Assets Required

| SFX ID | Usage | Description |
|--------|-------|-------------|
| `sfx_forced_unravel_trigger` | t20 | Low rising tension tone |
| `sfx_unravel_leadin_start` | tL | 80 BPM metallic pulse |
| `sfx_forced_unravel_cancel` | tX | Sharper mechanical snap |
| `sfx_forced_unravel_execute` | tE | Heavier structural collapse |
| `sfx_unravel_aftershock` | tE+ | Rumble bed (2.0s) |
| `sfx_ui_warning_chime` | t20+ | Higher pitch warning |

**Reused Assets:**
- `sfx_collapse_charge_start` (modified attack)
- `sfx_collapse_charge_loop` (modified to 1.5 Hz)
- `sfx_integrity_reduce` / `protected` / `reset`
- `sfx_window_exposed`
