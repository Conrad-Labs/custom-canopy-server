import base64
import json
from typing import Optional

from vercel_kv import KV, Opts
import uuid
import json

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.schema import OverlayRequest, TentSides, ValencesText, AddOns, Table
from app.services.image_processor import generate_mockups
from app.constants import DEFAULT_FONT_COLOUR, DEFAULT_FONT_SIZE, DEFAULT_FONT_URL, DEFAULT_TENT_COLOR, DEFAULT_TEXT, DEFAULT_TENT_TYPES, DEFAULT_TENT_TYPES, EXPIRY_TIME
from dotenv import load_dotenv

load_dotenv()
kv = KV()
opts = Opts(
    ex=EXPIRY_TIME,
    px=None,
    exat=None,
    pxat=None,
    keepTtl=None
)
router = APIRouter()


def validate_color(color_str: str, optional=False):
    if color_str:
        color = json.loads(color_str)
        if (
            len(color) != 3 or not all(isinstance(c, int) for c in color)
        ) and not optional:
            raise ValueError(
                "Color must be a list of three integers representing B, G, and R values."
            )

        return color
    if optional:
        return None
    else:
        raise ValueError(
            "Color must be a list of three integers representing B, G, and R values."
        )
        
def validate_tent_types(tent_types: str):
    try:
        return json.loads(tent_types)
    except Exception as e:
        print(f"Error parsing provided tent types: {e}")


@router.post("/create-mockups", tags=["Mockup Creation"])
async def create_mockups(
    logo: UploadFile = File(...),
    peaks_front: str = Form(
        f'"{DEFAULT_TENT_COLOR}"',
        description="Front color for peaks. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    peaks_left: Optional[str] = Form(
        "",
        description="Left color for peaks. Defaults to the same as peaks_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    peaks_right: Optional[str] = Form(
        "",
        description="Right color for peaks. Defaults to the same as peaks_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    peaks_back: Optional[str] = Form(
        "",
        description="Back color for peaks. Defaults to the same as peaks_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    valences_front: str = Form(
        f'"{DEFAULT_TENT_COLOR}"',
        description="Front color for valences. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    valences_left: Optional[str] = Form(
        "",
        description="Left color for valences. Defaults to the same as valences_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    valences_right: Optional[str] = Form(
        "",
        description="Right color for valences. Defaults to the same as valences_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    valences_back: Optional[str] = Form(
        "",
        description="Back color for valences. Defaults to the same as valences_front if not provided.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    panels_back: Optional[str] = Form(
        "",
        description="Back color for panel. Must be a string representation of a list of three integers representing the BGR color value",
    ),
    panels_left: Optional[str] = Form(
        "",
        description="Left color for panel. Must be a string representation of a list of three integers representing the BGR color value",
    ),
    panels_right: Optional[str] = Form(
        "",
        description="Right color for panel. Must be a string representation of a list of three integers representing the BGR color value",
    ),
    text_color: str = Form(
        f'"{DEFAULT_FONT_COLOUR}"',
        description="Font color for the text. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_FONT_COLOUR}"',
    ),
    text_size: Optional[int] = Form(
        DEFAULT_FONT_SIZE,
        description="Font size for the text. Must be an integer.",
        example=f'"{DEFAULT_FONT_SIZE}"',
    ),
    font_url: Optional[str] = Form(
        DEFAULT_FONT_URL,
        description="The URL for the font the user wishes to use",
        example=DEFAULT_FONT_URL
    ),
    front_text: Optional[str] = Form(
        "",
        description="Text to be added to the front valence of the canopy.",
        example=DEFAULT_TEXT,
    ),
    left_text: Optional[str] = Form(
        "",
        description="Text to be added to the left valence of the canopy.",
        example=DEFAULT_TEXT,
    ),
    back_text: Optional[str] = Form(
        "",
        description="Text to be added to the back valence of the canopy.",
        example=DEFAULT_TEXT,
    ),
    right_text: Optional[str] = Form(
        "",
        description="Text to be added to the right valence of the canopy.",
        example=DEFAULT_TEXT,
    ),
    table_color: Optional[str] = Form(
        "",
        description="Color for the table. Must be a string representation of a list of three integers representing the BGR color value.",
        example=f'"{DEFAULT_TENT_COLOR}"',
    ),
    output_dir: str = Form('"{DEFAULT_OUTPUT_DIR}"'),
    tent_types: Optional[str] = Form(
        description="The tent types which should be generated"
    )
):
    """
    Create mockups for canopy layouts with the provided logo, colour, and text, if any
    """
    try:
        request_id = str(uuid.uuid4())
        kv.set(f"{output_dir}:{request_id}", json.dumps({"status": "processing"}), opts)
        
        tent_types = validate_tent_types(tent_types)
        font_color = validate_color(text_color)
        text = ValencesText(
            front=front_text, left=left_text, back=back_text, right=right_text
        )

        peaks = TentSides(
            front=validate_color(peaks_front),
            left=validate_color(peaks_left, optional=True)
            or validate_color(peaks_front),
            right=validate_color(peaks_right, optional=True)
            or validate_color(peaks_front),
            back=validate_color(peaks_back, optional=True)
            or validate_color(peaks_front),
        )

        valences = TentSides(
            front=validate_color(valences_front),
            left=validate_color(valences_left, optional=True)
            or validate_color(valences_front),
            right=validate_color(valences_right, optional=True)
            or validate_color(valences_front),
            back=validate_color(valences_back, optional=True)
            or validate_color(valences_front),
        )
        panels = TentSides(
            back=validate_color(panels_back, optional=True),
            left=validate_color(panels_left, optional=True),
            right=validate_color(panels_right, optional=True),
        )

        addons = (
            AddOns(table=Table(sides=TentSides(front=validate_color(table_color))))
            if table_color
            else None
        )

        logo_content = await logo.read()
        overlay_data = OverlayRequest(
            peaks=peaks,
            valences=valences,
            panels=panels,
            font_color=font_color,
            font_size=text_size,
            font_url=font_url,
            text=text,
            add_ons=addons,
            output_dir=output_dir,
            tent_types=tent_types
        )
        
        from threading import Thread
        def run_generation():
            try:
                result = generate_mockups(overlay_data, logo_content)
                payload = json.dumps({ "status": "ready", "mockups": result})
                encoded_payload = base64.urlsafe_b64encode(payload.encode()).decode()
                kv.set(f"{output_dir}:{request_id}", encoded_payload, opts)
            except Exception as e:
                kv.set(f"{output_dir}:{request_id}", json.dumps({ "status": "error", "error": str(e)}), opts)

        Thread(target=run_generation).start()

        return {"mockupRequestId": request_id}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/mockup-status", tags=["Mockup Creation"])
async def get_mockup_status(request_id: str, output_dir: str):
    result = kv.get(f"{output_dir}:{request_id}")
    if not result:
        raise HTTPException(status_code=404, detail="Invalid request ID")
    if ("status" in result):
        return json.loads(result)
    else:
        decoded = base64.urlsafe_b64decode(result).decode()
        return json.loads(decoded)