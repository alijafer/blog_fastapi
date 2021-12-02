from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication
from fastapi.responses import RedirectResponse
app = FastAPI()
@app.get('/', response_class=RedirectResponse)
def home():
    return "/docs"

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
models.Base.metadata.create_all(bind= engine)
