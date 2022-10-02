from pydantic import BaseModel  # create model
class Blog(BaseModel):
    title: str
    description: str