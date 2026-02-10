# Chroma's Edge - Hidden Area Completion Notes (v1)
## Sunken City and Dragon's Graveyard Coverage Check

---

## 0) Scope

Verified hidden-area package completeness for:
- `Sunken City`
- `Dragon's Graveyard`

Focus:
- Document presence
- Submap structure
- Core mechanic definitions
- Reward and flag wiring

---

## 1) Presence Check (PASS)

Verified present:
- `chroma_edge_hidden_sunken_city_map_sheet.md`
- `chroma_edge_hidden_dragons_graveyard_map_sheet.md`

Both docs include technical specs, macro flow, anchors, and completion flags.

---

## 2) Sunken City (PASS)

Coverage confirmed:
- 4-submap expedition structure
- Oxygen gauge rules and refill sources
- Tide Sigil puzzle path to vault
- Optional boss package (`The Drowned Archivist`)
- Floodgate shortcut return loop
- Completion flags:
  - `SUNKEN_CITY_DISCOVERED`
  - `SUNKEN_CITY_VAULT_OPENED`
  - `SUNKEN_CITY_BOSS_DEFEATED`
  - `SUNKEN_CITY_FLOODGATE_UNLOCKED`

---

## 3) Dragon's Graveyard (PASS)

Coverage confirmed:
- 4-submap expedition structure
- Boneweight gauge rules and relief systems
- Anchor Plate and gravity-well traversal mechanics
- 3-sigil vault progression (`Skull`, `Rib`, `Spine`)
- Optional boss package (`Gravewyrm Echo`)
- Riblift shortcut return loop
- Completion flags:
  - `DRAGONS_GRAVEYARD_DISCOVERED`
  - `DRAGONS_GRAVEYARD_SIGILS_COLLECTED`
  - `DRAGONS_GRAVEYARD_VAULT_OPENED`
  - `GRAVEWYRM_ECHO_DEFEATED`
  - `RIBLIFT_SHORTCUT_UNLOCKED`
  - `FOSSIL_DRAKE_UNLOCKED`

---

## 4) Integration Notes

- Sunken City uses Tide progression gating and Brinegate entry context.
- Dragon's Graveyard uses Mass progression gating and Gravemark entry context.
- Both areas include optional-boss outcome states that can safely coexist with story-critical progression.

---

## 5) Outcome

Hidden area documentation coverage is complete and tracker-ready (`2/2`).
