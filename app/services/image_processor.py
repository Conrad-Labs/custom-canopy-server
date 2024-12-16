import io
import zipfile
import cv2
from fastapi import HTTPException
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from app.schema import OverlayRequest
from app.constants import OVERLAY_CONFIGURATIONS, DEFAULT_TEXT, DEFAULT_FONT_SIZE, DEFAULT_PADDING, DEFAULT_ROTATION_ANGLE, DEFAULT_FONT_COLOUR, DEFAULT_TENT_COLOR, TENT_MOCKUPS, SLOPE_CENTERS, DEFAULT_FONT_URL, DEFAULT_TEMPLATE_URL

# Helper function to create an image to overlay text on mockup
def create_text_image(
    text=DEFAULT_TEXT,
    font_size=DEFAULT_FONT_SIZE,
    font_color=DEFAULT_FONT_COLOUR,
    padding=DEFAULT_PADDING,
    rotation_angle=DEFAULT_ROTATION_ANGLE,
    font_url=DEFAULT_FONT_URL
    ):
    """
    Creates an image for the text provided by the user with the specified font size, color, padding, and rotation angle.
    The text image can then be overlaid onto the mockup like any other image.

    """
    if not font_url:
        raise ValueError("Font URL must be provided.")
    
    response = requests.get(font_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the font file. Status code: {response.status_code}")
    
    font_bytes = io.BytesIO(response.content)
    font = ImageFont.truetype(font_bytes, font_size)
    font_color_rgba = (font_color[2], font_color[1], font_color[0], 255)

    dummy_img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    draw = ImageDraw.Draw(dummy_img)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = (text_bbox[2] - text_bbox[0])
    text_height = (text_bbox[3] - text_bbox[1])

    canvas_size = (text_width + 2 * padding, text_height + 2 * padding)
    container = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(container)

    text_x = (canvas_size[0] - text_width) // 2
    text_y = (canvas_size[1] - text_height) // 2
    draw.text((text_x, text_y), text, font=font, fill=font_color_rgba)

    if rotation_angle != 0:
        container = container.rotate(rotation_angle, expand=True)

    downscaled_container = container.resize(
        (canvas_size[0], canvas_size[1]),
        Image.LANCZOS
    )

    return cv2.cvtColor(np.array(downscaled_container), cv2.COLOR_RGBA2BGRA)


# Helper functions to extract and reapply masks from base mockup
def extract_masks(tent_image, coordinates):
    """
    Extracts a mask from the tent image.
    Supports both bounding box (x1, y1, x2, y2) and quadrilateral coordinates.
    """
    if len(coordinates) == 2:
        (x1, y1), (x2, y2) = coordinates
        extracted = tent_image[y1:y2, x1:x2].copy()
    elif len(coordinates) == 4:
        src_points = np.array(coordinates, dtype="float32")
        x_min = int(min([pt[0] for pt in coordinates]))
        y_min = int(min([pt[1] for pt in coordinates]))
        x_max = int(max([pt[0] for pt in coordinates]))
        y_max = int(max([pt[1] for pt in coordinates]))

        dst_points = np.array([[0, 0], [x_max - x_min, 0], [x_max - x_min, y_max - y_min], [0, y_max - y_min]], dtype="float32")

        M = cv2.getPerspectiveTransform(src_points, dst_points)
        extracted = cv2.warpPerspective(tent_image, M, (x_max - x_min, y_max - y_min))
    else:
        raise ValueError("Invalid coordinates provided for mask extraction. Must be 2 points (x1, y1, x2, y2) or 4 points for a quadrilateral.")

    return extracted


def overlay_masks(tent_image, extracted_mask, coordinates):
    """
    Overlays the extracted mask onto the tent image.
    Supports both bounding box (x1, y1, x2, y2) and quadrilateral coordinates.
    """
    if len(coordinates) == 2:
        (x1, y1), (x2, y2) = coordinates
        tent_image[y1:y2, x1:x2] = extracted_mask
    elif len(coordinates) == 4:
        src_points = np.array([[0, 0], [extracted_mask.shape[1], 0], 
                               [extracted_mask.shape[1], extracted_mask.shape[0]], [0, extracted_mask.shape[0]]], dtype="float32")
        dst_points = np.array(coordinates, dtype="float32")

        M = cv2.getPerspectiveTransform(src_points, dst_points)
        warped_mask = cv2.warpPerspective(extracted_mask, M, (tent_image.shape[1], tent_image.shape[0]))

        mask_gray = cv2.cvtColor(warped_mask, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask_gray, 1, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        tent_bg = cv2.bitwise_and(tent_image, tent_image, mask=mask_inv)
        mask_fg = cv2.bitwise_and(warped_mask, warped_mask, mask=mask)
        tent_image = cv2.add(tent_bg, mask_fg)
    else:
        raise ValueError("Invalid coordinates provided for overlay. Must be 2 points (x1, y1, x2, y2) or 4 points for a quadrilateral.")

    return tent_image


# Helper functions to apply logos to a mockup
def scale_quadrilateral(coordinates, scale):
    """Scales a quadrilateral around its centroid by the given scale factor."""
    centroid_x = int(np.mean([p[0] for p in coordinates]))
    centroid_y = int(np.mean([p[1] for p in coordinates]))

    scaled_coordinates = []
    for (x, y) in coordinates:
        scaled_x = int(centroid_x + scale * (x - centroid_x))
        scaled_y = int(centroid_y + scale * (y - centroid_y))
        scaled_coordinates.append((scaled_x, scaled_y))

    return scaled_coordinates


def apply_color(tent_image, config, slope_color=DEFAULT_TENT_COLOR, canopy_color=DEFAULT_TENT_COLOR, walls_color=DEFAULT_TENT_COLOR):
    """
    Applies the chosen color to the mockup while preserving shadows and highlights.
    """
    tent_image_hsv = cv2.cvtColor(tent_image, cv2.COLOR_BGR2HSV)

    def get_normalized_color(color):
        color_hsv = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0]
        return color_hsv[0], color_hsv[1], color_hsv[2]
    
    slope_hue, slope_saturation, slope_value = get_normalized_color(slope_color)
    canopy_hue, canopy_saturation, canopy_value = get_normalized_color(canopy_color)
    walls_hue, walls_saturation, walls_value = get_normalized_color(walls_color)

    for region, points in config.items():
        if "slope" in region:
            hue, saturation, value = slope_hue, slope_saturation, slope_value
        elif "canopy" in region:
            hue, saturation, value = canopy_hue, canopy_saturation, canopy_value
        else: 
            hue, saturation, value = walls_hue, walls_saturation, walls_value
        mask = np.zeros(tent_image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points, np.int32)], 255)
        masked_hsv = cv2.bitwise_and(tent_image_hsv, tent_image_hsv, mask=mask)
        masked_hsv[..., 0] = hue
        masked_hsv[..., 1] = saturation
        masked_hsv[..., 2] = value
        colored_region = cv2.cvtColor(masked_hsv, cv2.COLOR_HSV2BGR)
        color_overlay = cv2.bitwise_and(colored_region, colored_region, mask=mask)
        tent_image = cv2.bitwise_and(tent_image, tent_image, mask=cv2.bitwise_not(mask))
        tent_image = cv2.add(tent_image, color_overlay)

    return tent_image


