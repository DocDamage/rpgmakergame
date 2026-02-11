# Route Micro-Map: R17e - Crown Hub Connector

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Crown Hub Connector (R17e) |
| **Theme** | Safe inner-capital traversal with high narrative pressure |
| **Encounter Level Band** | N/A (encounters OFF) |
| **Mounts** | OFF |
| **Map Size** | 128 x 96 (x 0-127, y 0-95) |
| **Purpose** | Connects Crown Approach to Conduit gate and Palace staging access |
| **Related Full Sheet** | `chroma_edge_submap_crown_district_hub_map_sheet.md` |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Crown District Approach** | (0, 52) | Main arrival |
| **Back to Crown District Approach** | (0, 60) | Return lane |
| **To Crown Spire Conduit** | (127, 44) | D8 lane |
| **To Palace upper steps** | (88, 0) | Final-act lane |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Crown Beacon save crystal | (72, 82) | Main reset point |
| Crown Conduit Node terminal | (104, 44) | Route status + unlock messaging |
| Empty Regent plinth | (22, 62) | Narrative landmark |

---

## Terrain / Hazards

### A) Seam Pulse (Atmosphere-Only)

| Property | Value |
|----------|-------|
| **Zones** | x 92-122, y 30-52 and x 58-74, y 48-58 |
| **Telegraph** | 1.2s air ripple + low bass rise |
| **Active** | 2.0s |
| **Effect** | Camera wobble only (no damage or debuff) |
| **Cooldown** | 12.0s |

### B) Mirror Tile Drift (Navigation Cue)

| Property | Value |
|----------|-------|
| **Zone** | x 56-74, y 48-58 |
| **Telegraph** | 1.0s tile shimmer |
| **Active** | 2.5s |
| **Effect** | Briefly brightens true path toward active objective |
| **Cooldown** | 10.0s |

---

## Encounter Pockets

| Pocket | Location | Composition |
|--------|----------|-------------|
| **None (by design)** | N/A | Random encounters disabled in hub |

---

## Interactables

| Type | Coordinates | Contents / Function |
|------|-------------|---------------------|
| Save crystal | (72, 82) | Save point |
| Rest chamber door | (72, 92) | Rest + stash |
| Field clinic pod | (86, 86) | Status cleanse |
| Vendor pod | (58, 86) | Endgame supplies |
| Contract board | (72, 76) | Capital contracts |

---

## Gating

| Lock | Condition |
|------|-----------|
| **Conduit route open** | `CROWN_ARCHIVE_KEY_ACQUIRED = TRUE` |
| **Conduit authorization** | Foundation alignment flags satisfied |
| **Palace steps open** | `RELIC_SHADOW_SEATED = TRUE` and `FINAL_ACT_OPEN = TRUE` |

---

## Quick Reference Coordinates

```text
Approach entry: (0, 52)           Approach return: (0, 60)
Conduit exit: (127, 44)           Palace steps exit: (88, 0)

Crown Beacon: (72, 82)            Conduit Node: (104, 44)
Regent plinth: (22, 62)

Rest door: (72, 92)               Clinic: (86, 86)
Vendor: (58, 86)                  Contract board: (72, 76)
```

---

## Implementation Notes

- Keep this route non-combat for pacing and prep.
- Use objective markers from the Conduit Node to steer players to either D8 (`127,44`) or Palace steps (`88,0`) based on progression.
