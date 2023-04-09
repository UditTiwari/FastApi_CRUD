from fastapi import Body , FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get('/')
async def real_all_books():
    return BOOKS 

# @app.get("/books/{book_title}")
# async def read_book(book_title:str):
#     return {'book_title':book_title}

#Path Parameters
@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

#Query Paramerters
@app.get('/books/')
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


'''Get all the books from specific author using path or query parameters'''

# @app.get("/books/byauthor/{author}")
#if we just removed {author} then it will take author as query parameters
@app.get("/books/byauthor/")
async def read_books_by_author_path(author:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    
    return books_to_return


'''before ('/books/{book_author}/') so query parameter can work'''

#Path and Query parameters both
@app.get('/books/{book_author}/')
async def read_author_category_query(book_author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold() :
            books_to_return.append(book)
    return books_to_return


#POST method - used to create data
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


#PUT method - used to update data
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


#DELETE method
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break



# '''Get all the books from specific author using path or query parameters'''

# # @app.get("/books/byauthor/{author}")
# #if we just removed {author} then it will take author as query parameters
# @app.get("/books/byauthor/")
# async def read_books_by_author_path(author:str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('author').casefold() == author.casefold():
#             books_to_return.append(book)
    
#     return books_to_return


@app.get('/route')
async def all_data(title):
    return {'postgreas_pipeline':title}



