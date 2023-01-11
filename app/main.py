from fastapi import FastAPI
from . import models,schemas
from .database import engine
from .Routers import student,user

# Create model
models.Base.metadata.create_all(bind=engine)

#  create an instance
app = FastAPI()

app.include_router(user.router)
app.include_router(student.router)



