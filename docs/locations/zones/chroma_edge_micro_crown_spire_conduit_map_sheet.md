# Chroma's Edge — Crown Spire Conduit: Recordfall Descent Map Sheet (v1)
## Pre-Entry Micro-Map — "The Building is Processing You as Paperwork"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Name** | Crown Spire Conduit: Recordfall Descent |
| **Type** | Micro-map (cinematic connector) |
| **Role** | Bridge from Crown District hub → D8 Void Nexus (Breach Vestibule) |
| **Size** | 144 × 72 tiles (2304 × 1152 px) |
| **Encounters** | OFF (pure atmosphere + gating) |
| **Time States** | Day / Night |
| **Night Atmosphere** | Stronger wrong-shadow VFX + deeper bass hum |
| **Mounts** | Disabled |
| **Save** | None (player has Crown Beacon); optional autosave at D8 entry |

---

## 1) Core Intent

1. **Transition feeling:** Capital dread → Foundation dread
2. **Clean gate:** "Authorized Records Required" + "Foundations aligned"
3. **First shadow seam:** Visual without mechanic dump
4. **Optional side pocket:** Lore + "you're choosing this" moment

---

## 2) Visual Identity

| Element | Description |
|---------|-------------|
| **Materials** | Polished black marble → ribbed iron conduits → glass-inlaid floor panels → stone too smooth to be old |
| **Lighting** | Thin cyan lines in floor; occasional violet shimmer near seam points |

### Signature Props

| Prop | Description |
|------|-------------|
| **Record Gate Column** | Key socket + rotating seals |
| **Conduit ribs** | Arched, repeating like a throat |
| **Shadow seam** | Hairline crack in air, not in stone |
| **Lumen Anchor pads** | Small warm-white circles that feel "safe" |

---

## 3) Layout Blocks (Sections)

### Section 1: Gate Threshold (Key + Authorization)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–44, y 42–72 |
| **Features** | Clean, geometric, "official" architecture |

### Section 2: Conduit Gallery (Processional Descent)

| Property | Value |
|----------|-------|
| **Bounds** | x 44–104, y 28–64 |
| **Features** | Long hallway with repeating ribs + slow tonal shift |

### Section 3: Seam Antechamber (First Umbral Glimpse)

| Property | Value |
|----------|-------|
| **Bounds** | x 104–144, y 16–64 |
| **Features** | Reality seam VFX + "entry breach" door |

### Section 4: Optional Scriptor Pocket (Lore Nook)

| Property | Value |
|----------|-------|
| **Bounds** | x 52–84, y 0–28 |
| **Features** | Small side room for lore tablet + optional reward |

---

## 4) Entrances / Exits (Edge Triggers)

Local coords (0–143, 0–71)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **From Crown District** (hub) | (0, 56) | West edge |
| **Back to Crown District** | (0, 64) | West edge; bidirectional |
| **To D8: Breach Vestibule** (Map 1) | (143, 40) | East edge — final entry |

---

## 5) Key Anchors & Coordinates

### Gate / Authorization

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Record Gate Column** (Key socket) | (18, 58) | Crown Archive Key insertion |
| **Seal Ring Console** (Foundation check) | (30, 58) | Foundation alignment verification |
| **Status Plaque** (flavor text) | (12, 50) | Authorization instructions |

### Safe / Tone Beats

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Lumen Anchor #1** (safe pad) | (48, 56) | Visual safety marker |
| **Lumen Anchor #2** (safe pad) | (96, 46) | Visual safety marker |
| **Seam Shiver Point** (visual tear) | (118, 44) | Shadow mismatch VFX |

### Seam / Entry

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Umbral Altar** (glimpse/tutorial-lite) | (124, 36) | Seen/Unseen toggle preview |
| **Breach Door** (to D8) | (140, 40) | Final entry point |

### Optional Side Pocket

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Scriptor Door** (side nook entrance) | (62, 28) | Optional lore room access |
| **Lore Tablet** | (70, 14) | Alternating text lore |
| **Chest / Cache** | (78, 10) | Prep item reward |

---

## 6) Gating Logic (Production-Friendly)

### 1) Record Gate Column — Key Check

| Condition | Result |
|-----------|--------|
| **Interact at (18, 58)** | — |
| `CROWN_ARCHIVE_KEY_ACQUIRED = FALSE` | Prompt: "AUTHORIZED RECORD REQUIRED." Door sealed. |
| `CROWN_ARCHIVE_KEY_ACQUIRED = TRUE` | Insert animation; seal ring turns. |

### 2) Seal Ring Console — Foundation Alignment Check

| Condition | Result |
|-----------|--------|
| **Interact at (30, 58)** after key insertion | — |
| **Required (recommended):** | `RELIC_TIDE_SEATED`, `RELIC_MASS_SEATED`, `RELIC_TIME_SEATED` (plus earlier) |
| **Missing any** | Prompt: "FOUNDATION ALIGNMENT INCOMPLETE." Console highlights missing with icon list. |
| **All complete** | Prompt: "CONDUIT AUTHORIZED." Opens Conduit Gallery barrier at x≈44. |

### 3) Autosave (Recommended)

| Trigger | Location | Purpose |
|---------|----------|---------|
| **Seam Antechamber threshold** | (110, 44) | Safety save before D8 |

---

## 7) Micro-Mechanics (Keep it Light)

### A) Umbral Altar (Preview Mode)

