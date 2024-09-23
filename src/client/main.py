import socket
from client import client
def main():
    Client: client = client("127.0.0.1",5416)        
    Client.Startup()
main()