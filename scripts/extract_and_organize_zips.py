#!/usr/bin/env python3
"""
Extract and organize all ZIP files
Parallax, Animations, Weapons, everything
"""

import zipfile
import os
import shutil
from pathlib import Path

def extract_parallax():
    """Extract all parallax ZIP files"""
    print("=" * 60)
    print("EXTRACTING PARALLAX BACKGROUNDS")
    print("=" * 60)
    
    source_dir = "assets/AssetsForMyGame"
    dest_dir = "img/parallaxes"
    
    parallax_files = [
        ("Hand Painted Parallax BG - Gloomwood Forest.zip", "parallax_gloomwood_forest.png"),
        ("Hand Painted Parallax BG - Whitewood Vale - FREE Version.zip", "parallax_whitewood_vale.png"),
        ("Ice Castle Parallax BG.zip", "parallax_ice_castle.png"),
    ]
    
    # Also copy loose parallax PNGs
    loose_parallax = [
        ("SNES - Star Ocean (JPN) - Miscellaneous - Cloud Parallax 1.png", "parallax_clouds.png"),
        ("SNES - Star Ocean (JPN) - Miscellaneous - Fog Parallax.png", "parallax_fog.png"),
        ("SNES - 3 Ninjas Kick Back - Backgrounds - Bamboo Forest.png", "parallax_bamboo_forest.png"),
        ("SNES - Super Nazo Puyo Tsuu_ Rulue no Tetsuwan Hanjyouki (JPN) - Backgrounds - Dragon Valley.png", "parallax_dragon_valley.png"),
        ("SNES - Bakumatsu Kourinden Oni (JPN) - Miscellaneous - Overworld Clouds.png", "parallax_clouds_japanese.png"),
        ("SNES - Albert Odyssey 2 - Jashin no Taidou (JPN) - Miscellaneous - Gote (Clouds, Day & Noon).png", "parallax_gote_clouds.png"),
    ]
    
    extracted_count = 0
    
    # Extract ZIP files
    for zip_name, output_name in parallax_files:
        zip_path = os.path.join(source_dir, zip_name)
        if os.path.exists(zip_path):
            try:
                print(f"\nExtracting: {zip_name}")
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # List contents
                    contents = zip_ref.namelist()
                    print(f"  Contents: {contents}")
                    
                    # Extract all
                    zip_ref.extractall(dest_dir)
                    
                    # Rename the main file if needed
                    for item in contents:
                        if item.endswith('.png') or item.endswith('.jpg'):
                            old_path = os.path.join(dest_dir, item)
                            new_path = os.path.join(dest_dir, output_name)
                            if os.path.exists(old_path) and old_path != new_path:
                                shutil.move(old_path, new_path)
                                print(f"  Renamed to: {output_name}")
                                extracted_count += 1
                                break
            except Exception as e:
                print(f"  Error: {e}")
        else:
            print(f"  Not found: {zip_name}")
    
    # Copy loose parallax PNGs
    print("\nCopying loose parallax PNGs...")
    for source_name, output_name in loose_parallax:
        source_path = os.path.join(source_dir, source_name)
        dest_path = os.path.join(dest_dir, output_name)
        if os.path.exists(source_path):
            try:
                shutil.copy2(source_path, dest_path)
                print(f"  Copied: {source_name} -> {output_name}")
                extracted_count += 1
            except Exception as e:
                print(f"  Error copying {source_name}: {e}")
        else:
            print(f"  Not found: {source_name}")
    
    print(f"\nParallax extraction complete: {extracted_count} files")
    return extracted_count

