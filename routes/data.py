from pydantic import BaseModel

class Product(BaseModel):
    product_id : int
    product_name : str
    product_price : float

products = [{'product_id':1,
             'product_name':'moniter',
             'product_price':10000.00},
             {'product_id':2,
             'product_name':'keyboard',
             'product_price':5000.00},
             {'product_id':3,
             'product_name':'mouse',
             'product_price':1000.00}]

class User(BaseModel):
    id : int
    name : str
    age : int

users = [{'id':1,
          "name":"rahul",
          "age":20},
          {'id':2,
           "name":'ravi',
           "age":21}]