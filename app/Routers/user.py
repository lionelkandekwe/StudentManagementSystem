from fastapi import status, Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas,models

router=APIRouter()
#CREATE USER
@router.post("/users", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#GET USER BY ID
@router.get("/users/{id}",response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with {id} was not found")

    return user