from pyraknet.bitstream import c_uint8, c_uint16, ReadStream, WriteStream
from core.structs import CString
from core.packet_headers import PacketHeaders

from util.logger import Logger


class ClientLoginRequest(object):
    logger = Logger('ClientLoginRequest')

    def __init__(self, database=None):
        self.database = database

    def construct_packet(self, packet):
        stream = ReadStream(packet)

        uname = stream.read(str, allocated_length=33)
        pword = stream.read(str, allocated_length=41)

        res = WriteStream()
        res.write(PacketHeaders.CLIENT_LOGIN_REQ.value)

        found = False
        while found is False:
            for account in self.database.accounts:
                if account.username == uname and account.password == password:
                    res.write(c_uint8(0x01))
                    found = True
                elif account.username == uname and account.password != password:
                    res.write(c_uint8(0x06))
                    found = True
                elif account.is_banned:
                    res.write(c_uint8(0x02))
                    found = True
            break
        
        if found is False:
            try:
                self.database.register_account_db(username=uname, password=pword)
                self.database.register_account_client(username=uname, password=pword)
                res.write(c_uint8(0x01))
            except Exception as e:
                self.logger.warn('unable to create user \'{}\''.format())
        
        res.write(CString('Talk_Like_A_Pirate', allocated_length=33))  # unknown
        res.write(CString(allocated_length=33*7))  # unknown
        res.write(c_uint16(1))  # v. major
        res.write(c_uint16(10))  # v. current
        res.write(c_uint16(64))  # v. minor

        return res
