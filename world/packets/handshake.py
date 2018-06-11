import os
import socket
from pyraknet.bitstream import c_short, c_ulong, ReadStream, WriteStream
from core.packet_headers import PacketHeaders


class Handshake(object):
    def __init__(self):
        self.database = None

    def construct_packet(self, packet, address):
        stream = ReadStream(packet)
        client_ver = stream.read(c_ulong)  # TODO - check client ver against server

        res = WriteStream()
        res.write(PacketHeaders.HANDSHAKE.value)
        res.write(c_ulong(171022))  # TODO - fix checking client ver
        res.write(c_ulong(0x93))
        res.write(c_ulong(4))
        res.write(c_ulong(os.getpid()))
        res.write(c_short(0xff))
        res.write(str(socket.gethostbyname(socket.gethostname())), allocated_length=33)

        return res
