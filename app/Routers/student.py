from typing import List
from fastapi import Response,status, Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas,models


router=APIRouter(
    prefix="/students",
    tags=["Students"]
)

# GET ALL STUDENTS


@router.get("/",response_model=List[schemas.Student])
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return  students


# Register New Student
@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.Student)
def register_students(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

#GET STUDENT BY ID
@router.get("/{id}",response_model=schemas.Student)
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"student with {id} was not found")

    return student

# DELETE Student

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id)
    if student.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"student with id: {id} does not exist")
    student.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Student

@router.put("/{id}",response_model=schemas.Student)
def update_student(id: int, updated_student: schemas.StudentBase, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == id)
    student = student_query.first()
    if student == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with id: {id} does not exist")
    student_query.update(updated_student.dict(), synchronize_session=False)
    db.commit()

    return  student_query.first()

    