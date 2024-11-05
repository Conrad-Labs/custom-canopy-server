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

        logo_content = await logo.read()
        overlay_data = OverlayRequest(color=color, text=text)
        output_files = apply_all_logos(overlay_data, logo_content)

        # Create a zip file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zf:
            for file_path, file_content in output_files:
                zf.writestr(file_path, file_content)
        zip_buffer.seek(0)

        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=mockups.zip"}
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    