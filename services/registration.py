from fastapi import APIRouter, Depends, HTTPException
from database import db
from pydantic import BaseModel
from models.user import User  # Import your User model
from passlib.hash import bcrypt  # Import the password hashing library

router = APIRouter()

# pydantic model for validation while creating user
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register", response_model=UserCreate)
async def user_registration(user: UserCreate):
    # check if user already exist
    existing_user = User.select().where(
        (user.username == User.username) | (user.email == User.email)
    ).first()

    if(existing_user):
        raise HTTPException(
            status_code = 400, 
            description = "User already exists" 
        )
    
    # hash the password before storing to db
    hashed_password = bcrypt.hash(user.password)

    # create a new user => create saves new_user to db
    new_user = User.create(
        username = user.username,
        email = user.email,
        password = hashed_password
    )

    return new_user
