#!/usr/bin/env python3
"""
Extended Battle Background Extraction Script
Extracts from Breath of Fire, FF6, Bakumatsu, Tengai Makyou, and more
"""

from PIL import Image
import os
import sys

def extract_region(source_path, output_path, coords, target_size=(640, 360)):
    """Extract a region from source image and resize"""
    try:
        with Image.open(source_path) as img:
            region = img.crop(coords)
            resized = region.resize(target_size, Image.NEAREST)
            resized.save(output_path, 'PNG')
            print(f"[OK] {os.path.basename(output_path)}")
            return True
    except Exception as e:
        print(f"[FAIL] {os.path.basename(output_path)}: {e}")
        return False

def extract_bof_backgrounds():
    """Extract Breath of Fire battle backgrounds"""
    print("\n=== BREATH OF FIRE BATTLE BACKGROUNDS ===")
    
    # Static backgrounds
    source = "assets/AssetsForMyGame/SNES - Breath of Fire - Battle Backgrounds - Battle Backgrounds (Static).png"
    output_dir = "assets/extracted_battlebacks/bof_static"
    os.makedirs(output_dir, exist_ok=True)
    
    if os.path.exists(source):
        # Extract various backgrounds - full sheet is 1024x1024 typically
        extractions = [
            ("bof_grassland.png", (0, 0, 512, 288)),
            ("bof_forest.png", (512, 0, 1024, 288)),
            ("bof_desert.png", (0, 288, 512, 576)),
            ("bof_mountain.png", (512, 288, 1024, 576)),
            ("bof_cave.png", (0, 576, 512, 864)),
            ("bof_water.png", (512, 576, 1024, 864)),
        ]
        for filename, coords in extractions:
            extract_region(source, os.path.join(output_dir, filename), coords)
    
    # Breath of Fire 2 backgrounds
    source2 = "assets/AssetsForMyGame/SNES - Breath of Fire 2 - Battle Backgrounds - Battle Backgrounds (Static).png"
    output_dir2 = "assets/extracted_battlebacks/bof2_static"
    os.makedirs(output_dir2, exist_ok=True)
    
    if os.path.exists(source2):
        extractions2 = [
            ("bof2_city.png", (0, 0, 512, 288)),
            ("bof2_ruins.png", (512, 0, 1024, 288)),
            ("bof2_sea.png", (0, 288, 512, 576)),
            ("bof2_underwater.png", (512, 288, 1024, 576)),
            ("bof2_castle.png", (0, 576, 512, 864)),
            ("bof2_dark.png", (512, 576, 1024, 864)),
        ]
        for filename, coords in extractions2:
            extract_region(source2, os.path.join(output_dir2, filename), coords)

def extract_interior_rooms():
    """Extract house and shop interiors for battle backgrounds"""
    print("\n=== INTERIOR ROOMS ===")
    output_dir = "assets/extracted_battlebacks/interiors"
    os.makedirs(output_dir, exist_ok=True)
    
    interiors = [
        ("SNES - Aretha (JPN) - Maps - Sarah's House (Interior).png", "aretha_house.png", (20, 20, 500, 380)),
        ("SNES - Breath of Fire - Maps - Old Woman's House.png", "bof_oldhouse.png", (20, 20, 500, 380)),
        ("SNES - Breath of Fire 2 - Maps - Bo & Karn's House.png", "bof2_house1.png", (20, 20, 500, 380)),
        ("SNES - Last Bible III (JPN) - Maps - Baghi's House _ Huey's House & Maia's House (Interior).png", "lastbible_house.png", (20, 20, 500, 380)),
        ("SNES - Rudra no Hihou (JPN) - Maps - Small Church (Interior).png", "rudra_church.png", (20, 20, 500, 380)),
        ("SNES - Rudra no Hihou (JPN) - Maps - Temple of Spirit (Interior).png", "rudra_temple.png", (20, 20, 500, 380)),
        ("SNES - Tales of Phantasia (JPN) - Maps - Bart's House (Interior).png", "top_house1.png", (20, 20, 500, 380)),
        ("SNES - Tales of Phantasia (JPN) - Maps - Edward D. Morrison's House (Interior).png", "top_house2.png", (20, 20, 500, 380)),
        ("SNES - Tales of Phantasia (JPN) - Maps - Fenrir Church (Interior).png", "top_church.png", (20, 20, 500, 380)),
        ("SNES - Terranigma - Maps - Will's House.png", "terranigma_house.png", (20, 20, 500, 380)),
    ]
    
    for source_file, output_name, coords in interiors:
        source = f"assets/AssetsForMyGame/{source_file}"
        if os.path.exists(source):
            extract_region(source, os.path.join(output_dir, output_name), coords)

