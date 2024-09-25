import socket
from client import client
def main():
    Client: client = client("localhost",5416)        
    Client.Startup()
main()