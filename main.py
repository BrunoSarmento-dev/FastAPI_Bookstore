import json
from typing import Optional, Literal
from uuid import uuid4
from fastapi import FastAPI
import os
from fastapi import HTTPException
import random
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class Book(BaseModel):
    name: str
    price: float
    id: Optional[str] = uuid4().hex
    genre: Literal['fiction', 'non-fiction']


books_file = 'books.json'

# Maneira anterior de salvar os livros
book_database = []


if os.path.exists(books_file):
    with open(books_file, 'r') as f:
        book_database = json.load(f)


# /      -> Boas vindas!
@app.get('/')
async def home():
    return 'Welcome to my bookstore'


# /list-books -> Listar todos os livros
@app.get('/list-books')
async def list_books():
    return {'books': book_database}


# /list-book-by-index{index} -> listar 1 livro
@app.get('/list-book-by-index/{index}')
async def list_book_by_index(index: int):
    if index < 0 or index >= len(book_database):
        raise HTTPException(404, "Index out of range")  # Error
    return {'books': book_database[index]}


# /get-random-book -> livro aleátorio
@app.get('/get-random-book')
async def get_random_book():
    return random.choice(book_database)


# /add-book -> adicionar novo livro
@app.post('/add-book')
async def add_book(book: Book):
    json_book = jsonable_encoder(book)
    book_database.append(json_book)
    with open(books_file, 'w') as f:
        json.dump(book_database, f)
    return f' Book {book} was added'
