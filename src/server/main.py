from server import server

def main() -> int:
    Server: server = server()
    Server.Running()
    return 0


main()