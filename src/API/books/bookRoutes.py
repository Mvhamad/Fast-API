from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schema, service
from db import get_db

# Créer un router pour les routes de livres
router = APIRouter(
    prefix="/books",  # Préfixe pour toutes les routes
    tags=["books"],   # Tag pour la documentation Swagger
)

@router.post("/new-book", response_model=schema.Book)
def create_a_book(data: schema.BookCreate, db: Session = Depends(get_db)):
    return service.createBook(db, data)

@router.get("/", response_model=list[schema.Book])
def get_all_books(db: Session = Depends(get_db)):
    books = service.getBooks(db)
    if books:
        return books
    raise HTTPException(status_code=404, detail='Books not found')

@router.get("/{id}", response_model=schema.Book)
def get_a_book(id: int, db: Session = Depends(get_db)):
    book = service.getBookById(db, id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/update/{id}", response_model=schema.Book)
def update_a_book(id: int, data: schema.BookCreate, db: Session = Depends(get_db)):
    updatedBook = service.updateBookById(db, data, id)
    if updatedBook:
        return updatedBook
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/delete/{id}", response_model=schema.Book)
def delete_a_book(id: int, db: Session = Depends(get_db)):
    deletedBook = service.deleteBook(db, id)
    if not deletedBook:
        raise HTTPException(status_code=404, detail="Book not found")
    return deletedBook