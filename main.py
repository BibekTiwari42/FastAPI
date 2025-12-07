from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
app = FastAPI()

# @app.get("/")
# def hello_world():
#     # return {"message": "Hello, World!"}
#     return{'data': {'name':'Bibek'}}

# @app.get("/about")
# def about():
#     return "This is a sample FastAPI application."
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/blogs")
def get_blogs(limits:int , published:bool):
    if published:
        return {"data": "All Published Blogs"}
    return {"data": "{} Blogs from DB".format(limits)}

@app.get("/blogs/unpublished")
def get_unpublished_blogs():
    return {"data": "All Unpublished Blogs"}

@app.get("/blogs?limit=10&published=true")
def get_blog(id:int):
    return {"blog_id": id }

# @app.get("/blogs/{id}")
# def get_blog(id:int):
#     return {"blog_id": id }



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    tags: List[str] = []

@app.post("/blogs")
def create_blogs(blog: Blog):
    return {"data": "Blog is created with title {}".format(blog.title)}


