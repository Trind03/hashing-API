import socket
from sys import path
path.append("./")
from common import internet_computer

class server(internet_computer): 
    def __init__(self) -> None:
        super().__init__("127.0.0.1",4532)
        self.Sock = socket.socket(self._IP_FAMILY,self._PROTOCOL)
        self.Sock.bind((self._IP,self._PORT))
        self._Running = True

    def __del__(self):
        self._Running = False

    def Running(self):
        while(self._Running):
            self.Sock.listen()
            