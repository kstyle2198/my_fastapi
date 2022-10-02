from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
# from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags= ["Blog"]
)


@router.get("/", response_model= List[schemas.ShowBlog],)
def all(db:Session = Depends(database.get_db)):
    # blogs = db.query(models.Blog).all()
    # return blogs
    return blog.get_all_post(db)


@router.post("/", status_code=status.HTTP_201_CREATED)   # create Post API
def create_post(request: schemas.Blog, db: Session= Depends(database.get_db)):
    # new_blog = models.Blog(title=request.title, description=request.description, user_id="1")
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create_post(request, db)


@router.get("/{id}", response_model= schemas.ShowBlog,status_code=status.HTTP_200_OK)
def get_post(id:str, db:Session = Depends(database.get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # return blog
    return blog.get_post(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:str, db:Session = Depends(database.get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # else:
    #     blog.delete(synchronize_session=False)
    # db.commit()
    # return "deleted successfully"
    return blog.delete_post(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id:str, request: schemas.Blog, db: Session= Depends(database.get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # else:
    #     blog.update(request.dict())
    # db.commit()
    # return 'updated successfully'
    return blog.update_post(id, request, db)

