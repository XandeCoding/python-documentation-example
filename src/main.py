from fastapi import FastAPI
import uvicorn

from config.database import database
from models.ClientModel import ClientModel
from routers.clientRouter import clientRouter

app = FastAPI()
app.include_router(clientRouter)

@app.on_event("startup")
def startup():
    database.connect()
    database.create_tables([ClientModel])
    database.close()

@app.on_event("shutdown")
def shutdown():
    if not database.is_closed():
        database.close()

if __name__ == '__main__':
    app = application = uvicorn.run(app, host='0.0.0.0', port=8000)