from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    pinCode:int


class User(BaseModel):
    id : int
    name : str
    address: Address

address = Address(street="1234", city="KOta", pinCode=1234)
vip_user = User(id = 1, name="You tube",address=address)   
print(vip_user)     