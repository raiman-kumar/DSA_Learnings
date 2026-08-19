from fastapi import FastAPI
from routes.products import product_router
from routes.users import user_router

app = FastAPI()

# call at 127.0.0.1:8000
@app.get('/') # from browser only get method will call 
def show():
    return {'greet':'welcome to my e commerce plateform'}

# for other route except get you need Swagger UI or API testing tool like Postman
# call at 127.0.0.1:8000/docs

# CRUD operation using FastAPI

app.include_router(product_router,prefix='/products',tags=['products'])
app.include_router(user_router,prefix='/users',tags=['users'])
