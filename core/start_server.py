from auth.auth_server import AuthServer
from database.database import Database

from util.logger import Logger


class Server(object):
    logger = Logger('lego.py')

    def __init__(self):
        self.db = Database(b'MfUZyaOtwjTkcQR-llEy9hyBB6BrViT_tkqyQ8R-MUQ=')
        self.auth_server = AuthServer(database=self.db)
        self.logger.info('server started')
