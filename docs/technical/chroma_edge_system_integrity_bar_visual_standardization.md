# Integrity Bar Visual Standardization (Tower / Palace / Remnant)

**Purpose:** Single shared visual language for the Integrity widget across all content

**Design Philosophy:** Theme-agnostic base that can be skinned per area without changing behavior

---

## 1) Widget Parts (Consistent Everywhere)

### A) Bar + Pips

| Element | Specification |
|---------|---------------|
| **Bar** | 6 segments OR continuous bar with 6 tick marks |
| **Crack Pips** | One pip per point (0–6) |
| **Crack Overlay** | Subtle fracture texture that intensifies by tier |

### B) Icon States

**Main Icon:** `icon_meter_integrity`

| State ID | Animation | Tier Usage |
|----------|-----------|------------|
| `idle_stable` | Steady, no motion | 0–1 (STABLE) |
| `pulse_strained` | Soft pulse every 1.5s | 2 (STRAINED) |
| `flicker_fractured` | Mild jitter + shimmer | 3 (FRACTURED) |
| `flash_critical` | Short flash every 1.0s | 4–5 (CRITICAL) |
| `alarm_breakpoint` | Rapid pulse + shake | 6 (BREAKPOINT) |

### C) Screen-Edge Warning

| Integrity | Edge Vignette |
|-----------|---------------|
| 0–3 | OFF |
| 4–6 | ON with intensity scaling |

---

## 2) Tier Visual Rules

### Tier 0–1: STABLE

| Element | Visual |
|---------|--------|
| **Bar** | Normal fill, no animation |
| **Icon** | `idle_stable` (steady) |
| **Crack Overlay** | None / barely visible |
| **Audio** | None |
| **Status Text** | `STATUS: STABLE` |

### Tier 2: STRAINED

| Element | Visual |
|---------|--------|
| **Bar** | Subtle slow "breath" pulse (low amplitude) |
| **Icon** | `pulse_strained` (soft pulse every 1.5s) |
| **Crack Overlay** | Faint hairline fractures appear |
| **Audio** | Single soft "tick" on tier entry (optional) |
| **Status Text** | `STATUS: STRAINED` |

### Tier 3: FRACTURED

| Element | Visual |
|---------|--------|
| **Bar** | Light flicker ripple across segments every 2.0s |
| **Icon** | `flicker_fractured` (tiny jitter + shimmer) |
| **Crack Overlay** | Clearly visible fractures (still not loud) |
| **Screen Edges** | OFF (keep calm) |
| **Status Text** | `STATUS: FRACTURED` |

### Tier 4–5: CRITICAL

| Element | Visual |
|---------|--------|
| **Bar** | Brighter pulse + thin "warning sweep" line every 1.2s |
| **Icon** | `flash_critical` (short flash every 1.0s) |
| **Crack Overlay** | Heavy fractures + occasional spark/glint |
| **Screen Edges** | ON (low at 4, medium at 5) |
| **Audio** | Warning tick on each increase (throttled; no spam) |
| **Status Text** | `STATUS: CRITICAL` |

#### Extra at 5/6 (CRITICAL HIGH)

| Addition | Visual |
|----------|--------|
| Badge | Small "!" over Integrity icon |
| Pulse | Slightly increased frequency (not more brightness) |

### Tier 6: BREAKPOINT

| Element | Visual |
|---------|--------|
| **Bar** | Full alarm state (fast pulse) |
| **Icon** | `alarm_breakpoint` (rapid pulse + shake) |
| **Crack Overlay** | Maximum + animated "splitting" seam |
| **Screen Edges** | ON (high intensity, brief strobe on entry only) |
| **Audio** | One strong alarm tone on reaching 6 (do not loop) |
| **Status Text** | `STATUS: BREAKPOINT` |

---

## 3) Micro-Animations (Timing Spec)

### Bar Pulse Cadence (by Tier)

| Tier | Cadence |
|------|---------|
| STRAINED | Pulse every 1.5s |
| FRACTURED | Flicker sweep every 2.0s |
| CRITICAL | Warning sweep every 1.2s |
| BREAKPOINT | Pulse every 0.6s (until collapse cast begins) |

### Icon Pulse Cadence

| Tier | Cadence |
|------|---------|
| STRAINED | 1.5s |
| FRACTURED | 1.8s + mild jitter |
| CRITICAL | 1.0s flash |
| BREAKPOINT | 0.6s flash + shake |

---

