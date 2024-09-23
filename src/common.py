import socket
import pickle


class internet_computer:
    def __init__(self,IP,PORT) -> None:
        # Authenticaion 
        self.AUTH_TOKEN = "5c304a425e04d1fcba6a43853e6b10ffe35c725dc0ccc1bec0be8194264e4f44c17163b57cdadd88573f4f5f51c378af0ea2440081a9f1c0056204e71f2682dbA"

        self._Header = 64
        self._IP = IP
        self._PORT = PORT
        self._IP_FAMILY = socket.AF_INET
        self._PROTOCOL = socket.SOCK_STREAM


    # Protocol will first broadcast a header: size of data. This function pads out the header with ' ' to match expected size.
    def Process_header(self, Size: int):
        TARGETS = len(Size) - self._Header
        DATA = str(self._Header)
        return DATA.ljust(TARGETS)
        
    def Process_metadata(self,data):
        Serialized_data = pickle.dumps(data)
        myset:tuple = (len(Serialized_data),Serialized_data)
        return myset
    
    
    def Load_metadata(data):
        return pickle.loads(data)


    def __del__(self) -> None:
        self._IP = None
        self._PORT = None
        self._IP_FAMILY = None
        self.PROTOCOL = None