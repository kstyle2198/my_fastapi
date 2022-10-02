from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", tags= ["Blog"], status_code=status.HTTP_201_CREATED)   # create Post API
def create_post(request: schemas.Blog, db: Session= Depends(get_db)):
    new_blog = models.Blog(title=request.title, description=request.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", tags= ["Blog"])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=200, tags= ["Blog"])
def get_post(id:str, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
def delete_post(id:str, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return "done"
    
    