## 4) Collapse Cast State (Widget Overlay)

### When Boss Begins Collapse Cast

#### Overlay Behavior

| Element | Change |
|---------|--------|
| **Status Line** | Replace with: `COLLAPSE PROTOCOL — CHARGING ({SEC}s)` |
| **Integrity Count** | Freeze at 6/6 (stop bar animation upward) |
| **Icon Transition** | `alarm_breakpoint` → `cast_warning` (steady bright + ticking ring) |

#### Screen Edges During Charge

| Change | Visual |
|--------|--------|
| Edge vignette | Steady (no strobe) — feels "locked in," not chaotic |

---

## 5) Stabilizer Interaction Visual Feedback

### When Stabilization Field Becomes Active

| Element | Visual |
|---------|--------|
| **Integrity Icon** | Thin ring overlay: `integrity_ring_stabilized` (steady halo) |
| **Bar Pulse** | Reduces by one tier visually (CRITICAL looks like FRACTURED while active) |

### When Integrity Is Reduced (-2)

| Element | Animation |
|---------|-----------|
| **Bar** | Reverse sweep (right-to-left) for 0.6s |
| **Crack Overlay** | Brief "re-knits" (quick seam close animation) |

### When Collapse Is Cancelled

| Element | Instant Visual |
|---------|----------------|
| **Cracks** | "Snap shut" flash (0.2s) |
| **Icon** | Calm drop to FRACTURED visuals for 1s, then resume at new tier |

---

## 6) Accessibility / Readability Rules

### Integrity State Must Be Readable Without Color

| Tier | Non-Color Cues |
|------|----------------|
| **STABLE** | No cracks |
| **STRAINED** | Faint cracks + soft pulse |
| **FRACTURED** | Visible cracks + flicker sweep |
| **CRITICAL** | "!" badge + edge vignette |
| **BREAKPOINT** | Shake + heavy seam animation |

### Rule
> Don't rely on hue changes alone—use motion + icon badges.

---

## 7) UI Copy Tie-In

### Standard Display (Always)

```
INTEGRITY: {N}/6
STATUS: {TIER}
```

### Additional Text Only When

| Condition | Added Text |
|-----------|------------|
| Entering CRITICAL (4+) | — |
| Reaching BREAKPOINT (6) | — |
| Collapse cast begins | `COLLAPSE PROTOCOL — CHARGING ({SEC}s)` overlay |

---

## Quick Reference — Visual Tier Summary

| Tier | Integrity | Bar | Icon | Cracks | Edge Vignette | Audio |
|------|-----------|-----|------|--------|---------------|-------|
| **STABLE** | 0–1 | Normal | Idle | None | OFF | None |
| **STRAINED** | 2 | Breath pulse | Soft pulse | Faint hairlines | OFF | Entry tick |
| **FRACTURED** | 3 | Flicker sweep | Jitter/shimmer | Visible | OFF | None |
| **CRITICAL** | 4–5 | Warning sweep | Flash | Heavy + sparks | ON (low/med) | Throttled tick |
| **BREAKPOINT** | 6 | Fast pulse | Flash + shake | Max + splitting | ON (high) | One alarm |

---

## Asset Naming Convention

| Asset | ID | Type |
|-------|-----|------|
| Widget icon | `icon_meter_integrity` | Sprite/animation |
| Stable state | `integrity_icon_idle_stable` | Animation state |
| Strained state | `integrity_icon_pulse_strained` | Animation state |
| Fractured state | `integrity_icon_flicker_fractured` | Animation state |
| Critical state | `integrity_icon_flash_critical` | Animation state |
| Breakpoint state | `integrity_icon_alarm_breakpoint` | Animation state |
| Cast warning | `integrity_icon_cast_warning` | Animation state |
| Stabilized ring | `integrity_ring_stabilized` | Overlay effect |
| Crack overlay | `integrity_overlay_cracks` | Texture mask |
| Edge vignette | `integrity_vignette_edge` | Screen effect |
| "!" badge | `integrity_badge_critical` | Icon overlay |

---

## Implementation Notes

1. **Animation states should blend** between tiers, not snap
2. **Screen-edge vignette intensity** scales 0.0 → 1.0 from tier 4 to 6
3. **Breakpoint strobe** only on initial entry (0.5s), then steady high
4. **Stabilizer halo** persists until field expires or Integrity changes
5. **Cast warning state** overrides all other icon states
6. **Reverse sweep** on Integrity reduction should feel "healing" not "damaging"
