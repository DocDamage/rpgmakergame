# NPC Dialog Templates
## Chroma's Edge - Dialog Production Guide

**Total NPCs:** 180+ Quirky NPCs + 40+ Standard NPCs  
**Target:** 5-10 lines per NPC minimum = **1,000+ lines of NPC dialog**  
**Plus:** Party reactions = **500+ lines of character dialog**

---

## 📁 FILE ORGANIZATION

```
content/dialog/
├── npcs/
│   ├── dustbelt/
│   │   ├── tunneler_brown.json
│   │   ├── barrelman_wood.json
│   │   └── ...
│   ├── mire/
│   ├── ember/
│   └── ... (one file per NPC)
├── party/
│   ├── kade/
│   │   ├── reactions_quirky.json
│   │   ├── reactions_beast.json
│   │   └── zone_comments.json
│   ├── nix7/
│   └── ... (one folder per party member)
└── systems/
    ├── greeting_types.json
    ├── personality_archetypes.json
    └── reaction_triggers.json
```

---

## 🎭 NPC PERSONALITY ARCHETYPES

### 1. THE MERCHANT (barrelman, shoewoman, foodboys)
**Structure:**
- Greeting (pitch)
- Shop menu
- Haggle attempt
- Purchase success
- Purchase fail (too expensive)
- Rumor/hint
- Farewell

**Template:**
```json
{
  "npc_id": "barrelman_wood_dustbelt",
  "name": "Barrelman Bob",
  "personality": "shrewd_but_friendly",
  "dialog": {
    "greeting": [
      "Need storage? I got barrels for every occasion!",
      "You look like someone with things to hide. I mean, store!",
      "Barrelman Bob's the name, containment's my game!"
    ],
    "shop_open": "What size you need? Small, medium, or 'hide-a-body' large? ...Kidding!",
    "haggle": [
      "These prices are already scraping the barrel! Get it?",
      "Tell you what - buy two, I'll throw in a lid."
    ],
    "purchase_success": [
      "Pleasure doing business! Need rope to tie it down?",
      "That one's waterproof, fireproof, and mostly gnaw-proof!"
    ],
    "purchase_fail": [
      "Money's tight, huh? Come back when the barrels are flowing!",
      "Can't do credit. Learned that lesson the hard way."
    ],
    "rumor": "Heard there's a barrel in the Mire that walks around at night. My cousin swears it!",
    "farewell": "Roll on back anytime! ...Barrel joke. Sorry."
  }
}
```

---

### 2. THE ENTERTAINER (snakecharmer, lucha, coolcat)
**Structure:**
- Performance intro
- Crowd work
- Show climax
- Tips request
- Behind the scenes (quieter moment)
- Backstory hint

**Template:**
```json
{
  "npc_id": "snakecharmer_mire",
  "name": "Sssilas the Serpent Speaker",
  "personality": "dramatic_mysterious",
  "dialog": {
    "performance_start": [
      "BEHOLD! The dance of the deadly cobra!",
      "Ladies and gentlemen, prepare to be CHARMED!"
    ],
    "crowd_work": "You there! Yes, you with the nervous face! Don't worry - he only bites volunteers!",
    "show_climax": "And now... the cobra rises! Mesmerized by the ancient melody!",
    "tips_request": "If the performance pleased you... the hat accepts all denominations!",
    "quiet_moment": "Honestly? The cobra's name is Mr. Whiskers. He's harmless. Don't tell anyone.",
    "backstory_hint": "I didn't choose the snake life. The snake life chose me. Then I chose the flute.",
    "party_reaction_trigger": "snake_performance"
  }
}
```

---

### 3. THE GUARDIAN (sumo, trenchcoat_security)
**Structure:**
- Challenge/block
- Warning
- Recognition (if reputation high)
- Advice/warning
- Let pass
- Combat bark (if attacked)

**Template:**
```json
{
  "npc_id": "sumo_white_prism",
  "name": "Guardian Hashimoto",
  "personality": "stoic_wise",
  "dialog": {
    "challenge": [
      "Halt. The crystals must not be disturbed.",
      "You may not pass... yet. State your purpose."
    ],
    "warning": "Beyond lies danger. Many have entered. Few have returned... centered.",
    "recognition_high_rep": "Ah, the Crystal Champions. The chamber awaits your wisdom.",
    "advice": "In the cave of echoes, silence is your loudest weapon.",
    "let_pass": "You may enter. Remember: the crystal reflects what you bring to it.",
    "combat_bark": "You mistake my stillness for weakness! HI-YAH!"
  }
}
```

---

### 4. THE MYSTERIOUS (trenchcoat, bush, twins)
**Structure:**
- Cryptic greeting
- Riddle/hint
- Refusal to elaborate
- Secret knowledge (quest trigger)
- Ominous warning
- Disappearance