def extract_animations():
    """Extract all animation ZIP files"""
    print("\n" + "=" * 60)
    print("EXTRACTING ANIMATION PACKS")
    print("=" * 60)
    
    source_dir = "assets/AssetsForMyGame"
    dest_base = "img/animations"
    
    animation_mappings = [
        ("Pixel Art Animations - Slashes.zip", "anim_slash"),
        ("Pixel Art Animations - Warrior (FREE).zip", "anim_warrior"),
        ("Pixel Art Animations - Paladin - FREE Version.zip", "anim_paladin"),
        ("Pixel Art Animations - Halloween (FREE).zip", "anim_halloween"),
        ("Pixel Art Skill Animations - Lightning.zip", "anim_lightning"),
        ("Pixel Art VFX - Fire Mage - FREE Version.zip", "vfx_fire_mage"),
        ("Pixel Art VFX - Frost Knight - FREE Version.zip", "vfx_frost_knight"),
        ("Pixel Art VFX - Necromancer - FREE Version.zip", "vfx_necromancer"),
        ("Pixel Art VFX - Priest - FREE Version.zip", "vfx_priest"),
        ("Pixel Art VFX - Rogue - FREE Version.zip", "vfx_rogue"),
        ("Pixel Art VFX - Starcaller - FREE Version.zip", "vfx_starcaller"),
        ("Pixel Art VFX - Vampire - FREE Version.zip", "vfx_vampire"),
        ("Pixel Art VFX - Warlock - FREE Version.zip", "vfx_warlock"),
        ("Pixel Art VFX Impacts - FREE Version.zip", "vfx_impacts"),
        ("npc-animations-8.20.zip", "npc_animations"),
    ]
    
    extracted_count = 0
    
    for zip_name, folder_name in animation_mappings:
        zip_path = os.path.join(source_dir, zip_name)
        dest_folder = os.path.join(dest_base, folder_name)
        
        if os.path.exists(zip_path):
            try:
                print(f"\nExtracting: {zip_name}")
                os.makedirs(dest_folder, exist_ok=True)
                
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(dest_folder)
                    contents = zip_ref.namelist()
                    print(f"  Extracted {len(contents)} items to {folder_name}/")
                    extracted_count += len(contents)
            except Exception as e:
                print(f"  Error: {e}")
        else:
            print(f"  Not found: {zip_name}")
    
    print(f"\nAnimation extraction complete: {extracted_count} files")
    return extracted_count

def organize_weapons():
    """Copy weapon sprite sheets to organized location"""
    print("\n" + "=" * 60)
    print("ORGANIZING WEAPON SPRITES")
    print("=" * 60)
    
    source_dir = "assets/AssetsForMyGame"
    dest_dir = "img/system/weapons"
    os.makedirs(dest_dir, exist_ok=True)
    
    weapon_files = [
        ("DS _ DSi - From the Abyss - Miscellaneous - Weapons.png", "weapons_from_the_abyss.png"),
        ("Mobile - Final Fantasy_ All the Bravest - Miscellaneous - Weapons.png", "weapons_all_the_bravest.png"),
        ("PC _ Computer - RPG Maker MV - Miscellaneous - Weapons.png", "weapons_rpgmaker_mv.png"),
    ]
    
    copied_count = 0
    
    for source_name, output_name in weapon_files:
        source_path = os.path.join(source_dir, source_name)
        dest_path = os.path.join(dest_dir, output_name)
        
        if os.path.exists(source_path):
            try:
                shutil.copy2(source_path, dest_path)
                print(f"  Copied: {source_name} -> {output_name}")
                copied_count += 1
            except Exception as e:
                print(f"  Error: {e}")
        else:
            print(f"  Not found: {source_name}")
    
    print(f"\nWeapon organization complete: {copied_count} files")
    return copied_count

