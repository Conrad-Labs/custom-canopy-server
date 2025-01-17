from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, model_validator
from typing import Optional, List
from app.constants import DEFAULT_TEXT, DEFAULT_FONT_COLOUR, DEFAULT_IS_PATTERNED, DEFAULT_TENT_COLOR

class TentSides(BaseModel):
    front: List[int] = Field(DEFAULT_TENT_COLOR, description="Front color is required.")
    left: Optional[List[int]] = None
    right: Optional[List[int]] = None
    back: Optional[List[int]] = None

    @model_validator(mode="before")
    def set_default_colors(cls, values):
        front_color = values.get("front")
        if front_color:
            values["left"] = values.get("left", front_color)
            values["right"] = values.get("right", front_color)
            values["back"] = values.get("back", front_color)
        return values

class WallsColors(BaseModel):
    primary: Optional[List[int]] = None
    secondary: Optional[List[int]] = None
    tertiary: Optional[List[int]] = None

    @model_validator(mode="after")
    def validate_wall_colors(cls, instance):
        if hasattr(instance, 'is_patterned') and instance.is_patterned.lower() == "true":
            if not instance.primary or not instance.secondary or not instance.tertiary:
                raise ValueError("All wall colors (primary, secondary, tertiary) must be provided if patterned.")
        return instance
    
class ValencesText(BaseModel):
    front: Optional[str] = None
    left: Optional[str] = None
    back: Optional[str] = None
    right: Optional[str] = None

class OverlayRequest(BaseModel):
    peaks: TentSides
    valences: TentSides
    walls: Optional[WallsColors] = None
    font_color: List[int] = Field(DEFAULT_FONT_COLOUR, description="Font color is required and must be a list of 3 integers.")
    is_patterned: str = DEFAULT_IS_PATTERNED
    text: ValencesText
    