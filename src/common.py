import socket

class internet_computer:
    def __init__(self,IP,PORT) -> None:
        self.AUTH_TOKEN = "5c304a425e04d1fcba6a43853e6b10ffe35c725dc0ccc1bec0be8194264e4f44c17163b57cdadd88573f4f5f51c378af0ea2440081a9f1c0056204e71f2682dbA"

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