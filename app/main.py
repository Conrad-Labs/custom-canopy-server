import re
from fastapi import FastAPI
from app.router.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Custom Canopy Mockup API")

def is_allowed_origin(origin: str) -> bool:
    allowed_patterns = [
        r"http://localhost:\d+",
        r"https://custom-canopy-chatbot-[a-zA-Z0-9-]+\.vercel\.app",
        r"https://custom-canopy-fastapi-server-1f8879954a5f.herokuapp.com"
    ]
    return any(re.match(pattern, origin) for pattern in allowed_patterns)

class DynamicCORS(CORSMiddleware):
    def is_allowed_origin(self, origin: str) -> bool:
        return is_allowed_origin(origin)

app.add_middleware(
    DynamicCORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
