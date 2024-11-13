from fastapi import FastAPI
from app.router.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Custom Canopy Mockup API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://custom-canopy-chatbot-app-git-disable-form-team-alpha-8576f1e5.vercel.app", 
        "https://localhost:3000",
        "https://custom-canopy-fastapi-server-1f8879954a5f.herokuapp.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
