# Dialog Production Scope
## Chroma's Edge - Writing Requirements

---

## 📊 TOTAL DIALOG REQUIREMENTS

### NPC Dialog (1,800+ lines)
| Zone | NPCs | Lines/NPC | Subtotal |
|------|------|-----------|----------|
| Dustbelt | 15 | 8 | 120 |
| Uplands | 10 | 8 | 80 |
| Mire | 14 | 8 | 112 |
| Prism | 12 | 8 | 96 |
| Ember | 13 | 8 | 104 |
| Tide | 14 | 8 | 112 |
| Obsidian | 11 | 8 | 88 |
| Frost | 12 | 8 | 96 |
| Chrono | 13 | 8 | 104 |
| Capital | 14 | 8 | 112 |
| Void | 8 | 10 | 80 |
| Tower | 10 | 6 | 60 |
| Palace | 8 | 6 | 48 |
| Aetherreach | 12 | 8 | 96 |
| Remnant | 6 | 10 | 60 |
| **TOTAL** | **172** | **~8** | **1,364** |

### Party Reactions (600+ lines)
| Character | Quirky NPCs (24) | Zone Entries (15) | Special | Subtotal |
|-----------|------------------|-------------------|---------|----------|
| Kade | 24 | 15 | 10 | 49 |
| Nix-7 | 24 | 15 | 10 | 49 |
| Twist | 24 | 15 | 10 | 49 |
| Korr | 24 | 15 | 5 | 44 |
| Renna | 24 | 15 | 5 | 44 |
| Suresh | 24 | 15 | 5 | 44 |
| Sova | 24 | 15 | 5 | 44 |
| Grit | 24 | 15 | 5 | 44 |
| Ashka | 24 | 15 | 5 | 44 |
| Senna | 24 | 15 | 5 | 44 |
| Callum | 24 | 15 | 5 | 44 |
| Petra | 24 | 15 | 5 | 44 |
| Vex | 24 | 15 | 5 | 44 |
| **TOTAL** | **312** | **195** | **75** | **582** |

### Grand Total: **~2,000 lines of dialog**

---

## 🎯 PRODUCTION PRIORITY TIERS

### Tier 1: Essential (Week 1)
**All zone hub NPCs** (innkeepers, main merchants, quest givers)
- ~50 NPCs
- ~400 lines

### Tier 2: Important (Week 2)
**All remaining quirky NPCs**
- ~122 NPCs
- ~960 lines

### Tier 3: Polish (Week 3)
**Party reactions and barks**
- ~600 lines

### Tier 4: Deluxe (Week 4)
**Quest-specific dialog and alternates**
- ~400 lines

---

## 📁 FILE STATUS TRACKER

### NPC Files (content/dialog/npcs/)
```
dustbelt/
  [x] barrelman_wood.json (Example created)
  [ ] barrelman_metal.json
  [ ] tunneler_brown.json
  [ ] tunneler_gray.json
  [ ] shoewoman_red.json
  [ ] shoewoman_blue.json
  [ ] signguy.json
  [ ] lucha_green.json
  [ ] lucha_red.json
  [ ] barrelgob_green.json
  [ ] barrelgob_brown.json
  [ ] barrel.json
  [ ] bush.json
  [ ] snakecharmer.json (Visiting)
  [ ] cobra.json (Visiting)
  
mire/
  [x] snakecharmer.json (Example created)
  [ ] pigman_brown.json
  [ ] pigman_purple.json
  [ ] foodboys_blue.json
  [ ] foodboys_yellow.json
  [ ] foodboys_red.json
  [ ] onionboss_white.json
  [ ] onionboss_purple.json
  [ ] barrelman_wood.json
  [ ] barrelgob_green.json
  [ ] signguy.json
  [ ] ironchef.json
  [ ] lucha_blue.json
  [ ] cobra.json

ember/
  [ ] ironchef_red.json
  [ ] ironchef_blue.json
  [ ] lucha_red.json
  [ ] lucha_green.json
  [ ] lucha_blue.json
  [ ] barrelgob_red.json
  [ ] barrelgob_black.json
  [ ] barrel.json
  [ ] tunneler_red.json
  [ ] pigman_red.json
  [ ] signguy.json
  [ ] sumo_white.json
  [ ] coolcat_red.json

[... 12 more zones ...]
```

