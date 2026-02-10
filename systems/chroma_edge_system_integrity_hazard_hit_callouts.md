# Hazard Hit → Integrity Gain Callouts (Standardized, Non-Spam)

**Usage:** Tower / Palace / Remnant Vault — Any content with signature hazards and Integrity meter

**Goal:** Readable feedback in hectic fights without notification spam

---

## 1) Core Rule (Anti-Spam)

Only show a hazard-hit toast if:

1. **Integrity increases** (N → N+1), **AND**
2. **One of these conditions applies:**
   - The hit crosses a tier boundary *(handled by tier-crossing toasts)*
   - It's the **first integrity gain in the last 6 seconds**
   - Integrity is now **≥ 4 (CRITICAL band)**

This keeps callouts readable in hectic fights.

---

## 2) Universal Hazard-Hit Toasts (Integrity +1)

### Standard (+1 Crack)

```
[SYSTEM] INTEGRITY COMPROMISED.
[SYSTEM] INTEGRITY: {N}/6
```

### Multiple Players Hit (Same Hazard Tick)

```
[SYSTEM] INTEGRITY COMPROMISED (MULTIPLE HITS).
[SYSTEM] INTEGRITY: {N}/6
```

### Fully Mitigated (No Integrity Gain)

**Optional** — Only if you want strong feedback for good play; do not spam

```
[SYSTEM] IMPACT MITIGATED.
[SYSTEM] INTEGRITY UNCHANGED.
```

---

## 3) Hazard-Type "Tag Lines" (Optional)

**Rule:** One extra line max; use at most once every 8 seconds

| Hazard Family | Tag Line |
|---------------|----------|
| **Lane strikes** | `CAUSE: FAULT LANES.` |
| **Rifts / pull zones** | `CAUSE: TEAR RINGS.` |
| **Slam / collapse ring / big AOE** | `CAUSE: COMPRESSION EVENT.` |
| **Flicker / fracture tiles** | `CAUSE: FRACTURE CONTACT.` |
| **Stillness / stop panels** | `CAUSE: STILLNESS FIELD.` |
| **Null pulse / dispel ring** | `CAUSE: NULL PULSE.` |

### Example Full Toast (Max 3 Lines Total)

```
INTEGRITY COMPROMISED.
INTEGRITY: 4/6
CAUSE: FAULT LANES.
```

---

## 4) Near-Breakpoint Special Warning (N=5)

**Rule:** Always show this, even if throttling

```
[SYSTEM] INTEGRITY CRITICAL (5/6).
[SYSTEM] NEXT HIT MAY TRIGGER COLLAPSE.
```

> Matches tier language exactly

---

## 5) Breakpoint Trigger Messaging (N=6)

### When Hit Pushes to 6/6

```
[SYSTEM] INTEGRITY CRITICAL (6/6).
[SYSTEM] COLLAPSE PROTOCOL IMMINENT.
```

### If Boss Doesn't Cast Immediately (Next Action)

```
[SYSTEM] PREPARE TO STABILIZE.
```

---

## 6) HUD Microtext (Persistent Hints)

**Rule:** Rotate once per 12–15s, max 2 per fight

```
Signature hazard hits increase Integrity.
```

```
At 6/6, COLLAPSE PROTOCOL will trigger.
```

```
Stabilizers reduce Integrity and suppress hazards.
```

---

## 7) Stabilizer "Counter-Feedback" (Closes the Loop)

### Stabilizer Prevents Integrity Gain (Inside Field)

```
[SYSTEM] SIGNATURE IMPACT SUPPRESSED.
[SYSTEM] INTEGRITY PROTECTED.
```

### Stabilizer Reduces Integrity

```
[SYSTEM] INTEGRITY REDUCED.
[SYSTEM] INTEGRITY: {N}/6
```

---

## 8) Implementation Notes

### Signature Hazards Definition

Treat as Integrity-gain sources:
- Fault Lanes
- Tear Rings
- Redaction Stamp hit
- *(Any hazard you designate as "signature")*

### Duplicate Prevention

Do **not** fire standard `INTEGRITY COMPROMISED` toast if tier-crossing toasts already fired on same tick. In that case, just show:
- Tier-crossing toast
- Optional cause tag

### Priority Hierarchy (Same Tick)

1. **Tier-crossing toasts** (highest priority)
2. **Breakpoint/Near-breakpoint** warnings
3. **Standard compromise** toast (if not throttled)
4. **Mitigation** toast (optional)

---

## Quick Reference — Toast Decision Tree

```
Player Hit by Signature Hazard
    ↓
Integrity Would Increase?
    ↓ NO → Optional: IMPACT MITIGATED
    ↓ YES
Crosses Tier Boundary?
    ↓ YES → Show Tier-Crossing Toast
    ↓ NO
First Gain in 6s OR ≥4 CRITICAL?
    ↓ NO → Suppress (throttle)
    ↓ YES
Integrity = 5?
    ↓ YES → NEAR-BREAKPOINT Warning
    ↓ NO
Integrity = 6?
    ↓ YES → BREAKPOINT Trigger
    ↓ NO
Show Standard Toast
    ↓
Optional: Append Cause Tag (8s cooldown)
```

---

## Token Reference

| Token | Usage | Example |
|-------|-------|---------|
| `{N}` | Current Integrity after hit | `3`, `4`, `5` |
| `{CAUSE}` | Hazard type tag | `FAULT LANES`, `TEAR RINGS` |

---

## Example Scenarios

### Scenario 1: Normal Hit in Safe Band

| Event | Toast |
|-------|-------|
| Hit at 1/6 → 2/6 | `INTEGRITY STRAINED (2/6).` *(tier-crossing, no compromise toast)* |

### Scenario 2: Critical Band Hit

| Event | Toast |
|-------|-------|
| Hit at 3/6 → 4/6 | `INTEGRITY CRITICAL (4/6).` *(tier-crossing)* |

### Scenario 3: Multiple Hits in 6 Seconds

| Event | Toast |
|-------|-------|
| Hit #1 at 2/6 → 3/6 | `INTEGRITY COMPROMISED.` `INTEGRITY: 3/6` |
| Hit #2 at 3/6 → 4/6 (3s later) | *(throttled — no toast)* |
| Hit #3 at 4/6 → 5/6 (8s later) | `INTEGRITY CRITICAL (5/6).` `NEXT HIT MAY TRIGGER COLLAPSE.` |

### Scenario 4: Near-Breakpoint

| Event | Toast |
|-------|-------|
| Hit at 4/6 → 5/6 | `INTEGRITY CRITICAL (5/6).` `NEXT HIT MAY TRIGGER COLLAPSE.` |

### Scenario 5: Breakpoint Trigger

| Event | Toast |
|-------|-------|
| Hit at 5/6 → 6/6 | `INTEGRITY CRITICAL (6/6).` `COLLAPSE PROTOCOL IMMINENT.` `PREPARE TO STABILIZE.` |

### Scenario 6: Stabilizer Protection

| Event | Toast |
|-------|-------|
| Hit inside Stabilization Field | `SIGNATURE IMPACT SUPPRESSED.` `INTEGRITY PROTECTED.` |
