from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic import BaseModel

from blogs.schemas import Blog
from . import models
from .database import engine, SessionLocal
from .models import Base
from sqlalchemy.orm import Session

# Create all tables
Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal(bind=engine)
    try:
        yield db
    finally:
        db.close()
        

@app.post("/blogs", status_code=status.HTTP_201_CREATED)
def create_blogs(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blogs", status_code=status.HTTP_200_OK)
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blogs/{id}", status_code=status.HTTP_200_OK)
def blog(id: int,response = Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Blog with the id {id} is not available')    
    # if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {'detail': f'Blog with the id {id} is not available'}
    return blog