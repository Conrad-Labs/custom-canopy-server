from fastapi import FastAPI
from app.router.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Custom Canopy Mockup API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Allow local frontend during development
        "https://*.vercel.app",  # Allow all Vercel subdomains
        "https://custom-canopy-fastapi-server-1f8879954a5f.herokuapp.com"
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",  # Regex for Vercel preview URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
