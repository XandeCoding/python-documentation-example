from typing import List

from models.ClientModel import ClientModel
from schemas.ClientSchema import ClientSchema

class ClientRepository():
    def create(clientData: ClientSchema):
        return ClientModel.create(
            name=clientData.name,
            age=clientData.age,
            email=clientData.email
        )

    def get(id: int) -> ClientSchema:
      return ClientModel \
            .filter(ClientModel.id == id) \
            .first()

    def get_all() -> List[ClientSchema]:
      return list(ClientModel.select())

    def update(id: str, clientData: ClientSchema) -> int:
      return ClientModel \
            .update(clientData.dict()) \
            .where(ClientModel.id == id) \
            .execute()

    def delete(id: str) -> id:
      return ClientModel \
            .delete() \
            .where(ClientModel.id == id) \
            .limit(1) \
            .execute()


    def get_by_email(email: str) -> ClientSchema:
      return ClientModel \
            .filter(ClientModel.email == email) \
            .first()
