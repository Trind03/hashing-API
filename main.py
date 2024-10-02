from server import server


if(__name__ == "__main__"):
    Server: server = server("0.0.0.0",4334)
    Server.Running()