import socket
import sys
sys.path.append("../")
import common

class server(common.internet_computer): 
    def __init__(self, IP_,PORT_) -> None:
        super().__init__(IP_,PORT_)
        self.Sock = socket.socket(self._IP_FAMILY,self._PROTOCOL)
        self.Sock.bind((self._IP,self._PORT))
        self._Running = True
        self.Active_connections = []

    def __del__(self) -> None:
        self._Running = False
        self.Sock.shutdown()
        self.Sock.close()

    def Connection_handler(self) -> None:
        Sock, Addr = self.Sock.accept()
    
        #if(Sock.recv(self._Header) == self.AUTH_TOKEN):
            #print(f"Connections Established with verified client: {Addr}")
            #self.Active_connections.append((Sock,Addr))


    def Running(self):
        self.Sock.listen()

        while(self._Running):
            self.Connection_handler()
            print(self.Sock.recv(13))
