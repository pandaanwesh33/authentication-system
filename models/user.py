from peewee import CharField, TextField
from models.base_model import BaseModel
from playhouse.postgres_ext import BinaryUUIDField
from passlib.hash import bcrypt_sha256
from database import db

class User(BaseModel):
    username : CharField(unique=True)
    email : CharField(unique=True)
    password : CharField()
