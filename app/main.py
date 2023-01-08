from fastapi import FastAPI, status, Depends,HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .models import StudentModel


# Create model
models.Base.metadata.create_all(bind=engine)

#  create an instance
app = FastAPI()


# GET ALL STUDENTS


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return {"data": students}


# Register New Student
@app.post("/students", status_code=status.HTTP_201_CREATED)
def register_students(student: StudentModel, db: Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"data": new_student}

#GET STUDENT BY ID
@app.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"student with {id} was not found")

    return {"data": student}