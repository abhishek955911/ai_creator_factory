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