from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.API.books import model, schema, service
from db import get_db, engine, Base,create_table

app = FastAPI()

create_table()
# Base.metadata.create_all(bind=engine)

@app.post("/new-book", response_model=schema.Book)
def creat_a_book(data: schema.BookCreate, db:Session=Depends(get_db)):
    return service.createBook(db, data)

@app.get("/books/", response_model=list[schema.Book])
def get_all_books(db:Session=Depends(get_db)):
    books = service.getBooks(db)
    if books :
        return books
    raise HTTPException(status_code=404, detail='Books not found')

@app.get("/book/{id}", response_model=schema.Book)
def get_a_book(id:int,db:Session=Depends(get_db)):
    book = service.getBookById(db,id)
    if book :
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/update-book/{id}", response_model=schema.Book)
def update_a_book(id:int,data: schema.BookCreate,db:Session=Depends(get_db)):
    updatedBook = service.updateBookById(db,data,id)
    if updatedBook :
        return updatedBook
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete('/delete-book/{id}', response_model=schema.Book)
def delete_a_book(id:int, db:Session=Depends(get_db)):
    deletedBook = service.deleteBook(db, id)
    if not deletedBook:
        raise HTTPException(status_code=404, detail="Book not found")