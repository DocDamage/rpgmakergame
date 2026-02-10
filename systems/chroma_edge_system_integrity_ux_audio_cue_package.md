# Integrity UX — Standard Audio Cue Package

**Usage:** Tower / Palace / Remnant Vault — Any content with Integrity mechanic

**Design Philosophy:** Single shared sound-language, skinnable per biome (different instrument layers), consistent timing + intent

---

## 1) Core SFX Event IDs

### Integrity Tier Entry (One-Shot)

| SFX ID | Trigger | Notes |
|--------|---------|-------|
| `sfx_integrity_tier_strained` | Enter 2/6 | Single soft tick |
| `sfx_integrity_tier_fractured` | Enter 3/6 | Tick + tiny after-click |
| `sfx_integrity_tier_critical` | Enter 4/6 | Double-tick |
| `sfx_integrity_tier_critical_hi` | Enter 5/6 | Double-tick + short warning chirp |
| `sfx_integrity_tier_breakpoint` | Enter 6/6 | Alarm tone (short, non-looping) |

### Integrity Gain (Generic +1 Crack)

| SFX ID | Trigger |
|--------|---------|
| `sfx_integrity_gain` | Short crack-tick on +1 increase |

### Integrity Protected / Suppressed

| SFX ID | Trigger |
|--------|---------|
| `sfx_integrity_protected` | Field negates a would-be gain — soft "shimmer lock" |

### Integrity Reduced

| SFX ID | Trigger |
|--------|---------|
| `sfx_integrity_reduce` | Stabilizer -2 — reverse-tick / stitch-back |

### Integrity Reset

| SFX ID | Trigger |
|--------|---------|
| `sfx_integrity_reset` | Post-collapse resolves → back to 3/6 — low "settle" thump |

---

## 2) Collapse Protocol (Universal Cast Audio)

### Collapse Charging Start

| SFX ID | Trigger |
|--------|---------|
| `sfx_collapse_charge_start` | One-shot when cast begins |

### Collapse Charging Loop

| SFX ID | Trigger |
|--------|---------|
| `sfx_collapse_charge_loop` | Very low, ticking bed while cast bar counts down — not loud |

### Collapse Executes

| SFX ID | Trigger |
|--------|---------|
| `sfx_collapse_execute` | Heavy fracture hit on cast completion |

### Collapse Cancelled

| SFX ID | Trigger |
|--------|---------|
| `sfx_collapse_cancel` | Sharp "snap shut" + release whoosh on Stabilizer counter |

---

## 3) Stabilizer Audio

### Deploy / Prime

| SFX ID | Trigger |
|--------|---------|
| `sfx_stabilizer_prime_start` | Interact start |
| `sfx_stabilizer_prime_interrupt` | Channel interrupted |
| `sfx_stabilizer_deploy` | Field turns on (successful deploy) |

### Field Bed

| SFX ID | Trigger |
|--------|---------|
| `sfx_stabilizer_field_loop` | Gentle hum while active — sits under music |

### Field Ending Cues

| SFX ID | Trigger |
|--------|---------|
| `sfx_stabilizer_field_ending` | 3s remaining |
| `sfx_stabilizer_field_off` | Field expires |

### Burst Window Confirmation (Optional)

| SFX ID | Trigger |
|--------|---------|
| `sfx_window_synced` | SYNCED applied — "hit the gas" ping |
| `sfx_window_exposed` | EXPOSED applied — more "premium" than SYNCED |

---

## 4) Trigger Rules (Exact, Consistent)

### A) Integrity Gain (+1)

| Property | Value |
|----------|-------|
| **Play** | `sfx_integrity_gain` |
| **When** | Integrity increases by +1 from signature hazard hit |
| **Throttle** | Max 1 per 6s, except when crossing into 4/6+ (see tiers) |

### B) Tier Entry (Overrides Gain Sound)

