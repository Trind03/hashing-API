import socket

class internet_computer:
    def __init__(self,IP,PORT) -> None:
        self.AUTH_TOKEN = ""

        self._Header = 64
        self._IP = IP
        self._PORT = PORT
        self._IP_FAMILY = socket.AF_INET
        self._PROTOCOL = socket.SOCK_STREAM


    def __del__(self) -> None:
        self._IP = None
        self._PORT = None
        self._IP_FAMILY = None
        self.PROTOCOL = None