# Core Vault Boss — Bark Budget Rules

**Purpose:** VO never spams; each line has maximum impact

**Boss:** The Remnant Custodian

---

## Global Budget Caps

| Metric | Limit | Rationale |
|--------|-------|-----------|
| **Total boss VO lines per fight** | 8 maximum | Keeps boss mysterious, not chatty |
| **Lines per phase** | 2–3 | Spread across ~5 minute fight |
| **Minimum gap between any two lines** | 20 seconds | Prevents back-to-back spam |
| **Mid-fight "ambient" barks** | 3 maximum | Only if player takes no damage |

---

## Phase Budgets

### Phase 1 — "Initial Stitch" (100% → 70% HP)

**Duration:** ~90–120 seconds

**Budget:** 2 lines maximum

| Trigger | Line | Priority |
|---------|------|----------|
| **Entry (mandatory)** | *"Leftovers belong to the vault."* | REQUIRED |
| Optional ambient | One of: *"You don't belong here."* / *"Stay edited."* / *"The vault remembers."* | Low (random 25–35s) |

**Rules:**
- If player takes damage within first 30s, skip ambient line
- If player flawless, play ambient at 35–45s mark

### Phase 2 — "Active Revision" (70% → 35% HP)

**Duration:** ~90–120 seconds

**Budget:** 2 lines maximum

| Trigger | Line | Priority |
|---------|------|----------|
| **Phase shift (mandatory)** | *"Revision begins."* | REQUIRED |
| Add spawn (optional) | *"Stop struggling."* | Low (if adds reach 2 cap) |

**Rules:**
- Add spawn line only if Errata Drones hit cap (2 alive)
- If adds die quickly, skip spawn line

### Phase 3 — "Final Redaction" (35% → 20% HP)

**Duration:** ~60–90 seconds

**Budget:** 2 lines maximum

| Trigger | Line | Priority |
|---------|------|----------|
| **Phase shift (mandatory)** | *"Final redaction."* | REQUIRED |
| High damage taken (optional) | *"Cease."* | Medium (if player drops below 30% HP) |

**Rules:**
- High damage line only plays once, even if player heals and drops again
- Must be 15s after phase shift line

### Forced 20% Event (Scripted)

**Duration:** ~5 seconds (lead-in)

**Budget:** 1 line (guaranteed)

| Trigger | Line | Priority |
|---------|------|----------|
| **Forced Unravel trigger (mandatory)** | *"The record closes."* | REQUIRED |

**Rules:**
- Plays at t20 (20% HP hit)
- No other VO within ±10s window

### Post-Cancel Window (If Forced Unravel Cancelled)

**Duration:** ~3 seconds

**Budget:** 1 line (conditional)

| Trigger | Line | Priority |
|---------|------|----------|
| **Successful cancel (optional)** | *"—Denied."* | Low |

**Rules:**
- Only if VO budget hasn't been exhausted
- Must be within 0.5s of cancel for impact
- Skip if music/SFX are dominant in mix

### Victory (Boss Defeat)

**Duration:** 3–5 seconds

**Budget:** 1 line (guaranteed)

| Trigger | Line | Priority |
|---------|------|----------|
| **Death (mandatory)** | *"Returned… to nothing."* | REQUIRED |

---

## Forbidden Patterns (Anti-Spam Rules)

### Never Allow

| Pattern | Prevention |
|---------|------------|
| Two lines within 10 seconds | Hard cooldown enforcement |
| Same line twice in one fight | Mark lines as "used" after play |
| Three consecutive ambient barks | Max 1 ambient per phase |
| VO over collapse charge telegraph | Duck VO, prioritize system callouts |
| VO over Stabilizer cancel moment | Cancel VO if "—Denied" plays |

### Cooldown Enforcement

| Line Type | Minimum Gap |
|-----------|-------------|
| Mandatory (entry, phase shift, death) | None (scripted) |
| Scripted event (20% forced) | 10s from any other line |
| Ambient / Optional | 20s from any other line |
| Cancel grunt | Immediate (can interrupt) |

---

## Line Usage Tracking

### Per-Fight Flags

| Flag | Purpose |
|------|---------|
| `VO_ENTRY_PLAYED` | Entry line done |
| `VO_PHASE1_AMBIENT_PLAYED` | Ambient used in P1 |
| `VO_PHASE2_SHIFT_PLAYED` | P2 shift done |
| `VO_PHASE2_ADD_PLAYED` | Add spawn line used |
| `VO_PHASE3_SHIFT_PLAYED` | P3 shift done |
| `VO_PHASE3_DAMAGE_PLAYED` | High damage line used |
| `VO_FORCED_20_PLAYED` | Forced Unravel line done |
| `VO_CANCEL_PLAYED` | Cancel grunt used |
| `VO_DEATH_PLAYED` | Death line done |
| `LAST_VO_TIMESTAMP` | Frame/time of last VO for cooldown check |

### Budget Calculation (Runtime)

```
Available_Budget = 8 (max)
Used_Budget = Count of flags set to TRUE
Remaining = 8 - Used_Budget

Can_Play_Optional_Line IF:
    Remaining > 0
    AND Current_Time - LAST_VO_TIMESTAMP > 20s
    AND Not_Collapse_Charge_Active
```

---

## Audio Mix Priority

| Event | VO Duck | Notes |
|-------|---------|-------|
| Entry | 0% | Full volume, quiet moment |
| Phase shift | -3 dB | Slight duck for system toast |
| Ambient | -6 dB | Background to combat |
| Forced 20% | 0% | Full priority, tension moment |
| Cancel grunt | -12 dB | Let SFX shine, grunt is garnish |
| Death | -3 dB | Match victory music level |

---

## Example Fight: Optimal VO Distribution

| Time | Event | VO Line | Budget Used |
|------|-------|---------|-------------|
| 0:00 | Entry | "Leftovers belong to the vault." | 1/8 |
| 0:30 | Ambient (flawless) | "You don't belong here." | 2/8 |
| 1:45 | P2 Shift (70%) | "Revision begins." | 3/8 |
| 2:30 | Adds cap | "Stop struggling." | 4/8 |
| 3:45 | P3 Shift (35%) | "Final redaction." | 5/8 |
| 4:20 | Forced 20% | "The record closes." | 6/8 |
| 4:23 | Cancelled | "—Denied." | 7/8 |
| 5:30 | Death | "Returned… to nothing." | 8/8 |

**Result:** Full budget used, no spam, each line lands with impact.

---

## Fallback Rules (If Player Speedruns)

### Sub-3-Minute Kill

| Priority | Lines Guaranteed |
|----------|------------------|
| 1 | Entry |
| 2 | Death |
| 3 | One phase shift (most recent) |
| 4 | Forced 20% (if reached) |

Skip: All ambient, add spawn, high damage, cancel grunt

### Sub-2-Minute Kill (Extreme)

| Priority | Lines Guaranteed |
|----------|------------------|
| 1 | Entry |
| 2 | Death |

Skip: Everything else (fight too fast for boss to "speak")

---

## Localization Notes

- All lines under 6 words for translation brevity
- No puns or cultural references
- Guttural sounds ("—Denied.") translate as em-dash + verb in most languages
- Death line ellipsis indicates fade, not pause
