from fastapi import APIRouter, Depends, status, HTTPException, Form
from blog import schemas, models, database
from sqlalchemy.orm import Session
from typing import List
from blog.repository import user


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post('/',response_model= schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session= Depends(database.get_db)):
    return user.create_user(request, db)

@router.get('/{id}',response_model= schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user(id:str, db: Session= Depends(database.get_db)):
    return user.get_user(id, db)

