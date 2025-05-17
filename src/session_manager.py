from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.browser import BrowserManager

router = APIRouter()

class StartSessionRequest(BaseModel):
    browser: str = "chromium"
    headless: bool = True
    url: str = None
    instances: int = 1

class StartSessionResponse(BaseModel):
    sessionId: str

class CloseSessionRequest(BaseModel):
    sessionId: str

@router.post("/start", response_model=StartSessionResponse)
async def start_session(req: StartSessionRequest):
    session_id = await BrowserManager.start_session(req.browser, req.headless, req.url)
    return {"sessionId": session_id}

@router.post("/close")
async def close_session(req: CloseSessionRequest):
    await BrowserManager.close_session(req.sessionId)
    return {"status": "success"}