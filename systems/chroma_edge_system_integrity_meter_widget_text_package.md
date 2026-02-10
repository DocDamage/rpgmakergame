# Integrity Meter Widget — Standardized Text + Tiers

**Usage:** Tower / Palace / Remnant Vault / Any "collapse / unravel" mechanic

**Design Philosophy:** Consistent SYSTEM phrasing (CRITICAL / IMMINENT / CHARGING / RESET)

---

## 1) Widget Identity

### Widget Title

```
INTEGRITY
```

### Icon IDs

| Icon | ID | Usage |
|------|-----|-------|
| **Widget icon** | `icon_meter_integrity` | Main meter display |
| **Crack pip icon** | `icon_integrity_crack` | Individual pip fills |
| **Critical overlay** | `icon_integrity_critical` | 6/6 state highlight |

### Primary Readout (Always Visible)

```
INTEGRITY: {N}/6
```

### Status Line (Under the Bar)

```
STATUS: {STABLE|STRAINED|FRACTURED|CRITICAL|BREAKPOINT}
```

---

## 2) Tooltip (Hover)

```
Title: INTEGRITY

Body:
Increases when you are hit by signature hazards.
At 6/6, a collapse event will trigger (e.g., CORE UNRAVEL).
Use Stabilizers to reduce Integrity and suppress hazards.

Footer:
Tip: Avoid hazard hits to prevent escalation.
```

### Mode-Specific Footer (Optional Swap)

| Mode | Footer Line |
|------|-------------|
| **Remnant Vault** | `Source: Vault Systems` |
| **Final Palace** | `Source: Palace Systems` |
| **Tower** | `Source: Tower Systems` |

---

## 3) Threshold Tiers (Warning Bands)

### Tier Mapping

| Value Range | Tier Name | Color Code |
|-------------|-----------|------------|
| 0–1 | **STABLE** | Green/Blue |
| 2–3 | **STRAINED** | Yellow |
| 4–5 | **CRITICAL** | Orange |
| 6 | **BREAKPOINT** | Red/Pulsing |

### Optional Mid-Tier Label (Exactly at 3/6)

```
FRACTURED
```

### Status Resolution Logic

| N Value | Status Display |
|---------|----------------|
| 0–1 | `STABLE` |
| 2 | `STRAINED` |
| 3 | `FRACTURED` (optional) or `STRAINED` |
| 4–5 | `CRITICAL` |
| 6 | `BREAKPOINT` |

---

## 4) System Toasts (Tier Crossings)

**Rule:** Only fire when meter crosses **upward** into a new band (prevents spam)

### Crossing into STRAINED (Hits 2/6)

```
[SYSTEM] INTEGRITY STRAINED (2/6).
```

### Crossing into FRACTURED (Hits 3/6) — Optional

```
[SYSTEM] INTEGRITY WARNING (3/6).
[SYSTEM] HAZARDS ESCALATING.
```

### Crossing into CRITICAL (Hits 4/6)

```
[SYSTEM] INTEGRITY CRITICAL (4/6).
```

### Near-Breakpoint (Hits 5/6)

```
[SYSTEM] INTEGRITY CRITICAL (5/6).
[SYSTEM] NEXT HIT MAY TRIGGER COLLAPSE.
```

### Breakpoint Reached (Hits 6/6)

```
[SYSTEM] INTEGRITY CRITICAL (6/6).
[SYSTEM] COLLAPSE IMMINENT.
```

---

## 5) Event-Specific Overrides

**Rule:** When collapse event is known, replace generic "COLLAPSE" with named threat

### Core Vault

```
[SYSTEM] CORE UNRAVEL IMMINENT.
```

### Palace / Tower (Generic Pattern)

```
[SYSTEM] {EVENT_NAME} IMMINENT.
```

**Example Events:**
- `SEAM COLLAPSE IMMINENT.`
- `VOID RUPTURE IMMINENT.`
- `CHRONO FRACTURE IMMINENT.`

---

## 6) Meter Change Toasts (Non-Tier, Low-Noise)

**Rule:** Use only when change is meaningful

### Integrity Reduced (e.g., Stabilizer -2)

```
[SYSTEM] INTEGRITY REDUCED.
```

**Optional Follow-Up:**
```
[SYSTEM] INTEGRITY: {N}/6
```

### Integrity Reset After Collapse Resolves

