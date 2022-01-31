from schemas.ORMBaseSchema import ORMBaseSchema

class ClientSchema(ORMBaseSchema):
    name: str
    age: int
    email: str