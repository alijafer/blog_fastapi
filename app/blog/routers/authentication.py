from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from blog.schemas import Login
from blog import models, database
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.repository import auth
from fastapi.security import  OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=['login']
)

@router.post('/')
def login(req:OAuth2PasswordRequestForm= Depends(),db:Session = Depends(get_db)):

    return auth.login(db=db, email=req.username, password=req.password)