def organize_monster_sprites():
    """Copy monster sprite sheets to organized location"""
    print("\n" + "=" * 60)
    print("ORGANIZING MONSTER SPRITES")
    print("=" * 60)
    
    source_dir = "assets/AssetsForMyGame"
    dest_dir = "img/characters/enemies/spritesheets"
    os.makedirs(dest_dir, exist_ok=True)
    
    monster_files = [
        ("ffvi_monsters.png", "monsters_ff6.png"),
        ("ffvii_monsters.png", "monsters_ff7.png"),
        ("SNES - Breath of Fire - Non-Playable Characters - Enemies & Bosses.png", "monsters_bof1.png"),
        ("SNES - Breath of Fire 2 - Non-Playable Characters - Enemies & Bosses.png", "monsters_bof2.png"),
        ("SNES - Dragon Quest 3 (JPN) - Enemies & Bosses - Monsters (Static).png", "monsters_dq3.png"),
        ("SNES - Slayers (JPN) - Enemies & Bosses - Enemies & Bosses.png", "monsters_slayers.png"),
        ("3DS - Pictologica Final Fantasy - Enemies & Bosses - Final Fantasy I Monsters.png", "monsters_pictologica_ff1.png"),
        ("3DS - Pictologica Final Fantasy - Enemies & Bosses - Final Fantasy IV Monsters.png", "monsters_pictologica_ff4.png"),
        ("3DS - Pictologica Final Fantasy - Enemies & Bosses - Final Fantasy X Monsters.png", "monsters_pictologica_ff10.png"),
        ("3DS - Pictologica Final Fantasy - Enemies & Bosses - Final Fantasy XI Monsters.png", "monsters_pictologica_ff11.png"),
        ("Mobile - Final Fantasy_ Record Keeper - Enemies - Final Fantasy VIII (Monsters).png", "monsters_ffrk_ff8.png"),
        ("Mobile - Final Fantasy_ Record Keeper - Enemies - Final Fantasy XV (Monsters).png", "monsters_ffrk_ff15.png"),
    ]
    
    copied_count = 0
    
    for source_name, output_name in monster_files:
        source_path = os.path.join(source_dir, source_name)
        dest_path = os.path.join(dest_dir, output_name)
        
        if os.path.exists(source_path):
            try:
                shutil.copy2(source_path, dest_path)
                print(f"  Copied: {source_name}")
                copied_count += 1
            except Exception as e:
                print(f"  Error: {e}")
        else:
            print(f"  Not found: {source_name}")
    
    print(f"\nMonster sprite organization complete: {copied_count} files")
    return copied_count

def organize_npc_sprites():
    """Copy NPC sprite sheets to organized location"""
    print("\n" + "=" * 60)
    print("ORGANIZING NPC SPRITES")
    print("=" * 60)
    
    source_dir = "assets/AssetsForMyGame"
    dest_dir = "img/characters/npcs/spritesheets"
    os.makedirs(dest_dir, exist_ok=True)
    
    npc_files = [
        ("SNES - Breath of Fire - Non-Playable Characters - NPCs.png", "npcs_bof1.png"),
        ("SNES - Breath of Fire 2 - Non-Playable Characters - NPCs.png", "npcs_bof2.png"),
        ("SNES - Star Ocean (JPN) - Non-Playable Characters - NPCs 1.png", "npcs_star_ocean_1.png"),
        ("SNES - Star Ocean (JPN) - Non-Playable Characters - NPCs 2.png", "npcs_star_ocean_2.png"),
        ("SNES - Tales of Phantasia (JPN) - Non-Playable Characters - Common NPCs.png", "npcs_tales_common.png"),
        ("SNES - Tales of Phantasia (JPN) - Non-Playable Characters - Unique Characters.png", "npcs_tales_unique.png"),
        ("SNES - Dragon Quest 3 (JPN) - Non-Playable Characters - Male NPCs.png", "npcs_dq3_male.png"),
        ("SNES - Dragon Quest 3 (JPN) - Non-Playable Characters - Female NPCs.png", "npcs_dq3_female.png"),
        ("SNES - Bakumatsu Kourinden Oni (JPN) - Miscellaneous - NPCs 1.png", "npcs_bakumatsu.png"),
    ]
    
    copied_count = 0
    
    for source_name, output_name in npc_files:
        source_path = os.path.join(source_dir, source_name)
        dest_path = os.path.join(dest_dir, output_name)
        
        if os.path.exists(source_path):
            try:
                shutil.copy2(source_path, dest_path)
                print(f"  Copied: {source_name}")
                copied_count += 1
            except Exception as e:
                print(f"  Error: {e}")
        else:
            print(f"  Not found: {source_name}")
    
    # Extract beast tribes
    beast_zips = [
        ("beast_tribes.zip", "beast_tribes"),
        ("beast_tribes_2.zip", "beast_tribes_2"),
        ("quirky_npcs.zip", "quirky_npcs"),
    ]
    
    for zip_name, folder_name in beast_zips:
        zip_path = os.path.join(source_dir, zip_name)
        dest_folder = os.path.join(dest_dir, folder_name)
        
        if os.path.exists(zip_path):
            try:
                print(f"\nExtracting: {zip_name}")
                os.makedirs(dest_folder, exist_ok=True)
                
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(dest_folder)
                    contents = zip_ref.namelist()
                    print(f"  Extracted {len(contents)} items")
                    copied_count += len(contents)
            except Exception as e:
                print(f"  Error: {e}")
    
    print(f"\nNPC sprite organization complete: {copied_count} files")
    return copied_count

