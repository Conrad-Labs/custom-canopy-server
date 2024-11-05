import os
import io
import zipfile
import json

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from app.config import Config
from app.schema import OverlayRequest
from app.services.image_processor import apply_all_logos
from app.constants import DEFAULT_TENT_COLOR, DEFAULT_TEXT

router = APIRouter()

@router.post("/create-mockups/", tags=["Mockup Creation"])
async def create_mockups(
    color: str = Form(f'"{DEFAULT_TENT_COLOR}"'),
    text: str = Form(DEFAULT_TEXT),
    logo: UploadFile = File(...),
):
    """
    Create mockups for canopy layouts with the provided logo, colour, and text, if any.
    """
    try:
        color = json.loads(color)  

        if len(color) != 3 or not all(isinstance(c, int) for c in color):
            raise ValueError("Color must be a list of three integers representing B, G, and R values.")

        logo_path = os.path.join(Config.BASE_IMAGE_PATH, logo.filename)
        with open(logo_path, "wb") as buffer:
            buffer.write(await logo.read())

        overlay_data = OverlayRequest(color=color, text=text)
        # Creates output files in the static/output directory, which can be viewed by calling the /images/ endpoint
        apply_all_logos(overlay_data, logo_path)

        return JSONResponse(content={"status": "ok"}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        if os.path.exists(logo_path):
            os.remove(logo_path)
    

@router.get("/images/", tags=["Mockup Creation"])
async def get_images():
    """
    Serve the processed images.
    """
    output_dir = Config.OUTPUT_PATH
    image_files = [f for f in os.listdir(output_dir) if f.endswith((".png", ".jpg", ".jpeg"))]

    if not image_files:
        raise HTTPException(status_code=404, detail="No images found")

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        for image_file in image_files:
            image_path = os.path.join(output_dir, image_file)
            zf.write(image_path, image_file)
    zip_buffer.seek(0)
    
    return StreamingResponse(zip_buffer, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=images.zip"})
