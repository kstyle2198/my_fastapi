from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, models, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from blog.repository import blog 


router = APIRouter(
    prefix="/blog",
    tags= ["Blog"]
)


@router.get("/", response_model= List[schemas.ShowBlog],)
def all(db:Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all_post(db)


@router.post("/", status_code=status.HTTP_201_CREATED)   # create Post API
def create_post(request: schemas.Blog, db: Session= Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.create_post(request, db)


@router.get("/{id}", response_model= schemas.ShowBlog,status_code=status.HTTP_200_OK)
def get_post(id:str, db:Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_post(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:str, db:Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.delete_post(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id:str, request: schemas.Blog, db: Session= Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.update_post(id, request, db)

