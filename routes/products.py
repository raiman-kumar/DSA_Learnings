from fastapi import APIRouter
from .data import products
from .schema import Product
from .services import get_specific_product, create_new_product

product_router = APIRouter()

@product_router.get('/')
def get_all_products():
    return products

@product_router.get('/{id}')
def get_single_product(id :int):
    val = get_specific_product(id)
    if val == -1:
        return {"message":"product not found"}
    else:
        return val

@product_router.post('/')
def create_product(product : Product):
    create_new_product(product)

@product_router.delete('/{id}')
def delete_product(id):
    products.remove(id)