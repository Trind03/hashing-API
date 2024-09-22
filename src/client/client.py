import socket
from sys import path
path.append("../")
from common import internet_computer


class client(internet_computer):

    def __init__(self,IP_,PORT_) -> None:
        super().__init__(IP_,PORT_)
        self._Sock = socket.socket(self._IP_FAMILY,self._PROTOCOL)
        self._Running = True

    def Startup(self):
        self._Sock.connect((self._IP,self._PORT))

    def Running(self):
        while(self._Running):
            ...


    def __del__(self):
        ...