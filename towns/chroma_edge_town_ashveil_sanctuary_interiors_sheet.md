# Chroma's Edge — Ashveil Sanctuary Interiors Sheet (v1)
## Build-Ready Interior Layouts + Interactables + NPC Schedules

---

## 0) Global Interior Rules (All Ashveil Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16×16 px |
| **Collision Style** | Cozy but readable (no maze interiors) |
| **Lighting - Day** | Warm diffuse + seed-lamps low glow |
| **Lighting - Night** | Amber lantern pools + faint cyan Lattice shimmer |
| **Music Layers** | Base calm loop + "Lattice undertone" toggles on PHASE 1+ |
| **Door Warps** | Every interior uses 1-tile "entry pad" so party doesn't spawn in NPCs |

---

## 1) HEARTROOT HALL (Story HQ)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 36 × 28 tiles |
| **Exterior Door** | Town door (58, 54) |
| **Interior Entry Pad** | (18, 25) (bottom center) |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Main Council Circle** | x 8–28, y 9–18 | Central meeting space |
| **Elder Dais** (raised stone) | x 15–21, y 6–8 | Leadership platform |
| **Side Benches - Left** | x 6–8, y 10–18 | NPC seating |
| **Side Benches - Right** | x 28–30, y 10–18 | NPC seating |
| **Back Glyph-Stone Wall** | x 10–26, y 2–5 | Lore prop (foreshadows Prime/pedestal) |

### C) Key Interactables (Tile Anchors)

| Interactable | Location | Function |
|--------------|----------|----------|
| **Council Table / "Briefing" prompt** | (18, 12) | Main story trigger |
| **Glyph-stone examine** | (18, 4) | Lore + foreshadow Prime/pedestal |
| **Sanctuary Ledger** | (26, 16) | Quest turn-ins |
| **Donation Bowl** | (10, 16) | Flavor; later "refugee supplies" sidequest |

### D) Cutscene Staging Points

| Point | Location | Use Case |
|-------|----------|----------|
| **CS_STAGE_A** | (18, 8) | Elder speaking |
| **CS_STAGE_B** | (18, 16) | Party line-up |
| **CS_STAGE_C** | (18, 13) | Argument beat / Kade forward |

### E) NPC Placements

| NPC | Default Location | Notes |
|-----|------------------|-------|
| **Elder Maelin** | (18, 7) | Leadership position |
| **Scout Captain Rooke Vale** | (12, 11) | — |
| **2–4 Refugees** | Benches (7, 12) / (29, 14) | Phase-dependent |

### F) Phase Changes

| Phase | Changes |
|-------|---------|
| **PHASE 0** | Fewer refugees, calm |
| **PHASE 1+** | "Warning map" prop appears on right wall (30, 6) |
| **PHASE 2** (after D1 clear) | Vines bloom around dais (pure visual) |

---

## 2) GREEN THREAD CLINIC (Healer Interior)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 × 22 tiles |
| **Exterior Door** | Town door (90, 62) |
| **Interior Entry Pad** | (16, 20) |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Reception Counter** | x 12–20, y 14–16 | Service point |
| **Triage Bed - Left** | x 4–10, y 7–10 | Patient bed |
| **Triage Bed - Right** | x 22–28, y 7–10 | Patient bed |
| **Herb Prep Wall** | x 2–6, y 2–6 | Crafting aesthetic |
| **Sterile Stone Table** | x 13–19, y 6–8 | Cutscene prop |

### C) Services / Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic Service Menu** | (16, 15) | Cures + later upgrades |
| **Herb Cabinet** | (4, 4) | Craft mat pickup (1/day) |
| **"Emergency Kit" Chest** | (28, 18) | Locked PHASE 0, unlock PHASE 1 |

### D) Cutscene Staging

| Point | Location | Use Case |
|-------|----------|----------|
| **Suresh medical beat** | (16, 7) | Stone table scene |
| **NPC collapse** | (10, 12) | "Pressure rising" scene |

### E) NPCs

| NPC | Location | Role |
|-----|----------|------|
| **Medic NPC (Lead)** | (16, 15) | Service provider |
| **Assistant** | (24, 15) | Support |

### F) Phase Changes

| Phase | Changes |
|-------|---------|
| **PHASE 1+** | Adds 1 injured refugee on bed (visual) |
| **PHASE 2+** | Clinic menu expands (status cures) + more clutter/medical props |

---

## 3) MOSSLIGHT REST (Inn Interior)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 30 × 20 tiles |
| **Exterior Door** | Town door (54, 86) |
| **Interior Entry Pad** | (15, 18) |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Front Desk** | x 12–18, y 12–14 | Check-in |
| **Common Room Seating** | x 6–24, y 6–11 | Social space |
| **Stairs / Hallway** | x 24–28, y 14–18 | Decorative or short hall to rooms |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Rest/Save (Innkeeper)** | (15, 13) | Core function |
| **Rumor Board** | (6, 12) | Information |
| **Food Bowl** (tiny regen buff, 1/day) | (20, 10) | Minor buff |

### D) Cutscene Staging

| Point | Location | Use Case |
|-------|----------|----------|
| **"Quiet Talk" Booth** | (10, 9) | Ashka/Kellen-related optional later |
| **"Party Planning" Center** | (15, 9) | Group discussion |

### E) Phase Changes

| Phase | Changes |
|-------|---------|
| **PHASE 0** | Calm |
| **PHASE 1+** | Overheard rumor NPC appears (22, 8) |
| **PHASE 4** | Fewer civilians; inn feels emptier (tone) |

---

