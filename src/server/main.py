from server import server

def main() -> int:
    Server: server = server("localhost",5416)
    server.Running(Server)

    return 0


main()