### Party Files (content/dialog/party/)
```
kade/
  [x] reactions_quirky.json (Example created)
  [ ] reactions_beast.json
  [ ] reactions_elf.json
  [ ] zone_entries.json
  [ ] quest_comments.json

nix7/
  [ ] reactions_quirky.json
  [ ] reactions_beast.json
  [ ] reactions_elf.json
  [ ] zone_entries.json
  [ ] quest_comments.json

twist/
  [ ] reactions_quirky.json
  [ ] reactions_beast.json
  [ ] reactions_elf.json
  [ ] zone_entries.json
  [ ] quest_comments.json

[... 10 more characters ...]
```

---

## ✍️ WRITING WORKFLOW

### Step 1: Batch Similar NPCs
Write all "Merchant" types together → consistent voice
Write all "Entertainer" types together → consistent voice

### Step 2: Zone Context Pass
Add zone-specific references
Add cross-NPC connections
Add ambient barks

### Step 3: Party Reaction Pass
Write all Kade reactions for NPC type X
Write all Nix-7 reactions for NPC type X
 etc.

### Step 4: Integration Pass
Add party reaction triggers to NPC files
Add quest hooks
Test flow

---

## 🎭 VOICE GUIDE QUICK REFERENCE

| NPC Type | Voice | Example Quirk |
|----------|-------|---------------|
| barrelman | Shrewd, puns | Must make barrel jokes |
| snakecharmer | Dramatic, fake-mystical | Acts mysterious but is normal |
| lucha | Boisterous, energetic | Talks in third person |
| ironchef | Intense, professional | Treats cooking like combat |
| trenchcoat | Cryptic, spy-novel | Vague warnings |
| sumo | Wise, minimal words | Speaks in zen koans |
| foodboys | Enthusiastic, salesy | Always pitching |
| coolcat | Laid-back, hip | Jazz slang |
| pigman | Jovial, gossip | Loves rumors |
| tunneler | Gruff, practical | Work complaints |
| bush | Cryptic, playful | Nature puns |
| twins | Synchronized, eerie | Finish each other |

---

## 🚀 RECOMMENDED APPROACH

### Option A: Zone-by-Zone
Complete one zone entirely before moving on
- Pros: Coherent storytelling within zone
- Cons: May feel repetitive

### Option B: Archetype-by-Archetype  
Write all merchants, then all entertainers, etc.
- Pros: Consistent voice across world
- Cons: May miss zone flavor

### Option C: Hybrid (Recommended)
1. Write all Tier 1 (essential) NPCs zone-by-zone
2. Batch write Tier 2 NPCs by archetype
3. Zone pass for connections and barks
4. Party reactions in character batches

---

## 📝 TEMPLATE USAGE

### Creating New NPC Dialog:
1. Copy template from NPC_DIALOG_TEMPLATES.md
2. Fill in zone-specific details
3. Add 3-5 variants per category
4. Add party reaction triggers
5. Test in context

### Writing Party Reactions:
1. Review NPC dialog first
2. Write reaction that acknowledges specifics
3. Match character voice (Kade=curious, Nix=analytical, etc.)
4. Add callback references

---

## ✅ COMPLETION CHECKLIST

- [ ] All 172 NPCs have dialog files
- [ ] All 13 party members have reaction files
- [ ] Cross-NPC references added
- [ ] Quest hooks integrated
- [ ] Ambient barks written
- [ ] Review for tone consistency
- [ ] Playtest for flow

---

*Target completion: 2,000 lines across 200+ files*
