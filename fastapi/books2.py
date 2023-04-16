from fastapi import FastAPI,Body

from pydantic import BaseModel ,Field

app = FastAPI()


#created book objects
class Book:
    id: int
    title: str
    author :str
    descriptions :str
    rating : int
    
    #Initialzing the Constructor
    def __init__(self,id,title,author,descriptions,rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.descriptions = descriptions
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title :str = Field(min_length=3)
    author :str = Field(min_length=1)
    descriptions :str =  Field(min_length=1,max_length=100)
    rating : int = Field(gt=0,lt=6)
    



BOOKS =[
    Book(1,"Computer Science Pro","code with u","Very Hard",5),
    Book(2,"Be Fast with FastApi","code with u","Great book",4),
    Book(3,"Master Endpoints","code with u","Good Book",3),
    Book(4,"Book@1","code with u","desc@2",2),
    Book(5,"Book@2","code with u","desc@1",3)
]

@app.get("/books")
async def read_all_books():
    return BOOKS


#No data validations
# @app.post("/create-book")
# async def create_book(book_request= Body()):
#     BOOKS.append(book_request)


#Using pydantic BaseModel
@app.post("/create-book")
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.dict())  #converting the request to Book object
    BOOKS.append(new_book)
