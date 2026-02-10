# Chroma's Edge - NPC Roster & Dialog Matrix
## Complete NPC Catalog with Dialog Trees and Conditions

---

# ASHVEIL SANCTUARY NPCs

## KEY NPCs

### MIRA THORN (Innkeeper)
**Location:** Mira's Rest Inn (58, 62)  
**Role:** Innkeeper, Quest Giver  
**Schedule:** Always present

**Appearance:**  
- 40s, tired eyes, practical clothing
- Wears husband's compass on a chain

**Dialog Matrix:**

| Condition | Greeting | Topics Available |
|-----------|----------|------------------|
| **First Meeting** | "Welcome to Mira's Rest. Beds are clean, food is hot, and I don't ask questions." | • The Sanctuary<br>• Rooms for rent<br>• Her husband (locked)<br>• Quest: Missing Scavengers |
| **Post-D1 Clear** | "You cleared the ruins? Maybe... maybe things can get better." | • The Bloom<br>• Her husband (unlocked)<br>• Quest: The Debt Collectors<br>• Deeper basement rumors |
| **Post-World Break** | "Sky's wrong. Ground's wrong. But I'm still here, and so are you." | • Coping<br>• Refugee influx<br>• Quest: Family Heirloom<br>• Keeping hope |
| **Quest Active** | "Any news? I... I need to know." | • Quest status<br>• Additional hints |
| **Quest Complete** | "Thank you. Truly. Now... now I can rest too." | • Shop discount<br>• Backstory<br>• Final quest chain |

**Key Dialog Lines:**

**Husband Backstory (Post-D1):**
```
MIRA: "My husband Tomas was a scavenger. Good one too.
       He went into the ruins six months ago, before...
       before they grew like they do now."

PLAYER: "I'm sorry."

MIRA: "Don't be. He knew the risks. But if you're going
        back in... he wore a compass. Old brass thing.
        If you find it... I'd like to bury it properly."
```

---

### CAPTAIN VARROS (Militia Captain)
**Location:** Barracks (72, 54)  
**Role:** Combat trainer, defense coordinator  
**Schedule:** Day: Barracks, Night: Patrol

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First Meeting** | "Varros. I run the militia. You look like you can handle yourself." | • Training<br>• Sanctuary defense<br>• Dominion threat<br>• Quest: Training Day |
| **Post-Training** | "Form's not bad. Could be better. Could be worse." | • Advanced tactics<br>• Quest: Dominion Scouts<br>• Weapon maintenance |
| **Post-D1** | "You fight like you mean it. We could use that." | • Quest: Siege Preparation<br>• Recruiting<br>• Tactics discussion |
| **World Break** | "No time for lessons. Either you know it or you're dead." | • Emergency protocols<br>• Evacuation plans<br>• Last stand preparations |

---

### SANCTUARY KEEPER (Unnamed)
**Location:** Heartroot Hall (58, 54)  
**Role:** Town leader, lore keeper  
**Schedule:** Always in Hall

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First Meeting** | "The Sanctuary welcomes survivors. Whether it can save them... that's another question." | • The Relics<br>• The ruins<br>• Prime Pedestal (post-D1)<br>• Ancient history |
| **Post-D1** | "You've done what Dominion soldiers couldn't. The Pedestal awaits." | • Seating ceremony<br>• The Eight<br>• Next steps<br>• Korr's arrival |
| **Post-Korr Join** | "Strange days. A Marshal helps us, the ruins yield their secrets... what next?" | • Trusting Korr<br>• The journey ahead<br>• Blessings |

---

## COMMON NPCs

### REFUGEE FAMILY (Father, Mother, Child)
**Location:** Tent cluster (48, 48)  
**Role:** Ambient, emotional weight

**Dialog Matrix:**

| NPC | Condition | Line |
|-----|-----------|------|
| **Father** | Default | "We had a farm. Three acres. It's... it's forest now. Just... grew over everything." |
| **Father** | Post-D1 | "You're the one who went into the ruins? My daughter thinks you're a hero." |
| **Mother** | Default | "Shh. Don't cry. The nice people here will help us. They will. They have to." |
| **Mother** | Night | "[Humming lullaby] Sleep, baby. Tomorrow will be better. It has to be." |
| **Child** | Default | "Are you a hero? You look like a hero." |
| **Child** | Post-D1 | "Did you see the monster? Was it big? Did you win?" |
| **Child** | World Break | "Mommy, why won't the sun come back?" |

---

### GAMBLER (No-name)
**Location:** Corner table, Mira's Rest  
**Role:** Mini-game introduction

**Dialog Matrix:**

