from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def show():
    return 'hello world'

@app.post('/user/{username}/')
def user(username):
    name = username
    return f'user name is {name}'

