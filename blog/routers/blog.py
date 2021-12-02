from sys import prefix
from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from ..schemas import ShowBlog, Blog, ShowUser
from .. import models, database
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

@router.get("/", response_model=List[ShowBlog] )
def get_all_blog(db:Session = Depends(get_db)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def creat_blog(re:Blog, db:Session = Depends(get_db)):
    return blog.create(db=db,title= re.title, body= re.body, user_id=1)

@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id:int, db:Session= Depends(get_db)):
    return blog.delete(db=db, id=id)

@router.put('/{id}', status_code=status.HTTP_201_CREATED)
def update_blog(id:int, req:Blog, db:Session= Depends(get_db)):
    return blog.update(db=db, id=id, title=req.title, body=req.body)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show_blog(id:int, res:Response, db:Session = Depends(get_db)):
   return blog.showBlog(db=db, id=id)
