import uvicorn
from fastapi import FastAPI
from rest_APIs.src import api_router

app = FastAPI(
    title="Practice"
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)