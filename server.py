from fastapi import FastAPI
import uvicorn
import hashlib
# Request format
# addr:port/algorithm/value

def process_data(data:str,Algorithm:str):
    Hash: hashlib = hashlib()

    match Algorithm:

        case "MD5"

class server:
    def __init__(self,HOST,PORT) -> None:
        self._HOST: str = HOST
        self._PORT: int = PORT
        self._APP: FastAPI  = FastAPI()

        @self._APP.get("/")
        def broadcast():
            return {f"Error-404"}
        
        @self._APP.get("/algo")
        def list_algo():
            data = ["MD5","SHA256", "SHA1","SHA512"]
            return data;
        @self._APP.get("/{algorithm}/{data}")
        def Process_data_ret():
            ...
    def Running(self):
        uvicorn.run(self._APP,host=self._HOST,port=self._PORT)