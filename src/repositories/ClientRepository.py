from typing import List

from models.ClientModel import ClientModel
from schemas.ClientSchema import ClientSchema

class ClientRepository():
    """Classe responsável por gerenciar ações realizadas no banco de dados"""
    def create(clientData: ClientSchema):
        """Cria um cliente no banco de dados """
        return ClientModel.create(
            name=clientData.name,
            age=clientData.age,
            email=clientData.email
        )

    def get(id: int) -> ClientSchema:
      """Obtém um cliente do banco com base no id recebido"""
      return ClientModel \
            .filter(ClientModel.id == id) \
            .first()

    def get_all() -> List[ClientSchema]:
      """Obtém todos os clientes no banco de dados"""
      return list(ClientModel.select())

    def update(id: str, clientData: ClientSchema) -> int:
      """Atualiza os dados de um usuário no banco de dados"""
      return ClientModel \
            .update(clientData.dict()) \
            .where(ClientModel.id == id) \
            .execute()

    def delete(id: str) -> id:
      """Deleta os dados de um cliente no banco de dados"""
      return ClientModel \
            .delete() \
            .where(ClientModel.id == id) \
            .limit(1) \
            .execute()


    def get_by_email(email: str) -> ClientSchema:
      """Obtém um cliente com base no email único recebido"""
      return ClientModel \
            .filter(ClientModel.email == email) \
            .first()
