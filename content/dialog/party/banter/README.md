# Party Banter and Interaction System

## Overview
Expanded and canon-aligned party dialog package for the 13-character Orion cast.

## Files

### 1. `party_banter.json`
- 324 exchanges
- Full 78/78 pair coverage
- Includes pair, trio, and squad conversations
- Story phase tags: `act1`, `post_world_break`, `post_korr_break`, `endgame`

### 2. `zone_commentary.json`
- 1300 zone commentary lines
- 10 zones with 5 trigger types each
- Trigger model: first visit, return visit, post-break, local hazard, nearby terminal

### 3. `npc_interactions.json`
- 780 interaction lines
- 8 NPC categories with contextual variants
- Structure normalized and JSON-valid

### 4. `combat_barks.json`
- 936 combat bark lines
- 9 categories fully populated:
  - `attack`, `damage_taken`, `healing_received`, `victory`, `defeat_warning`
  - `critical_hit`, `dodge`, `buff`, `debuff`

### 5. `story_reactions.json`
- 858 reaction lines
- 11 story categories including World Break, Korr liberation, Prime restoration, and Engine confrontation

### 6. `_character_reference.md`
- Canon-aligned voice and arc guide for all 13 party members
- Pair dynamic notes and timeline anchors

## Data Notes
- All JSON files are UTF-8 and parser-valid.
- Character IDs are standardized: `kade, nix7, renna, suresh, twist, sova, grit, ashka, senna, callum, petra, vex, korr`.
- Tone target: gritty frontier with tragic weight and disciplined pressure-release humor.

## Usage

### Banter selection
```javascript
const banter = require('./party_banter.json');
const pool = banter.banter_exchanges.filter((e) =>
  e.participants.includes('kade') && e.story_phase !== 'act1'
);
```

### Zone commentary selection
```javascript
const zones = require('./zone_commentary.json');
const lines = zones.zone_comments.desert.weather_sandstorm.korr;
const pick = lines[Math.floor(Math.random() * lines.length)];
```

### NPC interaction selection
```javascript
const npc = require('./npc_interactions.json');
const lines = npc.npc_reactions.merchant.kade.haggle;
```

### Combat barks selection
```javascript
const combat = require('./combat_barks.json');
const line = combat.combat_barks.critical_hit.vex[0];
```

## Version
- v2.0: Full cohesion pass, schema normalization, volume expansion, and canon alignment.
