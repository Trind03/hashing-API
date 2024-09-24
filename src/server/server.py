import socket
import sys
sys.path.append("../")
import common
from client import client

class server(common.internet_computer): 
    def __init__(self, IP_,PORT_) -> None:
        super().__init__(IP_,PORT_)
        self.Sock = socket.socket(self._IP_FAMILY,self._PROTOCOL)
        self.Sock.bind((self._IP,self._PORT))
        self._Running = True
        self.Active_connections: list = []

    def __del__(self) -> None:
        self._Running = False
        self.Sock.close()

    def Connection_handler(self) -> None:
        self.Sock.listen(1)
        Sock, Addr = self.Sock.accept()
        Client = client(Sock,Addr)

        self.Active_connections.append(Client)

    
        #if(Sock.recv(self._Header) == self.AUTH_TOKEN):
            #print(f"Connections Established with verified client: {Addr}")
            #self.Active_connections.append((Sock,Addr))

    def Check_data(self) -> None:
        for i in range(len(self.Active_connections)):
            print(self.Active_connections[i]._ID)


    def Running(self):
        while(self._Running):
            if(len(self.Active_connections) > 0):
                self.Check_data()
            else:
                self.Connection_handler()
