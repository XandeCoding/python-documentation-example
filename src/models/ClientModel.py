import peewee

from models.BaseModel import BaseModel

class ClientModel(BaseModel):
    name = peewee.CharField()
    age = peewee.IntegerField()
    email = peewee.CharField(unique=True, index=True)