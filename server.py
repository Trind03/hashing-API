from fastapi import FastAPI, Request
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
        self._HOST: str = HOST
        self._PORT: int = PORT
        self._APP: FastAPI  = FastAPI()

        @self._APP.get("/")
        async def empty_params(request: Request):
            return f"{request.client.host}"
        
        @self._APP.get("/new")
        async def generate_token(self) -> None:
            Token: uuid = str(uuid.uuid4())

            #if()
            

        @self._APP.get("/algo")
        async def list_algo():
            return ["MD5","SHA256", "SHA1","SHA512"];
    
        @self._APP.get("/{token}/{algorithm}/{data}")
        async def Process_data_ret(token,algorithm:str,data:str):
            if(token == self._Token):
                return process_data(data,algorithm)
            else:
                return "Invalid token :|"
        
    def Running(self):
        uvicorn.run(self._APP,host=self._HOST,port=self._PORT)

    
    def validate_token(Token: str) -> None:
        with open("valid_keys.json") as File:
                for Line in File:
                    #if(Token)
                    ...
