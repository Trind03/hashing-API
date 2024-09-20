import socket
import server


def main() -> int:
    Server: server = server()
    server.run()
    return 0