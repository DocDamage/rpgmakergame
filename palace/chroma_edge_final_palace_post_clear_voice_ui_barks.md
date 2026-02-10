# Chroma's Edge - Final Palace Post-Clear Voice and UI Barks (v1)
## Trigger: First and repeat returns after `FINAL_PALACE_F5_CLEARED = TRUE`

---

## 1) System Announcer (Sanctum Layer)

### First Arrival to Post-Clear Sanctum

```text
[SANCTUM SYSTEM] "FINAL CLEAR STATE VERIFIED."
[SANCTUM SYSTEM] "PROGENITOR CORE: QUIESCENT."
[SANCTUM SYSTEM] "RETURN ROUTES AUTHORIZED."
```

### Subsequent Returns

```text
[SANCTUM SYSTEM] "SANCTUM STATUS: STABLE."
```

---

## 2) Party-Adjacent Hub Barks (Short Rotation)

### Core Rotation (Any Return)

```text
[ALLY] "No alarms. No countdown. Feels wrong and right at the same time."
[ALLY] "This place finally sounds like stone again."
[ALLY] "We can leave now. We can also stay and finish what we missed."
```

### Conditional: Epilogue Not Watched

```text
[ALLY] "The ending is waiting. We don't have to force it."
```

### Conditional: Vaults Not Fully Cleared

```text
[ALLY] "Three seams still want answers. The Confluence can route us."
```

---

## 3) Sanctum Attendant / Keeper Lines

### First Return

```text
[KEEPER] "The Engine is silent. Your record is not."
```

### Rotation

```text
[KEEPER] "You may claim your rewards now, or return later."
[KEEPER] "A clean victory still leaves unfinished routes."
[KEEPER] "Nothing here decays. Choices don't either."
```

---

## 4) Reward Console UI Prompts

### Header

```text
POST-CLEAR SANCTUM
```

### Options

| Option | Function |
|--------|----------|
| `Claim Final Rewards` | Reward package and clear stamps |
| `Return to Eclipse Confluence` | Overworld/endgame hub route |
| `Return to Tower Lobby` | Tower routing and post-clear loop |
| `Delay Ending` | Leaves epilogue available without triggering |

### Confirm Modal: Return

```text
Return to selected route?
You can revisit this sanctum later.

[CONFIRM] [CANCEL]
```

---

## 5) Transition Barks

### Return to Eclipse Confluence

```text
[SANCTUM SYSTEM] "CONFLUENCE VECTOR LOCKED."
```

### Return to Tower Lobby

```text
[SANCTUM SYSTEM] "ASCENSION LOBBY VECTOR LOCKED."
```

### Delay Ending Selected

```text
[SANCTUM SYSTEM] "EPILOGUE REMAINS AVAILABLE."
```

---

## 6) Flag Dependencies

| Line / Prompt | Required Flag |
|---------------|---------------|
| All post-clear system lines | `FINAL_PALACE_F5_CLEARED = TRUE` |
| Epilogue reminder bark | `EPILOGUE_WATCHED = FALSE` |
| Unfinished seams bark | Any of `VAULT_QUIET_GLASS_CLEARED`, `VAULT_BONEWEIGHT_CLEARED`, `VAULT_DEEP_SALT_CLEARED` is FALSE |
| Tower return option | `D8_CLEARED = TRUE` |
| Confluence return option | `ECLIPSE_CONFLUENCE_DISCOVERED = TRUE` |

---

## 7) Budget and Priority Rules

| Priority | Type | Notes |
|----------|------|-------|
| **HIGH** | Route confirmation/system barks | Must not be interrupted |
| **MEDIUM** | Keeper lines | Can interrupt LOW |
| **LOW** | Ambient ally barks | Cooldown 20-30s, max 3 per sanctum visit |

Anti-overlap rules:
- Do not play ambient ally bark during reward claim animation.
- Do not overlap route confirmation with epilogue prompt.
