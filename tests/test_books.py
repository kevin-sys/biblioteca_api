import pytest
from fastapi.testclient import TestClient
from main import app  # Asegúrate de que tu aplicación se importe desde aquí

client = TestClient(app)

# Test para verificar que el servidor está funcionando
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API de la Biblioteca"}

# Test para crear un libro
def test_create_book():
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "year": 2023,
        "isbn": "676764733"
    }

    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == book_data["title"]
    assert response.json()["author"] == book_data["author"]

# Test para listar todos los libros
def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Asegúrate de que la respuesta es una lista
