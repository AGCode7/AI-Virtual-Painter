import cv2

FONT = cv2.FONT_HERSHEY_SIMPLEX


def draw_ui(img, brush_size: int, color_name: str, color):
    """رسم اطلاعات وضعیت و راهنماها روی تصویر."""
    cv2.putText(img, f"Size: {brush_size}", (20, 120), FONT, 1, (0, 255, 0), 4)
    cv2.putText(img, f"Color: {color_name}", (20, 160), FONT, 1, color, 4)
    cv2.putText(img, "Press 'c' to clear", (20, 200),
                FONT, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "Press 'q' to quit", (20, 230),
                FONT, 0.7, (255, 255, 255), 2)
