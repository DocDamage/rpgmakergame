#!/usr/bin/env python3
"""
Chroma's Edge Project Organization Script
Creates proper folder structure and organizes all assets
"""

import os
import shutil
from pathlib import Path

def create_folder_structure():
    """Create all necessary folders for the project"""
    print("Creating folder structure...")
    
    folders = [
        # Main image folders
        "img/animations/impacts",
        "img/animations/magic",
        "img/animations/physical",
        "img/animations/status",
        "img/battlebacks1/palace",
        "img/battlebacks1/capital_ruins",
        "img/battlebacks1/frost",
        "img/battlebacks1/ember",
        "img/battlebacks1/tide",
        "img/battlebacks1/uplands",
        "img/battlebacks1/aetherreach",
        "img/battlebacks1/chrono",
        "img/battlebacks1/mire",
        "img/battlebacks1/prism",
        "img/battlebacks1/obsidian",
        "img/battlebacks1/void",
        "img/battlebacks1/tower",
        "img/battlebacks1/bof_generic",
        "img/battlebacks1/interiors",
        "img/battlebacks1/dungeons",
        "img/battlebacks1/towns",
        "img/battlebacks2",
        "img/characters/actors",
        "img/characters/npcs",
        "img/characters/enemies/dustbelt",
        "img/characters/enemies/uplands",
        "img/characters/enemies/mire",
        "img/characters/enemies/prism",
        "img/characters/enemies/ember",
        "img/characters/enemies/tide",
        "img/characters/enemies/frost",
        "img/characters/enemies/obsidian",
        "img/characters/enemies/chrono",
        "img/characters/enemies/capital",
        "img/characters/enemies/void",
        "img/characters/enemies/bosses",
        "img/enemy_battlers",
        "img/faces/actors",
        "img/faces/npcs",
        "img/parallaxes",
        "img/pictures",
        "img/sv_actors",
        "img/sv_enemies",
        "img/system",
        "img/tilesets/time_fantasy",
        "img/tilesets/ice_cavern",
        "img/tilesets/lava_cavern",
        "img/tilesets/steampunk",
        "img/tilesets/dungeons",
        "img/titles1",
        "audio/bgm/towns",
        "audio/bgm/dungeons",
        "audio/bgm/battle",
        "audio/bgm/special",
        "audio/bgs",
        "audio/me",
        "audio/se",
        "data",
        "docs/asset_reference",
        "docs/design",
        "docs/technical",
        "docs/production",
        "js/plugins",
        "movies",
        "scripts",
        "save",
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"  Created: {folder}")
    
    print("Folder structure complete!\n")

def organize_battle_backgrounds():
    """Organize extracted battle backgrounds"""
    print("Organizing battle backgrounds...")
    
    source_base = "assets/extracted_battlebacks"
    dest_base = "img/battlebacks1"
    
    # Mapping of source folders to destinations
    mappings = {
        "palace": "palace",
        "capital_ruins": "capital_ruins",
        "bof_static": "bof_generic",
        "bof2_static": "bof_generic",
        "interiors": "interiors",
        "dungeons": "dungeons",
        "towns": "towns",
        "tide": "tide",
        "uplands": "uplands",
        "aetherreach": "aetherreach",
        "tower": "tower",
    }
    
    for source_folder, dest_folder in mappings.items():
        source_path = os.path.join(source_base, source_folder)
        dest_path = os.path.join(dest_base, dest_folder)
        
        if not os.path.exists(source_path):
            print(f"  Skip: {source_path} not found")
            continue
        
        for file in os.listdir(source_path):
            if file.endswith('.png'):
                src = os.path.join(source_path, file)
                dst = os.path.join(dest_path, file)
                
                # Rename with prefix if needed
                if dest_folder == "bof_generic":
                    # Already has bof_ prefix
                    new_name = file
                elif dest_folder == "interiors":
                    new_name = f"interior_{file}"
                elif dest_folder == "dungeons":
                    new_name = f"dungeon_{file}"
                elif dest_folder == "towns":
                    new_name = f"town_{file}"
                else:
                    new_name = f"{dest_folder}_{file}"
                
                dst = os.path.join(dest_path, new_name)
                
                try:
                    shutil.copy2(src, dst)
                    print(f"  Copied: {file} -> {new_name}")
                except Exception as e:
                    print(f"  Error copying {file}: {e}")
    
    print("Battle backgrounds organized!\n")