## 4) VINEWORK BENCH SHED (Craft Interior)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 × 18 tiles |
| **Exterior Door** | Town door (44, 92) |
| **Interior Entry Pad** | (14, 16) |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Main Workbench** | x 10–18, y 8–10 | Crafting station |
| **Tool Wall** | x 2–6, y 3–12 | Visual prop |
| **Material Bins** | x 20–26, y 9–14 | Storage aesthetic |

### C) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Craft Menu** | (14, 9) | Main crafting interface |
| **Upgrade Node** | (22, 12) | Unlocks after D1 |
| **"Vine Lattice" Display** | (4, 6) | Lore + recipe hints |

### D) Phase Changes

| Phase | Changes |
|-------|---------|
| **PHASE 0** | Basic recipes |
| **PHASE 2** (post D1) | Growth-resist + regen accessories unlock |
| **PHASE 3** (post D3) | Saddle/strap cosmetic crafts unlock |

---

## 5) OPTIONAL INTERIOR: TERMINAL ALCOVE (Tiny Tech Nook)

*(Highly recommended so the terminal doesn't feel like "random menu rock.")*

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 18 × 14 tiles |
| **Exterior Access** | From terminal tile (96, 56) via "Enter Alcove" prompt |
| **Interior Entry Pad** | (9, 12) |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Terminal Interface** | (9, 6) | Lattice terminal menu |
| **Lore Console** | (4, 9) | Prime foreshadow; changes after D1 |

### C) Phase Changes

| Phase | Changes |
|-------|---------|
| **PHASE 1+** | Faint static voice-line tease (no Mercer name yet) |
| **PHASE 2+** | "World feels calmer" readout after Growth seat |

---

## 6) OPTIONAL INTERIOR: MEMORIAL GROTTO (Quiet Character Beat Room)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 × 16 tiles |
| **Exterior Access** | From Memorial Stone (30, 58) via "Enter Grotto" prompt |
| **Interior Entry Pad** | (11, 14) |

### B) Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Memorial Wall** | (11, 6) | Adds names over time / phase |
| **Offering Spot** | (11, 10) | Sidequest hook |

### C) Use Cases

- Ashka/Korr optional scenes (non-critical but high emotional payoff)
- Late game: "names removed" if Dominion raids occurred (consequence)

---

## 7) NPC SCHEDULES (Day/Night + Phase)

*Use this to make the town feel alive without needing more maps.*

### Elder Maelin

| Time | Location | Notes |
|------|----------|-------|
| **Day** | Heartroot Hall (18,7) (PHASE 0–2), plaza later | — |
| **Night** | Quiet Terraces (exterior) OR Memorial Grotto (PHASE 4 tone) | — |

### Scout Captain Rooke Vale

| Time | Location | Notes |
|------|----------|-------|
| **Day** | Watch Post exterior (72,22) | — |
| **Night** | Gategrove exterior patrol loop | Adds tension PHASE 1+ |

### Clinic Medic (Lead)

| Time | Location | Notes |
|------|----------|-------|
| **Always** | Clinic counter (16,15) | Day default |
| **Night** | Triage bed (8,8) in PHASE 1+ | Visual "busy" |

### Innkeeper

| Time | Location | Notes |
|------|----------|-------|
| **Day** | Front desk (15,13) | — |
| **Night** | Common room (18,9) | With rumor NPC nearby |

### Craftsman

| Time | Location | Notes |
|------|----------|-------|
| **Day** | Craft Shed (14,9) | — |
| **Night** | Off-map (shed closed) until PHASE 2+ | Late nights for upgrades |

### "Wind-Listener" Mystic (Flavor)

| Time | Location | Notes |
|------|----------|-------|
| **Day** | Plaza edge exterior | — |
| **Night** | Terminal Alcove exterior | Foreshadow lines |

---

## 8) Hook List (Which Interiors Host Which Quests)

| Interior | Quest/Beat |
|----------|------------|
| **Heartroot Hall** | Main D1 briefing |
| **Craft Shed + Clinic** | Early gathering/tutorial |
| **Inn (Common Room)** | Post-D1 celebration tone |
| **Terminal Alcove** | Prime foreshadow |
| **Memorial Grotto** | Emotional character beats |

---

## Quick Reference: Interior Summary

```
HEARTROOT HALL (36×28)
   Door: (58, 54) exterior | Pad: (18, 25) interior
   Dais: (18, 7) | Table: (18, 12) | Glyph: (18, 4)
   Elder: (18, 7) | Scout: (12, 11)

GREEN THREAD CLINIC (32×22)
   Door: (90, 62) exterior | Pad: (16, 20) interior
   Counter: (16, 15) | Beds: (7,8) & (25,8) | Stone Table: (16, 7)
   Medic: (16, 15) | Assistant: (24, 15)

MOSSLIGHT REST (30×20)
   Door: (54, 86) exterior | Pad: (15, 18) interior
   Desk: (15, 13) | Board: (6, 12)
   Innkeeper: (15, 13) day, (18, 9) night

VINEWORK BENCH SHED (28×18)
   Door: (44, 92) exterior | Pad: (14, 16) interior
   Workbench: (14, 9) | Upgrade: (22, 12) post-D1

TERMINAL ALCOVE (18×14) — Optional
   Access: Terminal tile (96, 56) | Pad: (9, 12)
   Terminal: (9, 6) | Lore: (4, 9)

MEMORIAL GROTTO (22×16) — Optional
   Access: Memorial Stone (30, 58) | Pad: (11, 14)
   Wall: (11, 6) | Offering: (11, 10)
```
