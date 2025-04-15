import io
import cv2
from fastapi import HTTPException
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from app.schema import OverlayRequest
from app.constants import (
    OVERLAY_CONFIGURATIONS,
    DEFAULT_TEXT,
    DEFAULT_FONT_SIZE,
    DEFAULT_ROTATION_ANGLE,
    DEFAULT_FONT_COLOUR,
    DEFAULT_FONT_URL,
    MOCKUP_ITEMS,
    DEFAULT_OUTPUT_DIR,
)
from typing import List, Dict, Any
from enum import Enum
from vercel_storage import blob


def create_text_image(
    target_width,
    target_height,
    text=DEFAULT_TEXT,
    font_size=DEFAULT_FONT_SIZE,
    font_color=DEFAULT_FONT_COLOUR,
    rotation_angle=DEFAULT_ROTATION_ANGLE,
    font_url=DEFAULT_FONT_URL
):
    """
    Creates an image for the text provided by the user with the specified font size, color, padding, and rotation angle.
    The text image can then be overlaid onto the mockup like any other image.

    """
    if not font_url:
        raise ValueError("Font URL must be provided.")
    
    spacing = 20
    hi_res_factor = 4
    render_width = target_width * hi_res_factor
    render_height = target_height * hi_res_factor

    response = requests.get(font_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the font file. Status code: {response.status_code}")
    font_bytes = io.BytesIO(response.content)
    font = ImageFont.truetype(font_bytes, font_size)
    font_color_rgba = (font_color[2], font_color[1], font_color[0], 255)
    
    char_widths = [font.getbbox(c)[2] for c in text]
    text_width = sum(char_widths) + (len(text) - 1) * spacing
    text_height = font.getbbox(text)[3] - font.getbbox(text)[1]

    canvas_width = max(render_width, text_width + 20)
    canvas_height = max(render_height, text_height + 20)
    canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    text_x = (canvas_width - text_width) // 2
    text_y = (canvas_height - text_height) // 2
    x = text_x
    for char in text:
        draw.text((x, text_y), char, font=font, fill=font_color_rgba, stroke_width=12)
        char_width = font.getbbox(char)[2]
        x += char_width + spacing

    
    if rotation_angle != 0:
        canvas = canvas.rotate(rotation_angle, expand=True)

    return cv2.cvtColor(np.array(canvas), cv2.COLOR_RGBA2BGRA)

# Helper functions to extract and reapply masks from base mockup
def extract_masks(mockup_image, coordinates):
    """
    Extracts a mask from the tent image.
    Supports both bounding box (x1, y1, x2, y2) and quadrilateral coordinates.
    """
    if len(coordinates) == 2:
        (x1, y1), (x2, y2) = coordinates
        extracted = mockup_image[y1:y2, x1:x2].copy()
    elif len(coordinates) == 4:
        src_points = np.array(coordinates, dtype="float32")
        x_min = int(min([pt[0] for pt in coordinates]))
        y_min = int(min([pt[1] for pt in coordinates]))
        x_max = int(max([pt[0] for pt in coordinates]))
        y_max = int(max([pt[1] for pt in coordinates]))

        dst_points = np.array(
            [
                [0, 0],
                [x_max - x_min, 0],
                [x_max - x_min, y_max - y_min],
                [0, y_max - y_min],
            ],
            dtype="float32",
        )

        M = cv2.getPerspectiveTransform(src_points, dst_points)
        extracted = cv2.warpPerspective(mockup_image, M, (x_max - x_min, y_max - y_min))
    else:
        raise ValueError(
            "Invalid coordinates provided for mask extraction. Must be 2 points (x1, y1, x2, y2) or 4 points for a quadrilateral."
        )

    return extracted


def overlay_masks(mockup_image, extracted_mask, coordinates):
    """
    Overlays the extracted mask onto the tent image.
    Supports both bounding box (x1, y1, x2, y2) and quadrilateral coordinates.
    """
    if len(coordinates) == 2:
        (x1, y1), (x2, y2) = coordinates
        mockup_image[y1:y2, x1:x2] = extracted_mask
    elif len(coordinates) == 4:
        src_points = np.array(
            [
                [0, 0],
                [extracted_mask.shape[1], 0],
                [extracted_mask.shape[1], extracted_mask.shape[0]],
                [0, extracted_mask.shape[0]],
            ],
            dtype="float32",
        )
        dst_points = np.array(coordinates, dtype="float32")

        M = cv2.getPerspectiveTransform(src_points, dst_points)
        warped_mask = cv2.warpPerspective(
            extracted_mask, M, (mockup_image.shape[1], mockup_image.shape[0])
        )

        mask_gray = cv2.cvtColor(warped_mask, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask_gray, 1, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        mockup_bg = cv2.bitwise_and(mockup_image, mockup_image, mask=mask_inv)
        mask_fg = cv2.bitwise_and(warped_mask, warped_mask, mask=mask)
        mockup_image = cv2.add(mockup_bg, mask_fg)
    else:
        raise ValueError(
            "Invalid coordinates provided for overlay. Must be 2 points (x1, y1, x2, y2) or 4 points for a quadrilateral."
        )

    return mockup_image


# Helper functions to apply logos to a mockup
def scale_quadrilateral(pts, scale_factor):
    """Scales a quadrilateral inward toward its centroid."""
    pts = np.array(pts, dtype="float32")  # Ensure `pts` is a NumPy array
    centroid = np.mean(pts, axis=0)       # Calculate the centroid as a NumPy array
    scaled_pts = (1 - scale_factor) * centroid + scale_factor * pts
    return scaled_pts



def convert_color_to_hsv(color):
    return cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0]


def process_overlay_colors(obj):
    for attr, value in obj.__dict__.items():
        if value is not None:
            setattr(obj, attr, convert_color_to_hsv(value))


def convert_overlay_colors(overlay_data: OverlayRequest):
    process_overlay_colors(overlay_data.peaks)
    process_overlay_colors(overlay_data.valences)
    process_overlay_colors(overlay_data.panels)
    if overlay_data.add_ons and overlay_data.add_ons.table:
        process_overlay_colors(overlay_data.add_ons.table.sides)
    return overlay_data


def apply_color(mockup_image, config, overlay_data: OverlayRequest):
    """
    Applies the chosen color to the mockup while preserving shadows and highlights.
    """
    mockup_image_hsv = cv2.cvtColor(mockup_image, cv2.COLOR_BGR2HSV)

    def apply_region_color(region_mask, target_color):
        original_v = mockup_image_hsv[..., 2]
        solid_color_hsv = np.full_like(
            mockup_image_hsv, (target_color[0], target_color[1], 0)
        )  # (H, S, 0)
        solid_color_hsv[..., 2] = original_v
        colored_region = cv2.cvtColor(solid_color_hsv, cv2.COLOR_HSV2BGR)
        colored_region = cv2.bitwise_and(
            colored_region, colored_region, mask=region_mask
        )
        mockup_masked = cv2.bitwise_and(
            mockup_image, mockup_image, mask=cv2.bitwise_not(region_mask)
        )
        return cv2.add(mockup_masked, colored_region)

    # Apply colors for different regions
    for region, sides in config.items():
        reg = getattr(overlay_data, region)
        for side, points in sides.items():
            target_color = getattr(reg, side) if hasattr(reg, side) else reg
            if target_color is not None:
                if isinstance(points, dict):
                    points = points.values()
                    for point in points:
                        mask = np.zeros(mockup_image.shape[:2], dtype=np.uint8)
                        if isinstance(point, dict):
                            if "circle" in point:
                                circle = point.get("circle")
                                center = circle.get("center")
                                axes = circle.get("axes")
                                angle = circle.get("angle")
                                start_angle = circle.get("start_angle")
                                end_angle = circle.get("end_angle")
                                mask = np.zeros(mockup_image.shape[:2], dtype=np.uint8)
                                cv2.ellipse(
                                    mask,
                                    center,
                                    axes,
                                    angle,
                                    start_angle,
                                    end_angle,
                                    255,
                                    thickness=-1,
                                )
                        else:
                            cv2.fillPoly(mask, [np.array(point, np.int32)], 255)

                        mockup_image = apply_region_color(mask, target_color)
                else:
                    mask = np.zeros(mockup_image.shape[:2], dtype=np.uint8)
                    cv2.fillPoly(mask, [np.array(points, np.int32)], 255)
                    mockup_image = apply_region_color(mask, target_color)

    return mockup_image


def overlay_logo(mockup_image, logo_img, coordinates, scale=0.4):
    """Overlays a perspective-transformed logo within a scaled quadrilateral region on the tent image."""
    scaled_coordinates = scale_quadrilateral(coordinates, scale)
    dst_points = np.array(scaled_coordinates, dtype="float32")

    x_min = int(min(dst_points[:, 0]))
    y_min = int(min(dst_points[:, 1]))
    x_max = int(max(dst_points[:, 0]))
    y_max = int(max(dst_points[:, 1]))

    target_width = x_max - x_min
    target_height = y_max - y_min

    logo_resized = cv2.resize(logo_img, (target_width, target_height), interpolation=cv2.INTER_AREA)

    src_points = np.array([
        [0, 0],
        [target_width, 0],
        [target_width, target_height],
        [0, target_height],
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(src_points, dst_points)
    warped_logo = cv2.warpPerspective(logo_resized, M, (mockup_image.shape[1], mockup_image.shape[0]))
    
    if warped_logo.shape[2] == 4:
        alpha_channel = warped_logo[:, :, 3]
        warped_logo = cv2.cvtColor(warped_logo, cv2.COLOR_BGRA2BGR)
    else:
        alpha_channel = cv2.cvtColor(warped_logo, cv2.COLOR_BGR2GRAY)

    _, mask = cv2.threshold(alpha_channel, 1, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    mask_inv_rgb = cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2BGR)

    if warped_logo.shape[:2] != mockup_image.shape[:2]:
        warped_logo = cv2.resize(warped_logo, (mockup_image.shape[1], mockup_image.shape[0]))
        mask_rgb = cv2.resize(mask_rgb, (mockup_image.shape[1], mockup_image.shape[0]))
        mask_inv_rgb = cv2.resize(mask_inv_rgb, (mockup_image.shape[1], mockup_image.shape[0]))

    background = cv2.bitwise_and(mockup_image, mask_inv_rgb)
    foreground = cv2.bitwise_and(warped_logo, mask_rgb)
    mockup_image = cv2.add(background, foreground)

    return mockup_image

def filter_mockup_items(request_data: Dict[str, Any]) -> Dict[str, List[Dict]]:
    """
    Generalized function to filter mockup items based on include and exclude conditions
    and group the results by category.

    :param request_data: Dictionary containing request parameters.
    :return: Dictionary with categories as keys and lists of matching mockup items as values.
    """

    def matches_condition(value, condition):
        """
        Helper function to evaluate if a value matches a condition.
        Supports nested dictionaries and Enums.
        """
        if isinstance(condition, dict):
            return all(matches_condition(value.get(k), v) for k, v in condition.items())
        if isinstance(value, Enum):
            return value.value == condition
        return value == condition

    def satisfies_conditions(item, data):
        """
        Check if an item satisfies include conditions and avoids exclude conditions.
        """
        include_conditions = item.get("include_conditions", {})
        exclude_conditions = item.get("exclude_conditions", {})

        meets_include = all(
            matches_condition(data.get(k), v) for k, v in include_conditions.items()
        )
        tent_type = include_conditions.get("tent_type")
        if tent_type and "tent_types" in data:
            meets_include = tent_type in data["tent_types"]
        else:
            meets_include = all(
                matches_condition(data.get(k), v) for k, v in include_conditions.items()
            )
        avoids_exclude = not any(
            True if data.get(k) is None else matches_condition(data.get(k), v)
            for k, v in exclude_conditions.items()
        )

        return (
            (
                include_conditions
                and exclude_conditions
                and meets_include
                and avoids_exclude
            )
            or (include_conditions and not exclude_conditions and meets_include)
            or (not include_conditions and exclude_conditions and avoids_exclude)
        )

    return {
        category: [
            item
            for item in items
            if satisfies_conditions(item, request_data)
            or item.get("include_conditions", {}).get("tent_type") == "all"
        ]
        for category, items in MOCKUP_ITEMS.items()
    }


def generate_mockups(overlay_data: OverlayRequest, logo_content: bytes):
    """Generates canopy mockups based on user requirements of base color, text, font color, etc."""
    logo_image = preprocess_logo(logo_content)
    overlay_data = convert_overlay_colors(overlay_data)
    mockups = filter_mockup_items(overlay_data.model_dump())
    generate_mockups = {}
    for category, items in mockups.items():
        for item in items:
            config = (
                OVERLAY_CONFIGURATIONS.get(category)
                if category == "add_ons"
                else OVERLAY_CONFIGURATIONS
            )
            name = item.get("name")
            generate_mockups[name] = generate_single_mockup(
                item,
                config,
                (
                    getattr(getattr(overlay_data, category), name)
                    if category == "add_ons"
                    else overlay_data
                ),
                logo_image,
                overlay_data.output_dir,
                (
                    overlay_data.font_size * 2
                    if "front" in category
                    else overlay_data.font_size
                )
            )

    return generate_mockups


def generate_single_mockup(
    item: dict,
    config: dict,
    data: Dict[str, Any],
    logo_image: Image,
    output_dir: str = DEFAULT_OUTPUT_DIR,
    font_size: int = DEFAULT_FONT_SIZE
):
    name = item.get("name")
    mockup_image = fetch_mockup_image(name, item.get("url"))
    case_config = config.get(name)
    masks = case_config.get("masks")

    extracted_masks = extract_all_masks(mockup_image, masks)
    mockup_image = apply_color(mockup_image, case_config.get("color-coordinates"), data)
    mockup_image = apply_all_logos(
        mockup_image, data, logo_image, case_config.get("logos"), font_size
    )
    if len(extracted_masks) > 0:
        for mask_key, mask_coordinates in masks.items():
            mockup_image = overlay_masks(
                mockup_image, extracted_masks.get(mask_key), mask_coordinates
            )
    return save_mockup_image(mockup_image, name, output_dir)


def preprocess_logo(logo_content: bytes) -> np.ndarray:
    """Decodes and preprocesses the logo image."""
    logo_array = np.frombuffer(logo_content, np.uint8)
    return cv2.imdecode(logo_array, cv2.IMREAD_UNCHANGED)


def fetch_mockup_image(name: str, path: str) -> np.ndarray:
    """Fetches the tent image from the given path."""
    response = requests.get(path)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Tent image {name} not found.")
    return cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)


def extract_all_masks(mockup_image: np.ndarray, masks: dict) -> dict:
    """Extracts all masks based on the given configurations."""
    extracted_masks = {}
    if masks:
        for mask_key, mask_coordinates in masks.items():
            extracted_masks[mask_key] = extract_masks(mockup_image, mask_coordinates)
    return extracted_masks


def apply_all_logos(
    mockup_image: np.ndarray,
    overlay_data: OverlayRequest,
    logo_image: np.ndarray,
    logo_config: dict,
    font_size: int
) -> np.ndarray:
    """Applies all logos to the tent images."""
    for region, sub_region in logo_config.items():
        for sub_region_key, side in sub_region.items():
            if sub_region_key == "text":
                mockup_image = apply_text_logos(
                    mockup_image, overlay_data, side, font_size
                )
            else:
                mockup_image = apply_logo_images(mockup_image, logo_image, side)

    return mockup_image

def getTextContainerDimensions(coordinates: np.ndarray):
    width = abs(min(coordinates[1][0] - coordinates[0][0], coordinates[3][0] - coordinates[2][0]))
    height = abs(min(coordinates[2][1] - coordinates[1][1], coordinates[3][1] - coordinates[0][1]))
    return max(width, height), min(width, height)


def apply_text_logos(
    mockup_image: np.ndarray,
    overlay_data: OverlayRequest,
    texts: dict,
    font_size: int
) -> np.ndarray:
    """Overlays text-based logos on the tent image."""
    for logo_key, logo_value in texts.items():
        text = getattr(overlay_data.text, logo_key, DEFAULT_TEXT)
        
        coordinates, scale = logo_value.get("coordinates"), logo_value.get("scale")
        width, height = getTextContainerDimensions(coordinates)
        overlay_image = create_text_image(
            target_width=width,
            target_height=height,
            text=text,
            font_color=overlay_data.font_color,
            font_size=font_size,
            rotation_angle=logo_value.get("rotation_angle", DEFAULT_ROTATION_ANGLE),
            font_url=overlay_data.font_url
        )
        mockup_image = overlay_logo(
            mockup_image, overlay_image, coordinates=coordinates, scale=scale
        )
    return mockup_image


def apply_logo_images(
    mockup_image: np.ndarray, logo_image: np.ndarray, side: dict
) -> np.ndarray:
    """Overlays image-based logos on the tent image."""
    coordinates, scale, mask = (
        side.get("coordinates"),
        side.get("scale"),
        side.get("mask", None),
    )
    if mask is not None:
        extracted = extract_masks(mockup_image, coordinates=mask)
    mockup_image = overlay_logo(
        mockup_image, logo_image, coordinates=coordinates, scale=scale
    )
    if mask is not None:
        mockup_image = overlay_masks(
            mockup_image, coordinates=mask, extracted_mask=extracted
        )
    return mockup_image


def save_mockup_image(
    mockup_image: np.ndarray,
    name: str,
    output_dir: str = DEFAULT_OUTPUT_DIR,
) -> None:
    """Encodes the tent image and stores it in the blob storage."""
    is_success, buffer = cv2.imencode(".jpg", mockup_image)
    if is_success:
        return blob.put(f"{output_dir}/output_{name}.jpg", buffer.tobytes(), {})
    return None
