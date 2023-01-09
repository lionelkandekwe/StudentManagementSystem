from pydantic import BaseModel

class StudentBase(BaseModel):
    firstname: str
    lastname: str
    age: int
    faculty: str
    address: str
    handicap: bool = True

class StudentCreate(StudentBase):
    pass