# Chroma's Edge — Aurora Ascension Tower: Floor 25 Boss Arena Sheet (v1)
## Dr. Yakov Thorne — Growth Foundation Lieutenant ("The Cultivator")

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | Dr. Yakov Thorne |
| **Identity** | Growth Foundation Lieutenant — "The Cultivator" |
| **Stratum** | 21–30 (Growth) |
| **Recommended Level** | 120–145 (tower bracket 21–40) |
| **Arena Goal** | Endurance + add control + stop the regen + "save allies from absorption" |
| **Arena Size** | 80 × 64 tiles (1280 × 1024 px) |
| **Type** | Boss arena + prep hall + reward alcove |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | Floor 20 terminal (no save on 25) |

---

## 1) Layout Overview

### 1) Prep Hall (Entry Buffer)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–80, y 52–64 |
| **Features** | Safe pad + boss warning plaque + optional "antiseptic crate" (1-time) |

### 2) Bio-Containment Arena (Main Fight Bowl)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–74, y 10–52 |
| **Layout** | Circular-ish lab floor with nutrient channels, 4 purge pylons, 2 sterilizer valves, 3 specimen pods |

### 3) Reward Alcove (Post-Fight)

| Property | Value |
|----------|-------|
| **Bounds** | x 32–48, y 0–10 |
| **Features** | Chest + lift tile to Floor 26 |

---

## 2) Anchors & Coordinates (Local 0–79, 0–63)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry spawn** | (40, 60) | — |
| **Arena threshold** | y = 52 | Crossing to y≤51 locks doors |
| **Door lock trigger** | (40, 51) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Dr. Thorne spawn** | (40, 30) | Center dais |

### Specimen Pods (Absorption + Rescue)

| Pod | Coordinates | Notes |
|-----|-------------|-------|
| **Pod A** | (16, 18) | 2×2 collision, glass vat with root lattice |
| **Pod B** | (64, 18) | 2×2 collision |
| **Pod C** | (40, 44) | 2×2 collision |

### Sterilizer Valves (Add Control)

| Valve | Coordinates | Function |
|-------|-------------|----------|
| **Valve Left** | (10, 32) | Clears spores + stuns minions |
| **Valve Right** | (70, 32) | Clears spores + stuns minions |

### Purge Pylons (Regen Suppression)

| Pylon | Coordinates | Stack Effect |
|-------|-------------|--------------|
| **Pylon NW** | (22, 14) | Purge Stack |
| **Pylon NE** | (58, 14) | Purge Stack |
| **Pylon S** | (40, 50) | Purge Stack |
| **Pylon W** (optional 4th) | (12, 40) | Purge Stack |

### Nutrient Channels (Hazard Lanes)

| Channel | Location | Notes |
|---------|----------|-------|
| **Horizontal band 1** | y 22–24 | Walkable but hazardous when flowing |
| **Horizontal band 2** | y 38–40 | Walkable but hazardous when flowing |
| **Vertical bands** | x 30–32 and 48–50 | Cross-sections |

### Post-Fight Rewards

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Reward chest** | (40, 6) | — |
| **Lift tile to Floor 26** | (40, 2) | — |

---

## 3) Arena Hazards

### A) Nutrient Surge (Telegraphed Floor Hazard)

| Property | Value |
|----------|-------|
| **Frequency** | Every 10–14 seconds, one channel band |
| **Duration** | 4 seconds |
| **Effect** | Vinebind buildup + small chip damage |
| **Telegraph** | Channel turns bright green → bubbling → flow |

### B) Spore Burst (Localized)

| Property | Value |
|----------|-------|
| **Spawn** | Near pods during later phases |
| **Effect** | Short Accuracy down / Confounded-lite (brief) |

---

## 4) Player Counterplay Systems

### A) Purge Pylons — "Regen Lock"

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Effect** | Applies Purge Stack to boss for 20 seconds |
| **2 stacks** | Boss regen: 10% → 3% per turn |
| **3 stacks** | Boss regen: 0%, loses "heal on add death" |
| **Cooldown** | 30 seconds per pylon (independent) |
| **Visual feedback** | Pylons glow stronger as stacks accumulate |

### B) Sterilizer Valves — "Add Control"

| Property | Value |
|----------|-------|
| **Interact time** | 1.2s |
| **Effect** | Clears all active spores + stuns spawned minions for 2 turns |
| **Cooldown** | 25 seconds |
| **Use case** | Breather button during surge phases |

### C) Specimen Pods — "Absorb/Rescue"

| Property | Value |
|----------|-------|
| **Absorption** | Party member trapped in nearest pod |
| **Rescue** | Interact with pod to free member |
| **Bonus** | Freeing deals damage to boss' "growth shield" |

---

## 5) Boss Kit — Dr. Yakov Thorne

### Passive: Cultivator's Renewal

| Property | Value |
|----------|-------|
| **Base regen** | 10% max HP at end of turn |
| **Purge Stack reduction** | 2 stacks = 3% regen; 3 stacks = 0% regen |

### Passive: Biomass Economy

| Property | Value |
|----------|-------|
| **Effect per living minion** | +DEF (small) and/or +regen amplification |
| **Strategy** | Kill minions, but don't let them pile up |
| **Cap** | 6–8 max adds (prevent turn bloat) |

---

## 6) Phase Script (HP-Based)

### Phase 1 (100% → 70%): "Controlled Growth"

| Attack | Description | Counter |
|--------|-------------|---------|
| **Summon: Lab Sprouts** | 1–2 small adds per turn | Kill quickly |
| **Injector Lash** | Single target + Vinebind buildup | — |
| **Field Note** | Self-buff: +speed/initiative (2 turns) | Telegraphed by tablet glow |
| **Arena** | Nutrient Surges at normal frequency | — |

