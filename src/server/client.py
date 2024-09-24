import socket
import sys
import pickle
import asyncio
sys.path.append("../")
import common

class client:
    def __init__(self,Sock:socket.socket, Addr,ID:int) -> None:
        print(f"Client -> {Addr} Connected")
        self._ID: int = ID
        self._Sock = Sock
        self._Address = Addr

    # Protocol will first broadcast a header: size of data. This function pads out the header with ' ' to match expected size.

    def recv(self,Sock: socket) -> tuple:
        length:int = int(Sock.recv(64))
        data: str = Sock.recv(length)
        
        return (length, data)
    
    def Process_header(self, Size: int):
        TARGETS = len(Size) - self._Header
        DATA = str(self._Header)
        return DATA.ljust(TARGETS)
        
    def Process_metadata(self,data):
        Serialized_data = pickle.dumps(data)
        myset:tuple = (len(Serialized_data),data)
        return myset
    
    
    def Load_metadata(data):
        return pickle.loads(data)

    def __del__(self):
        print(f"Client: -> {self._Address} Disconnected")
        self._Sock.send(common.flags.Disconnect.encode())
        self._Sock.close()