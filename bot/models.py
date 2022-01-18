from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    telegram_id: int 
    name: str


class Wish(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    cost: int
    about: Optional[str]
    link: Optional[str]

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
