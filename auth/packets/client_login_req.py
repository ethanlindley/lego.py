import uuid
from pyraknet.bitstream import c_bool, c_uint8, c_uint16, c_ulong, c_ulonglong, c_ushort, ReadStream, WriteStream
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
                    self.logger.debug('found user {} in database'.format(uname))
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
                self.logger.debug('successfully created and added user \'{}\' to the database'.format(uname))
                res.write(c_uint8(0x01))
            except Exception as e:
                self.logger.warn('unable to create user \'{0}\' - {1}'.format(uname, e))
        
        res.write(CString('Talk_Like_A_Pirate', allocated_length=33))  # unknown
        res.write(CString(allocated_length=33*7))  # unknown
        
        res.write(c_uint16(1))  # v. major
        res.write(c_uint16(10))  # v. current
        res.write(c_uint16(64))  # v. minor

        user_token = str(uuid.uuid4())
        res.write(user_token[0:18], allocated_length=33)
        
        res.write(CString('127.0.0.1', allocated_length=33))  # world IP
        res.write(CString('127.0.0.1', allocated_length=33))  # chat IP
        res.write(c_uint16(2002))  # world port
        res.write(c_ushort(3003))  # chat port
        res.write(CString('0', allocated_length=33))  # unknown IP

        res.write(CString('00000000-0000-0000-0000-000000000000', allocated_length=37))
        res.write(c_ulong(0))
        res.write(CString('US', allocated_length=3))  # localization
        res.write(c_bool(False))
        res.write(c_bool(False))
        res.write(c_ulonglong(0))
        res.write('error', length_type=c_uint16)  # custom err msg
        res.write(c_uint16(0))
        res.write(c_ulong(4))
        
        return res
