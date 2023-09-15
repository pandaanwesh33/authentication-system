from peewee import Model, CharField, TextField
from playhouse.postgres_ext import BinaryUUIDField
from passlib.hash import bcrypt_sha256
from database import db

class User(Model):
    username : CharField(unique=True)
    email : CharField(unique=True)
    password : CharField()

    class Meta: 
        database = db