**Template:**
```json
{
  "npc_id": "bush_uplands",
  "name": "The Wandering Shrub",
  "personality": "enigmatic_playful",
  "dialog": {
    "greeting": [
      "Have you seen my... oh, never mind. It's not important. Or is it?",
      "A traveler! How... ordinary. Or are you?"
    ],
    "cryptic_hint": "The stone that grows knows the way. But does the way know you?",
    "refusal": "Some truths must be... leafed... to be believed. Ha! Leafed!",
    "secret_quest": "Find the three seeds. Plant them where stone weeps. Then we'll talk.",
    "ominous": "Beware the one who wears no shadow. They walk among us.",
    "farewell": "I'll be here. Or there. Bushes are everywhere, you know.",
    "if_exposed": "You saw through my disguise?! ...Fine. I'm actually a druid. Happy?"
  }
}
```

---

### 5. THE WORKER (tunneler, ironchef, barrelgob)
**Structure:**
- Work complaint
- Professional pride
- Tool/technique explanation
- Break time chat
- Union/labor concerns
- Retirement dreams

**Template:**
```json
{
  "npc_id": "tunneler_brown_dustbelt",
  "name": "Deep-Dig Dan",
  "personality": "gruff_proud",
  "dialog": {
    "work_complaint": [
      "Back's killing me. Shoulda been a banker.",
      "Dust in places dust shouldn't be, if you catch my drift."
    ],
    "professional_pride": "See that seam? Twenty years tells me that's grade-A ore. Can smell it.",
    "technique": "The trick is the angle. Too steep, you get cave-in. Too shallow, you get nowhere.",
    "break_chat": "Lunch break's sacred. Don't talk to me till I've had my sandwich.",
    "labor_concerns": "Management wants us deeper. Union says it's not safe. Guess who's winning?",
    "retirement": "Two more years. Gonna buy a boat. Something that FLOATS. Above ground.",
    "quest_hook": "Heard tell of a vein that glows. Down deep. Too deep. But maybe for you..."
  }
}
```

---

### 6. THE INNKEEPER (pigman variants)
**Structure:**
- Welcome
- Room/food offer
- Local gossip
- Rumor about other zones
- Regular customer mention
- Advice for travelers
- Sleep well wish

**Template:**
```json
{
  "npc_id": "pigman_pink_aetherreach",
  "name": "Hamilton Hogsworth",
  "personality": "jovial_gossipy",
  "dialog": {
    "welcome": [
      "Welcome to The Sky-High Snout! Best pork above the clouds!",
      "Room for rent, food for coin, ears for gossip!"
    ],
    "room_offer": "Got a cloud-view room with your name on it. Assuming your name's 'Guest'!",
    "food_offer": "Special today: Cloud-Caught Thunderbird Stew! ...It's chicken. But fancy!",
    "local_gossip": "See that aeronaut at the bar? Claims he touched the edge of the world once.",
    "zone_rumor": "Word from the Mire says the boardwalk's sinking. Again. Third time this year.",
    "regular_mention": "Your friend was just here! The serious one. Left something for you, maybe?",
    "travel_advice": "Heading to Frost? Pack layers. The cold bites harder than my ex-wife!",
    "sleep_well": "Sweet dreams! If you hear balloon noises, that's normal. Probably."
  }
}
```

---

## 💬 PARTY REACTION TEMPLATES

### Kade (Protagonist) - Curious, Good-Natured

```json
{
  "character": "Kade",
  "reaction_types": {
    "quirky_npc_first_meet": [
      "That's... certainly a look.",
      "Okay, I HAVE to know the story here.",
      "This world never stops surprising me."
    ],
    "merchant_haggle": [
      "Can you do any better? We're saving the world on a budget.",
      "How about a discount for heroes? No? Worth a shot."
    ],
    "weird_creature": [
      "Please don't eat me. Please don't eat me.",
      "Twist would know what this is. Where's Twist when you need him?"
    ],
    "sad_npc": [
      "Hey, things will get better. We're working on it.",
      "Wish I could help more... but I'll do what I can."
    ],
    "confusing_npc": [
      "I... have no idea what just happened.",
      "Did that make sense to anyone else?",
      "Nix, you trackin' this? 'Cause I sure ain't."
    ],
    "snakecharmer": [
      "That snake looks... surprisingly well-behaved?",
      "I could never do that. I'd panic and drop the flute."
    ],
    "lucha": [
      "Oh man, I loved watching the fights back home!",
      "Think they'd let me in the ring? ...No? Probably wise."
    ],
    "trenchcoat": [
      "Why do I feel like they know more than they're saying?",
      "Classic mysterious stranger. Bet they have a tragic backstory."
    ]
  }
}
```

---

### Nix-7 (Android) - Literal, Analytical, Deadpan