```
[SYSTEM] INTEGRITY RESET: 3/6.
```

### Integrity Stabilized to Safe Band (Drops Below 4)

```
[SYSTEM] INTEGRITY STABILIZED.
```

---

## 7) Cast State Overlay (Collapse Charging)

### Overlay Banner (On the Meter)

```
{EVENT_NAME} — CHARGING ({SEC}s)
```

**Examples:**
- `CORE UNRAVEL — CHARGING (2.6s)`
- `SEAM COLLAPSE — CHARGING (3.0s)`

### System Callouts (Paired)

```
[SYSTEM] {EVENT_NAME} — CHARGING.
[SYSTEM] STABILIZER REQUIRED.
```

**Note:** "STABILIZER REQUIRED" only for fights where Stabilizer is intended counterplay

---

## 8) HUD Microcopy (Compact, Always-On)

### Under-Bar Micro Hint

**Rotation:** Every ~12s, max 2 per fight

```
Avoid hazard hits to prevent escalation.
```

```
Stabilizers reduce Integrity and suppress hazards.
```

---

## Quick Reference — Full Flow Example

### Scenario: Player in Core Vault

| Event | Meter Display | Toast |
|-------|---------------|-------|
| Fight starts | `INTEGRITY: 0/6` `STATUS: STABLE` | — |
| Hit by Fault Lanes | `INTEGRITY: 1/6` | — |
| Hit by Tear Rings | `INTEGRITY: 2/6` | `[SYSTEM] INTEGRITY STRAINED (2/6).` |
| Hit by Echo Pulse | `INTEGRITY: 3/6` | `[SYSTEM] INTEGRITY WARNING (3/6).` |
| Redaction Stamp hits | `INTEGRITY: 4/6` | `[SYSTEM] INTEGRITY CRITICAL (4/6).` |
| Hit by Fault Lanes | `INTEGRITY: 5/6` | `[SYSTEM] INTEGRITY CRITICAL (5/6).` `[SYSTEM] NEXT HIT MAY TRIGGER COLLAPSE.` |
| Stabilizer deployed | `INTEGRITY: 3/6` | `[SYSTEM] INTEGRITY REDUCED.` `[SYSTEM] INTEGRITY: 3/6` |
| Hit by Echo Pulse | `INTEGRITY: 4/6` | `[SYSTEM] INTEGRITY CRITICAL (4/6).` |
| Hit by Fault Lanes | `INTEGRITY: 5/6` | `[SYSTEM] INTEGRITY CRITICAL (5/6).` |
| Redaction Stamp hits | `INTEGRITY: 6/6` | `[SYSTEM] INTEGRITY CRITICAL (6/6).` `[SYSTEM] CORE UNRAVEL IMMINENT.` |
| Core Unravel begins | Overlay: `CORE UNRAVEL — CHARGING (2.6s)` | `[SYSTEM] CORE UNRAVEL — CHARGING.` `[SYSTEM] STABILIZER REQUIRED.` |
| Unravel cancels | `INTEGRITY: 3/6` | `[SYSTEM] UNRAVEL CANCELLED.` `[SYSTEM] INTEGRITY RESET: 3/6.` |

---

## Implementation Checklist

- [x] Widget icon created: `icon_meter_integrity`
- [x] Crack pip icon created: `icon_integrity_crack`
- [x] Critical overlay created: `icon_integrity_critical`
- [x] Status text logic: STABLE → STRAINED → FRACTURED (optional) → CRITICAL → BREAKPOINT
- [x] Toast triggers only on upward tier crossings
- [x] Event-specific override system (replace "COLLAPSE" with named threat)
- [x] Cast overlay banner with countdown
- [x] Stabilizer "REDUCED" toast on deployment
- [x] Post-collapse "RESET" toast
- [x] Microcopy rotation system (12s interval, max 2 per fight)
- [x] Tooltip with mode-specific footer capability

---

## Token Reference

| Token | Description | Example Values |
|-------|-------------|----------------|
| `{N}` | Current Integrity value | `0`, `1`, `2`, `3`, `4`, `5`, `6` |
| `{SEC}` | Cast timer seconds | `2.6`, `3.0` |
| `{EVENT_NAME}` | Named collapse event | `CORE UNRAVEL`, `SEAM COLLAPSE`, `VOID RUPTURE` |
