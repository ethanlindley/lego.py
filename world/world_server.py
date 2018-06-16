from pyraknet.server import Server as RNServer
from pyraknet.server import Event as RNEvent
from core.packet_headers import PacketHeaders

from .packets.handshake import Handshake
from .packets.client_session_info import ClientSessionInfo

from util.logger import Logger


class WorldServer(RNServer):
    logger = Logger('WorldServer')

    def __init__(self, ip='127.0.0.1', port=2002, backlog=10000, password=b'3.25 ND1', database=None):
        super().__init__((ip, port), backlog, password)
        
        self.database = database

        self.add_handler(RNEvent.UserPacket, self.handle_packet)
        self.world_handlers = {}

        self.register_handler(PacketHeaders.HANDSHAKE.value, Handshake)
        self.register_handler(PacketHeaders.CLIENT_SESSION_INFO.value, ClientSessionInfo)

        self.omitted_headers = []  # add wanted omitted headers in here that dont need to send back a response to the client
        self.omitted_headers.append(PacketHeaders.CLIENT_SESSION_INFO.value)

    def handle_packet(self, packet, address):
        header = packet[0:8]
        if header in self.world_handlers:
            self.world_handlers[header].database = self.database
            res = self.world_handlers[header].construct_packet(self, packet, address)
            if res is not None and header not in self.omitted_headers:
                self.send(res, address)
            elif header in self.omitted_headers:
                pass  # don't need to send a packet response to client
            else:
                self.logger.warn('unable to construct packet for header {}'.format(header))
        else:
            self.logger.warn('no registered handlers found for header {}'.format(header))

    def register_handler(self, header, func):
        self.world_handlers[header] = func
