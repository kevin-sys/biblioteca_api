from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    isbn: str

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]
    isbn: Optional[str]

    class Config:
        orm_mode = True

class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True
