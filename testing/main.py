import fastapi
import uvicorn

from src import myname
from src import router

print(myname("j-org e"))

app = fastapi.FastAPI(title="testing")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)

# python -m pytest --cov=testing/src -v testing/tests/
# To execute all tests with coverage and with verbose to see more specific
# mypy ./testing --ignore-missing-imports --explicit-package-bases
