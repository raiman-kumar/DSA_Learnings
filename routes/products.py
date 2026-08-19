from fastapi import APIRouter
from .data import products, Product
from .services import get_specific_product

product_router = APIRouter()

@product_router.get('/')
def get_all_products():
    return products

@product_router.get('/{id}')
def get_single_product(id):
    val = get_specific_product(id)
    if val != -1:
        return val
    else:
        return {"message":"product not found"}

@product_router.post('/')
def create_product(product : Product):
    products.append(product)

@product_router.delete('/{id}')
def delete_product(id):
    products.remove(id)