from fastapi import FastAPI, Depends
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
        

@app.post("/blogs")
def create_blogs(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

