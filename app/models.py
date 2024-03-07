from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float

#model for books table
class Books(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pub_year = Column(Integer)

#model for reviews table
class Reviews(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.book_id"))
    review_txt = Column(String)
    rating = Column(Float)