import json
from pathlib import Path

from utils.database import SessionLocal
from utils.models import Character


CHARACTER_FILE = Path("characters/character_001.json")


with open(CHARACTER_FILE, "r", encoding="utf-8") as file:
    character_data = json.load(file)


db = SessionLocal()

try:
    existing = db.query(Character).filter(
    Character.character_id == character_data["id"]
     ).first()

    if existing:
        print("Character already exists.")
    else:
        character = Character(
            character_id=character_data["id"],
            name=character_data["name"],
            age=character_data["age"],
            is_fictional=character_data["is_fictional"],
            personality=json.dumps(character_data["personality"]),
            niche=json.dumps(character_data["niche"]),
            visual_identity=json.dumps(
                character_data["visual_identity"]
            )
        )

    db.add(character)
    db.commit()

    print("Character imported successfully.")

except Exception:
    db.rollback()
    raise

finally:
    db.close()