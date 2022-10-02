from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", tags= ["Blog"], status_code=status.HTTP_201_CREATED)   # create Post API
def create_post(request: schemas.Blog, db: Session= Depends(get_db)):
    new_blog = models.Blog(title=request.title, description=request.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", response_model= List[schemas.ShowBlog], tags= ["Blog"])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", response_model= schemas.ShowBlog,status_code=status.HTTP_200_OK, tags= ["Blog"])
def get_post(id:str, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
def delete_post(id:str, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        blog.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
def update_post(id:str, request: schemas.Blog, db: Session= Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        blog.update(request.dict())
    db.commit()
    return 'updated successfully'
    
    