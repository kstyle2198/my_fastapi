from pydantic import BaseModel  # create model


class Blog(BaseModel):
    title: str
    description: str
    
class ShowBlog(Blog):
    class Config():
        orm_mode = True
    pass

class User(BaseModel):
    name: str
    email: str
    password: str