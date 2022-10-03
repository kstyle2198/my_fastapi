from pydantic import BaseModel  # create model
from typing import List


class BlogBase(BaseModel):
    title: str
    description: str
        
class Blog(BlogBase):

    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    
    class Config():
        orm_mode = True
    
class ShowBlog(BaseModel):
    title: str
    description: str
    creator: ShowUser
    
    class Config():
        orm_mode = True
    pass

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str

    

