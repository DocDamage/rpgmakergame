# Modifier-Specific Echo Pulse Callouts — Core Vault (Remnant Custodian)

## 1. Global Callouts (Always Play)

| Trigger | Source | Line | Notes |
|---------|--------|------|-------|
| Telegraph Start | **SYSTEM** | *"ECHO PULSE — INCOMING."* | Primary alert |
| Alternate (rotate) | **SYSTEM** | *"RING SIGNATURE DETECTED."* | Don't play both; alternate between runs or phases |

---

## 2. Modifier-Specific Callouts

### ECHO OF NULL (Buff Strip)

#### Telegraph Phase

| Source | Line |
|--------|------|
| **SYSTEM** | *"ECHO PULSE: NULL SIGNATURE."* |
| **SYSTEM** | *"BUFFS AT RISK."* |

#### On Hit (If It Strips)

| Source | Line |
|--------|------|
| **SYSTEM** | *"DISPEL CONFIRMED."* |

---

### ECHO OF STILLNESS (Stop/Slow)

#### Telegraph Phase

| Source | Line |
|--------|------|
| **SYSTEM** | *"ECHO PULSE: STILLNESS FIELD."* |
| **SYSTEM** | *"STOP EFFECT IMMINENT."* |

#### On Hit

| Source | Line |
|--------|------|
| **SYSTEM** | *"MOTION HALTED."* |

#### If Stabilizer Field Active (Converts to Slow)

| Source | Line | Condition |
|--------|------|-----------|
| **SYSTEM** | *"STILLNESS MITIGATED: SLOW ONLY."* | Player inside Stabilization Field when hit |

---

### ECHO OF WEIGHT (Pull/Heavy)

#### Telegraph Phase

| Source | Line |
|--------|------|
| **SYSTEM** | *"ECHO PULSE: GRAVITY SURGE."* |
| **SYSTEM** | *"PULL INCOMING."* |

#### On Hit

| Source | Line |
|--------|------|
| **SYSTEM** | *"HEAVY APPLIED."* |

---

### ECHO OF VEIL (Confound/Accuracy Down)

#### Telegraph Phase

| Source | Line |
|--------|------|
| **SYSTEM** | *"ECHO PULSE: VEIL BLOOM."* |
| **SYSTEM** | *"VISIBILITY COMPROMISED."* |

#### On Hit

| Source | Line |
|--------|------|
| **SYSTEM** | *"VEIL APPLIED."* |

---

### ECHO OF HEAT (Overheat)

#### Telegraph Phase

| Source | Line |
|--------|------|
| **SYSTEM** | *"ECHO PULSE: THERMAL SPIKE."* |
| **SYSTEM** | *"OVERHEAT RISING."* |

#### On Hit

| Source | Line |
|--------|------|
| **SYSTEM** | *"IGNITION CONFIRMED."* |

---

### ECHO OF FRACTURE (Turn Delay / Flicker)

#### Telegraph Phase

| Source | Line |
|--------|------|
| **SYSTEM** | *"ECHO PULSE: FRACTURE WAVE."* |
| **SYSTEM** | *"TIMING UNSTABLE."* |

#### On Hit

| Source | Line |
|--------|------|
| **SYSTEM** | *"TURN DELAY APPLIED."* |

---

## 3. Multiple Modifiers Active (Clean Handling)

When two or three Echo Rules are rolled, **do not stack three separate callouts**. Use one of these patterns:

### Pattern A — Priority + Addendum

| Source | Line | Notes |
|--------|------|-------|
| **SYSTEM** | *"ECHO PULSE: {PRIMARY SIGNATURE}."* | Use highest priority modifier |
| **SYSTEM** | *"SECONDARY EFFECT PRESENT."* | Generic warning for additional effects |

### Pattern B — Combo Callout

| Source | Line |
|--------|------|
| **SYSTEM** | *"ECHO PULSE: COMPOSITE SIGNATURE."* |
| **SYSTEM** | *"EXPECT MULTIPLE EFFECTS."* |

### Primary Signature Priority (Recommended)

| Priority | Modifier | Rationale |
|----------|----------|-----------|
| 1 | **STILLNESS** (Stop) | Most disruptive |
| 2 | **NULL** (Dispel) | High build impact |
| 3 | **FRACTURE** (Turn Delay) | Action economy threat |
| 4 | **WEIGHT** (Pull) | Positioning threat |
| 5 | **HEAT** (Overheat) | Sustained pressure |
| 6 | **VEIL** (Accuracy) | Lower immediate impact |

---

## 4. Optional Boss VO (Very Light)

**Usage**: Sparingly (max 1 per phase), only on telegraph start, only if modifier is primary/active.

| Modifier | Boss Line |
|----------|-----------|
| **NULL** | *"Erase."* |
| **STILLNESS** | *"Hold."* |
| **WEIGHT** | *"Sink."* |
| **VEIL** | *"Blind."* |
| **HEAT** | *"Burn."* |
| **FRACTURE** | *"Break."* |

### Boss VO Rules

| Rule | Implementation |
|------|----------------|
| **Frequency** | Max 1 per phase (3 total max per fight) |
| **Timing** | Only on telegraph start, overlapping with system callout |
| **Priority** | Lower than system alerts; can be dropped if audio busy |
| **Multi-modifier** | Use only if boss VO matches primary signature |

---

## 5. Quick Reference — Callout Priority Matrix

| Situation | Primary Line | Secondary Line | Optional Boss VO |
|-----------|--------------|----------------|------------------|
| **Single Modifier** | Modifier-specific signature | Modifier-specific warning | 1/phase max |
| **Two Modifiers** | Primary signature OR "COMPOSITE" | "SECONDARY EFFECT" OR "EXPECT MULTIPLE" | If matches primary |
| **Three Modifiers** | "COMPOSITE SIGNATURE" | "EXPECT MULTIPLE EFFECTS" | Skip (too busy) |
| **Stabilizer Mitigation** | Original signature | "MITIGATED" variant | Skip |

---

## 6. Implementation Notes

- **Audio Channels**: System callouts on center/global channel; Boss VO on boss-positioned spatial channel
- **Overlap Prevention**: If Core Unravel is charging, suppress Echo Pulse callouts (Unravel takes priority)
- **Hit Confirm Delays**: On-hit callouts play 0.3–0.5s after impact to confirm effect application
- **Mitigation Detection**: Check if player is inside Stabilization Field radius at moment of hit for "MITIGATED" variants
- **Rotation Logic**: For global alternates ("ECHO PULSE — INCOMING" vs "RING SIGNATURE DETECTED"), rotate per run or per phase to avoid repetition fatigue
- **Boss VO Cooldown**: 20s minimum between boss VO lines to prevent spam
