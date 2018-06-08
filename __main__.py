import asyncio
from auth.auth_server import AuthServer

if __name__ == '__main__':
    aserver = AuthServer()
    loop = asyncio.get_event_loop()
    loop.run_forever()
    loop.close()
