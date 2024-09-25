import socket
import sys
import asyncio
sys.path.append("../")
import common
from client import client

class server(common.internet_computer): 
    def __init__(self,HOST,Port) -> None:

        super().__init__(HOST,Port)
        self.Sock = socket.socket(self._IP_FAMILY,self._PROTOCOL)
        self.Sock.bind((self._IP,self._PORT))
        self._Running = True
        self.Active_connections: list = []

    def __del__(self) -> None:
        self._Running = False
        self.Sock.close()

    def Connection_handler(self) -> None:
        ID = len(self.Active_connections) + 1
        self.Sock.listen(1)
        Sock, Addr = self.Sock.accept()
        Client = client(Sock,Addr,ID)

        self.Active_connections.append(Client)

    
        #if(Sock.recv(self._Header) == self.AUTH_TOKEN):
            #print(f"Connections Established with verified client: {Addr}")
            #self.Active_connections.append((Sock,Addr))

    def Check_data(self) -> None:
        for i in range(len(self.Active_connections)):
            print(self.Active_connections[len(self.Active_connections) - 1]._Last_message)



            
    def Running(self):
        while(self._Running):

            self.Connection_handler()
            self.Check_data()
