import json
from pathlib import Path

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from app.content_service import save_content_plan

from app.dtos import ContentPlan


CHARACTER_FILE = Path("characters/character_001.json")

with open(CHARACTER_FILE, "r", encoding="utf-8") as file:
    character = json.load(file)


llm = ChatOllama(
    model="qwen3:8b",
    temperature=0.7
)

structured_llm = llm.with_structured_output(ContentPlan)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are the content planning AI for a fictional AI creator.

Follow the character profile exactly.

Character profile:
{character}

Rules:
- The character is fictional.
- Keep her identity consistent.
- Keep her personality consistent.
- Keep her niche consistent.
"""
    ),
    (
        "human",
        """
Create exactly 5 Instagram content ideas.

For each idea provide:
- content_type
- scene
- outfit
- activity
- caption
"""
    )
])


chain = prompt | structured_llm

result = chain.invoke({
    "character": json.dumps(
        character,
        indent=2,
        ensure_ascii=False
    )
})

save_content_plan(
    character_id=character["id"],
    content_plan=result
)



for i, idea in enumerate(result.ideas, start=1):
    print(f"\n--- IDEA {i} ---")
    print(idea)