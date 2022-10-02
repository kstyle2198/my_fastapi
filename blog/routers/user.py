from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
# from ..database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
# from passlib.context import CryptContext
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=["User"]
)


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/',response_model= schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session= Depends(database.get_db)):
    # hashedPassword = user.get_password_hash(request.password)
    # new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create_user(request, db)

@router.get('/{id}',response_model= schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user(id:str, db: Session= Depends(database.get_db)):
    # user = db.query(models.User).filter(models.User.id==id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    # return user
    return user.get_user(id, db)

