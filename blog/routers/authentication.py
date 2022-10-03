from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import user


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

    return user1






