from fastapi import FastAPI

app = FastAPI()

book_database = [
    "Dom Quixote - Miguel de Cervantes",
    "Cem Anos de Solidão - Gabriel García Márquez",
    "1984 - George Orwell",
    "O Pequeno Príncipe - Antoine de Saint-Exupéry",
    "Harry Potter e a Pedra Filosofal - J.K. Rowling"
]

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
    return {'books': book_database [index]}



# /add-book -> adicionar novo livro