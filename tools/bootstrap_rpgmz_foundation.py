#!/usr/bin/env python3
"""
Week 1 bootstrap for Chroma's Edge RPG Maker MZ implementation.

This script:
1) Seeds a runnable RPG Maker MZ project skeleton from a local template project.
2) Generates starter database content for Actors/Classes/Skills/System.
3) Prepares a development test map entry.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any, Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
ASSET_DATA_DIR = ROOT / "assets" / "data"
DATA_DIR = ROOT / "data"


PARTY_BLUEPRINT: List[Dict[str, str]] = [
    {
        "id": "KADE",
        "name": "Kade",
        "class_name": "Gunblade Specialist",
        "archetype": "striker",
        "profile": "A pragmatic gunblade hunter with drake-blood overdrive.",
    },
    {
        "id": "NIX7",
        "name": "Nix-7",
        "class_name": "Tactical Android",
        "archetype": "support",
        "profile": "Lattice-interface android focused on tactical control.",
    },
    {
        "id": "RENNA",
        "name": "Renna Kyte",
        "class_name": "Tech Specialist",
        "archetype": "ranger",
        "profile": "Engineer and ranged DPS who deploys drones and turrets.",
    },
    {
        "id": "TWIST",
        "name": "Twist",
        "class_name": "Rogue",
        "archetype": "rogue",
        "profile": "Fast thief with high crit pressure and utility control.",
    },
    {
        "id": "SURESH",
        "name": "Dr. Marin Suresh",
        "class_name": "Combat Healer",
        "archetype": "healer",
        "profile": "Frontline medic with strong sustain and emergency recovery.",
    },
    {
        "id": "SOVA",
        "name": "Dr. Ines Sova",
        "class_name": "Arcane Researcher",
        "archetype": "mage",
        "profile": "Element-focused caster built around analysis and spell power.",
    },
    {
        "id": "GRIT",
        "name": "Grit",
        "class_name": "Heavy Vanguard",
        "archetype": "tank",
        "profile": "Durable frontliner that anchors threat and party defense.",
    },
    {
        "id": "ASHKA",
        "name": "Ashka Verne",
        "class_name": "Frontier Sniper",
        "archetype": "ranger",
        "profile": "Precision marksman with crit spikes and battlefield control.",
    },
    {
        "id": "SENNA",
        "name": "Senna",
        "class_name": "Iron Fist Monk",
        "archetype": "striker",
        "profile": "Fast melee bruiser with combo-oriented pressure tools.",
    },
    {
        "id": "CALLUM",
        "name": "Callum Drake",
        "class_name": "Summoner",
        "archetype": "summoner",
        "profile": "Summon specialist with high MP throughput and utility.",
    },
    {
        "id": "PETRA",
        "name": "Petra",
        "class_name": "Berserker",
        "archetype": "berserker",
        "profile": "High-risk attacker with mutation-fueled burst damage.",
    },
    {
        "id": "VEX",
        "name": "Vex",
        "class_name": "Oathbroken Paladin",
        "archetype": "paladin",
        "profile": "Hybrid defender with holy offense and team protection.",
    },
    {
        "id": "KORR",
        "name": "Nadia Korr",
        "class_name": "Marshal",
        "archetype": "commander",
        "profile": "Suppression specialist with command and tactical burst.",
    },
]


ARCHETYPE_PARAM_CURVES: Dict[str, Dict[str, Tuple[int, int]]] = {
    "striker": {
        "mhp": (420, 6400),
        "mmp": (90, 900),
        "atk": (48, 470),
        "def": (36, 360),
        "mat": (26, 260),
        "mdf": (30, 300),
        "agi": (42, 410),
        "luk": (26, 240),
    },
    "support": {
        "mhp": (360, 5200),
        "mmp": (140, 1300),
        "atk": (28, 300),
        "def": (30, 320),
        "mat": (44, 420),
        "mdf": (42, 420),
        "agi": (34, 350),
        "luk": (26, 240),
    },
    "rogue": {
        "mhp": (360, 5000),
        "mmp": (80, 760),
        "atk": (42, 420),
        "def": (28, 290),
        "mat": (24, 240),
        "mdf": (28, 280),
        "agi": (52, 490),
        "luk": (34, 300),
    },
    "healer": {
        "mhp": (340, 5000),
        "mmp": (180, 1550),
        "atk": (22, 250),
        "def": (30, 320),
        "mat": (46, 450),
        "mdf": (46, 470),
        "agi": (28, 300),
        "luk": (24, 220),
    },
    "mage": {
        "mhp": (320, 4700),
        "mmp": (200, 1700),
        "atk": (20, 230),
        "def": (26, 280),
        "mat": (52, 510),
        "mdf": (42, 430),
        "agi": (30, 320),
        "luk": (24, 220),
    },
    "tank": {
        "mhp": (520, 7600),
        "mmp": (60, 700),
        "atk": (42, 430),
        "def": (50, 510),
        "mat": (20, 220),
        "mdf": (36, 370),
        "agi": (24, 260),
        "luk": (20, 200),
    },
    "ranger": {
        "mhp": (380, 5400),
        "mmp": (100, 980),
        "atk": (44, 440),
        "def": (32, 330),
        "mat": (28, 280),
        "mdf": (30, 320),
        "agi": (46, 460),
        "luk": (30, 280),
    },
    "summoner": {
        "mhp": (340, 5000),
        "mmp": (210, 1800),
        "atk": (24, 250),
        "def": (28, 300),
        "mat": (50, 500),
        "mdf": (44, 450),
        "agi": (32, 340),
        "luk": (26, 240),
    },
    "berserker": {
        "mhp": (500, 7200),
        "mmp": (70, 740),
        "atk": (54, 540),
        "def": (38, 390),
        "mat": (18, 180),
        "mdf": (24, 260),
        "agi": (34, 350),
        "luk": (28, 260),
    },
    "paladin": {
        "mhp": (480, 7000),
        "mmp": (120, 1200),
        "atk": (40, 400),
        "def": (44, 460),
        "mat": (34, 360),
        "mdf": (42, 430),
        "agi": (28, 300),
        "luk": (24, 220),
    },
    "commander": {
        "mhp": (430, 6300),
        "mmp": (90, 920),
        "atk": (46, 460),
        "def": (40, 420),
        "mat": (28, 280),
        "mdf": (34, 350),
        "agi": (38, 390),
        "luk": (28, 260),
    },
}


RENNA_FALLBACK = {
    "id": "RENNA",
    "name": "Renna Kyte",
    "role": "Tech Specialist",
    "abilities": [
        {"name": "Wrench Jab", "type": "physical", "mp": 0, "power": 1.0, "learned": 1},
        {"name": "Turret Deploy", "type": "support", "mp": 25, "effect": "turret", "learned": 1},
        {"name": "Shock Round", "type": "physical", "mp": 12, "power": 1.6, "element": "thunder", "learned": 10},
        {"name": "Overcharge", "type": "support", "mp": 30, "effect": "party_tech_up", "learned": 18},
        {"name": "Limit: Siege Ascendant", "type": "limit", "mp": 0, "power": 3.8, "learned": "limit_unlock"},
    ],
    "magic": ["Thunder", "Haste", "Protect"],
    "unique_mechanic": "drone_support",
}


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, separators=(",", ":"))


def copy_file(src: Path, dst: Path, force: bool) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and not force:
        return
    shutil.copy2(src, dst)


def copy_dir(src: Path, dst: Path, force: bool) -> None:
    if dst.exists():
        if not force:
            return
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def find_template_project(explicit: str | None) -> Path:
    candidates: List[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    env_path = Path(
        Path.home().joinpath(
            ".rpgmz_template_project"
        )  # optional hint file path for automation
    )
    if env_path.exists():
        try:
            hinted = Path(env_path.read_text(encoding="utf-8").strip())
            if hinted:
                candidates.append(hinted.expanduser())
        except OSError:
            pass

    candidates.extend(
        [
            Path.home() / "Documents" / "RMMZ" / "Project1",
            Path.home() / "Downloads" / "RPG.Maker.MZ.v1.8" / "data" / "newdata",
        ]
    )

    for candidate in candidates:
        if (
            candidate.exists()
            and (candidate / "data").is_dir()
            and (candidate / "js").is_dir()
            and (candidate / "js" / "rmmz_core.js").is_file()
        ):
            return candidate

    raise FileNotFoundError(
        "No RPG Maker MZ template project found. "
        "Pass --template-project pointing to a project containing data/ and js/."
    )


def seed_runtime(template_project: Path, force: bool) -> None:
    for filename in ("index.html", "package.json", "game.rmmzproject"):
        source = template_project / filename
        if source.exists():
            copy_file(source, ROOT / filename, force)

    for dirname in ("css", "fonts", "effects", "icon"):
        source = template_project / dirname
        if source.is_dir():
            copy_dir(source, ROOT / dirname, force)

    for filename in (
        "main.js",
        "rmmz_core.js",
        "rmmz_managers.js",
        "rmmz_objects.js",
        "rmmz_scenes.js",
        "rmmz_sprites.js",
        "rmmz_windows.js",
    ):
        copy_file(template_project / "js" / filename, ROOT / "js" / filename, force)

    copy_dir(template_project / "js" / "libs", ROOT / "js" / "libs", force)


def seed_data(template_project: Path, force: bool) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for json_file in sorted((template_project / "data").glob("*.json")):
        copy_file(json_file, DATA_DIR / json_file.name, force)


def load_character_sources() -> Dict[str, Dict[str, Any]]:
    ability_path = ASSET_DATA_DIR / "abilities" / "ability_character_abilities.json"
    payload = read_json(ability_path)
    entries: Dict[str, Dict[str, Any]] = {}

    for item in payload.get("characters", []):
        key = str(item.get("id", "")).upper()
        if key:
            entries[key] = item

    entries.setdefault("RENNA", RENNA_FALLBACK)
    return entries


def class_traits() -> List[Dict[str, Any]]:
    traits: List[Dict[str, Any]] = [
        {"code": 23, "dataId": 0, "value": 1},
        {"code": 22, "dataId": 0, "value": 1},
        {"code": 22, "dataId": 1, "value": 0.05},
        {"code": 22, "dataId": 2, "value": 0.04},
    ]
    for weapon_type_id in range(1, 17):
        traits.append({"code": 51, "dataId": weapon_type_id, "value": 0})
    for armor_type_id in range(1, 7):
        traits.append({"code": 52, "dataId": armor_type_id, "value": 0})
    return traits


def param_curve(start: int, end: int) -> List[int]:
    return [int(round(start + ((end - start) * level / 99))) for level in range(100)]


def element_id_from_name(name: str | None, default: int) -> int:
    mapping = {
        "fire": 2,
        "ice": 3,
        "thunder": 4,
        "water": 5,
        "earth": 6,
        "wind": 7,
        "light": 8,
        "dark": 9,
    }
    if not name:
        return default
    return mapping.get(name.lower(), default)


def build_generated_skills(
    skills: List[Any], character_sources: Dict[str, Dict[str, Any]]
) -> Dict[Tuple[str, str], int]:
    next_id = len(skills)
    skill_index: Dict[Tuple[str, str], int] = {}

    for blueprint in PARTY_BLUEPRINT:
        source = character_sources.get(blueprint["id"], {})
        ability_list = source.get("abilities", [])
        actor_id = blueprint["id"]

        for ability in ability_list:
            name = str(ability.get("name", "")).strip()
            if not name:
                continue

            ability_type = str(ability.get("type", "physical")).lower()
            power = float(ability.get("power", 1.0) or 1.0)
            is_heal = bool(ability.get("heal", False))
            is_limit = ability_type == "limit"
            is_magic = ability_type == "magic"
            is_support = ability_type == "support"

            if is_support:
                damage_type = 0
                hit_type = 0
                formula = "0"
                scope = 7
            elif is_heal:
                damage_type = 3
                hit_type = 0
                formula = f"a.mat * {max(power, 1.0):.2f}"
                scope = 7
            elif is_magic:
                damage_type = 2
                hit_type = 2
                formula = f"a.mat * {max(power, 1.0):.2f} - b.mdf * 0.50"
                scope = 1
            else:
                damage_type = 1
                hit_type = 1
                formula = f"a.atk * {max(power, 1.0):.2f} - b.def * 0.50"
                scope = 1

            skill = {
                "id": next_id,
                "animationId": 0 if is_support else -1,
                "damage": {
                    "critical": not is_support and not is_heal,
                    "elementId": element_id_from_name(
                        str(ability.get("element", "") or ""), -1 if not is_magic else 0
                    ),
                    "formula": formula,
                    "type": damage_type,
                    "variance": 20,
                },
                "description": str(ability.get("effect", "")) if is_support else "",
                "effects": [],
                "hitType": hit_type,
                "iconIndex": 76 if not is_support else 82,
                "message1": "%1 uses %2!",
                "message2": "",
                "mpCost": 0 if is_limit else int(ability.get("mp", 0) or 0),
                "name": name,
                "note": (
                    f"<chromaActor:{actor_id}>\n"
                    f"<chromaAbilityType:{ability_type}>\n"
                    f"<chromaGenerated:true>"
                ),
                "occasion": 1,
                "repeats": int(ability.get("hits", 1) or 1),
                "requiredWtypeId1": 0,
                "requiredWtypeId2": 0,
                "scope": 2 if bool(ability.get("hits_all", False)) else scope,
                "speed": 0,
                "stypeId": 3 if is_limit else (1 if is_magic else 2),
                "successRate": 100,
                "tpCost": 100 if is_limit else 0,
                "tpGain": 0,
                "messageType": 1,
            }
            skills.append(skill)
            skill_index[(actor_id, name)] = next_id
            next_id += 1

    return skill_index


def build_classes(
    character_sources: Dict[str, Dict[str, Any]],
    skill_index: Dict[Tuple[str, str], int],
) -> List[Any]:
    classes: List[Any] = [None]

    for idx, blueprint in enumerate(PARTY_BLUEPRINT, start=1):
        archetype = blueprint["archetype"]
        curves = ARCHETYPE_PARAM_CURVES[archetype]

        params = [
            param_curve(*curves["mhp"]),
            param_curve(*curves["mmp"]),
            param_curve(*curves["atk"]),
            param_curve(*curves["def"]),
            param_curve(*curves["mat"]),
            param_curve(*curves["mdf"]),
            param_curve(*curves["agi"]),
            param_curve(*curves["luk"]),
        ]

        source = character_sources.get(blueprint["id"], {})
        learnings: List[Dict[str, Any]] = []
        for ability in source.get("abilities", []):
            skill_name = str(ability.get("name", "")).strip()
            if not skill_name:
                continue
            skill_id = skill_index.get((blueprint["id"], skill_name))
            if not skill_id:
                continue
            learned = ability.get("learned", 1)
            level = 30 if isinstance(learned, str) else int(learned)
            learnings.append({"level": max(level, 1), "note": "", "skillId": skill_id})

        learnings.sort(key=lambda entry: (entry["level"], entry["skillId"]))
        class_obj = {
            "id": idx,
            "expParams": [30, 20, 30, 30],
            "traits": class_traits(),
            "learnings": learnings,
            "name": blueprint["class_name"],
            "note": f"<chromaClass:{blueprint['id']}>",
            "params": params,
        }
        classes.append(class_obj)

    return classes


def default_equips(archetype: str) -> List[int]:
    weapon_map = {
        "striker": 2,
        "support": 7,
        "rogue": 1,
        "healer": 7,
        "mage": 7,
        "tank": 4,
        "ranger": 8,
        "summoner": 7,
        "berserker": 5,
        "paladin": 2,
        "commander": 9,
    }
    weapon_id = weapon_map.get(archetype, 2)
    return [weapon_id, 0, 0, 3, 0]


def build_actors() -> List[Any]:
    actors: List[Any] = [None]
    for idx, blueprint in enumerate(PARTY_BLUEPRINT, start=1):
        image_slot = ((idx - 1) % 8) + 1
        actor = {
            "id": idx,
            "battlerName": f"Actor1_{image_slot}",
            "characterIndex": (idx - 1) % 8,
            "characterName": "Actor1",
            "classId": idx,
            "equips": default_equips(blueprint["archetype"]),
            "faceIndex": (idx - 1) % 8,
            "faceName": "Actor1",
            "traits": [],
            "initialLevel": 1,
            "maxLevel": 99,
            "name": blueprint["name"],
            "nickname": blueprint["class_name"],
            "note": f"<chromaActor:{blueprint['id']}>",
            "profile": blueprint["profile"],
        }
        actors.append(actor)
    return actors


def apply_system_updates(system: Dict[str, Any], actors: List[Any]) -> Dict[str, Any]:
    system["gameTitle"] = "Chroma's Edge"
    system["partyMembers"] = [1, 2, 3, 4]
    system["skillTypes"] = ["", "Magic", "Technique", "Limit"]
    system["weaponTypes"] = [
        "",
        "Dagger",
        "Sword",
        "Flail",
        "Axe",
        "Whip",
        "Staff",
        "Bow",
        "Crossbow",
        "Gun",
        "Claw",
        "Glove",
        "Spear",
        "Gunblade",
        "Rifle",
        "Fist",
        "Polearm",
    ]
    system["elements"] = [
        "",
        "Physical",
        "Fire",
        "Ice",
        "Thunder",
        "Water",
        "Earth",
        "Wind",
        "Light",
        "Darkness",
        "Growth",
        "Time",
        "Void",
    ]
    system["startMapId"] = 1
    system["startX"] = 8
    system["startY"] = 6
    system["battleBgm"] = {"name": "", "pan": 0, "pitch": 100, "volume": 90}
    system["titleBgm"] = {"name": "", "pan": 0, "pitch": 100, "volume": 90}

    switches = [""] * 101
    variables = [""] * 101
    named_switches = {
        1: "D1_CLEARED",
        2: "D2_CLEARED",
        3: "D3_CLEARED",
        4: "D4_CLEARED",
        5: "D5_CLEARED",
        6: "D6_CLEARED",
        7: "D7_CLEARED",
        8: "D8_CLEARED",
        20: "KORR_RECRUITED",
        21: "KORR_LIBERATED",
        30: "WORLD_BREAK_TRIGGERED",
        40: "TOWER_UNLOCKED",
        41: "PALACE_UNLOCKED",
        50: "ENDING_FREE_PRIME",
        51: "ENDING_ANCHOR",
    }
    named_variables = {
        1: "AFFINITY_LAST_A",
        2: "AFFINITY_LAST_B",
        3: "AFFINITY_LAST_VALUE",
        4: "AFFINITY_DEBUG_DELTA",
        10: "QUEST_ACTIVE_COUNT",
        11: "QUEST_COMPLETED_COUNT",
        20: "INTEGRITY_METER",
        21: "DAY_NIGHT_HOUR",
    }

    for idx, label in named_switches.items():
        switches[idx] = label
    for idx, label in named_variables.items():
        variables[idx] = label

    system["switches"] = switches
    system["variables"] = variables
    system["testBattlers"] = [
        {"actorId": 1, "level": 1, "equips": actors[1]["equips"]},
        {"actorId": 2, "level": 1, "equips": actors[2]["equips"]},
        {"actorId": 3, "level": 1, "equips": actors[3]["equips"]},
        {"actorId": 4, "level": 1, "equips": actors[4]["equips"]},
    ]
    return system


def patch_test_map() -> None:
    map_info_path = DATA_DIR / "MapInfos.json"
    map_001_path = DATA_DIR / "Map001.json"
    if map_info_path.exists():
        map_infos = read_json(map_info_path)
        if isinstance(map_infos, list) and len(map_infos) > 1 and map_infos[1]:
            map_infos[1]["name"] = "DEV_AFFINITY_TEST"
            write_json(map_info_path, map_infos)

    if map_001_path.exists():
        map_001 = read_json(map_001_path)
        if isinstance(map_001, dict):
            map_001["displayName"] = "Dev Affinity Test"
            map_001["note"] = "<chromaDevMap:true>"
            write_json(map_001_path, map_001)


def generate_database_files() -> None:
    character_sources = load_character_sources()
    skills = read_json(DATA_DIR / "Skills.json")
    if not isinstance(skills, list) or not skills:
        raise RuntimeError("Skills.json is invalid or empty; template seed failed.")

    skill_index = build_generated_skills(skills, character_sources)
    classes = build_classes(character_sources, skill_index)
    actors = build_actors()
    system = apply_system_updates(read_json(DATA_DIR / "System.json"), actors)

    write_json(DATA_DIR / "Skills.json", skills)
    write_json(DATA_DIR / "Classes.json", classes)
    write_json(DATA_DIR / "Actors.json", actors)
    write_json(DATA_DIR / "System.json", system)

    patch_test_map()


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap RPG Maker MZ foundation.")
    parser.add_argument(
        "--template-project",
        default="",
        help="Path to local RPG Maker MZ project used as schema/runtime template.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing runtime/template files when seeding.",
    )
    args = parser.parse_args()

    template_project = find_template_project(args.template_project or None)
    seed_runtime(template_project, force=args.force)
    seed_data(template_project, force=args.force)
    generate_database_files()

    print(f"Template project: {template_project}")
    print("Generated:")
    print("- data/Actors.json (13 party members)")
    print("- data/Classes.json (13 class records)")
    print("- data/Skills.json (base + generated character abilities)")
    print("- data/System.json (Chroma's Edge system bootstrap)")
    print("- data/MapInfos.json + data/Map001.json (dev test map labels)")


if __name__ == "__main__":
    main()
