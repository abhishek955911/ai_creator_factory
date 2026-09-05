from typing import List
from pydantic import BaseModel, Field


class ContentIdea(BaseModel):
    content_type: str = Field(
        description="Type of Instagram content: photo or reel"
    )

    scene: str = Field(
        description="Detailed location and environment"
    )

    outfit: str = Field(
        description="Clothing and accessories"
    )

    activity: str = Field(
        description="What the character is doing"
    )

    caption: str = Field(
        description="Short Instagram caption"
    )


class ContentPlan(BaseModel):
    ideas: List[ContentIdea] = Field(
        description="Exactly 5 content ideas"
    )