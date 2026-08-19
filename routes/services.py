from .data import products, Product, users, User

def get_specific_product(id):
    for i in range(len(products)):
        if products[i]['id'] == id :
            return products[i]
    else:
        return -1