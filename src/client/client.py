import socket
from sys import path
path.append("../")
from common import internet_computer


class client(internet_computer):

    def __init__(self,IP_,PORT_) -> None:
        super().__init__(IP_,PORT_)
        self._Sock = socket.socket(self._IP_FAMILY,self._PROTOCOL)
        self._Running = True
        self.HOST = IP_
        self.PORT = PORT_
        self.data = input("> ")

    def Startup(self):
        self._Sock.connect((self.HOST,self._PORT))
        self._Sock.send(self.data.encode())

    def Running(self):
        while(self._Running):
            ...


    def __del__(self):
        self._Sock.close()
        self._Running = False