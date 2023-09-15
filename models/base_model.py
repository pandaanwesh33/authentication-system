from peewee import Model
from database import db

class BaseModel(Model):
    class Meta:
        database = db
        only_save_dirty = True