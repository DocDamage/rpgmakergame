# Chroma's Edge — Marinus's Sanctum Shrine Map Sheet (v1)
## Optional Side Location — "The sea kept a promise here, and you can feel it"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Shrine Name** | Marinus's Sanctum |
| **Type** | Optional shrine map (side location) tied to D5 Abyssal Trench |
| **Recommended Level** | Lv 28–46 (safe, but access path may have encounters) |
| **Map Size** | 32 × 24 tiles (512 × 384 px) |
| **Design Philosophy** | Small on purpose: a "pause room" |
| **Encounters** | OFF |
| **Lighting States** | Day/Night variants (same layout, different ambience) |

### Access Points

| Access | Source | Notes |
|--------|--------|-------|
| **Primary** | D5 Submap 2 (Pressure Midpoint) via north door | Recommended first visit |
| **Secondary** | Overworld coastal node | Optional later, post-D5 sea node |

---

## 1) Tone + Visual Identity

| Element | Description |
|---------|-------------|
| **Materials** | Pale coral-stone, sea-glass tiles, salt lines, hanging kelp ribbons, driftwood offerings |
| **Palette** | Muted teal + seafoam + soft pearl glow + amber lantern accents |

### Signature VFX/SFX

| Effect | Description |
|--------|-------------|
| **Tide Inhale/Exhale** | Slow reverb loop |
| **Sonar Ping** | Faint (night only) |
| **Water Surface** | Still even if waves audible outside |

---

## 2) Layout (Room Plan)

The shrine is a single space with tiny side alcoves for interactables.

### Room Blocks

| Block | Bounds | Purpose |
|-------|--------|---------|
| **Entry Antechamber** | x 12–20, y 18–23 | Transition space |
| **Main Pool + Pedestal** | x 10–22, y 8–17 | Central focal point |
| **Left Offering Alcove** | x 2–9, y 10–16 | Offering mechanics |
| **Right Lore Alcove** | x 23–30, y 10–16 | Lore tablet |
| **Back "Quiet Wall"** | x 10–22, y 2–7 | Whisper echo, Tide Chime |

### ASCII Micro Layout

```
y=0   ┌────────────────────────────────────────────────────────────┐
      │                    [Quiet Wall / Shell Mosaic]              │
y=2   │                                                            │
y=6   │##########~~~~~~~~~~~~POOL~~~~~~~~~~~~##########            │
      │#         #                        #         #               │
      │#  Offer  #         [ ] O          #  Lore   #               │
      │#  Alcove #        Sanctum         # Alcove  #               │
      │#         #        Pool            #         #               │
      │#    ◯    #        (16,12)         #    ◯    #               │
      │#         #                        #         #               │
y=12  │##########~~~~~~~~~~~~~~~~~~~~~~~~~##########               │
      │            ║                         ║                      │
      │            ║        (16,6)          ║                      │
      │            ║       Tide Chime       ║                      │
      │            ╚══════════╦════════════╝                      │
y=18  │    ◯                   ║                    ◯              │
      │  Lantern             ENTRY            Lantern               │
      │  (12,18)           (16,23)           (20,18)               │
      │                         ║                                  │
      │                         ║                                  │
y=23  └─────────────────────────╨──────────────────────────────────┘
                              EXIT
```

---

## 3) Anchors & Coordinates (Local 0–31, 0–23)

### Entrances / Exits

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY from D5** (north spoke) | (16, 23) | From Pressure Midpoint |
| **Exit back to D5** | (16, 23) | Same tile bidirectional |

### Key Interactables

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Sanctum Pool / "Marinus Seal" pedestal** | (16, 12) | Main reward location |
| **Offering Bowl** | (6, 14) | Blessing mechanic |
| **Lore Tablet** (sea-glass slab) | (26, 14) | Story text |
| **Tide Chime** (sound interact) | (16, 6) | Hint system |

### Flavor Props

| Prop | Coordinates | Description |
|------|-------------|-------------|
| **Driftwood prayer rack** | (4, 12) | — |
| **Shell mosaic wall** | (16, 3) | Back wall decoration |
| **Lantern post** | (12, 18) | Entry area lighting |
| **Lantern post** | (20, 18) | Entry area lighting |

---

## 4) Interactions

### A) Lore Tablet (Right Alcove)

| Property | Value |
|----------|-------|
| **Location** | (26, 14) |
| **Theme** | Tide is not erasure; Tide is memory in motion |
| **Pre-D5 Text** | Warns about pressure + currents |
| **Post-D5 Text** | Updates to "the sea is calmer" line |

### B) Tide Chime (Back Wall)

| Property | Value |
|----------|-------|
| **Location** | (16, 6) |
| **Function** | Plays short chime pattern; hint system |
| **Pre-D5 Hint** | Clue about current routing in Coral Throne (D5 Submap 3) |
| **Post-D5 Hint** | Hints at Sunken City node directions |

