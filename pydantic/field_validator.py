from pydantic import BaseModel,field_validator,model_validator
from typing import Optional

class Tweet(BaseModel):
    tweet_id: Optional[int] = 1
    content : Optional[str] = None
    like_count : Optional[int] = 1
    retweet_count : Optional[int] = 2
    postedBy : str

    @field_validator('postedBy')
    def func(cls, v):
        if len(v) <= 10:
            raise ValueError("Name should be greater that 10 chars")
        return v
# t = Tweet(**{"postedBy":"ANa"})   

class Signup(BaseModel):
    password: str
    confirmPassword: str
    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirmPassword :
            raise ValueError("Passwords do not match")
        return values
user = {"password" : '123', "confirmPassword":"1253"}
u = Signup(**user)


