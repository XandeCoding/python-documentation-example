import peewee

from config.database import database

class BaseModel(peewee.Model):

    class Meta:
        database = database

