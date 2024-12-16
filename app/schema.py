from pydantic import BaseModel
from typing import Optional, List
from app.constants import DEFAULT_TEXT, DEFAULT_TENT_COLOR, DEFAULT_FONT_COLOUR, DEFAULT_IS_PATTERNED

class OverlayRequest(BaseModel):
    slope_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    canopy_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    walls_primary_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    walls_secondary_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    walls_tertiary_color: Optional[List[int]] = DEFAULT_TENT_COLOR
    text: Optional[str] = DEFAULT_TEXT
    font_color: Optional[List[int]] = DEFAULT_FONT_COLOUR
    is_patterned: Optional[str] = DEFAULT_IS_PATTERNED