def overlay_logo(tent_image, logo_img, coordinates, scale=0.4):
    """ Overlays a perspective-transformed logo within a scaled quadrilateral region on the tent image. """
    scaled_coordinates = scale_quadrilateral(coordinates, scale)
    src_points = np.array([[0, 0], [logo_img.shape[1], 0], 
                           [logo_img.shape[1], logo_img.shape[0]], [0, logo_img.shape[0]]], dtype="float32")
    dst_points = np.array(scaled_coordinates, dtype="float32")


    if logo_img.shape[2] == 4:
        b, g, r, a = cv2.split(logo_img)
        logo_rgb = cv2.merge((b, g, r))
        alpha_mask = cv2.merge((a, a, a))
    else:
        logo_rgb = logo_img
        alpha_mask = np.ones((logo_img.shape[0], logo_img.shape[1], 3), dtype=np.uint8) * 255

    M = cv2.getPerspectiveTransform(src_points, dst_points)
    warped_logo = cv2.warpPerspective(logo_rgb, M, (tent_image.shape[1], tent_image.shape[0]))
    warped_mask = cv2.warpPerspective(alpha_mask, M, (tent_image.shape[1], tent_image.shape[0]))

    mask_gray = cv2.cvtColor(warped_mask, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask_gray, 1, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    x_min = max(0, min([pt[0] for pt in scaled_coordinates]))
    y_min = max(0, min([pt[1] for pt in scaled_coordinates]))
    x_max = min(tent_image.shape[1], max([pt[0] for pt in scaled_coordinates]))
    y_max = min(tent_image.shape[0], max([pt[1] for pt in scaled_coordinates]))

    roi = tent_image[y_min:y_max, x_min:x_max]

    warped_logo_cropped = warped_logo[y_min:y_max, x_min:x_max]
    mask_cropped = mask[y_min:y_max, x_min:x_max]
    mask_inv_cropped = mask_inv[y_min:y_max, x_min:x_max]

    tent_bg = cv2.bitwise_and(roi, roi, mask=mask_inv_cropped)
    logo_fg = cv2.bitwise_and(warped_logo_cropped, warped_logo_cropped, mask=mask_cropped)

    dst = cv2.add(tent_bg, logo_fg)
    tent_image[y_min:y_max, x_min:x_max] = dst

    return tent_image


def overlay_template(tent_image, template_img, coordinates, scale=0.4):
    """
    Applies a perspective-transformed template (logo or pattern) onto the tent image
    while preserving the natural shadows and highlights of the tent surface and adhering
    to the shape of the quadrilateral (slope).
    """
    scaled_coordinates = scale_quadrilateral(coordinates, scale)
    x_min, y_min = np.min(scaled_coordinates, axis=0)
    x_max, y_max = np.max(scaled_coordinates, axis=0)
    x_min = max(0, x_min)
    y_min = max(0, y_min)
    x_max = min(tent_image.shape[1], x_max)
    y_max = min(tent_image.shape[0], y_max)

    region = tent_image[y_min:y_max, x_min:x_max]
    template_resized = cv2.resize(template_img, (x_max - x_min, y_max - y_min))
    region_hsv = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    template_hsv = cv2.cvtColor(template_resized, cv2.COLOR_BGR2HSV)
    avg_lightness = np.mean(region_hsv[:, :, 2]) 
    avg_template_lightness = np.mean(template_hsv[:, :, 2])
    lightness_scale = avg_lightness / avg_template_lightness
    template_hsv[:, :, 2] = np.clip(template_hsv[:, :, 2] * lightness_scale, 0, 255)
    adjusted_template = cv2.cvtColor(template_hsv, cv2.COLOR_HSV2BGR)
    template_gray = cv2.cvtColor(adjusted_template, cv2.COLOR_BGR2GRAY)
    _, template_mask = cv2.threshold(template_gray, 1, 255, cv2.THRESH_BINARY)
    template_fg = cv2.bitwise_and(adjusted_template, adjusted_template, mask=template_mask)
    src_points = np.array([[0, 0], [template_resized.shape[1], 0],
                           [template_resized.shape[1], template_resized.shape[0]], [0, template_resized.shape[0]]], dtype="float32")
    dst_points = np.array(scaled_coordinates, dtype="float32")
    M = cv2.getPerspectiveTransform(src_points, dst_points)
    warped_template = cv2.warpPerspective(template_fg, M, (tent_image.shape[1], tent_image.shape[0]))
    tent_image[y_min:y_max, x_min:x_max] = warped_template[y_min:y_max, x_min:x_max]

    return tent_image


def color_template(template, walls_primary_color, walls_secondary_color, walls_tertiary_color):
    """
    Colors the different regions of a template based on black lines separating the regions.
    """
    gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    colors = [(walls_secondary_color[0], walls_secondary_color[1], walls_secondary_color[2]), 
              (walls_tertiary_color[0], walls_tertiary_color[1], walls_tertiary_color[2]), 
              (walls_primary_color[0], walls_primary_color[1], walls_primary_color[2]), 
              (walls_secondary_color[0], walls_secondary_color[1], walls_secondary_color[2]),
              (walls_tertiary_color[0], walls_tertiary_color[1], walls_tertiary_color[2]), ]
    colored_image = template.copy()
    for idx, contour in enumerate(contours):
        color = colors[idx % len(colors)]
        cv2.drawContours(colored_image, [contour], -1, color, thickness=cv2.FILLED)
            
    return colored_image


# Main function that applies logos and generates a mockup based on user requirements
def apply_all_logos(overlay_data: OverlayRequest, logo_content: bytes, zipfile: zipfile.ZipFile):
    """Generates canopy mockups based on user requirements of base color, text, font color, etc"""
    logo_array = np.frombuffer(logo_content, np.uint8)
    logo_image = cv2.imdecode(logo_array, cv2.IMREAD_UNCHANGED)
    
    response = requests.get(DEFAULT_TEMPLATE_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Tent image {tent_type} not found.")
    
    template = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    template = color_template(template, overlay_data.walls_primary_color, overlay_data.walls_secondary_color, overlay_data.walls_tertiary_color)
    
    for tent_type, tent_path in TENT_MOCKUPS.items():
        
        response = requests.get(tent_path)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail=f"Tent image {tent_type} not found.")
        
        tent_image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
        case_config = OVERLAY_CONFIGURATIONS.get(tent_type)
        color_coordinates = case_config.get("color-coordinates")
        logos = case_config.get("logos")
        masks = case_config.get("masks")
        
        extracted_masks = {}
        
        if (masks is not None) and (len(masks) > 0):
            for mask_key, mask_coordinates in masks.items():
                extracted_masks[mask_key] = extract_masks(tent_image, mask_coordinates)
                
        tent_image = apply_color(tent_image, color_coordinates, 
                        slope_color=overlay_data.slope_color, 
                        canopy_color=overlay_data.canopy_color, 
                        walls_color=overlay_data.walls_primary_color)
        
        for logo_key, logo_value in logos.items():
            overlay_image = logo_image
            if "text" in logo_key:
                overlay_image = create_text_image(overlay_data.text, font_color=overlay_data.font_color)
                
            coordinates = logo_value.get("coordinates")
            scale = logo_value.get("scale")
            mask = logo_value.get("mask", None)
            
            if mask is not None:
                extracted = extract_masks(tent_image, coordinates=mask)
            if "template" in logo_key:
                if 'true' in overlay_data.is_patterned:
                    tent_image = overlay_template(tent_image, template, coordinates=coordinates, scale=scale)
            else:
                tent_image = overlay_logo(tent_image, overlay_image, coordinates=coordinates, scale=scale)
            if mask is not None:
                tent_image = overlay_masks(tent_image, coordinates=mask, extracted_mask=extracted)
            
        if len(extracted_masks) > 0:
            for mask_key, mask_coordinates in masks.items():
                tent_image = overlay_masks(tent_image, extracted_masks.get(mask_key), mask_coordinates)
                
        is_success, buffer = cv2.imencode(".jpg", tent_image)
        if is_success:
            zipfile.writestr(f"output_{tent_type}.jpg", buffer.tobytes())
        
         
        