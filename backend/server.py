import os

from fastapi import Depends, FastAPI, Header, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

API_KEY = os.environ["API_KEY"]


async def require_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key"
        )


class AgentEndRequest(BaseModel):
    prompt: str


@app.post("/agent_end", dependencies=[Depends(require_api_key)])
async def agent_end(request: AgentEndRequest):
    prompt = request.prompt
    return {"message": "agent will eventually respond"}

