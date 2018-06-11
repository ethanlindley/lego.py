from auth.auth_server import AuthServer
from world.world_server import WorldServer
from database.database import Database

from util.logger import Logger


class Server(object):
    logger = Logger('lego.py')

    def __init__(self):
        db = Database('$2a$12$DuLWTxWJ.WdWrbIYKf7Es.')
        auth_server = AuthServer(port=1001, database=db)
        world_server = WorldServer(port=2002, database=db)
        self.logger.info('server started')
