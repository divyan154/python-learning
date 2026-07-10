from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name: str
    price: float
    in_stock: bool = True

product_one = {"id" : 1, "name":"Laptop" , "price":99.98 , "in_stock":False}
p1 = Product(**product_one)
print(p1)

product_two = Product(**{"id":2,"name":"keyboard","price":80.90})
print(product_two)

product_three = Product(**{"name":"Mouse"})