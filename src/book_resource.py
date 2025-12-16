from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi import Header, HTTPException
import dependencies as deps



router = APIRouter(
    prefix="/books",
    tags=["items"], # Optional: adds a tag for grouping in the API docs
    responses={ 204: {"description": "Not found"}, 200: {"description":"Success"}}
    #,dependencies = [Depends(deps.get_token_header)]
)

books = list([
    {"id": 1, "title": "Python Programming"},
    {"id": 2, "title": "Python Programming 2"},
    {"id": 3, "title": "Python Programming 3"},
    {"id": 4, "title": "Python Programming 4"}
])


@router.get("/{book_id}", tags=["books"])
def get_book(book_id:int):
    if book_id is None:
        raise HTTPException(status_code=204, detail="Book not found")

    result = [b for b in books if b["id"]== book_id]

    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Book not found")



