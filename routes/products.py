from fastapi import APIRouter

router = APIRouter()

products = ['abc']
@router.get('/products')
def get_products():
    return products

