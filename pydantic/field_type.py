from pydantic import BaseModel,Field
from typing import Dict , List, Optional

class Cart(BaseModel):
    user_id : int
    items : List[int]
    quantities : Dict[str, int]

class BlogPost(BaseModel):
    title : str
    content: str
    img_url : Optional[str] = None    

class User(BaseModel):
    age : int = Field(
        ...,
        ge=0,
        lt=18,
        description="User age",
        examples=17
    )  
    name : str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="User name"
    ) 

user1 = User(**{"age":15, "name":"Padro"})    

