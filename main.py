from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def index():
    return {
        "data" : "blog list"
    }

@app.get("/blog")
def about(limit= 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {
            "data" : f"{limit} published blogs from db."
        }
    else:
        return {
            "data" : f"{limit} blogs from db."
        }

@app.get("/blog/unpublished")
def unpublised():
    return {
        'data': {"all unpublished blogs"}
    }

@app.get("/blog/{id}")
def about(id:int):
    return {
        "data" : id
    }


@app.get("/blog/{id}/comment")
def comments(id):
    return {
        "data" : {"comments":{"1", "2"}}
    }

class Blog(BaseModel):
    titel : str
    body: str
    published: Optional[bool]

@app.post('/blog')
def creat_blog(req: Blog):
    return {
        'data': f'Blog is created {req.titel}'
    }