from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models
from blog.hashing import Hash
from blog.JWTtoken import create_access_token

def login(db:Session, email, password):
    user = db.query(models.User).filter(models.User.email== email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Invalid Credentials")
    if not Hash.verify(hashed_password=user.password, plain_password=password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= f"Invalid Credentials")   
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
