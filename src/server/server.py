import socket
import pickle
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
        self.Sock.close()

    def Process_metadata(self,data) -> str:
        Serialized_data = pickle.dumps(data)
        return Serialized_data.hex()

    def Connection_handler(self) -> None:
        self.Sock.listen(1)
        Sock, Addr = self.Sock.accept()

    
        #if(Sock.recv(self._Header) == self.AUTH_TOKEN):
            #print(f"Connections Established with verified client: {Addr}")
            #self.Active_connections.append((Sock,Addr))


    def Running(self):
        ...