def extract_dungeon_rooms():
    """Extract dungeon and cave rooms"""
    print("\n=== DUNGEON ROOMS ===")
    output_dir = "assets/extracted_battlebacks/dungeons"
    os.makedirs(output_dir, exist_ok=True)
    
    dungeons = [
        ("SNES - Arabian Nights_ Sabaku no Seirei Ou (JPN) - Maps - Mt. Elyrita (Roc Cave).png", "arabian_cave.png", (20, 20, 500, 380)),
        ("SNES - Arabian Nights_ Sabaku no Seirei Ou (JPN) - Maps - Quicksand Cave Entrance.png", "arabian_quicksand.png", (20, 20, 500, 380)),
        ("SNES - Breath of Fire - Maps - Nanai Dungeon _ Gaia Temple.png", "bof_dungeon.png", (20, 20, 500, 380)),
        ("SNES - Breath of Fire 2 - Maps - Bleu's Cave.png", "bof2_cave.png", (20, 20, 500, 380)),
        ("SNES - Dragon Quest 6 (JPN) - Maps - Baptismal Cave.png", "dq6_cave.png", (20, 20, 500, 380)),
        ("SNES - Tengai Makyou Zero (JPN) - Maps - Crab-Crab Cavern.png", "tengai_cave.png", (20, 20, 500, 380)),
        ("SNES - Tales of Phantasia (JPN) - Maps - Alvanista Castle (Dungeon).png", "top_dungeon.png", (20, 20, 500, 380)),
        ("SNES - Rudra no Hihou (JPN) - Maps - Giant's Tower (Interior).png", "rudra_tower.png", (20, 20, 500, 380)),
        ("SNES - Rudra no Hihou (JPN) - Maps - Undersea Palace (Waterless Interior).png", "rudra_undersea.png", (20, 20, 500, 380)),
    ]
    
    for source_file, output_name, coords in dungeons:
        source = f"assets/AssetsForMyGame/{source_file}"
        if os.path.exists(source):
            extract_region(source, os.path.join(output_dir, output_name), coords)

def extract_town_interiors():
    """Extract town interior sections"""
    print("\n=== TOWN INTERIORS ===")
    output_dir = "assets/extracted_battlebacks/towns"
    os.makedirs(output_dir, exist_ok=True)
    
    towns = [
        ("SNES - Star Ocean (JPN) - Astral Kingdom - Maps - Astral Castle Town (Unique Interior).png", "so_astral_town.png", (50, 50, 600, 410)),
        ("SNES - Star Ocean (JPN) - Van Kingdom - Maps - Van Castle Town (Unique Interior).png", "so_van_town.png", (50, 50, 600, 410)),
        ("SNES - Tales of Phantasia (JPN) - Maps - Midgard (Southern Interior).png", "top_midgard.png", (50, 50, 600, 410)),
        ("SNES - Tengai Makyou Zero (JPN) - Maps - Dragon Eyes Village (Interior).png", "tengai_village1.png", (50, 50, 600, 410)),
        ("SNES - Tengai Makyou Zero (JPN) - Maps - Katana Village (Interior).png", "tengai_village2.png", (50, 50, 600, 410)),
        ("SNES - Tengai Makyou Zero (JPN) - Maps - Royal Dragon Town (Interior).png", "tengai_dragontown.png", (50, 50, 600, 410)),
        ("SNES - Burning Heroes - Maps - Fire City (Interior).png", "burning_city.png", (50, 50, 600, 410)),
    ]
    
    for source_file, output_name, coords in towns:
        source = f"assets/AssetsForMyGame/{source_file}"
        if os.path.exists(source):
            extract_region(source, os.path.join(output_dir, output_name), coords)

def extract_special_rooms():
    """Extract throne rooms, boss rooms, special areas"""
    print("\n=== SPECIAL ROOMS ===")
    output_dir = "assets/extracted_battlebacks/special"
    os.makedirs(output_dir, exist_ok=True)
    
    special = [
        ("SNES - Albert Odyssey 2 - Maps - Throne Room.png", "albert_throne.png", (20, 20, 500, 380)),
        ("SNES - Tengai Makyou Zero - Maps - Ice Fang Castle (Zettai Reido's Room).png", "tengai_iceboss.png", (20, 20, 500, 380)),
        ("SNES - Tengai Makyou Zero - Maps - Royal Dragon Castle 10 (Throne Room).png", "tengai_dragonthrone.png", (20, 20, 500, 380)),
        ("SNES - Tengai Makyou Zero - Maps - Phantom Castle (Sara's Room).png", "tengai_phantom.png", (20, 20, 500, 380)),
        ("SNES - Rudra no Hihou - Maps - Temple of Spirit (Interior).png", "rudra_spirit.png", (20, 20, 500, 380)),
        ("SNES - Rudra no Hihou - Maps - Gomorrah City (Interior).png", "rudra_gomorrah.png", (20, 20, 500, 380)),
        ("SNES - Lufia 2 - Maps - Submarine Town of Preamarl (Waterless Interior).png", "lufia_subtown.png", (20, 20, 500, 380)),
        ("SNES - Bakumatsu Kourinden Oni - Miscellaneous - Battle Backgrounds 1.png", "bakumatsu_bg.png", (20, 20, 500, 380)),
        ("SNES - Tengai Makyou Zero - Miscellaneous - Battle Backgrounds 3.png", "tengai_bg.png", (20, 20, 500, 380)),
    ]
    
    for source_file, output_name, coords in special:
        source = f"assets/AssetsForMyGame/{source_file}"
        if os.path.exists(source):
            extract_region(source, os.path.join(output_dir, output_name), coords)

def main():
    print("=" * 60)
    print("CHROMA'S EDGE - EXTENDED BACKGROUND EXTRACTION")
    print("=" * 60)
    
    if not os.path.exists("assets/AssetsForMyGame"):
        print("\n[ERROR] Must run from project root")
        sys.exit(1)
    
    extract_bof_backgrounds()
    extract_interior_rooms()
    extract_dungeon_rooms()
    extract_town_interiors()
    extract_special_rooms()
    
    print("\n" + "=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print("\nNew backgrounds in:")
    print("  - assets/extracted_battlebacks/bof_static/")
    print("  - assets/extracted_battlebacks/bof2_static/")
    print("  - assets/extracted_battlebacks/interiors/")
    print("  - assets/extracted_battlebacks/dungeons/")
    print("  - assets/extracted_battlebacks/towns/")
    print("  - assets/extracted_battlebacks/special/")

if __name__ == "__main__":
    main()
