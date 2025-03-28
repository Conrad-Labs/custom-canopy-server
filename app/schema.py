from pydantic import BaseModel, Field, model_validator
from typing import Optional, List
from enum import Enum
from app.constants import DEFAULT_FONT_COLOUR, DEFAULT_OUTPUT_DIR

class TentTypes(str, Enum):
    no_walls = "no-walls"
    half_walls = "half-walls"
    full_walls = "full-walls"

class Side(str, Enum):
    front = "front"
    back = "back"
    left = "left"
    right = "right"
    top = "top"
    bottom = "bottom"

class TentSides(BaseModel):
    front: Optional[List[int]] = None
    left: Optional[List[int]] = None
    right: Optional[List[int]] = None
    back: Optional[List[int]] = None
    top: Optional[List[int]] = None
    bottom: Optional[List[int]] = None

    @model_validator(mode="before")
    def set_default_colors(cls, values):
        front_color = values.get("front")
        if front_color:
            values["left"] = values.get("left", front_color)
            values["right"] = values.get("right", front_color)
            values["back"] = values.get("back", front_color)
            values["top"] = values.get("top", front_color)
            values["bottom"] = values.get("bottom", front_color)
        return values
    
class ValencesText(BaseModel):
    front: Optional[str] = None
    left: Optional[str] = None
    back: Optional[str] = None
    right: Optional[str] = None

class Table(BaseModel):
    sides: TentSides

class AddOns(BaseModel):
    table: Optional[Table] = None

class OverlayRequest(BaseModel):
    peaks: TentSides
    valences: TentSides
    panels: TentSides
    font_color: List[int] = Field(DEFAULT_FONT_COLOUR, description="Font color is required and must be a list of 3 integers.")
    text: ValencesText
    add_ons: Optional[AddOns] = None
    tent_type: TentTypes
    output_dir: Optional[str] = DEFAULT_OUTPUT_DIR

    @model_validator(mode="before")
    def set_tent_type(cls, values):
        primary_sides = [Side.front, Side.back, Side.left, Side.right]
        panel_states = {side: getattr(values.get("panels"), side.value) for side in primary_sides}
        if all(panel_states.values()):
            values["tent_type"] = TentTypes.full_walls
        elif panel_states[Side.front] is None and all(
            panel_states[side] for side in [Side.back, Side.left, Side.right]
        ):
            values["tent_type"] = TentTypes.half_walls
        else:
            values["tent_type"] = TentTypes.no_walls

        return values