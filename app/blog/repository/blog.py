from sqlalchemy.orm import Session
from blog import schemas, models
from fastapi import HTTPException, status


def get_all_post(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_post(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog

def create_post(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, description=request.description, user_id="1")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
def delete_post(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        blog.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

def update_post(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        blog.update(request.dict())
    db.commit()
    return 'updated successfully'
    
    
    