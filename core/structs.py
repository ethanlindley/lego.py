from pyraknet.bitstream import Serializable


class CString(Serializable):
    def __init__(self, data='', allocated_length=None, length_type=None):
        self.data = data
        self.allocated_length = allocated_length
        self.length_type = length_type

    def serialize(self, stream):
        stream.write(self.data if isinstance(self.data, bytes) else bytes(self.data, 'latin1'), 
        allocated_length=self.allocated_length, length_type=self.length_type)

    def deserialize(self, stream):
        return stream.read(bytes, allocated_length=self.allocated_length, length_type=self.length_type).decode('latin1')
