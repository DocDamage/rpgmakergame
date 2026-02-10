#!/usr/bin/env python3
"""
Battle Background Extractor for Chroma's Edge
Extracts specific regions from SNES asset sheets for use as battle backgrounds
"""

from PIL import Image
import os
import sys

def extract_region(source_path, output_path, coords, target_size=(640, 360)):
    """
    Extract a region from source image and resize to target dimensions
    
    Args:
        source_path: Path to source PNG
        output_path: Path to save extracted PNG
        coords: Tuple (left, top, right, bottom)
        target_size: Tuple (width, height) for output
    """
    try:
        with Image.open(source_path) as img:
            # Extract region
            region = img.crop(coords)
            
            # Resize using nearest neighbor to maintain pixel art crispness
            resized = region.resize(target_size, Image.NEAREST)
            
            # Save
            resized.save(output_path, 'PNG')
            print(f"[OK] Extracted: {os.path.basename(output_path)}")
            return True
    except Exception as e:
        print(f"[FAIL] Failed to extract {os.path.basename(output_path)}: {e}")
        return False

def process_palace_assets():
    """Extract Palace (Loire Castle) backgrounds"""
    print("\n=== PROCESSING PALACE ASSETS ===")
    
    source = "assets/AssetsForMyGame/SNES - Terranigma - Maps - Loire Castle 2F (Throne Room & Lounges).png"
    output_dir = "assets/extracted_battlebacks/palace"
    
    # Key extractions from Loire Castle 2F
    extractions = [
        # (name, (left, top, right, bottom))
        ("throne_room_main.png", (20, 20, 460, 380)),
        ("throne_room_alt.png", (480, 20, 920, 380)),
        ("guard_stations.png", (940, 20, 1380, 380)),
        ("royal_lounge.png", (20, 380, 460, 740)),
        ("throne_side.png", (480, 380, 920, 740)),
        ("castle_hallway.png", (940, 380, 1380, 740)),
    ]
    
    for filename, coords in extractions:
        output_path = os.path.join(output_dir, filename)
        extract_region(source, output_path, coords)

def process_capital_ruins():
    """Extract Capital Ruins (Louran) backgrounds"""
    print("\n=== PROCESSING CAPITAL RUINS ASSETS ===")
    
    source = "assets/AssetsForMyGame/SNES - Terranigma - Maps - Louran (Ruins - Interior).png"
    output_dir = "assets/extracted_battlebacks/capital_ruins"
    
    # Louran is 1712x2464 pixels with multiple rooms
    # Grid: ~8 rows, variable columns
    
    extractions = [
        # Row 1 - Large buildings
        ("entry_plaza.png", (20, 20, 400, 300)),
        ("ruined_shop_a.png", (428, 20, 856, 320)),
        ("ruined_shop_b.png", (856, 20, 1284, 320)),
        
        # Row 2-3 - Residential
        ("destroyed_home_a.png", (20, 320, 214, 568)),
        ("destroyed_home_b.png", (214, 320, 428, 568)),
        ("apartment_building.png", (428, 320, 856, 568)),
        
        # Row 4 - Town square
        ("town_square.png", (20, 568, 400, 820)),
        ("market_stalls.png", (400, 568, 800, 820)),
        
        # Row 5 - Memorial
        ("memorial_hall.png", (20, 820, 400, 1070)),
        
        # Row 6-7 - Underground
        ("sewer_tunnel.png", (400, 1070, 800, 1320)),
        ("underground_chamber.png", (800, 1070, 1200, 1320)),
        
        # Row 8 - Palace approach
        ("palace_gate.png", (20, 2100, 500, 2400)),
    ]
    
    for filename, coords in extractions:
        output_path = os.path.join(output_dir, filename)
        extract_region(source, output_path, coords)

