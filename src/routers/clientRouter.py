from typing import List
from fastapi import APIRouter, Depends
from http.client import HTTPException

from repositories.ClientRepository import ClientRepository
from routers.commons.dependencies import get_db
from schemas.ClientSchema import ClientSchema

clientRouter = APIRouter(
  prefix='/client',
  tags=["client"],
  dependencies=[Depends(get_db)]
)

@clientRouter.post('/', response_model=ClientSchema)
def create(client: ClientSchema):
  db_client = ClientRepository.get_by_email(client.email)
  if db_client:
      raise HTTPException(status_code=400, detail="Email already registered")
  return ClientRepository.create(client)

@clientRouter.get('/{id}', response_model=ClientSchema)
async def get(id: str):
  return ClientRepository.get(id)

@clientRouter.get('/', response_model=List[ClientSchema])
async def get_all():
  return ClientRepository.get_all()

@clientRouter.put('/{id}')
async def update(id: str, client: ClientSchema) -> int:
  db_client = ClientRepository.get(id)
  if not db_client:
      raise HTTPException(status_code=400, detail="Client don't exist")
  return ClientRepository.update(id, client)

@clientRouter.delete('/{id}')
async def delete(id: str) -> id:
  db_client = ClientRepository.get(id)
  if not db_client:
      raise HTTPException(status_code=400, detail="Client don't exist")
  return ClientRepository.delete(id)
