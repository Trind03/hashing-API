from fastapi import FastAPI
import uvicorn
import hashlib
import uuid
# Request format
# addr:port/algorithm/value

def process_data(data:str,Algorithm:str) -> str:
    Hash: hashlib = hashlib
    print(f"Hashing data for client using {Algorithm}: {data}")
    match Algorithm.upper():

        case "MD5":
            data = data.encode()
            return {f"{Hash.md5(data).hexdigest()}"}
        case "SHA256":
            data = data.encode()
            return {f"{Hash.sha256(data).hexdigest()}"}
        case "SHA1":
            data = data.encode()
            return {f"{Hash.sha1(data).hexdigest()}"}
        case "SHA512":
            data = data.encode()
            return {f"{Hash.sha512(data).hexdigest()}"}

class server:
    def __init__(self,HOST,PORT) -> None:
        self._Token = self.generate_token()
        self._HOST: str = HOST
        self._PORT: int = PORT
        self._APP: FastAPI  = FastAPI()
        print(self._Token)

        @self._APP.get("/")
        async def broadcast():
            return {f"Error-404"}
        
        @self._APP.get("/algo")
        async def list_algo():
            return ["MD5","SHA256", "SHA1","SHA512"];
    
        @self._APP.get("/{algorithm}/{data}")
        async def Process_data_ret(algorithm:str,data:str):
            return process_data(data,algorithm)
        
    def Running(self):
        uvicorn.run(self._APP,host=self._HOST,port=self._PORT)

    def generate_token(self) -> str:
        Token: uuid = str(uuid.uuid4())
        
        return Token
    
    def validate_token(Token: str) -> None:
        ...
