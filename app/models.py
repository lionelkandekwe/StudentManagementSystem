from .database import Base
from sqlalchemy import Column, INTEGER, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text



class Student(Base):
    __tablename__ = "students"
    id = Column(INTEGER, primary_key=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(INTEGER, nullable=False)
    faculty = Column(String, nullable=False)
    address = Column(String, nullable=False)
    handicap = Column(Boolean, server_default="False", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

class User(Base):
    __tablename__="users"
    id = Column(INTEGER, primary_key=True, nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )