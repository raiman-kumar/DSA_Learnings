from fastapi import APIRouter
from .data import users
from .schema import User
from .services import create_new_user, get_specific_user

user_router = APIRouter()

@user_router.get('/')
def get_all_user():
    return users

@user_router.get('/{id}')
def get_single_user(id : int):
    val = get_specific_user(id)
    if val == -1:
        return {"message":"user not found"}
    else:
        return val

@user_router.post('/')
def create_user(user : User):
    create_new_user(user)

@user_router.delete('/{id}')
def delete_user(id):
    users.remove(id)