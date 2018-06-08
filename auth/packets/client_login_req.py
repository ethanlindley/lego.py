from pyraknet.bitstream import c_short, c_ulong, ReadStream, WriteStream
from core.packet_headers import PacketHeaders

from util.logger import Logger


class ClientLoginRequest(object):
    logger = Logger('ClientLoginRequest')

    def __init__(self):
        pass

    def construct_packet(self, packet):
        stream = ReadStream(packet)

        uname = stream.read(str, allocated_length=33)
        pword = stream.read(str, allocated_length=41)
