from enum import Enum


class PacketHeaders(Enum):
    HANDSHAKE = b'S\x00\x00\x00\x00\x00\x00\x00'
    CLIENT_LOGIN_REQ = b'S\x01\x00\x00\x00\x00\x00\x00'