def organize_parallax():
    """Organize parallax backgrounds"""
    print("Organizing parallax backgrounds...")
    
    dest_path = "img/parallaxes"
    
    # These would be extracted from ZIP files
    # For now, just create the destination
    print(f"  Destination ready: {dest_path}")
    print("  Note: Extract parallax ZIP files manually to this folder")
    print("  Files to extract:")
    print("    - Hand Painted Parallax BG - Gloomwood Forest.zip -> parallax_gloomwood_forest.png")
    print("    - Hand Painted Parallax BG - Whitewood Vale.zip -> parallax_whitewood_vale.png")
    print("    - Ice Castle Parallax BG.zip -> parallax_ice_castle.png")
    print("    - Star Ocean - Cloud Parallax 1.png -> parallax_clouds.png")
    print("    - Star Ocean - Fog Parallax.png -> parallax_fog.png")
    
    print("Parallax folder ready!\n")

def organize_animations():
    """Organize animation packs"""
    print("Organizing animation packs...")
    
    dest_base = "img/animations"
    
    animation_mappings = {
        "Pixel Art Animations - Slashes.zip": ("physical", "anim_slash"),
        "Pixel Art Animations - Warrior.zip": ("physical", "anim_warrior"),
        "Pixel Art Animations - Paladin.zip": ("magic", "anim_paladin"),
        "Pixel Art Animations - Halloween.zip": ("magic", "anim_halloween"),
        "Pixel Art Animations - Lightning.zip": ("magic", "anim_lightning"),
        "Pixel Art Skill Animations - Lightning.zip": ("magic", "anim_skill_lightning"),
        "Pixel Art VFX - Fire Mage.zip": ("magic", "vfx_fire_mage"),
        "Pixel Art VFX - Frost Knight.zip": ("magic", "vfx_frost_knight"),
        "Pixel Art VFX - Necromancer.zip": ("magic", "vfx_necromancer"),
        "Pixel Art VFX - Priest.zip": ("magic", "vfx_priest"),
        "Pixel Art VFX - Rogue.zip": ("physical", "vfx_rogue"),
        "Pixel Art VFX - Starcaller.zip": ("magic", "vfx_starcaller"),
        "Pixel Art VFX - Vampire.zip": ("magic", "vfx_vampire"),
        "Pixel Art VFX - Warlock.zip": ("magic", "vfx_warlock"),
        "Pixel Art VFX Impacts.zip": ("impacts", "vfx_impacts"),
        "npc-animations-8.20.zip": ("status", "npc_animations"),
    }
    
    print("  Animation destinations prepared:")
    for zip_file, (category, folder_name) in animation_mappings.items():
        dest_folder = os.path.join(dest_base, folder_name)
        print(f"    {zip_file} -> {dest_folder}")
    
    print("\n  Note: Extract animation ZIP files to their respective folders")
    print("Animations organized!\n")