| Condition | Line |
|-----------|------|
| **First** | "Fancy a game? Nothing serious. Just friendly wagering." |
| **Win** | "You're lucky. Or skilled. Or both. Care to double your winnings?" |
| **Lose** | "Tough break. House always wins in the end. Usually." |
| **High Winnings** | "You're making me nervous. Big winners attract attention." |

---

# DUSTHAVEN NPCs

## KEY NPCs

### BROKER VANE (Information Dealer)
**Location:** Shadow Market (82, 88)  
**Role:** Quest hub, rumor mill  
**Schedule:** Night only

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First Meeting** | "I hear things. You want things. Maybe we can help each other." | • Rumors (paid)<br>• Quests<br>• Dominion movements |
| **Reputation Low** | "Don't know you. Don't trust you. Come back when someone vouches." | • Limited info<br>• High prices |
| **Reputation Med** | "You're making a name. Names have value." | • Better prices<br>• More quests<br>• Syndicate info |
| **Reputation High** | "The hero of Ashveil. Please, sit. What do you need?" | • Best prices<br>• Exclusive quests<br>• Hidden areas |

**Rumor Purchase:**
```
VANE: "Information is currency. Here's today's rates:"

• Dominion patrol routes (500 G)
• Hidden cache location (800 G)
• Syndicate meeting place (1200 G)
• [Endgame] Progenitor site map (5000 G)
```

---

### BLACKSMITH KELLEN
**Location:** Forge (58, 58)  
**Role:** Equipment, crafting

**Dialog Matrix:**

| Condition | Greeting | Services |
|-----------|----------|----------|
| **First** | "Need metal bent? I'm your man." | • Buy/sell<br>• Repair<br>• Basic crafting |
| **Post-D2** | "Heard you dealt with that... thing in the swamp. Good. Had a cousin go missing there." | • Steel tier unlocked<br>• Discount |
| **Post-D4** | "World's ending and you want a sharper sword? Fair enough. Sharp sword's better than no sword." | • All tiers<br>• Masterwork option |

---

## MERCHANT NPCs

### WEAPON MERCHANT
**Dialog:**
- **Browse:** "Best iron this side of the fracture. No refunds."
- **Purchase:** "Good choice. Treat her well, she'll treat you well."
- **No money:** "Come back when you have coin. This isn't a charity."

### ARMOR MERCHANT
**Dialog:**
- **Browse:** "A good coat stops arrows. A great coat stops questions."
- **Heavy armor:** "Slow and sure. That's the way to survive."
- **Light armor:** "Fast? Good. Dead heroes don't need armor."

---

# CHRONOWAKE PIER NPCs

## KEY NPCs

### DOCKMASTER SARAI
**Location:** Main Dock (56, 64)  
**Role:** Transportation, quest giver

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Chronowake Pier. If you need on or off the water, I'm who you see." | • Boat schedules<br>• Passage prices<br>• D5 information (locked) |
| **Post-D4** | "You survived the Skyspire? [Whistles] That's a story I want to hear." | • World Break reactions<br>• Refugee boats |
| **D5 Unlocked** | "The Trench? Yeah, I can get you there. But I won't go down. No one goes down and comes up." | • Submersible charter<br>• Marinus info<br>• Tide warnings |

---

### MARINUS (Pre-Recruitment)
**Location:** Pier edge (80, 80)  
**Role:** Mysterious figure, future party member

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "[The figure doesn't turn. Their cloak moves like water, not wind.]" | • Who are you?<br>• The tide (cryptic)<br>• D5 warnings |
| **D5 Clear** | "You returned. The depths recognized something in you." | • Join offer<br>• Tide Foundation<br>• Ancient pacts |
| **Post-Join** | "The water speaks of you now. Favorably, which is rare." | • Companion dialog<br>• Water lore |

---

# PRISMRIDGE NPCs

## KEY NPCs

### OLD KELL (Cartographer)
**Location:** Survey Office (42, 58)  
**Role:** Quest giver, map seller

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Maps. I sell maps. Real ones, not Dominion-approved fantasies." | • Buy maps<br>• Quest: Incomplete Maps<br>• The uncharted |
| **Quest Active** | "Found anything interesting? Mark it. Bring it back. Knowledge is shared or it's lost." | • Progress check<br>• Mapping tips |
| **D3 Active** | "My mentor is down there. Has been for years. If you find him... tell him Kell never stopped looking." | • Varnis search<br>• Quest: Missing Expedition |

---

### MINE FOREMAN
**Location:** Mine entrance (88, 42)  
**Role:** Gatekeeper, warning

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **Pre-D3** | "Mines are closed. Dominion orders. "Crystal formations unstable." As if they care." | • Closure reason<br>• Smuggling rumors |
| **D3 Clear** | "Light's back to normal. You're saying that thing in the caves was the cause?" | • Reopening<br>• Gratitude<br>• Miner jobs |