When Integrity hits a tier boundary, **play only the tier sound** (don't double-play gain):

| At | Sound |
|----|-------|
| 2/6 | `sfx_integrity_tier_strained` |
| 3/6 | `sfx_integrity_tier_fractured` |
| 4/6 | `sfx_integrity_tier_critical` |
| 5/6 | `sfx_integrity_tier_critical_hi` |
| 6/6 | `sfx_integrity_tier_breakpoint` (alarm) |

**Throttle:** None (tier entry is inherently rare)

### C) Breakpoint (6/6) → Impending Collapse

On reaching 6/6, immediately play:
- `sfx_integrity_tier_breakpoint`

**Rule:** If boss doesn't start casting right away, do not loop anything. Save the loop for when cast actually begins.

### D) Collapse Charging

When collapse cast begins:
1. Play `sfx_collapse_charge_start`
2. Start `sfx_collapse_charge_loop` until cast ends

When cast ends: Stop loop immediately

### E) Collapse Executes

If cast completes:
1. Play `sfx_collapse_execute`
2. Then (if resetting Integrity) play `sfx_integrity_reset` 0.2–0.4s later

### F) Collapse Cancelled (Stabilizer Counter)

If Stabilizer cancels the cast:
1. Play `sfx_collapse_cancel`
2. Then play `sfx_integrity_reduce` if Integrity drops (-2), otherwise `sfx_integrity_protected`

### G) Stabilizer Lifecycle

| Event | Sound |
|-------|-------|
| On interact start | `sfx_stabilizer_prime_start` |
| On interrupt | `sfx_stabilizer_prime_interrupt` |
| On successful deploy | `sfx_stabilizer_deploy` + start `sfx_stabilizer_field_loop` |
| At 3s remaining | `sfx_stabilizer_field_ending` |
| On end | Stop loop + `sfx_stabilizer_field_off` |

### H) Field Negates Integrity Gain

If signature hazard hit is suppressed (no Integrity increase):
- Play `sfx_integrity_protected`
- **Throttle:** Max 1 per 8s (prevents spam)

### I) Burst Window Confirmation

| Event | Sound |
|-------|-------|
| Boss receives SYNCED | `sfx_window_synced` (optional) |
| Boss receives EXPOSED | `sfx_window_exposed` (optional, more premium) |

---

## 5) Mixing / Priority (Never Obnoxious)

### Priority Order (Highest → Lowest)

1. `sfx_collapse_execute`
2. `sfx_collapse_cancel`
3. `sfx_integrity_tier_breakpoint`
4. `sfx_collapse_charge_start`
5. Tier entry sounds (2–5)
6. `sfx_stabilizer_deploy`
7. `sfx_integrity_gain` / `reduce` / `protected`
8. Field loop

### Ducking Rules (Recommended)

| Condition | Behavior |
|-----------|----------|
| During `collapse_charge_loop` | Duck other UI ticks by ~30% (soften, don't remove) |
| Field loop | Sit well under music — players should "feel" it, not hear it distinctly |

---

## 6) Biome Skinning (Same Rhythm, Different Flavor)

**Rule:** Keep same timing and trigger points, swap timbre layer only.

| Biome | Sound Profile |
|-------|---------------|
| **Tower** | Clean synth ticks + metallic snap |
| **Palace** | Orchestral "clockwork" tick + stone fracture |
| **Remnant Vault** | Paper-tear + static tick + seam snap |

**Critical:** Do not change cadence per biome — cadence is the UX language.

---

## 7) Accessibility

### Tier Entry Distinction

Tier entry sounds must be distinct by **pattern**, not just pitch:

| Tier | Pattern |
|------|---------|
| **STRAINED** | Single soft tick |
| **FRACTURED** | Tick + tiny after-click |
| **CRITICAL** | Double-tick |
| **5/6** | Double-tick + short warning chirp |
| **6/6** | Alarm tone (short, non-looping) |

### Design Rationale

- Pattern recognition supports hearing-impaired and colorblind players
- Short sounds prevent audio fatigue
- Non-looping alarm at 6/6 avoids stress overload
- Distinct layers allow players to "read" Integrity state without looking at UI

---

## Quick Reference — Event Flow Audio

### Scenario: Clean Fight, No Collapse

| Event | Audio |
|-------|-------|
| Hit → 2/6 | `sfx_integrity_tier_strained` |
| Hit → 3/6 | `sfx_integrity_tier_fractured` |
| Hit → 4/6 | `sfx_integrity_tier_critical` |
| Stabilizer deploy | `sfx_stabilizer_deploy` + loop start |
| Integrity -2 → 2/6 | `sfx_integrity_reduce` |
| Field expires | `sfx_stabilizer_field_ending` → `sfx_stabilizer_field_off` |

### Scenario: Full Collapse + Cancel

| Event | Audio |
|-------|-------|
| Hit → 6/6 | `sfx_integrity_tier_breakpoint` |
| Cast begins | `sfx_collapse_charge_start` + loop start |
| Stabilizer cancels | `sfx_collapse_cancel` |
| Integrity -2 → 4/6 | `sfx_integrity_reduce` |
| Stop loop | (immediate) |

### Scenario: Collapse Executes

| Event | Audio |
|-------|-------|
| Hit → 6/6 | `sfx_integrity_tier_breakpoint` |
| Cast begins | `sfx_collapse_charge_start` + loop start |
| Cast completes | `sfx_collapse_execute` |
| Reset → 3/6 | `sfx_integrity_reset` (0.2–0.4s after) |
| Stop loop | (immediate) |

---

## Asset Summary Table

| Category | Count | Notes |
|----------|-------|-------|
| Tier entry sounds | 5 | Distinct patterns |
| Core integrity sounds | 3 | Gain, protected, reduce, reset |
| Collapse sounds | 4 | Start, loop, execute, cancel |
| Stabilizer sounds | 6 | Prime, deploy, loop, ending, off |
| Window sounds | 2 | Optional burst confirmations |
| **Total** | **20** | Plus biome variants |
