from fastapi import APIRouter
from .routes import router as main_router  # Import the router from routes.py
from .blob_storage_cleanup import router as blob_storage_cleanup_router

router = APIRouter()
router.include_router(main_router)
router.include_router(blob_storage_cleanup_router)

