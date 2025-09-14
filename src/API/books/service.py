from .model import Book
from sqlalchemy.orm import Session
from .schema import BookCreate

def createBook(db:Session, data: BookCreate) :
    newBook = Book(**data.model_dump())
    db.add(newBook)
    db.commit()
    db.refresh(newBook)
    return newBook

def getBooks(db:Session) :
    return db.query(Book).all()

def getBookById(db:Session, bookId:int) :
    return db.filter(Book).filter(Book.id == bookId).first()

def updateBookById(db:Session,data:BookCreate, bookId:int):
    book = db.filter(Book).filter(Book.id == bookId).first()
    if book:
        for key,value in data.model_dump().items():
            setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def deleteBook(db:Session, bookId:int):
    book = db.filter(Book).filter(Book.id == bookId).first()
    if book:
        db.delete(book)
        db.commit()
    return book