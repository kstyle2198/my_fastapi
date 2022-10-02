from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
# from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext


router = APIRouter()


@router.get("/blog", response_model= List[schemas.ShowBlog], tags= ["Blog"])
def all(db:Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post("/blog", tags= ["Blog"], status_code=status.HTTP_201_CREATED)   # create Post API
def create_post(request: schemas.Blog, db: Session= Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, description=request.description, user_id="1")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/blog/{id}", response_model= schemas.ShowBlog,status_code=status.HTTP_200_OK, tags= ["Blog"])
def get_post(id:str, db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog

@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
def delete_post(id:str, db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        blog.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
def update_post(id:str, request: schemas.Blog, db: Session= Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        blog.update(request.dict())
    db.commit()
    return 'updated successfully'

