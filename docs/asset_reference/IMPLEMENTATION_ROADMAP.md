# Asset Implementation Roadmap
## From SNES Reference to In-Game Assets

This document provides a step-by-step implementation plan for integrating SNES assets into Chroma's Edge.

---

## 📅 PHASE 1: FOUNDATION (Week 1)

### Day 1-2: Setup & Extraction

**Tasks:**
1. Create folder structure:
   ```
   assets/
   ├── reference/snes/
   │   ├── terranigma/
   │   ├── albert_odyssey/
   │   ├── breath_of_fire/
   │   └── extracted/
   ├── battle_backgrounds/
   │   ├── palace/
   │   ├── capital_ruins/
   │   ├── tide/
   │   ├── uplands/
   │   └── aetherreach/
   └── tileset_reference/
   ```

2. Copy all SNES assets to reference folders

3. Install image editing tools:
   - GIMP (free) or Aseprite (recommended for pixel art)
   - Bulk image processor (optional)

**Deliverables:**
- Organized asset library
- Tools ready

---

### Day 3-4: Critical Extractions

**Priority 1 Assets (Extract First):**

| # | Asset Name | Source File | Time Est. |
|---|-----------|-------------|-----------|
| 1 | palace_throne_room_main.png | Loire Castle 2F | 30 min |
| 2 | palace_throne_room_alt.png | Loire Castle 2F | 20 min |
| 3 | ruins_entry_plaza.png | Louran Ruins | 20 min |
| 4 | ruins_shop_a.png | Louran Ruins | 20 min |
| 5 | ruins_town_square.png | Louran Ruins | 25 min |
| 6 | aetherreach_plaza.png | BoF2 Windia | 30 min |
| 7 | tide_harbor_main.png | Harbor Freedom | 25 min |

**Total Time:** ~3 hours

**Deliverables:**
- 7 essential battle backgrounds extracted
- Files saved to appropriate folders

---

### Day 5-7: Style Adjustment

**For Each Extracted Asset:**

1. **Open in GIMP/Aseprite**
2. **Resize to 640x360** (maintain aspect ratio)
3. **Apply color adjustments:**
   - Palace: Desaturate 10%, darken 5%
   - Ruins: Desaturate 20%, darken 15%
   - Tide: Enhance blue +10%
   - Aetherreach: Brighten 10%
4. **Export as PNG**
5. **Test in engine** (if available)

**Deliverables:**
- 7 adjusted backgrounds ready for use
- Style consistency verified

---

## 📅 PHASE 2: CORE CONTENT (Week 2)

### Day 8-10: Palace Dungeon Assets

**Extract Palace Components:**

| Room | Source | Status |
|------|--------|--------|
| Guard Stations | Loire 2F | ⬜ |
| Royal Lounge | Loire 2F | ⬜ |
| Bedchamber | Loire 3F | ⬜ |
| Library | Loire 1F | ⬜ |
| Chapel | Sylvain | ⬜ |
| Tower Top | Sylvain | ⬜ |
| Prison | Loire 1F | ⬜ |

**Map Layout Implementation:**
1. Create Palace dungeon map in editor
2. Place extracted backgrounds for each room
3. Add corruption effects (particle overlay)
4. Implement throne room final boss arena

**Deliverables:**
- Palace dungeon fully mapped
- All room backgrounds implemented
- Throne room boss arena ready

---

### Day 11-12: Capital Ruins Assets

**Extract Ruin Variations:**

| # | Ruin Type | Source | Status |
|---|-----------|--------|--------|
| 1 | Shop B | Louran R1C3 | ⬜ |
| 2 | Home A | Louran R2 | ⬜ |
| 3 | Home B | Louran R2 | ⬜ |
| 4 | Apartment | Louran R3 | ⬜ |
| 5 | Market | Louran R4 | ⬜ |
| 6 | Memorial | Louran R5 | ⬜ |
| 7 | Sewer | Louran R6 | ⬜ |
| 8 | Palace Gate | Louran R8 | ⬜ |

**Encounter Implementation:**
- Match backgrounds to encounter design doc
- Place enemies according to CAPITAL_RUINS_ENCOUNTERS.md
- Set up battle transitions

**Deliverables:**
- 8 ruin backgrounds ready
- Capital Ruins zone populated
- Encounters placed

---

### Day 13-14: Tide & Aetherreach

**Tide Assets:**
- Extract ship deck and cabin
- Extract dock sections
- Create harbor town layout

**Aetherreach Assets:**
- Extract Windia sections
- Extract Albert Odyssey cloud variants
- Create floating city layout

**Deliverables:**
- Tide Coast backgrounds
- Aetherreach backgrounds
- Both zones mapped

---

## 📅 PHASE 3: POLISH (Week 3)

### Day 15-17: Additional Zones

**Uplands:**
- Extract Storkolm village sections
- Adapt for stone sanctuary theme

**Tower:**
- Extract tower sections from Loire Castle
- Create ascending floor progression

