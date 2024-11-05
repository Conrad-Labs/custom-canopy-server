from pydantic import BaseModel
from typing import Optional, List
from app.constants import DEFAULT_TEXT, DEFAULT_TENT_COLOR

class OverlayRequest(BaseModel):
    color: Optional[List[int]] = DEFAULT_TENT_COLOR
    text: Optional[str] = DEFAULT_TEXT
