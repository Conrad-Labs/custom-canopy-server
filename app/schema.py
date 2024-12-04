from pydantic import BaseModel
from typing import Optional, List
from app.constants import DEFAULT_TEXT, DEFAULT_TENT_COLOR, DEFAULT_FONT_COLOUR

class OverlayRequest(BaseModel):
    slope_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    canopy_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    walls_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    text: Optional[str] = DEFAULT_TEXT
    font_color: Optional[List[int]] = DEFAULT_FONT_COLOUR
