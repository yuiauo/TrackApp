from pydantic import BaseModel

from app_types import Genre, Language


class UserModel(BaseModel):
    """ Поля пользователя """
    id: int
    full_name: str
    login: str
    states: list["BookStateModel"]
    password: str

class BookModel(BaseModel):
    """ Поля книги """
    id: int
    category: Language
    genre: Genre
    title: str
    pages: int
    chapters: list["ChapterModel"]
    summary: str | None

class ChapterModel(BaseModel):
    """ Отдельные главы книги """
    id: int
    title: str
    book_id: int
    start_page: int
    end_page: int

class BookStateModel(BaseModel):
    """ Модель состояния книги привязка к юзеру """
    id: int
    user_id: int
    book_id: int
    read: bool
    pages: int
    user_summary: str
    favorite: bool
