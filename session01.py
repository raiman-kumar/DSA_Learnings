from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def show():
    return 'hello world'

print(show())