---

# CINDERSTEP NPCs

## KEY NPCs

### FORGE MASTER GRIMJAW
**Location:** Main Forge (64, 64)  
**Role:** Master smith, Grit's former boss

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Steel doesn't care about your problems. It just is. Remember that." | • Crafting<br>• Ore trading<br>• The Quarry (locked) |
| **Post-D6** | "Grit survived? Ha! Of course she did. Rock couldn't break that woman." | • Grit reunion<br>• Masterwork quests<br>• Colossus info |
| **Grit in Party** | "[Spits] Still alive, Stoneheart? Should've known. Rock's stubborn, and so are you." | • Banter<br>• Old stories<br>• Grudge match offer |

---

### SENNA (Pre-Recruitment)
**Location:** Forge floor (60, 60)  
**Role:** Smith apprentice, future party member

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Keep clear of the quenching trough. Hot metal, cold water, bad combination for skin." | • Forge work<br>• Heat Foundation rumors<br>• Escaping Cinderstep |
| **Post-D6** | "You went to the Quarry? Saw what the Mass Foundation did? And you're still walking?" | • Impressed<br>• Join offer<br>• Family in Rimehold |
| **Quest Active** | "My turn to prove something. Let's go." | • Companion dialog |

---

# MIREWATCH NPCs

## KEY NPCs

### SISTER AMARA (Healer)
**Location:** Infirmary (48, 72)  
**Role:** Healing, quest giver

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Wounds physical or spiritual, I treat both. Though the spiritual take longer." | • Healing (free/paid)<br>• Quest: Medicinal Herbs<br>• The sick |
| **Quest Active** | "The herbs you seek grow where the marsh meets the ruins. Be careful." | • Location hints<br>• Danger warnings |
| **World Break** | "More wounded than I can treat. If you can help... please." | • Emergency aid<br>• Quarantine quest |

---

# RIMEHOLD NPCs

## KEY NPCs

### ARCHIVIST VELM
**Location:** Ledger of Seasons (22, 34)  
**Role:** Lore keeper, D7 quest giver

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Twelve thousand years of history. Most of it lies, but the lies are interesting too." | • Codex entries<br>• Time Foundation<br>• Elder Mordai |
| **D7 Active** | "You're going to confront Mordai? [Laughs] Good. Someone should. Man's been "pausing" his death for fifty years." | • Mordai's history<br>• Citadel layout<br>• Time puzzles |
| **D7 Clear** | "Time flows true again. I can hear the clocks ticking. Hadn't realized how much I missed it." | • Post-D7 lore<br>• Future predictions |

---

### CALLUM (Pre-Recruitment)
**Location:** Phoenix roost (hidden, 120, 20)  
**Role:** Phoenix keeper, future party member

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **Found** | "Shh. She doesn't like strangers. None of them do." | • The phoenixes<br>• Rebirth<br>• Ashborn |
| **Post-D4** | "You felt the Heat Foundation scream. I felt it answer. Ashborn wants to meet you." | • Join offer<br>• Phoenix rider training |

---

# MERIDIAN JUNCTION NPCs

## KEY NPCs

### TERMINAL OPERATOR
**Location:** Central Terminal (74, 72)  
**Role:** Fast travel unlock, route info

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Terminal's active. I can route you anywhere the conduits reach. For a fee." | • Unlock fast travel<br>• Route stabilization<br>• Quests |
| **World Break** | "Conduits are unstable. Routes might drop you... elsewhere. Still willing to try?" | • Risky travel<br>• Stabilization quests |
| **All Routes** | "You've been everywhere, haven't you? Few can say that. Fewer still survive it." | • Congratulations<br>• Final routes |

---

### PETRA (Pre-Recruitment)
**Location:** Weight of Ages monument (88, 88)  
**Role:** Pilgrim, future party member

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "[She doesn't look up. Her shoulders carry weight you can't see.]" | • The monument<br>• Burden<br>• Agonis |
| **Post-D6** | "You spared the Colossus. Or ended its pain. Either way... you chose mercy." | • Join offer<br>• Shared burden |

---

# GAVEMARK OUTPOST NPCs

## KEY NPCs

### RAIL CAPTAIN DORSA
**Location:** Loading Yard (54, 66)  
**Role:** Transportation, Dominion resistance

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "Trains run on time or they don't run. Dominion learned that. We all learned it." | • Rail schedules<br>• Dominion permits<br>• Underground routes |
| **Korr in Party** | "Marshal. Didn't expect to see you off-leash. Hope you know what you're doing." | • Tension<br>• Trust check |
| **World Break** | "Tracks are damaged. World shook hard. But we're still moving. Always moving." | • Route changes<br>• Emergency transport |

