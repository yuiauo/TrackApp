from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)

from sqlalchemy.ext.asyncio import (
    AsyncAttrs
)

from app_types import Language


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    login: Mapped[str]
    password: Mapped[str]


class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[Language]
    title: Mapped[str]
    pages: Mapped[int]
    summary: Mapped[str | None]


class BookStateModel(Base):
    __tablename__ = 'book_states'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    read: Mapped[bool] = mapped_column(default=False)
    pages: Mapped[int]
    user_summary: Mapped[str | None]
    favorite: Mapped[bool] = mapped_column(default=False)
