from pydantic import BaseModel,field_validator

class Person(BaseModel):
    first_name:str
    last_name:str

    @field_validator('first_name','last_name')
    def must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError("Names Must be Capitalized")
        return v

# person = Person(**{"first_name":"effefwe","last_name":"efaefaf"})    
# person = Person(first_name="fewfe",last_name='fewwf')    

# # print(person)
# person.first_name="efe"
# person.last_name="efeswf"

# print(person)

# Normally you want to save emails in lowercase in db and after removing spaces
class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize(cls,v):
        return v.lower().strip()

user = User(email="Deed@deed.com   ")
print(user.email)


# $4.44 -- > 4.44
class Product(BaseModel):
    price: str

    @field_validator('price',mode='before')
    def parse(cls, v):
        return float(v.replace('$',''))

product = Product(price="$4.44")
print(product)