import os
import socket
from pyraknet.bitstream import c_short, c_ulong, ReadStream, WriteStream
from core.packet_headers import PacketHeaders

from util.logger import Logger


class Handshake(object):
    logger = Logger('Handshake')

    def __init__(self):
        pass

    def construct_packet(self, packet):
        stream = ReadStream(packet)
        client_ver = stream.read(c_ulong)  # TODO - check client ver against server

        res = WriteStream()
        res.write(PacketHeaders.HANDSHAKE.value)
        res.write(c_ulong(171022))
        res.write(c_ulong(0x93))
        res.write(c_ulong(1))  # 1 for auth, 4 for everything else
        res.write(c_ulong(os.getpid()))
        res.write(c_short(0xff))
        res.write(str(socket.gethostbyname(socket.gethostname())), allocated_length=33)

        return res
