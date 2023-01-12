from fastapi import APIRouter,status,Depends,HTTPException,Response
from sqlalchemy.orm import Session
from .. import database,models,utils,OAuth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(database.get_db)):
   user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()
   if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
   if not utils.verify_password(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
   #Create Token
   access_token=OAuth2.create_access_token(data={"user_id": user.id})
   #Return Token
   return{"access_token": access_token, "token_type": "bearer"}