### C) Offering Bowl (Left Alcove)

| Property | Value |
|----------|-------|
| **Location** | (6, 14) |
| **Offering** | "Saltglass Token" or "Storm Lantern" or 100 credits |
| **Reward** | Blessing of Stillwater (one-time buff) |

#### Blessing of Stillwater (Buff Effects)

| Effect | Description |
|--------|-------------|
| Pressure reduction | Pressure Gauge gain reduced by ~25% for next 10 battles |
| Status resist | Silence/Fear chance reduced for same duration |

### D) Sanctum Pool — Reward Pedestal

| Property | Value |
|----------|-------|
| **Location** | (16, 12) |
| **Function** | Grants shrine's main reward |

---

## 5) Rewards

### Primary Reward (First Visit Only)

| Item | MARINER'S SEAL |
|------|----------------|
| **Type** | Accessory |
| **Pressure gain** | -15% |
| **Silence resist** | +20% |
| **Optional bonus** | Small HP regen while in water zones |

### Optional Secondary Reward (Post-D5 Only)

| Condition | RELIC_TIDE_SEATED = TRUE |
|-----------|--------------------------|
| **Interaction** | Revisit pool after seating Tide relic |
| **Reward A** | Chart Ping — reveals 1 Sea Node marker on overworld (Sunken City breadcrumb) |
| **Reward B** | "Pearl Dust" craft mat for high-tier Tide gear |

---

## 6) Character Beats (Optional Cutscene Hooks)

### Beat 1 — Suresh (Recommended)

| Trigger | First shrine entry OR first pool interaction |
|---------|----------------------------------------------|
| **Visual** | Suresh stands at pool edge, unusually quiet |

**Dialogue:**

> **SURESH:**  
> "People think the sea 'cleans' things.  
> That it makes them disappear.  
> It doesn't.  
> It keeps them… moving."

*He exhales, like he's letting something stop gripping him.*

### Beat 2 — Nix (Optional)

| Trigger | Post-D5, after Tide relic seated |
|---------|----------------------------------|
| **Visual** | Nix watches the still water |

**Dialogue:**

> **NIX-7:**  
> "Stillness is not the absence of motion.  
> It is motion… agreeing."

### Beat 3 — Dominion Echo (Phase-Based)

| Condition | Dominion pressure is high |
|-----------|---------------------------|
| **Effect** | Lore tablet adds second line about "charts rewritten by authority" |
| **Combat?** | No — pure flavor tension |

---

## 7) State Changes / Phases

### PHASE 0 — Pre-D5

| Aspect | State |
|--------|-------|
| Pool glow | Dimmer |
| Lore theme | "Prepare / equalize / don't fight currents" |
| Tide Chime hint | Present but subtle |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Flavor prop | Torn permit placard floats near entry |
| Tide Chime hint | More explicit (reduces puzzle frustration) |

### PHASE 2 — Post-D5 Clear

| Aspect | State |
|--------|-------|
| Pool glow | Brighter |
| Soundscape | Calmer |
| Unlocks | Chart ping / Sea Node breadcrumb |
| Blessing buff | Slightly stronger (optional) |

---

## 8) Implementation Notes (So it feels special)

1. **Camera framing:** Keep tight so the pool is always in view
2. **Atmosphere:** No menu spam, no loud UI — a "safe breath"
3. **Audio detail:** Subtle "drip" sound sync'd with tide inhale/exhale loop
4. **Lighting:** Soft pearl glow from pool should be primary light source
5. **Interactivity:** All interactables should feel deliberate and weighty

---

## Quick Reference Summary

```
┌───────────────────────────────────────────────────────────────┐
│  MARINUS'S SANCTUM — 32×24 tiles                            │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  ACCESS: D5 Submap 2 north door (64,18) → (16,23)            │
│  ENCOUNTERS: OFF                                             │
│                                                               │
│  ANCHORS:                                                    │
│  ├─ Pool/Reward: (16,12) — MARINER'S SEAL                    │
│  ├─ Offering: (6,14) — Blessing of Stillwater                │
│  ├─ Lore: (26,14) — Tide = memory in motion                  │
│  ├─ Chime: (16,6) — D5 puzzle hint / Sunken City direction   │
│  └─ Exit: (16,23) — Return to Pressure Midpoint              │
│                                                               │
│  REWARDS:                                                    │
│  ├─ 1st Visit: Mariner's Seal (accessory)                    │
│  └─ Post-D5: Chart Ping (Sea Node) OR Pearl Dust mat         │
│                                                               │
│  CHARACTER BEATS:                                            │
│  ├─ Suresh: "The sea keeps things moving"                    │
│  └─ Nix-7: "Stillness is motion agreeing"                    │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```
