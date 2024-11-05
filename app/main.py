from fastapi import FastAPI
from app.router.routes import router

app = FastAPI(title="Custom Canopy Mockup API")

app.include_router(router)
