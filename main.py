import os
import logging
from fastapi import FastAPI, Request, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Backend-Assignment-Playwright",
    description="A fast and minimal FastAPI Playwright browser with async support.",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FastAPI async boilerplate is running."}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Dummy async inference logic
    content = await file.read()
    logger.info(f"Received file of size {len(content)} bytes")
    # Simulate async processing
    # result = await some_async_inference_function(content)
    result = {"prediction": "dummy_result"}
    return JSONResponse(content=result)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), reload=True)