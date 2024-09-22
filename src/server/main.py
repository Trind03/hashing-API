from server import server

def main() -> int:
    Server: server = server("127.0.0.1",5416)
    Server.Running()
    return 0


main()