def process_tide():
    """Extract Tide Coast (Harbor) backgrounds"""
    print("\n=== PROCESSING TIDE ASSETS ===")
    
    source = "assets/AssetsForMyGame/SNES - Terranigma - Maps - Harbor of Freedom (Exterior).png"
    output_dir = "assets/extracted_battlebacks/tide"
    
    extractions = [
        ("harbor_main.png", (20, 20, 600, 400)),
        ("ship_deck.png", (600, 20, 1100, 400)),
        ("dock_area.png", (20, 400, 400, 780)),
        ("warehouse_district.png", (400, 400, 800, 780)),
    ]
    
    for filename, coords in extractions:
        output_path = os.path.join(output_dir, filename)
        extract_region(source, output_path, coords)

def process_aetherreach():
    """Extract Aetherreach (Windia) backgrounds"""
    print("\n=== PROCESSING AETHERREACH ASSETS ===")
    
    # Breath of Fire 2 - Windia
    source = "assets/AssetsForMyGame/SNES - Breath of Fire 2 - Maps - Windia (Exterior).png"
    output_dir = "assets/extracted_battlebacks/aetherreach"
    
    # Try to extract, but file might not exist or be named differently
    if os.path.exists(source):
        extractions = [
            ("floating_plaza.png", (100, 100, 700, 500)),
            ("cloud_bridge.png", (50, 500, 450, 800)),
            ("sky_dock.png", (500, 500, 900, 800)),
        ]
        
        for filename, coords in extractions:
            output_path = os.path.join(output_dir, filename)
            extract_region(source, output_path, coords)
    else:
        print(f"[WARN] Source not found: {source}")
        print("  Skipping Aetherreach extraction (will need manual processing)")

def process_uplands():
    """Extract Uplands (Storkolm) backgrounds"""
    print("\n=== PROCESSING UPLANDS ASSETS ===")
    
    source = "assets/AssetsForMyGame/SNES - Terranigma - Maps - Storkolm (Exterior).png"
    output_dir = "assets/extracted_battlebacks/uplands"
    
    if os.path.exists(source):
        extractions = [
            ("village_center.png", (100, 100, 500, 400)),
            ("stone_houses.png", (50, 400, 450, 700)),
            ("mountain_overlook.png", (400, 100, 800, 400)),
        ]
        
        for filename, coords in extractions:
            output_path = os.path.join(output_dir, filename)
            extract_region(source, output_path, coords)
    else:
        print(f"⚠ Source not found: {source}")
        print("  Skipping Uplands extraction (will need manual processing)")

def process_tower():
    """Extract Tower backgrounds"""
    print("\n=== PROCESSING TOWER ASSETS ===")
    
    source = "assets/AssetsForMyGame/SNES - Terranigma - Maps - Loire Castle (Tower).png"
    output_dir = "assets/extracted_battlebacks/tower"
    
    if os.path.exists(source):
        extractions = [
            ("tower_base.png", (50, 400, 450, 800)),
            ("tower_mid.png", (50, 200, 450, 600)),
            ("tower_top.png", (50, 50, 450, 450)),
        ]
        
        for filename, coords in extractions:
            output_path = os.path.join(output_dir, filename)
            extract_region(source, output_path, coords)
    else:
        print(f"⚠ Source not found: {source}")
        print("  Skipping Tower extraction (will need manual processing)")

def main():
    """Main extraction routine"""
    print("=" * 60)
    print("CHROMA'S EDGE - BATTLE BACKGROUND EXTRACTOR")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists("assets/AssetsForMyGame"):
        print("\n[ERROR] Must run from project root directory")
        print("  Looking for: assets/AssetsForMyGame")
        sys.exit(1)
    
    # Process each zone
    process_palace_assets()
    process_capital_ruins()
    process_tide()
    process_aetherreach()
    process_uplands()
    process_tower()
    
    print("\n" + "=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print("\nExtracted backgrounds are in: assets/extracted_battlebacks/")
    print("\nNext steps:")
    print("1. Review extracted images")
    print("2. Apply color adjustments per VISUAL_STYLE_GUIDE.md")
    print("3. Copy to engine's battleback directory")

if __name__ == "__main__":
    main()
