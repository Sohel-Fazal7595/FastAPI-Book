from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.schema import BookSchema, BooksSchema, ReviewSchema
from app.models import Books, Reviews
from app.database import get_db

app = FastAPI()

@app.get("/book/getall")
async def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Books).all()
    if books:
        return books
    else:
        return {"Error": "No books found"}

@app.post("/book/create")
async def add_book(book : BookSchema, db: Session = Depends(get_db)):
    book = Books(title = book.title, author = book.author, pub_year = book.pub_year)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@app.post("/review/create")
async def create_review(review: ReviewSchema, db: Session = Depends(get_db)):
    review = Reviews(book_id = review.book_id, review_txt = review.review_txt, rating = review.rating)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

@app.get("/reivew/{book_id}")
async def get_reivew_by_book_id(book_id, db: Session = Depends(get_db)):
    try:
        reviews = db.query(Reviews).filter(Reviews.book_id == book_id).all()
        if reviews:
            return reviews
        else:
            return {"Error": "Book not found"}
    except Exception:
        return {"Error": "An exception occurred"}
    
@app.get("/books/{pub_year}")
async def get_book_by_publication_year(pub_year, db: Session = Depends(get_db)):
    try:
        books = db.query(Books).filter(Books.pub_year == pub_year).all()
        if books:
            return books
        else:
            return {"Error": "Book with given publication year not found"}
    except TypeError:
        return {"Error": "Invalid data type for publication year supplied"}
    except Exception:
        return {"Error": "Invalid publication year supplied"}

@app.get("/books/author/{author}")
async def get_book_by_author(author, db: Session = Depends(get_db)):
    try:
        books = db.query(Books).filter(Books.author == author).all()
        if books:
            return books
        else:
            return {"Error": "Book with given author not found"}
    except TypeError:
        return {"Error": "Invalid data type for author name supplied"}
    except Exception:
        return {"Error": "Invalid author name supplied"}
    
@app.delete("/book/{book_id}")
async def delete_book_by_book_id(book_id, db: Session = Depends(get_db)):
    try:
        books = db.query(Books).filter(Books.book_id == book_id).first()
        db.delete(books)
        db.commit()
        return {"Message": "Book deleted"}
    except Exception:
        return {"Error": "An exception occurred"}
    
@app.delete("/review/{review_id}")
async def delete_review_by_review_id(review_id, db: Session = Depends(get_db)):
    try:
        reviews = db.query(Reviews).filter(Reviews.review_id == review_id).first()
        db.delete(reviews)
        db.commit()
        return {"Message": "Review deleted"}
    except Exception:
        return {"Error": "An exception occurred"}







    