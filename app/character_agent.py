import json
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# -----------------------------
# Structured output schema
# -----------------------------

class ContentIdea(BaseModel):
    content_type: str = Field(description="Photo or Reel")
    scene: str
    outfit: str
    activity: str
    caption: str


class ContentPlan(BaseModel):
    ideas: List[ContentIdea]


# -----------------------------
# Load character
# -----------------------------

CHARACTER_FILE = Path("characters/character_001.json")

with open(CHARACTER_FILE, "r", encoding="utf-8") as file:
    character = json.load(file)


# -----------------------------
# LLM
# -----------------------------

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0.7
)


# -----------------------------
# Structured LLM
# -----------------------------

structured_llm = llm.with_structured_output(ContentPlan)


# -----------------------------
# Prompt
# -----------------------------

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
- The character is 22 years old.
- Keep her identity consistent.
- Keep her personality consistent.
- Keep her niche consistent.
- Generate realistic social-media content.
"""
    ),
    (
        "human",
        """
Create exactly 5 Instagram content ideas.

For each idea provide:
- content_type: Photo or Reel
- scene
- outfit
- activity
- short caption

Return only the structured output.
"""
    )
])


# -----------------------------
# Run chain
# -----------------------------

character_text = json.dumps(
    character,
    indent=2,
    ensure_ascii=False
)

chain = prompt | structured_llm

result = chain.invoke({
    "character": character_text
})


# -----------------------------
# Print result
# -----------------------------

print("\n========== MAYA'S CONTENT PLAN ==========\n")

for i, idea in enumerate(result.ideas, start=1):
    print(f"\n--- IDEA {i} ---")
    print(f"Type     : {idea.content_type}")
    print(f"Scene    : {idea.scene}")
    print(f"Outfit   : {idea.outfit}")
    print(f"Activity : {idea.activity}")
    print(f"Caption  : {idea.caption}")