**Purpose:** Teach pylons/valves without overwhelming.

### Phase 2 (70% → 40%): "Mutation Protocol"

| Attack | Description | Counter |
|--------|-------------|---------|
| **Summon: Spore Drones** | Adds every turn or every 2 turns | Manage count |
| **Bloom Wave** | Cone AOE, leaves spore patch | Move out |
| **Reinforce Tissue** | Growth Shield (reduce damage until X adds killed OR valve used) | Kill adds OR valve |
| **Arena** | Nutrient Surges faster until valve pulled | Valves = breather |

**Transition:** Mutation VFX at 70% (short, no cutscene)

### Phase 3 (40% → 0%): "Assimilation"

| Attack | Description | Counter |
|--------|-------------|---------|
| **ABSORB** (signature) | Every 3 turns or at 35%/20%: telegraphed tether → traps in pod | Break tether, deal X damage, interrupt, or cleanse |
| **Mitosis Command** | Doubles existing small adds (capped) | AOE or burn |
| **Harvest Beam** | Line attack through channels; stronger if channels active | Avoid channels |
| **Arena** | Spores heavier; valves critical; pod rescues mandatory | — |

**Transition:** Mutation VFX at 40%

---

## 7) Absorption Rules (Fair Implementation)

| Property | Value |
|----------|-------|
| **Telegraph** | 1 full turn with clear UI marker + visible root tether |
| **Audio cue** | Yes (distinctive) |
| **Ways to stop** (pick 2) | Deal X damage to Thorne, break tether HP, cleanse/interrupt |
| **On success** | Member removed from battle, trapped in pod |
| **Rescue** | Interact with pod → freed at start of next player turn |

---

## 8) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Player crosses threshold → doors lock |
| 2 | Boss bark (optional): "A controlled environment yields controlled outcomes." |
| 3 | Phase 1 begins |
| 4 | Phase transitions at 70% and 40% (mutation VFX) |
| 5 | On defeat: hazards stop, alcove unlocks, chest spawns, lift activates |

---

## 9) Rewards (Floor 25 Boss)

### Clear Chest (Boss)

| Reward | Details |
|--------|---------|
| **Tier 5 Rare Equipment** | 1 piece, Growth-biased affix pool |
| **Tower Tokens** | +18 |
| **Duckets** | +110,000–150,000 |
| **Rare Mats** | 3 rolls from Growth pool |

### Bonus Challenge

| Condition | Bonus |
|-----------|-------|
| Free all absorbed allies within 2 turns each time | +7 tokens OR extra Tier-5 mat roll |

---

## 10) Flags

| Flag | Condition |
|------|-----------|
| `TOWER_F25_CLEARED` | TRUE |
| `TOWER_BOSS_25_DEFEATED` | TRUE |
| `TOWER_LAST_REACHED_FLOOR` | 25 |

---

## 11) Failure / Retry Behavior

| Condition | Behavior |
|-----------|----------|
| **On wipe** | Respawn at Floor 20 terminal (or Tower Lobby → Resume Floor 20) |
| **Boss intro** | Skippable after first attempt |

---

## 12) Implementation Notes

| Note | Priority |
|------|----------|
| Cap total adds at 6–8 (prevent turn bloat) | High |
| Purge Pylons glow stronger with stacks (feel the regen suppression) | High |
| Absorb tether unmistakable: audio + thick visual line + UI icon | Critical |
| Specimen Pods visually distinct (glass + root lattice) | Medium |
| Nutrient channels clearly marked when active | High |

---

## Quick Reference: Arena at a Glance

```
    NORTH (y=0, Reward Alcove)
       ↑
    ┌─────────────────────────────────────────────┐
    │  Reward Alcove (y 0–10)                     │
    │  - Chest (40,6)                             │
    │  - Lift to F26 (40,2)                       │
    └─────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════
                      │
    ┌─────────────────────────────────────────────┐
    │  Bio-Containment Arena (y 10–52)            │
    │                                             │
    │      NW Pylon      NE Pylon                 │
    │      (22,14)       (58,14)                  │
    │           │            │                     │
    │  Pod A    │   THORNE   │    Pod B            │
    │  (16,18)  │   (40,30)  │    (64,18)          │
    │           │            │                     │
    │      W Pylon (12,40)   │                     │
    │                         │                     │
    │  Valve L (10,32)        │  Valve R (70,32)    │
    │                         │                     │
    │      S Pylon (40,50)    │                     │
    │           │            │                     │
    │           └── Pod C ───┘                     │
    │              (40,44)                         │
    │                                             │
    │  ═══ Nutrient Channels ═══                   │
    │  Horizontal: y 22–24, y 38–40                │
    │  Vertical: x 30–32, x 48–50                  │
    │                                             │
    └─────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════ (y=52 threshold)
                      │
    ┌─────────────────────────────────────────────┐
    │  Prep Hall (y 52–64)                        │
    │  - Entry spawn (40,60)                      │
    │  - Lock trigger (40,51)                     │
    │  - Safe pad + antiseptic crate              │
    └─────────────────────────────────────────────┘
                      │
                   SOUTH (y=63, Entry)

PHASE SUMMARY:
P1 (100–70%): Controlled Growth — Lab Sprouts, Injector Lash, Field Note
P2 (70–40%): Mutation Protocol — Spore Drones, Bloom Wave, Reinforce Tissue
P3 (40–0%): Assimilation — ABSORB (signature), Mitosis Command, Harvest Beam

KEY MECHANICS:
- Purge Pylons suppress regen (stacks: 10% → 3% → 0%)
- Sterilizer Valves clear spores + stun adds
- Specimen Pods trap/rescue absorbed allies
- Nutrient Channels surge with telegraphed damage
- Add cap: 6–8 max
```
