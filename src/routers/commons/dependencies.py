from fastapi import Depends

from config.database import database, db_state_default

async def _reset_db_state():
    database._state._state.set(db_state_default.copy())
    database._state.reset()

def get_db(db_state=Depends(_reset_db_state)):
    try:
        database.connect()
        yield
    finally:
        if not database.is_closed():
            database.close()