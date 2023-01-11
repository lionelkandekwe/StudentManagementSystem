from pydantic import BaseModel,EmailStr
from datetime import datetime
class StudentBase(BaseModel):
    firstname: str
    lastname: str
    age: int
    faculty: str
    address: str
    handicap: bool = True

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id:int
    created_at: datetime
    class Config:
        orm_mode = True


#USER SCHEMAS
class UserBase(BaseModel):
    email:EmailStr
    password:str

class UserCreate(UserBase):
    pass

class UserOut(BaseModel):
   id:int
   email:EmailStr
   created_at: datetime
   class Config:
        orm_mode = True