| Property | Value |
|----------|-------|
| **Location** | (124, 36) |
| **Function** | Toggles Seen/Unseen locally |
| **Effects** | One small veil door panel shifts; floor glyphs change (cosmetic only) |
| **Hazards** | None — confidence-builder |

### B) Shadow Mismatch VFX (Atmosphere Only)

| Property | Value |
|----------|-------|
| **Location** | Near (118, 44) |
| **Effect** | Player shadow briefly "lags" by 1 frame |
| **Gameplay** | None — pure dread |

---

## 8) Scripted Beats (Cinematic, One-Time)

### Beat 1 — "Authorization Isn't Permission"

| Property | Value |
|----------|-------|
| **Trigger** | First interaction with Record Gate Column (18, 58) |
| **Event** | Seal ring turns, but hallway lights don't brighten — only floor line does |
| **Tone** | Approval without comfort |

### Beat 2 — "The Conduit Listens"

| Property | Value |
|----------|-------|
| **Trigger** | Stepping onto (58, 54) |
| **Event** | Soft audio dip + single deep click, like a lock engaging far away |

### Beat 3 — "Shadow Doesn't Match"

| Property | Value |
|----------|-------|
| **Trigger** | (118, 44) — Seam Shiver Point |
| **Event** | Player shadow pulls wrong direction for one second |
| **Tone** | Reality instability |

### Beat 4 — "Breach Door Pulse"

| Property | Value |
|----------|-------|
| **Trigger** | (136, 40) |
| **Event** | Breach door "breathes" once |
| **Prompt** | "ENTER THE NEXUS?" |

---

## 9) Optional Side Pocket (Scriptor Nook)

**Purpose:** Emotional opt-in + small prep item

### Lore Tablet (70, 14)

**Alternating text (every 2 seconds):**
- "THE SPIRE PROTECTS THE CITY."
- "THE SPIRE CONTAINS THE CITY."

### Chest / Cache (78, 10) — One-Time

**Reward options (pick one):**

| Option | Contents |
|--------|----------|
| **A** | Seal-Breaker Wax ×2 + Clockseal ×1 |
| **B** | Umbral Ward (minor) — reduces Umbral Gauge gain for first 10 D8 battles |

---

## 10) Set Dressing / Collision Notes

1. **Main hallway:** Keep straight and wide (no snagging)
2. **Repeating ribs:** Every ~10 tiles to create "throat" rhythm
3. **Breach door visibility:** Visible from ~20 tiles away once in Seam Antechamber

---

## 11) Flags / Tracking

| Flag | Condition |
|------|-----------|
| `CONDUIT_ENTERED` | TRUE — first time stepping into Conduit Gallery |
| `CONDUIT_AUTHORIZED` | TRUE — after Seal Ring Console success |
| `D8_ENTRY_AVAILABLE` | TRUE — breach door unlocked |
| `CONDUIT_SCRIPTOR_CACHE_TAKEN` | TRUE — optional (if cache collected) |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    SECTION 4: Optional Scriptor Pocket                    │
    │    (x 52–84, y 0–28)                                      │
    │    - Entrance door (62,28)                                │
    │    - Lore tablet (70,14)                                  │
    │    - Chest (78,10)                                        │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                      │                                    │
    │    ══════════════════╪══════════════════════              │
    │                      │                                    │
    │    SECTION 2: Conduit Gallery        SECTION 3: Seam      │
    │    (x 44–104, y 28–64)             Antechamber            │
    │    - Repeating rib architecture    (x 104–144, y 16–64)   │
    │    - Lumen Anchor #2 (96,46)       - Seam Shiver (118,44) │
    │    - "The Conduit Listens"         - Umbral Altar (124,36)│
    │      beat at (58,54)               - Breach Door (140,40) │
    │                                      "ENTER THE NEXUS?"   │
    │    ═══════════════════════════════════════════            │
    │                      │                                    │
    │    SECTION 1: Gate Threshold                              │
    │    (x 0–44, y 42–72)                                      │
    │                                                           │
    │    Status Plaque (12,50)                                  │
    │         │                                                 │
    │    Record Gate Column (18,58) ════► Key insertion         │
    │         │                    "AUTHORIZED RECORD REQUIRED" │
    │         ▼                                                 │
    │    Seal Ring Console (30,58) ════► Foundation check       │
    │         │                    "FOUNDATION ALIGNMENT        │
    │         │                     INCOMPLETE" / "CONDUIT      │
    │         ▼                     AUTHORIZED"                 │
    │    Lumen Anchor #1 (48,56)                                │
    │                                                           │
    │    Exits:                                                   │
    │    - Crown District ← (0,56) / (0,64)                     │
    │    - D8 Breach Vestibule → (143,40)                       │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Crown District Entry** | (0, 56) |
| **Crown District Return** | (0, 64) |
| **Status Plaque** | (12, 50) |
| **Record Gate Column** [Key] | (18, 58) |
| **Seal Ring Console** [Foundations] | (30, 58) |
| **Lumen Anchor #1** | (48, 56) |
| **"Conduit Listens" Beat** | (58, 54) |
| **Scriptor Door** | (62, 28) |
| **Lore Tablet** | (70, 14) |
| **Cache Chest** | (78, 10) |
| **Lumen Anchor #2** | (96, 46) |
| **Seam Shiver Point** | (118, 44) |
| **Umbral Altar** | (124, 36) |
| **Breach Door** | (140, 40) |
| **D8 Exit** | (143, 40) |
| **Autosave Trigger** | (110, 44) |
