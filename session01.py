from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# call at 127.0.0.1:8000
@app.get('/') # from browser only get method will call 
def show():
    return 'hello world'

# for other route except get you need Swagger UI or API testing tool like Postman
# call at 127.0.0.1:8000/docs

@app.post('/user/{firstname}/') # path parameter
def user(firstname,lastname): # query parameter
    name = firstname + lastname
    return f'user name is {name}'

names = ['aman','rohit','sahil']
@app.delete('/user')
def user(name):
    names.remove(name)
    return names

users = [{"name":"rahul",
          "age":20},
          {"name":'ravi',
           "age":21}]

class User(BaseModel):
    name : str
    age : int

@app.get('/user/{name}')
def get_user(name):
    for i in range(len(users)):
        if users[i]['name'] == name :
            return users[i]

@app.post('/user')
def create_user(user : User):
    users.append(user)
    return users