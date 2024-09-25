import socket
from time import sleep
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
        self.Process_send(self._Sock, self.data)

    def Process_send(self,Sock:socket.socket,data:str) -> None:
        Length:int = len(data)
        Sock.send(str(Length).encode())
        sleep(1)
        Sock.send(data.encode())

    def Process_recv(self,Sock:socket.socket) -> str:
        Length:int = int(str(Sock.recv(64).decode()))
        print("Size is: ", Length)
        Data:str = str(Sock.recv(Length).decode())
        return Data


    def Running(self):
        m_data:str = "5c304a425e04d1fcba6a43853e6b10ffe35c725dc0ccc1bec0be8194264e4f44c17163b57cdadd88573f4f5f51c378af0ea2440081a9f1c0056204e71f2682dbA"
        print("if tetsing")
        if(self.Process_recv(self._Sock) == m_data):
            print("Disconnect sucessful!") 


    def __del__(self):
        self._Sock.close()
        self._Running = False