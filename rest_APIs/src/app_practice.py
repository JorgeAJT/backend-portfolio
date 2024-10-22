import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/query_params/")
async def query(name: str = None, surname: str = None):
    return {"message": f"Hello {name} {surname}, good morning"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)