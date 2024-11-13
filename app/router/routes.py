import json
import base64

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from app.config import Config
from app.schema import OverlayRequest
from app.services.image_processor import apply_all_logos
from app.constants import DEFAULT_TENT_COLOR, DEFAULT_TEXT, DEFAULT_FONT_COLOUR

router = APIRouter()

@router.post("/create-mockups/", tags=["Mockup Creation"])
async def create_mockups(
    color: str = Form(f'"{DEFAULT_TENT_COLOR}"'),
    text: str = Form(f'"{DEFAULT_TEXT}"'),
    text_color: str = Form(f'"{DEFAULT_FONT_COLOUR}"'),
    logo: UploadFile = File(...),
):
    """
    Create mockups for canopy layouts with the provided logo, colour, and text, if any.
    """
    try:
        color = json.loads(color)
        if len(color) != 3 or not all(isinstance(c, int) for c in color):
            raise ValueError("Color must be a list of three integers representing B, G, and R values.")
        
        font_color = json.loads(text_color)
        if len(font_color) != 3 or not all(isinstance(c, int) for c in font_color):
            raise ValueError("Font color must be a list of three integers representing B, G, and R values.")

        logo_content = await logo.read()
        overlay_data = OverlayRequest(color=color, text=text, font_color=font_color)
        output_files = apply_all_logos(overlay_data, logo_content)

        # Create a zip file in memory
        images_data = []
        for file_path, file_content in output_files:
            encoded_image = base64.b64encode(file_content).decode("utf-8")
            images_data.append({"filename": file_path, "data": f"data:image/jpeg;base64,{encoded_image}"})

        # Return a JSON response with the images
        return JSONResponse(content={"images": images_data})

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    