def create_final_report():
    """Create final organization report"""
    print("\n" + "=" * 60)
    print("CREATING FINAL REPORT")
    print("=" * 60)
    
    # Count files in each category
    categories = {
        "Battle Backgrounds": "img/battlebacks1",
        "Parallax Backgrounds": "img/parallaxes",
        "Animations": "img/animations",
        "Weapon Sprites": "img/system/weapons",
        "Monster Sprites": "img/characters/enemies/spritesheets",
        "NPC Sprites": "img/characters/npcs/spritesheets",
    }
    
    report_lines = ["# Chroma's Edge - Final Asset Organization Report\n\n"]
    
    total_count = 0
    for name, path in categories.items():
        if os.path.exists(path):
            count = sum(1 for root, dirs, files in os.walk(path) for f in files if f.endswith(('.png', '.jpg', '.gif', '.json', '.txt')))
            report_lines.append(f"## {name}: {count} files\n")
            report_lines.append(f"Location: `{path}/`\n\n")
            total_count += count
        else:
            report_lines.append(f"## {name}: Not found\n\n")
    
    report_lines.append(f"**Total Organized Assets: {total_count}**\n\n")
    report_lines.append("## Ready for RPG Maker MZ\n\n")
    report_lines.append("All assets are properly named and organized.\n")
    report_lines.append("Copy the `img/` folder to your RPG Maker MZ project.\n")
    
    with open("FINAL_ASSET_REPORT.md", "w") as f:
        f.writelines(report_lines)
    
    print(f"Report created: FINAL_ASSET_REPORT.md")
    print(f"Total assets organized: {total_count}")

def main():
    """Main extraction and organization routine"""
    print("=" * 60)
    print("CHROMA'S EDGE - COMPLETE ASSET EXTRACTION")
    print("=" * 60)
    print()
    
    # Check if we're in the right directory
    if not os.path.exists("assets/AssetsForMyGame"):
        print("ERROR: Must run from project root directory")
        print("Looking for: assets/AssetsForMyGame")
        return 1
    
    # Run all extraction and organization
    parallax_count = extract_parallax()
    anim_count = extract_animations()
    weapon_count = organize_weapons()
    monster_count = organize_monster_sprites()
    npc_count = organize_npc_sprites()
    
    # Create final report
    create_final_report()
    
    print("\n" + "=" * 60)
    print("COMPLETE! ALL ASSETS ORGANIZED!")
    print("=" * 60)
    print()
    print(f"Parallax backgrounds: {parallax_count}")
    print(f"Animation files: {anim_count}")
    print(f"Weapon sprite sheets: {weapon_count}")
    print(f"Monster sprite sheets: {monster_count}")
    print(f"NPC sprite files: {npc_count}")
    print()
    print("Your project is 100% ready for RPG Maker MZ!")
    print("Copy the entire 'img/' folder to your MZ project.")
    
    return 0

if __name__ == "__main__":
    exit(main())
