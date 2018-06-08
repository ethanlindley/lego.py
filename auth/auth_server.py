from pyraknet.server import Server as RNServer
from pyraknet.server import Event as RNEvent
from .packets.handshake import Handshake
from core.packet_headers import PacketHeaders

from util.logger import Logger


class AuthServer(RNServer):
    logger = Logger('AuthServer')

    def __init__(self, ip='127.0.0.1', port=1001, backlog=10000, password=b'3.25 ND1'):
        super().__init__((ip, port), backlog, password)
        self.add_handler(RNEvent.UserPacket, self.handle_packet)
        self.auth_handlers = {}

        self.register_handler(PacketHeaders.HANDSHAKE.value, Handshake)

        self.logger.info('server started')

    def handle_packet(self, packet, address):
        header = packet[0:8]
        if header in self.auth_handlers:
            res = self.auth_handlers[header].construct_packet(self, packet)
            self.send(res, address)
        else:
            self.logger.warn('no registered handlers found for header-{}'.format(header))

    def register_handler(self, header, func):
        self.auth_handlers[header] = func