**Remaining Zones:**
- Check if Time Fantasy assets sufficient
- Extract any needed reference pieces

**Deliverables:**
- All 15 zones have backgrounds
- Complete visual coverage

---

### Day 18-19: Effects & Animation

**Add to All Backgrounds:**

1. **Corruption Effects:**
   - Purple smoke overlay (Palace, Capital)
   - Dark vines (Capital Ruins)
   - Void energy (Void zone)

2. **Lighting Effects:**
   - Torch flicker (Palace)
   - Lightning flash (Capital)
   - Water shimmer (Tide)
   - Cloud glow (Aetherreach)

3. **Particle Systems:**
   - Dust motes (all ruins)
   - Magic sparkles (Aetherreach)
   - Ash fall (Ember)
   - Snow (Frost)

**Deliverables:**
- All backgrounds have appropriate effects
- Animated elements added

---

### Day 20-21: Testing & Iteration

**Test Checklist:**

- [ ] All backgrounds display correctly
- [ ] No visual artifacts or seams
- [ ] Effects don't obscure characters
- [ ] Performance acceptable (60fps)
- [ ] Colors consistent across zones
- [ ] Resolution correct for target platform

**Feedback Loop:**
1. Screenshot each background in-game
2. Compare to style guide
3. Adjust as needed
4. Re-test

**Deliverables:**
- All assets tested and approved
- Bug fixes complete

---

## 📅 PHASE 4: COMPLETION (Week 4)

### Day 22-25: Documentation

**Update Documentation:**

1. Update PRODUCTION_CHECKLIST_MASTER.md:
   - Mark asset tasks complete
   - Note any changes

2. Create ASSET_USAGE_GUIDE.md:
   - Which backgrounds used where
   - File paths
   - Special notes

3. Update MASTER_INDEX.md:
   - Add asset references to dialog files
   - Note visual style for cutscenes

**Deliverables:**
- All documentation current
- Asset usage catalogued

---

### Day 26-28: Final Review

**Quality Assurance:**

1. **Visual Consistency Check:**
   - All backgrounds reviewed side-by-side
   - Color matching verified
   - Style uniformity confirmed

2. **Gameplay Integration:**
   - Playtest each zone
   - Verify backgrounds enhance gameplay
   - Check encounter visibility

3. **Optimization:**
   - Compress images if needed
   - Verify loading times
   - Check memory usage

**Deliverables:**
- Final asset package approved
- Ready for production

---

## 📊 MILESTONE SUMMARY

| Week | Milestone | Deliverables |
|------|-----------|--------------|
| Week 1 | Foundation | 7 critical backgrounds, tools ready |
| Week 2 | Core Content | Palace + Capital Ruins complete |
| Week 3 | Polish | All zones covered, effects added |
| Week 4 | Completion | Documentation, QA, approval |

**Total Timeline:** 28 days (~1 month)
**Total Assets:** ~35 battle backgrounds
**Total Zones Covered:** 15

---

## 🛠️ TOOLS & RESOURCES

### Required Software:
- **GIMP** (free) - Image editing
- **Aseprite** ($20) - Pixel art (recommended)
- **Bulk Resize Tool** - Batch processing
- **Color Picker Tool** - Palette matching

### Reference Documents:
- EXTRACTION_COORDINATES.md - Pixel coordinates
- VISUAL_STYLE_GUIDE.md - Color/style rules
- ZONE_ASSET_MAPPING.md - Zone assignments
- PALACE_DUNGEON_LAYOUT.md - Palace design
- CAPITAL_RUINS_ENCOUNTERS.md - Ruins design

### Asset Sources:
- Terranigma maps (primary)
- Breath of Fire 2 Windia
- Albert Odyssey 2 clouds

---

## 🚨 RISK MITIGATION

### Potential Issues:

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Colors don't match TF | Medium | Use style guide adjustments |
| Resolution looks wrong | Low | Test early, adjust scale |
| Too time-consuming | Medium | Prioritize critical assets |
| File sizes too large | Low | Compress, use lower res |
| Engine compatibility | Low | Test with placeholder first |

### Contingency Plans:

**If behind schedule:**
- Skip "Nice to Have" assets
- Use Time Fantasy defaults for less critical zones
- Focus on Palace and Capital only

**If colors won't match:**
- Desaturate all SNES assets more heavily
- Use as "inspiration" only, recreate in TF style
- Adjust TF tilesets instead (if possible)

---

## ✅ SUCCESS CRITERIA

Project considered complete when:

- [ ] Palace dungeon has 8+ unique backgrounds
- [ ] Capital Ruins has 8+ unique backgrounds
- [ ] Critical zones (Tide, Aetherreach, Uplands) covered
- [ ] All backgrounds match Time Fantasy style
- [ ] Effects added to key areas
- [ ] Documentation complete
- [ ] Playtested and approved

---

*"A goal without a plan is just a wish. This roadmap turns your assets into reality."*
