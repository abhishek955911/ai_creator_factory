from utils.database import SessionLocal
from utils.models import Character, Content


def save_content_plan(character_id: str, content_plan):
    db = SessionLocal()

    try:
        # Find character
        character = (
            db.query(Character)
            .filter(Character.character_id == character_id)
            .first()
        )

        if not character:
            raise ValueError(
                f"Character '{character_id}' not found"
            )

        # Save every content idea
        for idea in content_plan.ideas:

            content = Content(
                character_id=character.id,
                content_type=idea.content_type,
                scene=idea.scene,
                outfit=idea.outfit,
                activity=idea.activity,
                caption=idea.caption,
                status="planned"
            )

            db.add(content)

        db.commit()

        print(
            f"Saved {len(content_plan.ideas)} "
            f"content ideas for {character.name}"
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()