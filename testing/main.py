import fastapi
import uvicorn

from src import router, myname
print(myname("j-org e"))

app = fastapi.FastAPI(title="integration-testing")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)