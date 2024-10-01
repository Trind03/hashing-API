from fastapi import FastAPI
import pickle


app = FastAPI()
@app.get("/")
def broadcast():
    data = pickle.dumps("Hello world")
    return {f"{data}"}

if(__name__ == "__main__"):
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port = 4334)