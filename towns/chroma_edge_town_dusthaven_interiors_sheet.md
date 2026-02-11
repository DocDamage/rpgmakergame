# Chroma's Edge - Dusthaven Interiors Sheet (v1)
## Build-Ready Interior Layouts + Services + Story Hooks

---

## 0) Global Interior Rules (All Dusthaven Interiors)

| Parameter | Value |
|-----------|-------|
| **Interior Tile Size** | 16x16 px |
| **Collision Style** | Dense but readable; no single-tile choke traps |
| **Lighting (Day)** | Warm dust light + neon spill near signage |
| **Lighting (Night)** | Lower key light, stronger neon and brazier pools |
| **Door Warp Rule** | Every interior uses 1-tile entry pad with 2-tile clear buffer |
| **Ambient Audio** | Wind + pipe rattle baseline, crowd loops near Cantina/Market |

---

## 1) DUSTHAVEN CANTINA (Scene 001 Interior)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 32 x 24 tiles |
| **Exterior Door** | Town door `(52, 46)` |
| **Interior Entry Pad** | `(16, 22)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Front Counter** | x 12-20, y 14-16 | Service lane + bartender anchor |
| **Booth Row (Left)** | x 4-10, y 7-14 | Social seating |
| **Booth Row (Right)** | x 22-28, y 7-14 | Social seating |
| **Back Wall Stage** | x 11-21, y 3-6 | Jukebox + cracked display sightline |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Bartender service** | `(16, 15)` | Rumors + healing drinks (non-inn) |
| **Booth #3** | `(18, 12)` | Scene 001 Ironhawk broker beat |
| **Jukebox** | `(24, 5)` | Flavor interaction |
| **Back exit curtain** | `(4, 5)` | One-way to Ironhawk Cut in PHASE 1+ |

### D) Staging Points

| Point | Location | Use Case |
|-------|----------|----------|
| `CS_CANTINA_A` | `(18, 12)` | Broker confrontation |
| `CS_CANTINA_B` | `(16, 10)` | Party lineup |
| `CS_CANTINA_C` | `(11, 15)` | Dominion interruption beat |

### E) Exit Triggers

| Exit | Coordinates |
|------|-------------|
| **Return to Dusthaven** | `(16, 23)` |
| **Back curtain to alley** | `(4, 5)` (PHASE 1+) |

---

## 2) RENNA'S SCRAP GARAGE

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 40 x 28 tiles |
| **Exterior Door** | Town door `(26, 78)` |
| **Interior Entry Pad** | `(20, 26)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Main Lift Bay** | x 14-26, y 10-18 | Core scene/crafting zone |
| **Tool Wall** | x 3-9, y 5-18 | Dense prop lane |
| **Parts Crates** | x 29-36, y 8-20 | Material storage |
| **Work Office Nook** | x 16-24, y 3-7 | Dialogue corner |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Workbench menu** | `(20, 14)` | Upgrades (`NIX_JOINED = TRUE`) |
| **Lift control** | `(20, 12)` | Scene prop, no free use |
| **Parts ledger** | `(31, 10)` | Recipe hints |
| **Dispatch board** | `(8, 8)` | Early salvage sidequest tracking |

### D) Exit Triggers

| Exit | Coordinates |
|------|-------------|
| **Return to Dusthaven** | `(20, 27)` |

---

## 3) THE RUSTY COT (Inn)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 28 x 20 tiles |
| **Exterior Door** | Town door `(60, 62)` |
| **Interior Entry Pad** | `(14, 18)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Inn Desk** | x 11-17, y 11-13 | Service counter |
| **Common Tables** | x 6-21, y 6-10 | Rumor zone |
| **Back Hall** | x 22-26, y 12-18 | Room access (decorative) |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Inn service** | `(14, 12)` | Rest + save |
| **Rumor board** | `(6, 12)` | Local hints |
| **Water jug** | `(20, 9)` | 1/day minor heal |

### D) Exit Triggers

| Exit | Coordinates |
|------|-------------|
| **Return to Dusthaven** | `(14, 19)` |

---

## 4) DUST & BOLT (General Goods)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 26 x 18 tiles |
| **Exterior Door** | Town door `(64, 70)` |
| **Interior Entry Pad** | `(13, 16)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Checkout Counter** | x 10-16, y 10-12 | Vendor anchor |
| **Consumables Wall** | x 2-8, y 4-12 | Shelf props |
| **Utility Bin Stack** | x 18-24, y 5-13 | Ammo/filter props |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Shop menu** | `(13, 11)` | Potions, cures, smoke items |
| **Notice placard** | `(6, 6)` | Economy hints |
| **Lockbox** | `(22, 12)` | Opens PHASE 2 sidequest |

