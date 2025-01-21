import io
import json
from typing import List, Optional
import zipfile

from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import Field
from app.schema import OverlayRequest, TentSides, ValencesText, WallsColors
from app.services.image_processor import apply_all_logos
from app.constants import DEFAULT_IS_PATTERNED, DEFAULT_FONT_COLOUR, DEFAULT_TENT_COLOR, DEFAULT_TEXT

router = APIRouter()

def validate_color(color_str: str, optional=False):
    if (color_str):
        color = json.loads(color_str)
        if ((len(color) != 3 or not all(isinstance(c, int) for c in color)) and not optional):
                raise ValueError("Color must be a list of three integers representing B, G, and R values.")
        
            
        return color
    if (optional):
        return None
    else: 
        raise ValueError("Color must be a list of three integers representing B, G, and R values.")

@router.post("/create-mockups", tags=["Mockup Creation"])
async def create_mockups(
    logo: UploadFile = File(...),
    peaks_front: str = Form(
        f'"{DEFAULT_TENT_COLOR}"', 
        description="Front color for peaks. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    peaks_left: Optional[str] = Form(
        "",
        description="Left color for peaks. Defaults to the same as peaks_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    peaks_right: Optional[str] = Form(
        "",
        description="Right color for peaks. Defaults to the same as peaks_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    peaks_back: Optional[str] = Form(
        "",
        description="Back color for peaks. Defaults to the same as peaks_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    valences_front: str = Form(
        f'"{DEFAULT_TENT_COLOR}"', 
        description="Front color for valences. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    valences_left: Optional[str] = Form(
        "",
        description="Left color for valences. Defaults to the same as valences_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    valences_right: Optional[str] = Form(
        "",
        description="Right color for valences. Defaults to the same as valences_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    valences_back: Optional[str] = Form(
        "",
        description="Back color for valences. Defaults to the same as valences_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    is_patterned: str = Form(
        "false",
        description="Indicates whether the tent is patterned. Use 'true' or 'false'.",
        example=DEFAULT_IS_PATTERNED
    ),
    walls_primary: Optional[str] = Form(
        "",
        description="Primary wall color. Required if is_patterned is True, defaults to None otherwise (walls will not be colored). Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    walls_secondary: Optional[str] = Form(
        "",
        description="Secondary wall color. Required if is_patterned is True, defaults to walls_primary if provided, otherwise None. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    walls_tertiary: Optional[str] = Form(
        "",
        description="Tertiary wall color. Required if is_patterned is True, defaults to walls_primary if provided, otherwise None. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"'
    ),
    text_color: str = Form(
        f'"{DEFAULT_FONT_COLOUR}"',
        description="Font color for the text. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_FONT_COLOUR}"'
    ),
    front_text: Optional[str] = Form(
        '',
        description="Text to be added to the front valence of the canopy.",
        example=DEFAULT_TEXT
    ),
    left_text: Optional[str] = Form(
        '',
        description="Text to be added to the left valence of the canopy.",
        example=DEFAULT_TEXT
    ),
    back_text: Optional[str] = Form(
        '',
        description="Text to be added to the back valence of the canopy.",
        example=DEFAULT_TEXT
    ),
    right_text: Optional[str] = Form(
        '',
        description="Text to be added to the right valence of the canopy.",
        example=DEFAULT_TEXT
    )
):
    """
    Create mockups for canopy layouts with the provided logo, colours, and text, if any.
    """
    try:
        font_color = validate_color(text_color)
        
        text = ValencesText(
            front=front_text,
            left=left_text,
            back=back_text,
            right=right_text
        )
        
        peaks = TentSides(
            front=validate_color(peaks_front),
            left=validate_color(peaks_left, optional=True) or validate_color(peaks_front),
            right=validate_color(peaks_right, optional=True) or validate_color(peaks_front),
            back=validate_color(peaks_back, optional=True) or validate_color(peaks_front),
        )

        valences = TentSides(
            front=validate_color(valences_front),
            left=validate_color(valences_left, optional=True) or validate_color(valences_front),
            right=validate_color(valences_right, optional=True) or validate_color(valences_front),
            back=validate_color(valences_back, optional=True) or validate_color(valences_front),
        )

        walls = None
        if is_patterned.lower() == "true":
            if not (walls_primary and walls_secondary and walls_tertiary):
                raise HTTPException(
                    status_code=400, detail="All walls colors (primary, secondary, tertiary) are required if patterned."
                )
            walls = WallsColors(primary=validate_color(walls_primary), secondary=validate_color(walls_secondary), tertiary=validate_color(walls_tertiary))
        elif walls_primary: 
            walls = WallsColors(
                primary=validate_color(walls_primary),
                secondary=validate_color(walls_secondary, optional=True) or validate_color(walls_primary),
                tertiary=validate_color(walls_tertiary, optional=True) or validate_color(walls_primary)
            )
        logo_content = await logo.read()        
        overlay_data = OverlayRequest(peaks=peaks, valences=valences, walls=walls, font_color=font_color, is_patterned=f"{is_patterned}", text=text)

        # Process images and create zip
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
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    