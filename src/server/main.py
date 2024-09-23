from server import server

def main() -> int:
    Server: server = server("localhost",5416)
    print(len(Server.Process_metadata("Hello world!")))

    return 0


main()