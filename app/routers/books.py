from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import SessionLocal
from app.models import Book
from app.schemas import BookCreate, BookUpdate, BookResponse

# Crear el enrutador
router = APIRouter(prefix="/books", tags=["Books"])

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un libro
@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Listar libros con filtro opcional
@router.get("/", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def list_books(author: Optional[str] = None, year: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(Book)
    if author:
        query = query.filter(Book.author == author)
    if year:
        query = query.filter(Book.year == year)
    return query.all()

# Actualizar un libro
@router.put("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    for key, value in book_update.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

# Eliminar un libro
@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    db.delete(db_book)
    db.commit()
    return {"detail": "Libro eliminado exitosamente"}

# Buscar libros por título o autor
@router.get("/search", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def search_books(title: Optional[str] = None, author: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    return query.all()
