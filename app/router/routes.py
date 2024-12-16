import io
import json
import zipfile

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from app.schema import OverlayRequest
from app.services.image_processor import apply_all_logos
from app.constants import DEFAULT_TENT_COLOR, DEFAULT_TEXT, DEFAULT_FONT_COLOUR

router = APIRouter()

@router.post("/create-mockups", tags=["Mockup Creation"])
async def create_mockups(
    slope_color: str = Form(f'"{DEFAULT_TENT_COLOR}"'),
    canopy_color: str = Form(f'"{DEFAULT_TENT_COLOR}"'),
    walls_primary_color: str = Form(f'"{DEFAULT_TENT_COLOR}"'),
    walls_secondary_color: str = Form(f'"{DEFAULT_TENT_COLOR}"'),
    walls_tertiary_color: str = Form(f'"{DEFAULT_TENT_COLOR}"'),
    text: str = Form(f'"{DEFAULT_TEXT}"'),
    text_color: str = Form(f'"{DEFAULT_FONT_COLOUR}"'),
    logo: UploadFile = File(...),
    patterned: str = Form('false')
):
    """
    Create mockups for canopy layouts with the provided logo, colour, and text, if any.
    """
    try:
        slope_color = json.loads(slope_color)
        if len(slope_color) != 3 or not all(isinstance(c, int) for c in slope_color):
            raise ValueError("Slope color must be a list of three integers representing B, G, and R values.")
        
        canopy_color = json.loads(canopy_color)
        if len(canopy_color) != 3 or not all(isinstance(c, int) for c in canopy_color):
            raise ValueError("Canopy color must be a list of three integers representing B, G, and R values.")
        
        walls_primary_color = json.loads(walls_primary_color)
        if len(walls_primary_color) != 3 or not all(isinstance(c, int) for c in walls_primary_color):
            raise ValueError("Walls' primary color must be a list of three integers representing B, G, and R values.")
        
        walls_secondary_color = json.loads(walls_secondary_color)
        if len(walls_secondary_color) != 3 or not all(isinstance(c, int) for c in walls_secondary_color):
            raise ValueError("Walls' secondary color must be a list of three integers representing B, G, and R values.")
        
        walls_tertiary_color = json.loads(walls_tertiary_color)
        if len(walls_tertiary_color) != 3 or not all(isinstance(c, int) for c in walls_tertiary_color):
            raise ValueError("Walls' tertiary color must be a list of three integers representing B, G, and R values.")
        
        font_color = json.loads(text_color)
        if len(font_color) != 3 or not all(isinstance(c, int) for c in font_color):
            raise ValueError("Font color must be a list of three integers representing B, G, and R values.")

        logo_content = await logo.read()
        overlay_data = OverlayRequest(slope_color=slope_color, canopy_color=canopy_color, walls_primary_color=walls_primary_color, walls_secondary_color=walls_secondary_color, walls_tertiary_color=walls_tertiary_color, text=text, font_color=font_color, is_patterned=f"{patterned}")
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            apply_all_logos(overlay_data, logo_content, zip_file)

        zip_buffer.seek(0)
        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=mockups.zip"}
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    