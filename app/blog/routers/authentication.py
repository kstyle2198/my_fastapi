from fastapi import APIRouter, Depends, HTTPException, status
from blog import schemas, database, models, token, oauth2
from sqlalchemy.orm import Session
from blog.repository import user
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    tags = ['Login']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db:Session = Depends(database.get_db)):
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







