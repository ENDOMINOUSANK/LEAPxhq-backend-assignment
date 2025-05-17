from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.browser import BrowserManager
from utils.helpers import get_locator
import base64

router = APIRouter()

class ActionRequest(BaseModel):
    sessionId: str
    locator: dict | str
    value: str = None 

class ActionResponse(BaseModel):
    status: str
    screenshot: str = None
    error: str = None

@router.post("/click", response_model=ActionResponse)
async def click_action(req: ActionRequest):
    try:
        page = await BrowserManager.get_page(req.sessionId)
        locator = get_locator(page, req.locator)
        await locator.first.click()
        screenshot_bytes = await page.screenshot(type="png")
        screenshot_b64 = base64.b64encode(screenshot_bytes).decode("utf-8")
        return {"status": "success", "screenshot": screenshot_b64}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@router.post("/fill", response_model=ActionResponse)
async def fill_action(req: ActionRequest):
    try:
        page = await BrowserManager.get_page(req.sessionId)
        locator = get_locator(page, req.locator)
        await locator.fill(req.value)
        screenshot_bytes = await page.screenshot(type="png")
        screenshot_b64 = base64.b64encode(screenshot_bytes).decode("utf-8")
        return {"status": "success", "screenshot": screenshot_b64}
    except Exception as e:
        return {"status": "error", "error": str(e)}
    

@router.post("/hover", response_model=ActionResponse)
async def hover_action(req: ActionRequest):
    try:
        page = await BrowserManager.get_page(req.sessionId)
        locator = get_locator(page, req.locator)
        await locator.hover()
        screenshot_bytes = await page.screenshot(type="png")
        screenshot_b64 = base64.b64encode(screenshot_bytes).decode("utf-8")
        return {"status": "success", "screenshot": screenshot_b64}
    except Exception as e:
        return {"status": "error", "error": str(e)}
