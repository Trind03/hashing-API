from fastapi import FastAPI
import pickle
import uvicorn

# Request format
# addr:port/algorithm/value

class server:
    def __init__(self,HOST,PORT) -> None:
        self._HOST: str = HOST
        self._PORT: int = PORT
        self._APP: FastAPI  = FastAPI()

        @self._APP.get("/")
        def broadcast():
            return {f"Error-404"}
    
    def run(self):
        uvicorn.run(self._APP,host=self._HOST,port=self._PORT)


if(__name__ == "__main__"):
    Server: server = server("0.0.0.0",4334)
    Server.run()