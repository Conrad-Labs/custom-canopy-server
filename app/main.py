import os
import logging
from fastapi import FastAPI, Request
from app.router.routes import router
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

logging.getLogger("uvicorn.access").setLevel(logging.DEBUG)

app = FastAPI(title="Custom Canopy Mockup API")

if os.getenv("DISABLE_HTTPS_REDIRECT", "false").lower() != "true":
    from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
    app.add_middleware(HTTPSRedirectMiddleware)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://custom-canopy-chatbot-app-git-disable-form-team-alpha-8576f1e5.vercel.app", 
        "http://localhost:3000",
        "https://custom-canopy-fastapi-server-1f8879954a5f.herokuapp.com",
        "https://custom-canopy-chatbot-4ttha4kgf-team-alpha-8576f1e5.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger = logging.getLogger("uvicorn.access")
    logger.setLevel(logging.INFO)
    
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    
    return response

@app.get("/")
async def root():
    return {"message": "Welcome to Custom Canopy Mockup API"}

app.include_router(router)
