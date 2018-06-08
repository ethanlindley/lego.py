import asyncio
from auth.auth_server import AuthServer
from database.database import Database

if __name__ == '__main__':
    db = Database()
    aserver = AuthServer()

    loop = asyncio.get_event_loop()
    loop.run_forever()
    loop.close()
