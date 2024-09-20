from sys import path
path.append("../")
from common import internet_computer

class server(internet_computer): 
    def __init__(self) -> None:
        super().__init__("127.0.0.1",4532)
