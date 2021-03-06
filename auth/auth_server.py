from pyraknet.server import Server as RNServer
from pyraknet.server import Event as RNEvent
from core.packet_headers import PacketHeaders

from .packets.handshake import Handshake
from .packets.client_login_req import ClientLoginRequest

from util.logger import Logger


class AuthServer(RNServer):
    logger = Logger('AuthServer')

    def __init__(self, ip='127.0.0.1', port=1001, backlog=10000, password=b'3.25 ND1', database=None):
        super().__init__((ip, port), backlog, password)
        
        self.database = database

        self.add_handler(RNEvent.UserPacket, self.handle_packet)
        self.auth_handlers = {}

        self.register_handler(PacketHeaders.HANDSHAKE.value, Handshake)
        self.register_handler(PacketHeaders.CLIENT_LOGIN_REQ.value, ClientLoginRequest)

    def handle_packet(self, packet, address):
        header = packet[0:8]
        if header in self.auth_handlers:
            self.auth_handlers[header].database = self.database
            res = self.auth_handlers[header].construct_packet(self, packet)
            if res is not None:
                self.send(res, address)
            else:
                self.logger.warn('unable to construct packet for header-{}'.format(header))
        else:
            self.logger.warn('no registered handlers found for header-{}'.format(header))

    def register_handler(self, header, func):
        self.auth_handlers[header] = func
