from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)



# @app.post("/blog", tags= ["Blog"], status_code=status.HTTP_201_CREATED)   # create Post API
# def create_post(request: schemas.Blog, db: Session= Depends(get_db)):
#     new_blog = models.Blog(title=request.title, description=request.description, user_id="1")
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get("/blog", response_model= List[schemas.ShowBlog], tags= ["Blog"])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get("/blog/{id}", response_model= schemas.ShowBlog,status_code=status.HTTP_200_OK, tags= ["Blog"])
# def get_post(id:str, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     return blog

# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
# def delete_post(id:str, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     else:
#         blog.delete(synchronize_session=False)
#     db.commit()
#     return "deleted successfully"

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
# def update_post(id:str, request: schemas.Blog, db: Session= Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     else:
#         blog.update(request.dict())
#     db.commit()
#     return 'updated successfully'


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# @app.post('/user',response_model= schemas.ShowUser, tags=["User"], status_code=status.HTTP_201_CREATED)
# def create_user(request: schemas.User, db: Session= Depends(get_db)):
#     hashedPassword = get_password_hash(request.password)
#     new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model= schemas.ShowUser, status_code=status.HTTP_200_OK, tags= ["User"])
# def get_user(id:str, db: Session= Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
#     return user
    