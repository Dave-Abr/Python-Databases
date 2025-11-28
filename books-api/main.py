from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.get("/")
def get_root():
    return "Welcome to the Books API"

@app.post("/book/")
def create_book(request: schemas.BookAuthorPayload):
    return "New book created " + request.book.title + " " + str(request.book.number_of_pages) + \
           " by " + request.author.first_name + " " + request.author.last_name