def organize_documentation():
    """Organize documentation files"""
    print("Organizing documentation...")
    
    doc_mappings = {
        "docs/asset_reference/": [
            "ZONE_ASSET_MAPPING.md",
            "EXTRACTION_COORDINATES.md",
            "VISUAL_STYLE_GUIDE.md",
            "IMPLEMENTATION_ROADMAP.md",
            "MASTER_ASSET_INDEX.md",
            "PALACE_DUNGEON_LAYOUT.md",
            "CAPITAL_RUINS_ENCOUNTERS.md",
            "NEW_ASSET_INTEGRATION_GUIDE.md",
            "ASSET_TO_ZONE_MAPPING.md",
            "COMPLETE_ASSET_INVENTORY.md",
            "EXTRACTED_ASSETS_SUMMARY.md",
            "ADDITIONAL_ASSETS_FOUND.md",
        ],
        "docs/design/": [
            "SNES_NPC_MASTER_CATALOG.md",
            "MONSTER_ECOLOGY_COMPENDIUM.md",
            "MONSTER_SPRITE_REFERENCE.md",
            "ITEM_COMPENDIUM.md",
            "MASSIVE_CONTENT_EXPANSION.md",
            "NPC_MONSTER_EXPANSION_SUMMARY.md",
            "EXPANSION_COMPLETE_SUMMARY.md",
            "WORLD_NPC_DISTRIBUTION.md",
            "WORLD_NPC_DISTRIBUTION_NEW.md",
            "QUIRKY_NPC_ASSIGNMENTS.md",
        ],
        "docs/technical/": [
            "ENGINE_RECOMMENDATION.md",
            "IMPLEMENTATION_SUMMARY.md",
            "PROJECT_STRUCTURE.md",
            "VFX_EFFECTS_INVENTORY.md",
            "WEAPONS_ARMOR_ASSETS.md",
            "DESIGN_DOC_v2_13_party.md",
        ],
        "docs/production/": [
            "PRODUCTION_CHECKLIST_MASTER.md",
            "PROJECT_INDEX.md",
        ],
    }
    
    docs_dir = "docs"
    
    for dest_folder, files in doc_mappings.items():
        os.makedirs(dest_folder, exist_ok=True)
        print(f"  {dest_folder}:")
        for file in files:
            src = os.path.join(docs_dir, file)
            dst = os.path.join(dest_folder, file)
            if os.path.exists(src):
                try:
                    shutil.move(src, dst)
                    print(f"    Moved: {file}")
                except Exception as e:
                    print(f"    Error moving {file}: {e}")
            else:
                print(f"    Not found: {file}")
    
    print("Documentation organized!\n")

def create_inventory_report():
    """Create an inventory report of organized assets"""
    print("Creating inventory report...")
    
    report_lines = ["# Chroma's Edge - Asset Inventory Report\n"]
    report_lines.append(f"Generated: {os.popen('date').read().strip()}\n\n")
    
    # Count battle backgrounds
    battlebacks_path = "img/battlebacks1"
    if os.path.exists(battlebacks_path):
        battlebacks = []
        for root, dirs, files in os.walk(battlebacks_path):
            for file in files:
                if file.endswith('.png'):
                    battlebacks.append(os.path.join(root, file))
        report_lines.append(f"## Battle Backgrounds: {len(battlebacks)}\n")
        for bb in sorted(battlebacks):
            report_lines.append(f"- {os.path.basename(bb)}\n")
        report_lines.append("\n")
    
    # Count folders created
    report_lines.append("## Folder Structure Created\n")
    for root, dirs, files in os.walk("."):
        if '.git' not in root and 'node_modules' not in root:
            level = root.count(os.sep)
            if level <= 3:  # Only show up to 3 levels deep
                indent = '  ' * level
                report_lines.append(f"{indent}{os.path.basename(root)}/\n")
    
    # Write report
    with open("ASSET_INVENTORY_REPORT.md", "w") as f:
        f.writelines(report_lines)
    
    print("Inventory report created: ASSET_INVENTORY_REPORT.md\n")

def main():
    """Main organization routine"""
    print("=" * 60)
    print("CHROMA'S EDGE - PROJECT ORGANIZATION")
    print("=" * 60)
    print()
    
    # Check if we're in the right directory
    if not os.path.exists("assets/extracted_battlebacks"):
        print("ERROR: Must run from project root directory")
        print("Looking for: assets/extracted_battlebacks")
        return 1
    
    # Run organization
    create_folder_structure()
    organize_battle_backgrounds()
    organize_parallax()
    organize_animations()
    organize_documentation()
    create_inventory_report()
    
    print("=" * 60)
    print("ORGANIZATION COMPLETE!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Extract parallax ZIP files to img/parallaxes/")
    print("2. Extract animation ZIP files to img/animations/")
    print("3. Copy weapon sprite PNGs to img/system/ or img/icons/")
    print("4. Review ASSET_INVENTORY_REPORT.md")
    print("5. Ready for RPG Maker MZ import!")
    
    return 0

if __name__ == "__main__":
    exit(main())
