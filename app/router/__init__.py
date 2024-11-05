from fastapi import APIRouter
from .routes import router as main_router  # Import the router from routes.py

router = APIRouter()
router.include_router(main_router)
