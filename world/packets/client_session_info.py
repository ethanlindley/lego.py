from pyraknet.bitstream import ReadStream, WriteStream

from util.logger import Logger


class ClientSessionInfo(object):
    logger = Logger('WorldServer')

    def __init__(self):
        self.database = None

    def construct_packet(self, packet, address):
        stream = ReadStream(packet)

        uname = stream.read(str, allocated_length=33)
        user_key = stream.read(str, allocated_length=33)

        session = self.database.get_session(address)
        if session is None or session.acc_userkey != user_key or session.acc_username != uname:
            # TODO - handle disconnect user here
            self.logger.warn('FIXME :: connection from {} has sent invalid data! disconnecting...'.format(address))

        return None