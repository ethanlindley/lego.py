import asyncio
from core.start_server import Server


if __name__ == '__main__':
    server = Server()

    loop = asyncio.get_event_loop()
    loop.run_forever()
    loop.close()
