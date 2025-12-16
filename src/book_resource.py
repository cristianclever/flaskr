from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi import Header, HTTPException
import dependencies as deps
from pydantic import BaseModel


class Book(BaseModel):
    id: int| None = None
    title: str


router = APIRouter(
    prefix="/books",
    tags=["books"], # Optional: adds a tag for grouping in the API docs
    responses={ 204: {"description": "Not found"}, 200: {"description":"Success"}}
    #,dependencies = [Depends(deps.get_token_header)]
)

books = list([
    Book(  id=1,title= "Python Programming" ),
Book(  id=2,title= "Java Como Programar" ),
Book(  id=3,title= "EJB3 em ação" )

])


@router.get("/{book_id}", tags=["books"])
def get_book(book_id:int ,  response_model=Book) -> Book:
    if book_id is None:
        raise HTTPException(status_code=204, detail="Book not found")

    result = [b for b in books if b["id"]== book_id]

    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Book not found")




@router.post("/", tags=["books"])
def save_book(book:Book) -> Book:

    if book.title is None:
        raise HTTPException(status_code=400, detail="invalid Book title")

    books.append(book)
    book.id = len(books)+1


    return book
