
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return  blogs

def create(db:Session, title, body, user_id):
    new_blog = models.Blog(title= title, body= body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        "data": {"title": title, "body": body}
        }

def delete(db:Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id ==id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blogs with the id {id} is not found") 
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return {"done"}

def update(db:Session, id, title, body):
    blog = db.query(models.Blog).filter(models.Blog.id ==id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blogs with the id {id} is not found") 
    else:
        blog.update({'title': title, "body": body})
        db.commit()
        return {"update done"}

def showBlog(db:Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blogs with the id {id} is not found")
       # res.status_code = status.HTTP_404_NOT_FOUND
       # return {"detail": f"Blogs with the id {id} is not found"}
    return  blog