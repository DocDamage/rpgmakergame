#!/usr/bin/env python3
"""Normalize content/quests authoring files into canonical assets/data IDs.

Outputs:
- assets/data/quests/quest_content_main_normalized.json
- assets/data/quests/quest_content_mini_normalized.json
- assets/data/items/item_content_story_generated.json
- assets/data/system/content_id_aliases_generated.json
- docs/reports/content_id_normalization_pass_2026-02-10.md
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


ZONE_DEFAULT_MAP: dict[str, str] = {
    "dustbelt": "T_DUSTHAVEN_112x72",
    "uplands": "T_ASHVEIL_112x72",
    "mire": "T_MIREWATCH_112x72",
    "prism": "T_PRISMRIDGE_112x72",
    "ember": "T_CINDERSTEP_112x72",
    "tide": "T_BRINEGATE_112x72",
    "obsidian": "T_GRAVEMARK_112x72",
    "frost": "T_RIMEHOLD_112x72",
    "chrono": "T_CHRONOWAKE_112x72",
    "capital": "T_CROWN_HUB_112x72",
    "void": "D8_VOID_112x96",
    "tower": "TWR_LOBBY_96x64",
    "palace": "D_PALACE_128x96",
    "aetherreach": "T_AETHERREACH_112x72",
    "remnant": "RV_GATEHOUSE_96x72",
}


ZONE_DEFAULT_NPC: dict[str, str] = {
    "dustbelt": "NPC_BROKER_VANE",
    "uplands": "NPC_MIRA_THORN",
    "mire": "NPC_SISTER_AMARA",
    "prism": "NPC_OLD_KELL",
    "ember": "NPC_FORGE_MASTER_GRIMJAW",
    "tide": "NPC_DOCKMASTER_SARAI",
    "obsidian": "NPC_FORGE_MASTER_GRIMJAW",
    "frost": "NPC_ARCHIVIST_VELM",
    "chrono": "NPC_TERMINAL_OPERATOR",
    "capital": "NPC_RESISTANCE_CONTACT",
    "void": "NPC_RESISTANCE_CONTACT",
    "tower": "NPC_SEAM_WARDEN",
    "palace": "NPC_SEAM_WARDEN",
    "aetherreach": "NPC_SEAM_WARDEN",
    "remnant": "NPC_SEAM_WARDEN",
}


ZONE_DEFAULT_PREREQ_QUEST: dict[str, str] = {
    # Mid-game zones open after act 1 relic arc.
    "ember": "Q_FOURTH_RELIC",
    "tide": "Q_FOURTH_RELIC",
    "obsidian": "Q_FOURTH_RELIC",
    "frost": "Q_FOURTH_RELIC",
    # Late-game zones open with world-breach progression.
    "chrono": "Q_WORLD_BREACHED",
    "capital": "Q_WORLD_BREACHED",
    "void": "Q_WORLD_BREACHED",
    "tower": "Q_WORLD_BREACHED",
    "palace": "Q_WORLD_BREACHED",
    # Post-game-only zones.
    "aetherreach": "Q_EPILOGUE",
    "remnant": "Q_EPILOGUE",
}


DIALOG_TREE_TO_NPC: dict[str, str] = {
    "DT_AMBIENT_BROKER": "NPC_BROKER_VANE",
    "DT_AMBIENT_BOUNTY_CLERK": "NPC_CAPTAIN_VARROS",
    "DT_AMBIENT_CARAVANER": "NPC_DOCKMASTER_SARAI",
    "DT_AMBIENT_COURIER": "NPC_CAPTAIN_VARROS",
    "DT_AMBIENT_GUARD_CAPTAIN": "NPC_CAPTAIN_VARROS",
    "DT_AMBIENT_INNKEEPER": "NPC_MIRA_THORN",
    "DT_AMBIENT_MECHANIC": "NPC_FORGE_MASTER_GRIMJAW",
    "DT_AMBIENT_PRIESTESS": "NPC_SISTER_AMARA",
    "DT_AMBIENT_RESISTANCE_SCOUT": "NPC_RESISTANCE_CONTACT",
    "DT_AMBIENT_SAILOR": "NPC_DOCKMASTER_SARAI",
    "DT_AMBIENT_SCHOLAR": "NPC_ARCHIVIST_VELM",
    "DT_AMBIENT_SCHOLAR_ELDER": "NPC_OLD_KELL",
    "DT_AMBIENT_SCAVENGER": "NPC_BROKER_VANE",
    "DT_AMBIENT_SMITH": "NPC_BLACKSMITH_KELLEN",
    "DT_AMBIENT_STREET_PROPHET": "NPC_RESISTANCE_CONTACT",
    "DT_AMBIENT_TRACKER": "NPC_RAIL_CAPTAIN_DORSA",
    "DT_DOMINION_OFFICIAL_MAIN": "NPC_DOMINION_OFFICIAL",
    "DT_FALLBACK_MISC": "NPC_RESISTANCE_CONTACT",
}


NPC_HEURISTIC_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"(smith|forge|ironchef|tunneler|mechanic|quarry|gear)", re.I), "NPC_FORGE_MASTER_GRIMJAW"),
    (re.compile(r"(dock|sail|tide|brine|harbor|pirate|captain)", re.I), "NPC_DOCKMASTER_SARAI"),
    (re.compile(r"(scholar|scribe|priest|oracle|sunandmoon|twins|prophet)", re.I), "NPC_ARCHIVIST_VELM"),
    (re.compile(r"(resistance|spy|trenchcoat|dominion|warden)", re.I), "NPC_RESISTANCE_CONTACT"),
    (re.compile(r"(inn|healer|rest)", re.I), "NPC_MIRA_THORN"),
    (re.compile(r"(merchant|broker|barrel|pigman|coolcat|foodboys|signguy|lucha|sumo|bush)", re.I), "NPC_BROKER_VANE"),
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def slug(token: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9]+", "_", token.strip())
    clean = re.sub(r"_+", "_", clean).strip("_")
    return clean.upper() if clean else "UNKNOWN"


def title_from_token(token: str) -> str:
    t = re.sub(r"[_\-]+", " ", token.strip())
    t = re.sub(r"\s+", " ", t).strip()
    return t.title() if t else "Unknown Story Token"


def infer_objective(text: str) -> str:
    t = (text or "").lower()
    if any(x in t for x in ["defeat", "kill", "battle", "fight"]):
        return "defeat"
    if any(x in t for x in ["talk", "speak", "ask", "report", "return to"]):
        return "talk"
    if any(x in t for x in ["travel", "journey", "reach", "go to", "arrive", "escort"]):
        return "travel"
    if any(x in t for x in ["collect", "recover", "find", "search", "bring", "gather", "acquire"]):
        return "collect"
    if any(x in t for x in ["solve", "riddle", "puzzle"]):
        return "solve_puzzle"
    return "story_event"


def normalize_act(value: Any) -> Any:
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        if value.lower() == "post_game":
            return "post_game"
        if value.isdigit():
            return int(value)
    return value


def main() -> None:
    main_files = sorted((ROOT / "content/quests/main").glob("quest_*.json"))
    mini_files = sorted((ROOT / "content/quests/mini").rglob("*.json"))

    # Canonical runtime IDs.
    map_ids: set[str] = set()
    for mp in sorted((ROOT / "assets/data/maps").glob("*.json")):
        data = load_json(mp)
        if isinstance(data.get("maps"), list):
            for rec in data["maps"]:
                if isinstance(rec, dict) and isinstance(rec.get("id"), str):
                    map_ids.add(rec["id"])
        elif isinstance(data.get("id"), str):
            map_ids.add(data["id"])

    npc_ids: set[str] = set()
    for np in sorted((ROOT / "assets/data/npcs").glob("*.json")):
        data = load_json(np)
        nid = data.get("id")
        if isinstance(nid, str):
            npc_ids.add(nid)

    item_ids: set[str] = set()
    for ip in sorted((ROOT / "assets/data/items").glob("*.json")):
        # Skip normalization output to keep generated story item IDs deterministic
        # across reruns of this tool.
        if ip.name == "item_content_story_generated.json":
            continue
        data = load_json(ip)
        for rec in data.get("items", []):
            if isinstance(rec, dict) and isinstance(rec.get("id"), str):
                item_ids.add(rec["id"])

    alias_registry = load_json(ROOT / "content/dialog/story_npc_alias_registry.json")
    story_npc_aliases: dict[str, dict[str, Any]] = {}
    for rec in alias_registry.get("aliases", []):
        if not isinstance(rec, dict):
            continue
        token = rec.get("story_npc")
        if isinstance(token, str) and token:
            story_npc_aliases[token.lower()] = rec

    # Build quest id maps first so prerequisite/unlock mapping is deterministic.
    main_src_to_norm: dict[str, str] = {}
    mini_src_to_norm: dict[str, str] = {}
    for p in main_files:
        d = load_json(p)
        qid = d.get("quest_id", p.stem)
        main_src_to_norm[qid] = f"Q_CONTENT_MAIN_{slug(qid)}"
    for p in mini_files:
        d = load_json(p)
        qid = d.get("quest_id", p.stem)
        mini_src_to_norm[qid] = f"Q_CONTENT_MINI_{slug(qid)}"

    quest_lookup: dict[str, str] = {}
    for src, dst in {**main_src_to_norm, **mini_src_to_norm}.items():
        quest_lookup[src] = dst
        quest_lookup[f"quest_{src}"] = dst

    # Story item map with collision-safe id assignment.
    story_item_token_to_id: dict[str, str] = {}
    story_item_id_to_token: dict[str, str] = {}

    def map_item(token: str) -> str:
        if token in item_ids:
            return token
        if token in story_item_token_to_id:
            return story_item_token_to_id[token]

        base = f"ITEM_STORY_{slug(token)}"
        candidate = base
        i = 2
        while candidate in item_ids or (
            candidate in story_item_id_to_token and story_item_id_to_token[candidate] != token
        ):
            candidate = f"{base}_{i}"
            i += 1

        story_item_token_to_id[token] = candidate
        story_item_id_to_token[candidate] = token
        return candidate

    resolved_npc_aliases: dict[str, str] = {}

    def resolve_npc(token: str | None, zone: str | None) -> str | None:
        if not token:
            return None
        t = token.strip()
        if t in npc_ids:
            return t
        upper = t.upper()
        if upper in npc_ids:
            return upper
        lower = t.lower()

        if lower in resolved_npc_aliases:
            return resolved_npc_aliases[lower]

        # Story alias registry has strongest signal.
        reg = story_npc_aliases.get(lower)
        if reg is not None:
            dt = reg.get("fallback_dialog_tree")
            if isinstance(dt, str) and dt in DIALOG_TREE_TO_NPC:
                resolved = DIALOG_TREE_TO_NPC[dt]
                resolved_npc_aliases[lower] = resolved
                return resolved

        # Heuristic fallback.
        for pattern, npc_id in NPC_HEURISTIC_RULES:
            if pattern.search(t):
                resolved_npc_aliases[lower] = npc_id
                return npc_id

        zone_key = (zone or "").lower()
        resolved = ZONE_DEFAULT_NPC.get(zone_key, "NPC_RESISTANCE_CONTACT")
        resolved_npc_aliases[lower] = resolved
        return resolved

    def map_quest_token(token: str) -> str:
        return quest_lookup.get(token, token)

    def split_quest_refs(tokens: Any) -> tuple[list[str], list[str]]:
        quest_refs: list[str] = []
        state_flags: list[str] = []
        if not isinstance(tokens, list):
            return quest_refs, state_flags

        for token in tokens:
            if not isinstance(token, str) or not token:
                continue
            mapped = map_quest_token(token)
            if mapped.startswith("Q_CONTENT_MAIN_") or mapped.startswith("Q_CONTENT_MINI_"):
                quest_refs.append(mapped)
            else:
                state_flags.append(token)
        return quest_refs, state_flags

    def location_for_zone(zone: str | None) -> str:
        z = (zone or "").lower()
        fallback = ZONE_DEFAULT_MAP.get(z, "T_DUSTHAVEN_112x72")
        return fallback if fallback in map_ids else "T_DUSTHAVEN_112x72"

    normalized_main: list[dict[str, Any]] = []
    normalized_mini: list[dict[str, Any]] = []

    # MAIN QUESTS
    for p in main_files:
        d = load_json(p)
        src_id = d.get("quest_id", p.stem)
        zone = d.get("zone", "")
        stages = d.get("stages", [])
        steps: list[dict[str, Any]] = []

        for idx, st in enumerate(stages, start=1):
            if not isinstance(st, dict):
                continue

            st_id = st.get("stage", idx)
            desc = st.get("description", "")
            objectives = st.get("objectives", [])
            obj_text = objectives[0] if isinstance(objectives, list) and objectives else desc
            loc = st.get("target_location_id")
            if not isinstance(loc, str) or loc not in map_ids:
                loc = location_for_zone(zone)

            step: dict[str, Any] = {
                "id": st_id,
                "name": st.get("name", f"Stage {idx}"),
                "description": desc,
                "objective": infer_objective(obj_text),
                "target_location": loc,
                "objectives": objectives if isinstance(objectives, list) else [],
                "dialog_start": st.get("dialog_start", ""),
                "dialog_complete": st.get("dialog_complete", ""),
            }

            npc_alias = st.get("npc")
            if isinstance(npc_alias, str) and npc_alias:
                step["target_npc"] = resolve_npc(npc_alias, str(zone))
                step["story_npc_alias"] = npc_alias

            rewards = st.get("rewards")
            if isinstance(rewards, dict):
                step_rewards: dict[str, Any] = {}
                if isinstance(rewards.get("exp"), int):
                    step_rewards["xp"] = rewards["exp"]
                if isinstance(rewards.get("gold"), int):
                    step_rewards["gil"] = rewards["gold"]
                item_token = rewards.get("item")
                if isinstance(item_token, str) and item_token:
                    step_rewards["items"] = [
                        {
                            "item": map_item(item_token),
                            "count": 1,
                            "source_item_token": item_token,
                        }
                    ]
                unlock_token = rewards.get("unlock")
                if isinstance(unlock_token, str) and unlock_token:
                    mapped_unlock = map_quest_token(unlock_token)
                    if mapped_unlock.startswith("Q_CONTENT_MAIN_") or mapped_unlock.startswith("Q_CONTENT_MINI_"):
                        step_rewards["unlocks"] = [mapped_unlock]
                    else:
                        step_rewards["unlock_flags"] = [unlock_token]
                if step_rewards:
                    step["rewards"] = step_rewards

            steps.append(step)

        quest_rewards: dict[str, Any] = {}
        if steps:
            last = steps[-1]
            if isinstance(last.get("rewards"), dict):
                # Strip source metadata at quest summary level.
                lr = dict(last["rewards"])
                if "items" in lr and isinstance(lr["items"], list):
                    clean_items = []
                    for it in lr["items"]:
                        if isinstance(it, dict):
                            clean_items.append(
                                {
                                    "item": it.get("item"),
                                    "count": int(it.get("count", 1)),
                                }
                            )
                    lr["items"] = clean_items
                quest_rewards = lr

        prereq_quests, prereq_flags = split_quest_refs(d.get("prerequisites", []))
        unlock_quests, unlock_flags = split_quest_refs(d.get("unlocks", []))

        normalized_main.append(
            {
                "id": main_src_to_norm[src_id],
                "source_quest_id": src_id,
                "name": d.get("name", src_id),
                "type": "main",
                "zone": zone,
                "act": normalize_act(d.get("act")),
                "prerequisites": prereq_quests,
                "prerequisite_flags": prereq_flags,
                "description": d.get("story_beats", [d.get("name", "")])[0]
                if isinstance(d.get("story_beats"), list)
                else d.get("name", ""),
                "steps": steps,
                "rewards": quest_rewards,
                "unlocks": unlock_quests,
                "unlock_flags": unlock_flags,
                "story_beats": d.get("story_beats", []),
                "party_reactions": d.get("party_reactions", {}),
            }
        )

    # MINI QUESTS
    mini_stage_order = ["start", "progress", "complete"]
    for p in mini_files:
        d = load_json(p)
        src_id = d.get("quest_id", p.stem)
        zone = str(d.get("zone", "")).lower()
        giver_alias = d.get("giver", "")
        giver_id = resolve_npc(giver_alias if isinstance(giver_alias, str) else None, zone)
        quest_steps: list[dict[str, Any]] = []

        stages = d.get("stages", {})
        for idx, key in enumerate(mini_stage_order, start=1):
            sv = stages.get(key) if isinstance(stages, dict) else None
            if not isinstance(sv, dict):
                continue
            objective_text = sv.get("objective", "")
            dialog_text = sv.get("dialog", "")
            merged = " ".join(x for x in [objective_text, dialog_text] if isinstance(x, str))

            step: dict[str, Any] = {
                "id": idx,
                "name": key.title(),
                "description": objective_text if isinstance(objective_text, str) and objective_text else dialog_text,
                "objective": infer_objective(merged),
                "target_location": location_for_zone(zone),
                "dialog": dialog_text if isinstance(dialog_text, str) else "",
            }
            if key in {"start", "complete"} and giver_id:
                step["target_npc"] = giver_id
                step["story_npc_alias"] = giver_alias

            rewards = sv.get("rewards")
            if isinstance(rewards, dict):
                step_rewards: dict[str, Any] = {}
                if isinstance(rewards.get("exp"), int):
                    step_rewards["xp"] = rewards["exp"]
                if isinstance(rewards.get("gold"), int):
                    step_rewards["gil"] = rewards["gold"]
                item_token = rewards.get("item")
                if isinstance(item_token, str) and item_token:
                    step_rewards["items"] = [
                        {
                            "item": map_item(item_token),
                            "count": 1,
                            "source_item_token": item_token,
                        }
                    ]
                if isinstance(rewards.get("reputation"), int):
                    step_rewards["reputation"] = rewards["reputation"]
                if step_rewards:
                    step["rewards"] = step_rewards

            quest_steps.append(step)

        quest_rewards: dict[str, Any] = {}
        if quest_steps and isinstance(quest_steps[-1].get("rewards"), dict):
            lr = dict(quest_steps[-1]["rewards"])
            if "items" in lr and isinstance(lr["items"], list):
                clean_items = []
                for it in lr["items"]:
                    if isinstance(it, dict):
                        clean_items.append({"item": it.get("item"), "count": int(it.get("count", 1))})
                lr["items"] = clean_items
            quest_rewards = lr

        prereq_quests, prereq_flags = split_quest_refs(d.get("prerequisites", []))
        unlock_quests, unlock_flags = split_quest_refs(d.get("unlocks", []))
        if not prereq_quests and not prereq_flags:
            auto_gate = ZONE_DEFAULT_PREREQ_QUEST.get(zone)
            if isinstance(auto_gate, str) and auto_gate:
                prereq_quests = [auto_gate]

        normalized_mini.append(
            {
                "id": mini_src_to_norm[src_id],
                "source_quest_id": src_id,
                "name": d.get("name", src_id),
                "type": d.get("type", "side"),
                "zone": zone,
                "giver": giver_id,
                "giver_alias": giver_alias,
                "prerequisites": prereq_quests,
                "prerequisite_flags": prereq_flags,
                "description": d.get("stages", {}).get("start", {}).get("objective", d.get("name", ""))
                if isinstance(d.get("stages"), dict)
                else d.get("name", ""),
                "steps": quest_steps,
                "rewards": quest_rewards,
                "unlocks": unlock_quests,
                "unlock_flags": unlock_flags,
                "party_comments": d.get("party_comments", {}),
                "hidden_outcome": d.get("hidden_outcome", ""),
            }
        )

    normalized_main.sort(key=lambda q: q["id"])
    normalized_mini.sort(key=lambda q: q["id"])

    # Emit normalized quest packs.
    dump_json(
        ROOT / "assets/data/quests/quest_content_main_normalized.json",
        {"id": "Q_CONTENT_MAIN_NORMALIZED", "quests": normalized_main},
    )
    dump_json(
        ROOT / "assets/data/quests/quest_content_mini_normalized.json",
        {"id": "Q_CONTENT_MINI_NORMALIZED", "quests": normalized_mini},
    )

    # Emit generated story reward items for previously unknown tokens.
    generated_items: list[dict[str, Any]] = []
    for item_id, src_token in sorted(story_item_id_to_token.items()):
        generated_items.append(
            {
                "id": item_id,
                "name": title_from_token(src_token),
                "type": "key_item",
                "subtype": "story_reward",
                "rarity": 3,
                "icon": "icon_archive_key",
                "description": "Story reward token generated from authored content quest data.",
                "flavor": "Recovered from authored side or main story content.",
                "story_significance": "content_story_reward",
                "source_item_token": src_token,
                "buy_price": 0,
                "sell_price": 0,
                "usable_in": ["story"],
            }
        )

    dump_json(
        ROOT / "assets/data/items/item_content_story_generated.json",
        {"id": "ITEM_CONTENT_STORY_GENERATED", "items": generated_items},
    )

    # Emit mapping registry artifact.
    item_aliases = [
        {
            "source_token": token,
            "canonical_item_id": item_id,
            "generated": item_id.startswith("ITEM_STORY_"),
        }
        for token, item_id in sorted(story_item_token_to_id.items())
    ]
    npc_aliases = [
        {
            "source_token": token,
            "canonical_npc_id": npc_id,
            "used_story_alias_registry": token in story_npc_aliases,
        }
        for token, npc_id in sorted(resolved_npc_aliases.items())
    ]
    quest_aliases = [
        {
            "source_token": src,
            "canonical_quest_id": dst,
            "type": "main" if src in main_src_to_norm else "mini",
        }
        for src, dst in sorted({**main_src_to_norm, **mini_src_to_norm}.items())
    ]
    state_token_refs: set[str] = set()
    for q in normalized_main + normalized_mini:
        for token in q.get("prerequisite_flags", []):
            if isinstance(token, str) and token:
                state_token_refs.add(token)
        for token in q.get("unlock_flags", []):
            if isinstance(token, str) and token:
                state_token_refs.add(token)
        rewards = q.get("rewards")
        if isinstance(rewards, dict):
            for token in rewards.get("unlock_flags", []):
                if isinstance(token, str) and token:
                    state_token_refs.add(token)
        for st in q.get("steps", []):
            if not isinstance(st, dict):
                continue
            st_rewards = st.get("rewards")
            if not isinstance(st_rewards, dict):
                continue
            for token in st_rewards.get("unlock_flags", []):
                if isinstance(token, str) and token:
                    state_token_refs.add(token)

    dump_json(
        ROOT / "assets/data/system/content_id_aliases_generated.json",
        {
            "id": "CONTENT_ID_ALIASES_GENERATED",
            "summary": {
                "main_quests": len(normalized_main),
                "mini_quests": len(normalized_mini),
                "quest_aliases": len(quest_aliases),
                "npc_aliases": len(npc_aliases),
                "item_aliases": len(item_aliases),
                "generated_story_items": len(generated_items),
                "state_tokens": len(state_token_refs),
            },
            "quest_aliases": quest_aliases,
            "npc_aliases": npc_aliases,
            "item_aliases": item_aliases,
            "state_tokens": sorted(state_token_refs),
        },
    )

    # Lightweight pass report.
    report = [
        "# Content ID Normalization Pass (2026-02-10)",
        "",
        "## Summary",
        f"- Main quests normalized: **{len(normalized_main)}**",
        f"- Mini quests normalized: **{len(normalized_mini)}**",
        f"- Quest alias entries: **{len(quest_aliases)}**",
        f"- NPC alias entries: **{len(npc_aliases)}**",
        f"- Item alias entries: **{len(item_aliases)}**",
        f"- Generated story reward items: **{len(generated_items)}**",
        f"- State token references (non-quest prereq/unlock): **{len(state_token_refs)}**",
        "",
        "## Outputs",
        "- `assets/data/quests/quest_content_main_normalized.json`",
        "- `assets/data/quests/quest_content_mini_normalized.json`",
        "- `assets/data/items/item_content_story_generated.json`",
        "- `assets/data/system/content_id_aliases_generated.json`",
        "",
        "## Notes",
        "- `content/quests/*` text and structure remain untouched (authoring source).",
        "- Normalized quests use canonical IDs and runtime-compatible location/item/NPC references where possible.",
        "- `prerequisites`/`unlocks` contain quest IDs only.",
        "- Non-quest gate tokens are preserved in `prerequisite_flags`/`unlock_flags`.",
        "- Original quest/item/NPC tokens are preserved as metadata fields (`source_*`, `*_alias`).",
    ]
    report_path = ROOT / "docs/reports/content_id_normalization_pass_2026-02-10.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report) + "\n", encoding="utf-8")

    print("Normalization complete.")
    print(f"Main quests: {len(normalized_main)}")
    print(f"Mini quests: {len(normalized_mini)}")
    print(f"Generated story items: {len(generated_items)}")
    print(f"NPC aliases: {len(npc_aliases)}")


if __name__ == "__main__":
    main()