### D) Exit Triggers

| Exit | Coordinates |
|------|-------------|
| **Return to Dusthaven** | `(13, 17)` |

---

## 5) EDGEWORKS STALL (Smith / Parts)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 24 x 18 tiles |
| **Exterior Door** | Town door `(48, 72)` |
| **Interior Entry Pad** | `(12, 16)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Forge Bench** | x 8-16, y 8-10 | Upgrade interaction |
| **Rack Wall** | x 2-6, y 3-12 | Weapon/display props |
| **Scrap Smelter** | x 18-22, y 6-12 | Visual heat source |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Upgrade menu** | `(12, 9)` | Weapon/parts upgrades |
| **Conversion node** | `(20, 9)` | Material conversion (PHASE 2+) |
| **Order ledger** | `(4, 8)` | Recipe unlock hints |

### D) Exit Triggers

| Exit | Coordinates |
|------|-------------|
| **Return to Dusthaven** | `(12, 17)` |

---

## 6) CLINIC TENT (Minor Treatment)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 22 x 16 tiles |
| **Exterior Door** | Town door `(80, 50)` |
| **Interior Entry Pad** | `(11, 14)` |

### B) Layout Blocks

| Block | Coordinates | Description |
|-------|-------------|-------------|
| **Triage Desk** | x 9-13, y 9-11 | Service point |
| **Cot Left** | x 3-7, y 5-7 | Patient prop |
| **Cot Right** | x 15-19, y 5-7 | Patient prop |
| **Medicine shelf** | x 2-5, y 2-4 | Flavor + item source |

### C) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Clinic menu** | `(11, 10)` | Status cures |
| **Supply cabinet** | `(3, 3)` | 1/day herb item |
| **Emergency cot** | `(17, 6)` | Scene beat anchor |

### D) Exit Triggers

| Exit | Coordinates |
|------|-------------|
| **Return to Dusthaven** | `(11, 15)` |

---

## 7) IRONHAWK BACKROOM (Optional)

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 20 x 16 tiles |
| **Exterior Access** | Hidden alley prompt in Ironhawk Cut (`District 5`) |
| **Interior Entry Pad** | `(10, 14)` |

### B) Key Interactables

| Interactable | Location | Function |
|--------------|----------|----------|
| **Broker crate** | `(10, 8)` | Black market menu (flagged availability) |
| **Signal radio** | `(4, 5)` | Optional lore |
| **Stash locker** | `(16, 5)` | Sidequest objective storage |

### C) Exit Triggers

| Exit | Coordinates |
|------|-------------|
| **Return to Dusthaven alley** | `(10, 15)` |

---

## 8) Day/Night + Phase Service Changes

| Phase | Change |
|-------|--------|
| **PHASE 0** | Base inventories, no backroom access |
| **PHASE 1** (`Scene 001 complete`) | Cantina back curtain opens; patrol flavor added |
| **PHASE 2** (`D1_CLEARED`) | Clinic and Smith inventory tier up |
| **PHASE 3** (`D3_CLEARED`) | Stable-adjacent items appear at General Goods |
| **PHASE 4** (late game) | Reduced civilian density, higher security flavor lines |

---

## 9) Interior-to-Quest Hook Map

| Interior | Main Hook |
|----------|-----------|
| **Cantina** | "The Contract" kickoff (Scene 001) |
| **Scrap Garage** | "Renna's Garage" recruitment/upgrade beats |
| **Rusty Cot** | Rumor pacing + safe return loop |
| **Dust & Bolt** | Early economy + fetch hooks |
| **Edgeworks** | Upgrade progression and material conversion |
| **Clinic Tent** | Status tutorial + escalation tone |
| **Ironhawk Backroom** | Optional black-market and late callback |

---

## Quick Reference

```text
CANTINA           32x24  door (52,46)  pad (16,22)
SCRAP GARAGE      40x28  door (26,78)  pad (20,26)
RUSTY COT INN     28x20  door (60,62)  pad (14,18)
DUST & BOLT       26x18  door (64,70)  pad (13,16)
EDGEWORKS STALL   24x18  door (48,72)  pad (12,16)
CLINIC TENT       22x16  door (80,50)  pad (11,14)
IRONHAWK BACKROOM 20x16  hidden alley   pad (10,14)
```
