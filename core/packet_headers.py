from enum import Enum


class PacketHeaders(Enum):
    HANDSHAKE = b'S\x00\x00\x00\x00\x00\x00\x00'
    
    CLIENT_LOGIN_REQ = b'S\x01\x00\x00\x00\x00\x00\x00'
    CLIENT_LOGIN_RES = b'S\x05\x00\x00\x00\x00\x00\x00'

    CLIENT_SESSION_INFO = b'S\x04\x00\x01\x00\x00\x00\x00'
    CLIENT_MINIFIG_LIST_REQ = b'S\x04\x00\x02\x00\x00\x00\x00'
    CLIENT_MINIFIG_LIST_RES = b'S\x05\x00\x06\x00\x00\x00\x00'
