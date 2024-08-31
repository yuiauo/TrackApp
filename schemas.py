from pydantic import BaseModel

from app_types import Language


class UserModel(BaseModel):
    """ Поля пользователя """
    id: int
    full_name: str
    login: str
    password: str
    favorite: list[int]


class BookModel(BaseModel):
    """ Поля книги """
    id: int
    category: Language
    title: str
    pages: int


class BookStateModel(BaseModel):
    user_id: int
    book_id: int
    read: bool
    pages: int
    summary: str

