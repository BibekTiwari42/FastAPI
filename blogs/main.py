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

