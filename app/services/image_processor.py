import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from app.schema import OverlayRequest
from app.config import Config
from app.constants import OVERLAY_CONFIGURATIONS, DEFAULT_TEXT, DEFAULT_FONT_SIZE, DEFAULT_PADDING, DEFAULT_ROTATION_ANGLE, DEFAULT_FONT_COLOUR, DEFAULT_TENT_COLOR, TENT_MOCKUPS, SLOPE_CENTERS

# Helper functions to add text to image
def create_text_image(text="Sample Text", font_size=DEFAULT_FONT_SIZE, font_color=DEFAULT_FONT_COLOUR, padding=DEFAULT_PADDING, rotation_angle=0):
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
def extract_masks(tent_image, mask_data):
    extracted = {}
    for key, (x1, y1, x2, y2) in mask_data.items():
        extracted[key] = tent_image[y1:y2, x1:x2].copy()
    
    return extracted

def overlay_masks(tent_image, extracted_masks, mask_data):
    for key, (x1, y1, x2, y2) in mask_data.items():
        if key in extracted_masks:
            tent_image[y1:y2, x1:x2] = extracted_masks[key]
    return tent_image



# Helper function to apply logo to mockup
def resize_logo(logo_bgr, logo_alpha, width_scale, height_scale, crop_type=None):
    logo_height, logo_width, _ = logo_bgr.shape
    logo_resized_width = int(logo_width * width_scale)
    logo_resized_height = int(logo_height * height_scale)

    logo_bgr_resized = cv2.resize(
        logo_bgr, (logo_resized_width, logo_resized_height), interpolation=cv2.INTER_CUBIC)
    logo_alpha_resized = cv2.resize(
        logo_alpha, (logo_resized_width, logo_resized_height), interpolation=cv2.INTER_CUBIC)

    if crop_type == 'vertical':
        # Crop logo to half vertically
        logo_bgr_resized = logo_bgr_resized[:, :logo_resized_width // 2]
        logo_alpha_resized = logo_alpha_resized[:, :logo_resized_width // 2]
    elif crop_type == 'horizontal':
        logo_bgr_resized = logo_bgr_resized[:logo_resized_height // 2, :]
        logo_alpha_resized = logo_alpha_resized[:logo_resized_height // 2, :]

    return logo_bgr_resized, logo_alpha_resized

def apply_perspective(logo_bgr_resized, logo_alpha_resized, tent_image, target_points):
    original_points = np.float32([[0, 0], [logo_bgr_resized.shape[1], 0], [
                                 0, logo_bgr_resized.shape[0]], [logo_bgr_resized.shape[1], logo_bgr_resized.shape[0]]])

    # Apply the perspective warp to the logo
    perspective_matrix = cv2.getPerspectiveTransform(
        original_points, target_points)
    warped_logo = cv2.warpPerspective(logo_bgr_resized, perspective_matrix, (
        tent_image.shape[1], tent_image.shape[0]), flags=cv2.INTER_CUBIC)
    warped_logo_alpha = cv2.warpPerspective(logo_alpha_resized, perspective_matrix, (
        tent_image.shape[1], tent_image.shape[0]), flags=cv2.INTER_CUBIC)

    # Create a mask for the warped logo
    logo_fg = cv2.bitwise_and(warped_logo, warped_logo, mask=warped_logo_alpha)
    mask_inv = cv2.bitwise_not(warped_logo_alpha)

    # Extract the region of the tent where the logo will be placed (background)
    tent_roi = cv2.bitwise_and(tent_image, tent_image, mask=mask_inv)

    # Combine the warped logo with the tent
    return cv2.add(tent_roi, logo_fg)

def apply_image_overlay(tent_image, overlay_bgr, overlay_alpha, width_scale, height_scale,  
                        top_left_y_factor=0, top_left_x_factor=0, top_right_y_factor=0, 
                        top_right_x_factor=0, bottom_left_y_factor=0, bottom_left_x_factor=0, 
                        bottom_right_y_factor=0, bottom_right_x_factor=0, top_y_factor=0.4,  
                        left_x_factor=0.5, crop_type=None, perspective=False, rotation_angle=0):
    
    # Resize the overlay (logo or text) image
    overlay_bgr_resized, overlay_alpha_resized = resize_logo(overlay_bgr, overlay_alpha, width_scale, height_scale, crop_type)
    
    # Ensure that overlay_alpha_resized is single-channel
    if len(overlay_alpha_resized.shape) > 2 and overlay_alpha_resized.shape[2] > 1:
        overlay_alpha_resized = overlay_alpha_resized[:, :, 0]
    
    # Rotate the overlay image if rotation_angle is specified
    if rotation_angle != 0:
        (h, w) = overlay_bgr_resized.shape[:2]
        center = (w // 2, h // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, scale=1.0)
        
        # Rotate both BGR and alpha channels
        overlay_bgr_resized = cv2.warpAffine(overlay_bgr_resized, rotation_matrix, (w, h))
        overlay_alpha_resized = cv2.warpAffine(overlay_alpha_resized, rotation_matrix, (w, h))
    
    # Convert overlay_alpha_resized to uint8 to ensure it works as a mask
    overlay_alpha_resized = overlay_alpha_resized.astype("uint8")
    
    # Calculate placement positions based on left_x_factor and top_y_factor
    tent_height, tent_width, _ = tent_image.shape
    top_left_x = int(tent_width * left_x_factor) - overlay_bgr_resized.shape[1] // 2
    top_y = int(tent_height * top_y_factor)

    # Adjust top_left_x and top_y if they exceed the tent image bounds
    if top_left_x < 0:
        top_left_x = 0
    if top_y < 0:
        top_y = 0
    if top_left_x + overlay_bgr_resized.shape[1] > tent_width:
        overlay_bgr_resized = overlay_bgr_resized[:, :tent_width - top_left_x]
        overlay_alpha_resized = overlay_alpha_resized[:, :tent_width - top_left_x]
    if top_y + overlay_bgr_resized.shape[0] > tent_height:
        overlay_bgr_resized = overlay_bgr_resized[:tent_height - top_y, :]
        overlay_alpha_resized = overlay_alpha_resized[:tent_height - top_y, :]

    if not perspective:
        # Directly overlay the image without perspective transformation
        roi = tent_image[top_y:top_y + overlay_bgr_resized.shape[0],
                         top_left_x:top_left_x + overlay_bgr_resized.shape[1]]

        # Create foreground and background regions
        overlay_fg = cv2.bitwise_and(overlay_bgr_resized, overlay_bgr_resized, mask=overlay_alpha_resized)
        overlay_bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(overlay_alpha_resized))

        # Blend the foreground and background, then overlay
        tent_image[top_y:top_y + overlay_bgr_resized.shape[0], 
                   top_left_x:top_left_x + overlay_bgr_resized.shape[1]] = cv2.add(overlay_bg, overlay_fg)

        return tent_image

    # If perspective is needed, set target points
    target_points = np.float32([
        [int(tent_image.shape[1] * top_left_x_factor), int(tent_image.shape[0] * top_left_y_factor)],  # Top-left
        [int(tent_image.shape[1] * top_right_x_factor), int(tent_image.shape[0] * top_right_y_factor)],  # Top-right
        [int(tent_image.shape[1] * bottom_left_x_factor), int(tent_image.shape[0] * bottom_left_y_factor)],  # Bottom-left
        [int(tent_image.shape[1] * bottom_right_x_factor), int(tent_image.shape[0] * bottom_right_y_factor)]  # Bottom-right
    ])

    # Apply perspective transformation and overlay
    return apply_perspective(overlay_bgr_resized, overlay_alpha_resized, tent_image, target_points)

def apply_color(tent_image, config, color):
    # Create a mask for the regions to be colored
    mask = np.zeros(tent_image.shape[:2], dtype=np.uint8)
    
    for key, points in config.items():
        cv2.fillPoly(mask, [np.array(points, np.int32)], 255)
            
    mask_expanded = cv2.merge([mask] * 3)
    color_overlay = np.full(tent_image.shape, color, dtype=np.uint8)

    # Directly apply the color to the masked regions without blending
    colored_image = tent_image.copy()
    colored_image[mask_expanded == 255] = color_overlay[mask_expanded == 255]
    
    return colored_image

def calculate_perspective_factors(center_x, center_y, logo_width, logo_height, image_width, image_height):
    """
    Calculate the four corner factors for a logo's perspective transformation based on its center.
    """
    # Calculate the absolute coordinates of each corner of the logo
    top_left_x = center_x - (logo_width / 2)
    top_left_y = center_y - (logo_height / 2)
    top_right_x = center_x + (logo_width / 2)
    top_right_y = center_y - (logo_height / 2)
    bottom_left_x = center_x - (logo_width / 2)
    bottom_left_y = center_y + (logo_height / 2)
    bottom_right_x = center_x + (logo_width / 2)
    bottom_right_y = center_y + (logo_height / 2)

    # Convert to factors relative to the image size
    return {
        "top_left_x_factor": top_left_x / image_width,
        "top_left_y_factor": top_left_y / image_height,
        "top_right_x_factor": top_right_x / image_width,
        "top_right_y_factor": top_right_y / image_height,
        "bottom_left_x_factor": bottom_left_x / image_width,
        "bottom_left_y_factor": bottom_left_y / image_height,
        "bottom_right_x_factor": bottom_right_x / image_width,
        "bottom_right_y_factor": bottom_right_y / image_height,
    }


# Main function to apply all logos with configurable parameters
def apply_all_logos(overlay_data: OverlayRequest, logo_content: bytes):
    output_images = []
    
    for tent_type, tent_path in TENT_MOCKUPS.items():
        
        relative_path = f"{Config.BASE_IMAGE_PATH}/{tent_path}"
        tent_image = cv2.imread(relative_path)
        logo_array = np.frombuffer(logo_content, np.uint8)
        logo_image = cv2.imdecode(logo_array, cv2.IMREAD_UNCHANGED)
        case_config = OVERLAY_CONFIGURATIONS.get(tent_type)
        
        masks = case_config.get("masks")
        if masks is not None:
            masks = extract_masks(tent_image, masks)
            
        if case_config.get("coordinates") is not None:
            color = DEFAULT_TENT_COLOR
            if overlay_data.color:
                color = overlay_data.color
            tent_image = apply_color(tent_image, case_config.get("coordinates"), color)
        
        logos = case_config.get("logos")  
        if logos is not None:
            for key, value in logos.items():
                if "text" in key:
                    rotation_angle = value.get("rotation_angle", DEFAULT_ROTATION_ANGLE)
                    text = DEFAULT_TEXT
                    if overlay_data.text:
                        text = overlay_data.text
                    text_img = create_text_image(text=text, font_size=100, rotation_angle=rotation_angle, font_color=overlay_data.font_color)
                    bgr = text_img[:, :, :3]
                    alpha = text_img[:, :, 3]
                    rotation_angle = 0
                else:
                    bgr = logo_image[:, :, :3]
                    alpha = logo_image[:, :, 3]
                    rotation_angle = value.get("rotation_angle", DEFAULT_ROTATION_ANGLE) 
                    
                width_scale = value.get('width_scale', 0.5)
                height_scale = value.get('height_scale', 0.5)
                
                # Place logo at the center of each slope for top view
                if tent_type == "top-view" and "text" not in key:
                    for slope, (center_x, center_y) in SLOPE_CENTERS.items():
                        # Convert center coordinates to factors based on image dimensions
                        if slope in key:
                            overlay_bgr_resized, overlay_alpha_resized = resize_logo(
                                logo_image[:, :, :3], logo_image[:, :, 3], width_scale, height_scale
                            )

                            # Get logo dimensions
                            logo_height, logo_width = overlay_bgr_resized.shape[:2]

                            # Calculate perspective factors based on the center coordinates and logo dimensions
                            factors = calculate_perspective_factors(
                                center_x, center_y, logo_width, logo_height,
                                tent_image.shape[1], tent_image.shape[0]
                            )

                            # Overlay the logo onto the tent image with perspective transformation
                            tent_image = apply_image_overlay(
                                tent_image, overlay_bgr=overlay_bgr_resized, overlay_alpha=overlay_alpha_resized,
                                width_scale=1, height_scale=1,  # Already scaled in resize_logo
                                top_left_x_factor=factors["top_left_x_factor"],
                                top_left_y_factor=factors["top_left_y_factor"],
                                top_right_x_factor=factors["top_right_x_factor"],
                                top_right_y_factor=factors["top_right_y_factor"],
                                bottom_left_x_factor=factors["bottom_left_x_factor"],
                                bottom_left_y_factor=factors["bottom_left_y_factor"],
                                bottom_right_x_factor=factors["bottom_right_x_factor"],
                                bottom_right_y_factor=factors["bottom_right_y_factor"],
                                perspective=True,
                                rotation_angle=rotation_angle
                            )
                else:
                    # Existing logic for other tent types
                    if "perspective" in value and "crop_type" in value:
                        tent_image = apply_image_overlay(
                            tent_image, overlay_bgr=bgr, overlay_alpha=alpha,
                            width_scale=width_scale,
                            height_scale=height_scale,
                            top_left_y_factor=value.get('top_left_y_factor'),
                            top_left_x_factor=value.get('top_left_x_factor'),
                            top_right_y_factor=value.get('top_right_y_factor'),
                            top_right_x_factor=value.get('top_right_x_factor'),
                            bottom_left_y_factor=value.get('bottom_left_y_factor'),
                            bottom_left_x_factor=value.get('bottom_left_x_factor'),
                            bottom_right_y_factor=value.get('bottom_right_y_factor'),
                            bottom_right_x_factor=value.get('bottom_right_x_factor'),
                            perspective=True,
                            crop_type=value.get("crop_type"),
                            rotation_angle=rotation_angle
                        )
                    elif "perspective" in value and "crop_type" not in value:
                        tent_image = apply_image_overlay(
                            tent_image, overlay_bgr=bgr, overlay_alpha=alpha,
                            width_scale=width_scale,
                            height_scale=height_scale,
                            top_left_y_factor=value.get('top_left_y_factor'),
                            top_left_x_factor=value.get('top_left_x_factor'),
                            top_right_y_factor=value.get('top_right_y_factor'),
                            top_right_x_factor=value.get('top_right_x_factor'),
                            bottom_left_y_factor=value.get('bottom_left_y_factor'),
                            bottom_left_x_factor=value.get('bottom_left_x_factor'),
                            bottom_right_y_factor=value.get('bottom_right_y_factor'),
                            bottom_right_x_factor=value.get('bottom_right_x_factor'),
                            perspective=True,
                            rotation_angle=rotation_angle
                        )
                    elif "perspective" not in value and "crop_type" in value:
                        tent_image = apply_image_overlay(
                            tent_image, overlay_bgr=bgr, overlay_alpha=alpha,
                            width_scale=width_scale,
                            height_scale=height_scale,
                            top_y_factor=value.get('top_y_factor'),
                            left_x_factor=value.get('left_x_factor'),
                            crop_type=value.get("crop_type"),
                            rotation_angle=rotation_angle
                        )
                    elif "perspective" not in value and "crop_type" not in value:
                        tent_image = apply_image_overlay(
                            tent_image, overlay_bgr=bgr, overlay_alpha=alpha,
                            width_scale=width_scale,
                            height_scale=height_scale,
                            top_y_factor=value.get('top_y_factor'),
                            left_x_factor=value.get('left_x_factor'),
                            rotation_angle=rotation_angle
                        )
        
        if masks is not None:
            tent_image = overlay_masks(tent_image, masks, case_config.get("masks"))
        
        is_success, buffer = cv2.imencode(".jpg", tent_image)
        if is_success:
            output_images.append((f"output_{tent_type}.jpg", buffer.tobytes()))
        
    return output_images
