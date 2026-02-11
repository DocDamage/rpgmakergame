# Integrity Meter Widget — Universal Collapse Protocol (v1)

## 1) Universal Collapse Name

Use this as the **default** collapse event label across all content:

```
EVENT_NAME_DEFAULT: COLLAPSE PROTOCOL
```

**Swapping:** If a fight has a bespoke name later (e.g., CORE UNRAVEL), swap at runtime without changing other text.

---

## 2) Integrity Widget Text Pack

### Widget Display

| Element | Text |
|---------|------|
| **Title** | `INTEGRITY` |
| **Readout** | `INTEGRITY: {N}/6` |
| **Status Line** | `STATUS: {STABLE|STRAINED|FRACTURED|CRITICAL|BREAKPOINT}` |

### Tooltip

```
Title: INTEGRITY

Body:
Increases when you are hit by signature hazards.
At 6/6, COLLAPSE PROTOCOL will trigger.
Use Stabilizers to reduce Integrity and suppress hazards.
```

---

## 3) Threshold Bands (Warning Tiers)

| Value | Band | Status Display |
|-------|------|----------------|
| 0–1 | Safe | `STABLE` |
| 2 | Warning | `STRAINED` |
| 3 | Elevated | `FRACTURED` |
| 4–5 | Danger | `CRITICAL` |
| 6 | Maximum | `BREAKPOINT` |

---

## 4) Tier-Crossing System Toasts (No Spam)

**Rule:** Fire only when crossing **upward** into a new band.

| Threshold | Toast |
|-----------|-------|
| **At 2/6** | `INTEGRITY STRAINED (2/6).` |
| **At 3/6** | `INTEGRITY WARNING (3/6).` / `HAZARDS ESCALATING.` |
| **At 4/6** | `INTEGRITY CRITICAL (4/6).` |
| **At 5/6** | `INTEGRITY CRITICAL (5/6).` / `NEXT HIT MAY TRIGGER COLLAPSE.` |
| **At 6/6** | `INTEGRITY CRITICAL (6/6).` / `COLLAPSE PROTOCOL IMMINENT.` |

> **"COLLAPSE PROTOCOL IMMINENT"** = Your universal "oh no" callout.

---

## 5) Cast / Charge Overlay (Universal)

### When Collapse Cast Actually Starts

#### Meter Overlay Text

```
COLLAPSE PROTOCOL — CHARGING ({SEC}s)
```

#### Paired System Callouts

```
COLLAPSE PROTOCOL — CHARGING.
STABILIZER REQUIRED.
```

> **Note:** "STABILIZER REQUIRED" only in fights where Stabilizer is intended counterplay.

### If Cancelled

```
COLLAPSE CANCELLED.
TARGET STUNNED.
EXPOSED WINDOW — GO.
```

### If It Resolves

```
COLLAPSE EXECUTED.
INTEGRITY RESET: 3/6.
```

---

## 6) Optional: Specific Name Overrides

### Runtime Logic

```
IF event_name EXISTS:
    DISPLAY {EVENT_NAME}
ELSE:
    DISPLAY COLLAPSE PROTOCOL
```

### Example (Remnant Vault)

With `event_name = "CORE UNRAVEL"`:

```
CORE UNRAVEL — CHARGING ({SEC}s)
```

**Everything else stays identical.**

---

## Quick Reference — Comparison Table

| Situation | Universal (Default) | With Override |
|-----------|---------------------|---------------|
| 6/6 Toast | `COLLAPSE PROTOCOL IMMINENT.` | `CORE UNRAVEL IMMINENT.` |
| Cast Overlay | `COLLAPSE PROTOCOL — CHARGING.` | `CORE UNRAVEL — CHARGING.` |
| Cancel Toast | `COLLAPSE CANCELLED.` | `UNRAVEL CANCELLED.` |
| Execute Toast | `COLLAPSE EXECUTED.` | `UNRAVEL EXECUTED.` |

---

## Implementation Notes

1. **Default to COLLAPSE PROTOCOL** everywhere
2. **Event name override** = optional string field per fight/dungeon
3. **No other text changes** needed when swapping names
4. **Consistent verb usage:**
   - IMMINENT (warning)
   - CHARGING (cast active)
   - CANCELLED (success)
   - EXECUTED (failure/resolve)

---

## Example: Full Remnant Vault Flow (with Override)

| Event | Meter | Toast |
|-------|-------|-------|
| Fight starts | `INTEGRITY: 0/6` `STABLE` | — |
| Hits 2/6 | `STRAINED` | `INTEGRITY STRAINED (2/6).` |
| Hits 3/6 | `FRACTURED` | `INTEGRITY WARNING (3/6).` `HAZARDS ESCALATING.` |
| Hits 6/6 | `BREAKPOINT` | `INTEGRITY CRITICAL (6/6).` `CORE UNRAVEL IMMINENT.` |
| Cast begins | Overlay: `CORE UNRAVEL — CHARGING (2.6s)` | `CORE UNRAVEL — CHARGING.` `STABILIZER REQUIRED.` |
| Stabilizer deployed | `INTEGRITY: 3/6` `FRACTURED` | `UNRAVEL CANCELLED.` `TARGET STUNNED.` `EXPOSED WINDOW — GO.` |
| Reset complete | `FRACTURED` | `INTEGRITY RESET: 3/6.` |

---

## Example: Tower Boss (Default, No Override)

| Event | Meter | Toast |
|-------|-------|-------|
| Hits 6/6 | `BREAKPOINT` | `INTEGRITY CRITICAL (6/6).` `COLLAPSE PROTOCOL IMMINENT.` |
| Cast begins | Overlay: `COLLAPSE PROTOCOL — CHARGING (3.0s)` | `COLLAPSE PROTOCOL — CHARGING.` |
| Resolves | `INTEGRITY: 3/6` | `COLLAPSE EXECUTED.` `INTEGRITY RESET: 3/6.` |

---

## Token Summary

| Token | Usage | Example |
|-------|-------|---------|
| `{N}` | Current Integrity | `0`, `3`, `6` |
| `{SEC}` | Cast countdown | `2.6`, `3.0` |
| `{EVENT_NAME}` | Optional override | `CORE UNRAVEL`, `SEAM COLLAPSE` |

---

## One File to Rule Them All

This single text package works for:
- ✅ Remnant Vault (with `CORE UNRAVEL` override)
- ✅ Final Palace (default or custom name)
- ✅ Tower Bosses (default or custom name)
- ✅ Any future "collapse mechanic" content
