import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from app.schema import OverlayRequest
from app.config import Config
from app.constants import OVERLAY_CONFIGURATIONS, DEFAULT_TEXT, DEFAULT_FONT_SIZE, DEFAULT_PADDING, DEFAULT_ROTATION_ANGLE, DEFAULT_FONT_COLOUR, DEFAULT_TENT_COLOR, TENT_MOCKUPS, SLOPE_CENTERS

# Helper functions to add text to image
def create_text_image(text=DEFAULT_TEXT, font_size=DEFAULT_FONT_SIZE, font_color=DEFAULT_FONT_COLOUR, padding=DEFAULT_PADDING, rotation_angle=0):
    font_path = f"{Config.FONT_PATH}/font.ttf"
    font = ImageFont.truetype(font_path, font_size)

    # Convert BGR to RGBA
    font_color_rgba = (font_color[2], font_color[1], font_color[0], 255)  # Add full opacity

    # Calculate the size of the text using a dummy image
    dummy_img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    draw = ImageDraw.Draw(dummy_img)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Create a larger container (canvas) to allow for rotation and centering
    canvas_size = (text_width + 2 * padding, text_height + 2 * padding)
    container = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(container)

    # Draw the text centered in the container
    text_x = (canvas_size[0] - text_width) // 2
    text_y = (canvas_size[1] - text_height) // 2
    draw.text((text_x, text_y), text, font=font, fill=font_color_rgba)

    # Rotate the container if rotation_angle is specified
    if rotation_angle != 0:
        container = container.rotate(rotation_angle, expand=True)

    # Convert to a NumPy array for OpenCV with RGBA to BGRA conversion
    return cv2.cvtColor(np.array(container), cv2.COLOR_RGBA2BGRA)


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


# Helper function to apply logo to mockup
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

def apply_color(tent_image, config, color=[0, 0, 0]):
    mask = np.zeros(tent_image.shape[:2], dtype=np.uint8)
    
    for _, points in config.items():
        cv2.fillPoly(mask, [np.array(points, np.int32)], 255)
            
    mask_expanded = cv2.merge([mask] * 3)
    color_overlay = np.full(tent_image.shape, color, dtype=np.uint8)

    colored_image = tent_image.copy()
    colored_image[mask_expanded == 255] = color_overlay[mask_expanded == 255]
    
    return colored_image

def overlay_logo(tent_image, logo_img, coordinates, scale=0.4):
    """ Overlays a perspective-transformed logo within a scaled quadrilateral region on the tent image. """
    scaled_coordinates = scale_quadrilateral(coordinates, scale)

    src_points = np.array([[0, 0], [logo_img.shape[1], 0], 
                           [logo_img.shape[1], logo_img.shape[0]], [0, logo_img.shape[0]]], dtype="float32")

    dst_points = np.array(scaled_coordinates, dtype="float32")

    if logo_img.shape[2] == 4:
        logo_img = cv2.cvtColor(logo_img, cv2.COLOR_BGRA2BGR)

    M = cv2.getPerspectiveTransform(src_points, dst_points)
    warped_logo = cv2.warpPerspective(logo_img, M, (tent_image.shape[1], tent_image.shape[0]))

    if warped_logo.shape[2] == 4: 
        warped_logo = cv2.cvtColor(warped_logo, cv2.COLOR_BGRA2BGR)

    warped_gray = cv2.cvtColor(warped_logo, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(warped_gray, 1, 255, cv2.THRESH_BINARY)
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


def apply_all_logos(overlay_data: OverlayRequest, logo_content: bytes):
    output_images = []
    
    for tent_type, tent_path in TENT_MOCKUPS.items():
        
        relative_path = f"{Config.BASE_IMAGE_PATH}/{tent_path}"
        tent_image = cv2.imread(relative_path)
        logo_array = np.frombuffer(logo_content, np.uint8)
        logo_image = cv2.imdecode(logo_array, cv2.IMREAD_UNCHANGED)
        case_config = OVERLAY_CONFIGURATIONS.get(tent_type)
        color_coordinates = case_config.get("color-coordinates")
        logos = case_config.get("logos")
        masks = case_config.get("masks")
        
        extracted_masks = {}
        
        if (masks is not None) and (len(masks) > 0):
            for mask_key, mask_coordinates in masks.items():
                extracted_masks[mask_key] = extract_masks(tent_image, mask_coordinates)
                
        tent_image = apply_color(tent_image, color_coordinates, overlay_data.color)
        
        for logo_key, logo_value in logos.items():
            overlay_image = logo_image
            if "text" in logo_key:
                overlay_image = create_text_image(overlay_data.text)
                
            coordinates = logo_value.get("coordinates")
            scale = logo_value.get("scale")
            mask = logo_value.get("mask", None)
            
            if mask is not None:
                extracted = extract_masks(tent_image, coordinates=mask)
            tent_image = overlay_logo(tent_image, overlay_image, coordinates=coordinates, scale=scale)
            if mask is not None:
                tent_image = overlay_masks(tent_image, coordinates=mask, extracted_mask=extracted)
            
        if len(extracted_masks) > 0:
            for mask_key, mask_coordinates in masks.items():
                tent_image = overlay_masks(tent_image, extracted_masks.get(mask_key), mask_coordinates)
                
        is_success, buffer = cv2.imencode(".jpg", tent_image)
        if is_success:
            output_images.append((f"output_{tent_type}.jpg", buffer.tobytes()))
        
    return output_images
         
        