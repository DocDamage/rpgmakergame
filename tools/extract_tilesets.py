"""
Tileset Extraction Tool for Chroma's Edge
Extracts sections from composite spritesheets into RPG Maker format
"""

from PIL import Image
import os

# Configuration: Map target files to source crops
EXTRACTION_MAP = [
    # (target_file, source_file, crop_box)
    ("Dungeon_A1.png", "tileset_ashveilstone_source_primary.png", (0, 0, 768, 576)),
    ("Dungeon_A2.png", "tileset_ashveilstone_source_primary.png", (0, 576, 768, 1152)),
    ("Dungeon_A4.png", "tileset_capitalruins_source_primary.png", (0, 576, 768, 1152)),
    ("Dungeon_A5.png", "tileset_capitalruins_source_primary.png", (0, 0, 768, 576)),
    ("Dungeon_C.png", "tileset_voidnexus_source_primary.png", (0, 0, 464, 336)),
    
    ("Outside_A1.png", "tileset_dustbelt_source_primary.png", (0, 0, 608, 576)),
    ("Outside_A2.png", "tileset_dustbelt_source_primary.png", (0, 0, 608, 720)),
    ("Outside_A3.png", "tileset_uplands_source_primary.png", (0, 0, 768, 576)),
    ("Outside_A4.png", "tileset_emberbasalt_source_primary.png", (0, 0, 640, 336)),
    ("Outside_A5.png", "tileset_prismhighland_source_primary.png", (0, 0, 720, 448)),
    ("Outside_B.png", "tileset_mirestilts_source_primary.png", (0, 0, 352, 336)),
    ("Outside_C.png", "tileset_tidecoast_source_primary.png", (0, 0, 576, 416)),
    
    ("World_A1.png", "tileset_orionoverworld_source_primary.png", (0, 0, 256, 256)),
    ("World_A2.png", "tileset_orionoverworld_source_primary.png", (0, 0, 256, 256)),
    ("World_B.png", "tileset_tower_source_primary.png", (0, 0, 768, 464)),
    ("World_C.png", "tileset_palace_source_primary.png", (0, 0, 512, 768)),
]

# Direct copies (already correct size)
DIRECT_COPIES = [
    ("Dungeon_B.png", "tileset_interior_generic_source_primary.png"),
]

SOURCE_DIR = "assets/sprites/tilesets"
TARGET_DIR = "img/tilesets"


def extract_tilesets():
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    # Process extractions
    for target, source, crop_box in EXTRACTION_MAP:
        source_path = os.path.join(SOURCE_DIR, source)
        target_path = os.path.join(TARGET_DIR, target)
        
        if not os.path.exists(source_path):
            print(f"❌ Source not found: {source}")
            continue
            
        try:
            with Image.open(source_path) as img:
                # Extract crop region
                cropped = img.crop(crop_box)
                
                # Resize to target dimensions if needed
                target_size = get_target_size(target)
                if cropped.size != target_size:
                    cropped = cropped.resize(target_size, Image.Resampling.LANCZOS)
                
                cropped.save(target_path, "PNG")
                print(f"✅ Created: {target} ({cropped.size[0]}x{cropped.size[1]})")
        except Exception as e:
            print(f"❌ Error processing {target}: {e}")
    
    # Process direct copies
    for target, source in DIRECT_COPIES:
        source_path = os.path.join(SOURCE_DIR, source)
        target_path = os.path.join(TARGET_DIR, target)
        
        if os.path.exists(source_path):
            with Image.open(source_path) as img:
                img.save(target_path, "PNG")
            print(f"✅ Copied: {target}")
        else:
            print(f"❌ Source not found: {source}")


def get_target_size(filename):
    """Return target dimensions based on RPG Maker sheet type"""
    if "_A1" in filename or "_A2" in filename:
        return (768, 576)
    elif "_A3" in filename or "_A4" in filename or "_A5" in filename:
        return (768, 768)
    elif "_B" in filename or "_C" in filename:
        return (768, 768)
    return (768, 768)


if __name__ == "__main__":
    print("=" * 60)
    print("Chroma's Edge - Tileset Extraction Tool")
    print("=" * 60)
    print(f"\nSource: {SOURCE_DIR}")
    print(f"Target: {TARGET_DIR}\n")
    
    extract_tilesets()
    
    print("\n" + "=" * 60)
    print("Done! Run validation:")
    print("  python tools/run_project_audit_gate.py")
    print("=" * 60)
