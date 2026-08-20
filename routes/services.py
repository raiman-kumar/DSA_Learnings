from .data import products, users

# for product
def get_specific_product(id):
    try:
        for i in range(len(products)):
            if products[i]['product_id'] == id:
                return products[i]
        else:
            return -1
    except Exception as e:
        return e

def create_new_product(product):
    try:
        products.append(product)
    except Exception as e:
        return e

# for user
def get_specific_user(id):
    try:
        for i in range(len(users)):
            if users[i]['id'] == id:
                return users[i]
        else:
            return -1
    except Exception as e:
        return e

def create_new_user(user):
    try:
        users.append(user)
    except Exception as e:
        return e