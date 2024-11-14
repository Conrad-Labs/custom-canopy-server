import os
import logging
from fastapi import FastAPI, Request
from app.router.routes import router
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Custom Canopy Mockup API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://custom-canopy-chatbot-app-git-disable-form-team-alpha-8576f1e5.vercel.app", 
        "http://localhost:3000",
        "https://custom-canopy-fastapi-server-1f8879954a5f.herokuapp.com",
        "https://custom-canopy-chatbot-ndyysqjtw-team-alpha-8576f1e5.vercel.app",
        "https://custom-canopy-chatbot-app.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

@app.get("/")
async def root():
    return {"message": "Welcome to Custom Canopy Mockup API"}

app.include_router(router)
