from sqlalchemy.orm import Session
from blog import schemas, models
from fastapi import HTTPException, status
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(request: schemas.User, db: Session):
    hashedPassword = get_password_hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    duplicate_user_check = db.query(models.User).filter(models.User.email==request.email).first()
    if not duplicate_user_check: 
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"이미 등록된 이메일입니다.")
        

def get_user(id:str, db: Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user