---

# OLD LUMENCREST NPCs

## KEY NPCs

### RESISTANCE CONTACT (VARIN)
**Location:** Hidden basement (56, 56)  
**Role:** Underground network, safe houses

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First (need password)** | "Don't know you. Don't talk to people I don't know." | • Password required<br>• Reputation check |
| **Post-Password** | "Password's good. Means someone's vouching. What do you need?" | • Safe houses<br>• Dominion intel<br>• Escape routes |
| **World Break** | "Underground's safer now. Sky's wrong up there." | • Hideout network<br>• Resistance coordination |

---

# CROWN DISTRICT NPCs

## KEY NPCs

### SEAM WARDEN (Post-Game)
**Location:** Aetherreach (unlocked post-palace)  
**Role:** Remnant Vault guide

**Dialog Matrix:**

| Condition | Greeting | Topics |
|-----------|----------|--------|
| **First** | "You've done the impossible. Now... now you face the improbable." | • Vault access<br>• Superboss info<br>• Ultimate challenges |
| **Wing Clears** | "X of 3 wings cleared. The Core awaits your victory... or your failure." | • Progress<br>• Core unlock |

---

# DIALOG MATRIX TEMPLATES

## Standard Dialog Structure

```
NPC: [Name]
LOCATION: [X, Y] in [Zone]
ROLE: [Function]

GREETINGS (by condition):
├── Default: "[Line]"
├── Post-Quest-X: "[Line]"
├── Time-Day: "[Line]"
├── Time-Night: "[Line]"
└── Party-Member-Y: "[Line]"

TOPICS:
├── Topic A
│   ├── Choice 1 → Response A1
│   ├── Choice 2 → Response A2
│   └── Choice 3 → [Exit]
├── Topic B (locked until Flag Z)
│   └── ...
└── [Exit]

QUESTS:
├── Quest 1: [Name]
│   ├── Start condition
│   ├── Active lines
│   └── Complete lines
└── ...

SHOP (if applicable):
├── Buy
├── Sell
└── Special
```

---

## Condition Flags Reference

| Flag Category | Examples |
|---------------|----------|
| **Story** | `D1_CLEARED`, `WORLD_BREAK`, `ACT2_STARTED` |
| **Quest** | `QUEST_X_ACTIVE`, `QUEST_X_COMPLETE` |
| **Time** | `TIME_DAY`, `TIME_NIGHT`, `TIME_DAWN` |
| **Party** | `KORR_JOINED`, `RENNA_IN_PARTY` |
| **Reputation** | `REP_ASHVEIL_HIGH`, `REP_SYNDICATE_LOW` |
| **Hidden** | `FOUND_SECRET_X`, `PASSWORD_KNOWN` |

---

## Dialog Response Types

| Type | Effect |
|------|--------|
| **Information** | Adds codex entry |
| **Quest Start** | Begins quest chain |
| **Shop Open** | Opens merchant interface |
| **Flag Set** | Sets condition flag |
| **Party Change** | Adds/removes party member |
| **Teleport** | Moves player |
| **Battle** | Initiates combat |
| **Banter** | Triggers party comment |

---

# NPC COUNT SUMMARY

| Town/Area | Key NPCs | Common NPCs | Total |
|-----------|----------|-------------|-------|
| Ashveil Sanctuary | 3 | 8 | 11 |
| Dusthaven | 4 | 6 | 10 |
| Chronowake Pier | 3 | 4 | 7 |
| Prismridge | 3 | 5 | 8 |
| Cinderstep | 3 | 4 | 7 |
| Mirewatch | 2 | 4 | 6 |
| Rimehold | 3 | 4 | 7 |
| Meridian Junction | 3 | 6 | 9 |
| Gravemark Outpost | 2 | 3 | 5 |
| Old Lumencrest | 2 | 5 | 7 |
| Crown District | 1 | 4 | 5 |
| Aetherreach | 2 | 2 | 4 |
| **TOTAL** | **31** | **55** | **86** |

---

# IMPLEMENTATION CHECKLIST

- [ ] All 86 NPCs have unique identifiers
- [ ] Dialog trees mapped for all key NPCs (31)
- [ ] Bark pools created for common NPCs (55)
- [ ] Condition flags documented per NPC
- [ ] Quest triggers linked to NPCs
- [ ] Shop inventories linked to merchants
- [ ] Party member reactions scripted
- [ ] Time-based dialog variations set
- [ ] Post-clear reactive dialog implemented
- [ ] Voice acting markers (if applicable)
