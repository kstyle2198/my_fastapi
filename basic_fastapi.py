from fastapi import FastAPI
import uvicorn

app = FastAPI()

#--- Get API ---
@app.get("/")
def post_list():
    context = {'data': 'blog list'}
    return context

#--- Path Parameter ---
@app.get("/blog/{id}")
def post_detail(id:str):
    context = {'data': id}
    return context

#--- Query Parameter ---
@app.get("/blog")
def post_detail(limit:int):
    context = f"You have {limit} lists "
    return context

#--- Post API ---
from pydantic import BaseModel  # create model
class Blog(BaseModel):
    id: str
    name: str
    job: str

@app.post("/blog")   # create Post API
def create_post(blog: Blog):
    context = f"Blog has been created with the name of {blog.name}"
    return context

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)