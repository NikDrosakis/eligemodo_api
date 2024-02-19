from fastapi.encoders import jsonable_encoder
from models import Book,insert,fetchall,update,fetch,delete
@router.get("/")
async def root():
    return {"message": "APIFAST first page"}
@router.get("/books/")
async def getallitems():
    res = fetchall()
    return jsonable_encoder(res)
@router.get("/books/{id}")
async def getoneitem(id):
    res = fetch(id)
    return jsonable_encoder(res)

@router.post("/books/")
async def create_book_endpoint(book: Book):
 id=insert(book)
 return jsonable_encoder({"message": f"Book created {id}"})

@router.put('/books/{id}')
async def update_book(id,book: Book):
    res = update(id,book)
    return jsonable_encoder({"message": f"Updated book {res}"})
@router.delete('/books/{id}')
async def delete_book(id):
    res = delete(id)
    return jsonable_encoder({"message": f"Deleted book {res}"})

#uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
