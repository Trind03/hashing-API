import socket
import sys
sys.path.append("../")
import common

class client:
    def __init__(self,Sock:socket.socket, Addr,ID:int) -> None:
        print(f"Client -> {Addr} Connected")
        self._ID: int = ID
        self._Sock = Sock
        self._Address = Addr
    
    def __del__(self):
        print(f"Client: -> {self._Address} Disconnected")
        self._Sock.send(common.flags.Disconnect.encode())
        self._Sock.close()