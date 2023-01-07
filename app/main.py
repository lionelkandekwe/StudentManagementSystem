from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db


# Create model
models.Base.metadata.create_all(bind=engine)

#  create an instance
app = FastAPI()


# GET ALL STUDENTS


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return {"data": students}
