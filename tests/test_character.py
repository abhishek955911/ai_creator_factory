from utils.database import SessionLocal
from utils.models import Character


db = SessionLocal()

try:
    characters = db.query(Character).all()

    for character in characters:
        print("\nCharacter ID:", character.character_id)
        print("Name:", character.name)
        print("Age:", character.age)
        print("Fictional:", character.is_fictional)
        print("Niche:", character.niche)
        print("Visual:", character.visual_identity)

finally:
    db.close()