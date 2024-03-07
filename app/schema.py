from pydantic import BaseModel
from typing import List

#Payload validation with pydantic
class BookSchema(BaseModel):
    title: str
    author: str | None = None
    pub_year: int

class BooksSchema(BaseModel):
    books: List[BookSchema]

class ReviewSchema(BaseModel):
    book_id : int
    review_txt : str
    rating : float
