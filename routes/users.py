from fastapi import APIRouter
from .data import users, User

user_router = APIRouter()

@user_router.get('/')
def get_all_user():
    return users

@user_router.get('/{id}')
def get_specific_user(id):
    for i in range(len(users)):
        if users[i]['id'] == id :
            return users[i]

@user_router.post('/')
def create_user(user : User):
    users.append(user)

@user_router.delete('/{id}')
def delete_user(id):
    users.remove(id)