```json
{
  "character": "Nix-7",
  "reaction_types": {
    "quirky_npc_first_meet": [
      "Scanning... no threat detected. Also, no logical explanation detected.",
      "Human behavior continues to defy algorithmic prediction.",
      "Is this 'humor'? My database is unclear."
    ],
    "merchant_haggle": [
      "Your markup is 340% above material cost. Unreasonable.",
      "I have calculated the exact value. I will pay 73.2% of your asking price."
    ],
    "weird_creature": [
      "Fascinating. Lifeform does not match any database entry.",
      "Scanning... biological impossibility detected. And yet.",
      "I would like to study this creature. Dissection may be necessary."
    ],
    "confusing_npc": [
      "That statement contained 47% logical inconsistencies.",
      "Translation error detected. Or perhaps user malfunction.",
      "I will record this for later analysis. Expected analysis time: 400 years."
    ],
    "snakecharmer": [
      "The snake responds to auditory frequencies. Efficient training method.",
      "Query: Is the snake sentient? Secondary query: Is the human sentient?"
    ],
    "ironchef": [
      "Impressive thermal management of cooking implements.",
      "Requesting recipe data. My crew requires sustenance optimization."
    ],
    "trenchcoat": [
      "Concealment protocols detected. Subject is... mysterious.",
      "They are hiding something. 98.7% probability. I can smell the secrets."
    ],
    "sunandmoon": [
      "Astronomical data outdated by 300 years. Shall I provide corrections?",
      "The stars do not actually predict fate. But I will not interrupt their belief."
    ]
  }
}
```

---

### Twist (The Muscle) - Enthusiastic, Simple, Heart of Gold

```json
{
  "character": "Twist",
  "reaction_types": {
    "quirky_npc_first_meet": [
      "WHOA! Look at THAT! Can I touch it?",
      "You're the weirdest thing I've seen today! And that's saying something!",
      "I like your style! Weird but confident!"
    ],
    "merchant_haggle": [
      "Kade's got the money. I'm just here to look scary!",
      "How about I give you a hug instead? Hugs are priceless!"
    ],
    "weird_creature": [
      "AWWW IT'S SO UGLY! I LOVE IT!",
      "Can we keep it? Please? I'll feed it and walk it!",
      "What IS that?! I wanna wrestle it!"
    ],
    "lucha": [
      "OH MAN OH MAN OH MAN! Can we wrestle?! PLEASE?!",
      "I could take you! No offense! I just love wrestling!",
      "Best wrestler I ever saw was a guy named 'The Octopus.' Had eight arms!"
    ],
    "sumo": [
      "WHOA! You're BIG! Can you teach me to be big like you?!",
      "Let's have a pushing contest! I bet I can move you! ...Maybe!"
    ],
    "foodboys": [
      "FOOD?! WHERE?! I'm starving!",
      "I'll take three of everything! I'm a growing boy!",
      "Is this protein? I need protein! For the muscles!"
    ],
    "trenchcoat": [
      "Why are you hiding in that coat? Are you cold?",
      "You look mysterious! Are you a spy? Can I be a spy too?!"
    ],
    "snakecharmer": [
      "Can I pet the snake? Please? I promise I'm gentle!",
      "The snake likes you! That means you're good people!"
    ]
  }
}
```

---

## 🗣️ AMBIENT BARK SYSTEM

### Walking Past NPCs (Random chance)

```json
{
  "bark_triggers": {
    "zone_entry": [
      "First time in {zone}: 'Fresh meat!' / 'New face!' / 'Stranger danger!'",
      "Repeat visit: 'Back again?' / 'Couldn't stay away?' / 'The regular returns!'"
    ],
    "time_of_day": {
      "morning": "'Early bird!' / 'Sun's barely up!' / 'Crack of dawn!'",
      "evening": "'Night crawler!' / 'Burning the midnight oil?' / 'Past your bedtime!'",
      "storm": "'Weathering the storm?' / 'Came out in THIS?' / 'Seeking shelter?'"
    },
    "party_composition": {
      "with_korr": "'Nice dog!' / 'Does he bite?' / 'Big pup!'",
      "with_renn": "'Watch the mage!' / 'Magic user detected!' / 'Keep your spells to yourself!'",
      "low_health": "'You look terrible!' / 'Need a healer?' / 'Rough day?'",
      "high_level": "'The legends arrive!' / 'It's really them!' / 'We're not worthy!'"
    }
  }
}
```

---

## 📋 DIALOG PRODUCTION CHECKLIST

### Per NPC Minimum Requirements:
- [ ] 3-5 greeting variants
- [ ] 1 shop/service interaction (if applicable)
- [ ] 2-3 environmental reactions
- [ ] 1 quest hook or rumor
- [ ] 1 party reaction trigger
- [ ] 2 farewell variants

### Per Zone Minimum:
- [ ] 20+ NPCs with full dialog
- [ ] 5+ party reaction sets
- [ ] 10+ ambient barks
- [ ] 3+ interconnected NPC stories

### Per Party Member:
- [ ] Reactions to all 24 quirky NPC types
- [ ] Zone entry commentary
- [ ] NPC-specific callbacks

---

## 🎯 EXAMPLE: DUSTBELT NPC WEB

### Story Connection Example:
**tunneler_brown** mentions a "weird barrel" → 
**barrelgob_green** IS that barrel → 
**barrelman_wood** wants his stolen barrel back → 
**Party** resolves this → 
All three have new post-quest dialog

### Cross-Zone References:
- **Dustbelt tunneler** mentions brother in **Obsidian**
- **Mire snakecharmer** learned from master in **Uplands**
- **Ember lucha** wants to fight **Frost** champion

---

*Production Goal: 1,500+ lines of dialog for living world*
