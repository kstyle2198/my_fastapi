from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..repository import user
from datetime import datetime, timedelta


router = APIRouter(
    tags = ['Login']
)

@router.post('/login')
def login(request: schemas.Login, db:Session = Depends(database.get_db)):
    user1 = db.query(models.User).filter(models.User.email == request.username).first()
    if not user1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    if not user.verify_password(request.password, user1.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

    # generate the JWT token
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user1.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}







