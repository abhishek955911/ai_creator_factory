from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Character(Base):
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    character_id: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    age: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    is_fictional: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    personality: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    niche: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    visual_identity: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )


from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Content(Base):
    __tablename__ = "content"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    character_id: Mapped[int] = mapped_column(
        ForeignKey("characters.id"),
        nullable=False
    )

    content_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    scene: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    outfit: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    activity: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    caption: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="planned",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )