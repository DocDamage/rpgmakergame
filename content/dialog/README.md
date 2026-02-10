# Dialog System - Chroma's Edge

## 📂 Folder Structure

```
content/dialog/
├── README.md (this file)
├── NPC_DIALOG_TEMPLATES.md - Templates for creating NPC dialog
├── DIALOG_PRODUCTION_SCOPE.md - Production tracker and requirements
├── npcs/ - NPC dialog files organized by zone
│   ├── dustbelt/
│   │   └── barrelman_wood.json (EXAMPLE)
│   ├── mire/
│   │   └── snakecharmer.json (EXAMPLE)
│   └── [zone]/
│       └── [npc_id].json
└── party/ - Party member reactions
    ├── kade/
    │   └── reactions_quirky.json (EXAMPLE)
    ├── nix7/
    │   └── reactions_quirky.json (EXAMPLE)
    └── twist/
        └── reactions_quirky.json (EXAMPLE)
```

---

## 🎯 Production Goal

**2,000+ lines of dialog:**
- 1,364 lines for 172 NPCs
- 582 lines for 13 party member reactions
- 400+ quest-specific and ambient lines

---

## 📋 How to Create New NPC Dialog

### Step 1: Choose Template
Open `NPC_DIALOG_TEMPLATES.md` and select the archetype:
- Merchant (barrelman, shoewoman, foodboys)
- Entertainer (snakecharmer, lucha, coolcat)
- Guardian (sumo, trenchcoat)
- Mysterious (bush, twins)
- Worker (tunneler, ironchef, barrelgob)
- Innkeeper (pigman variants)

### Step 2: Create File
```bash
content/dialog/npcs/[zone]/[npc_id].json
```

### Step 3: Fill Template
Minimum required:
- 3-5 greeting variants
- 1 shop/service interaction (if merchant)
- 1 quest hook or rumor
- 2 farewell variants
- Party reaction triggers

### Step 4: Add Party Reactions
Edit `party/[character]/reactions_quirky.json`:
```json
"[npc_type]": [
  "Reaction line 1",
  "Reaction line 2",
  "Reaction line 3"
]
```

---

## 🎭 Character Voice Reference

| Character | Voice | Key Traits |
|-----------|-------|------------|
| **Kade** | Curious, good-natured | Asks questions, optimistic, diplomatic |
| **Nix-7** | Literal, analytical | Deadpan, statistical, misses social cues |
| **Twist** | Enthusiastic, simple | Excited, loves food/fighting, innocent |

See example files for full voice demonstrations.

---

## 📝 JSON Schema

### NPC File Structure:
```json
{
  "npc_id": "unique_identifier",
  "name": "Display Name",
  "sprite": "sprite_file_name",
  "zone": "zone_name",
  "location": "specific_location",
  "personality": "archetype_tag",
  "occupation": "job_title",
  "dialog": {
    "greeting": ["line1", "line2", "line3"],
    "shop_open": "shop_line",
    "haggle": ["line1", "line2"],
    "purchase_success": ["line1", "line2"],
    "purchase_fail": ["line1", "line2"],
    "rumor": "rumor_text",
    "quest_hook": "quest_text",
    "quest_active": "active_quest_text",
    "quest_complete": "completion_text",
    "farewell": ["line1", "line2"],
    "ambient_barks": ["line1", "line2", "line3"]
  },
  "party_reactions": {
    "kade": "reaction_line",
    "nix7": "reaction_line",
    "twist": "reaction_line"
  }
}
```

### Party Reaction File Structure:
```json
{
  "character": "CharacterName",
  "reaction_type": "quirky_npc_encounters",
  "personality_notes": "brief_description",
  "dialog": {
    "first_meet_generic": ["line1", "line2"],
    "[npc_type]": ["line1", "line2", "line3"]
  }
}
```

---

## ✅ Example Files Created

### NPC Examples:
- `npcs/dustbelt/barrelman_wood.json` - Merchant archetype
- `npcs/mire/snakecharmer.json` - Entertainer archetype

### Party Reaction Examples:
- `party/kade/reactions_quirky.json` - Curious protagonist voice
- `party/nix7/reactions_quirky.json` - Android analytical voice
- `party/twist/reactions_quirky.json` - Enthusiastic muscle voice

---

## 🚀 Production Workflow

### Recommended Order:
1. **Tier 1:** Write all innkeepers and main merchants (50 NPCs)
2. **Tier 2:** Write remaining quirky NPCs (122 NPCs)
3. **Tier 3:** Write party reactions zone by zone
4. **Tier 4:** Add quest-specific dialog and connections

### Batch Writing Strategy:
1. Pick NPC type (e.g., all merchants)
2. Write 3-5 variants per dialog category
3. Copy to zone files
4. Add zone-specific flavor
5. Move to next type

---

## 🎨 Writing Tips

### Keep It Snappy:
- Max 2 lines per dialog box
- Punchy, readable
- Character voice consistent

### Cross-Reference NPCs:
- Mention other NPCs by name
- Create mini-story webs
- Reference zone events

### Use Color Variants:
- Red variants = aggressive
- Blue variants = service
- Green variants = nature
- etc.

### Party Callbacks:
- Reference previous zones
- Acknowledge quest progress
- React to specific NPC quirks

---

## 📊 Progress Tracker

Update as you complete:

### NPCs Completed: [ ] / 172
- [ ] Dustbelt (15)
- [ ] Uplands (10)
- [ ] Mire (14)
- [ ] Prism (12)
- [ ] Ember (13)
- [ ] Tide (14)
- [ ] Obsidian (11)
- [ ] Frost (12)
- [ ] Chrono (13)
- [ ] Capital (14)
- [ ] Void (8)
- [ ] Tower (10)
- [ ] Palace (8)
- [ ] Aetherreach (12)
- [ ] Remnant (6)

### Party Reactions: [ ] / 13
- [ ] Kade
- [ ] Nix-7
- [ ] Twist
- [ ] Korr
- [ ] Renna
- [ ] Suresh
- [ ] Sova
- [ ] Grit
- [ ] Ashka
- [ ] Senna
- [ ] Callum
- [ ] Petra
- [ ] Vex

---

*Happy writing! Make the world feel alive!*
