from fastapi import APIRouter, FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from quest import q
import json
import starlette.responses
from models import lite
# Load variables from .env file into environment
app = FastAPI()
security = HTTPBasic()
router = APIRouter()
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "nikos"
    correct_password = "130177"

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>TriviaAPI</title>
        <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    </head>
    <body>
        <h1>TriviaAPI v.1.0.0</h1>
    </body>
</html>
"""


@app.get("/private-data")
async def get_private_data(username: str = Depends(get_current_username)):
    return {"message": "You have access to private data", "username": username}


@router.get("/")
async def root():
    return HTMLResponse(html)


@router.get("/{section}")
async def get_all_items(section):
    res = q(section)
    data = json.loads(res.body)
    lite.insert(data)
    return res


# uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
app.include_router(router)
