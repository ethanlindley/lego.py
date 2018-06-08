from enum import Enum


class PacketHeaders(Enum):
    HANDSHAKE = b'S\x00\x00\x00\x00\x00\x00\x00'
