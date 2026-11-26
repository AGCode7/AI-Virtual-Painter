"""تنظیمات و مقادیر ثابت برنامه."""

# --- MediaPipe ---
HANDS_MODEL_COMPLEXITY = 1
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.8

# --- نقاط کلیدی دست ---
LANDMARKS_HAND = [0, 2, 3, 4, 7, 8, 12, 17]
LANDMARKS_TOP = [8, 12, 16, 20]
LANDMARKS_DOWN = [6, 10, 14, 18]

# --- ایندکس نقاط در لیست مختصات ---
IDX_WRIST = 0
IDX_INDEX_MCP = 1
IDX_INDEX_PIP = 2
IDX_THUMB_TIP = 3
IDX_INDEX_TIP = 4
IDX_INDEX_DIP = 5
IDX_MIDDLE_MCP = 6
IDX_PINKY_MCP = 7

# --- رنگ‌ها: (x, y, BGR, name) ---
COLORS = [
    (100, 50, (0, 0, 255), "RED"),
    (200, 50, (0, 255, 0), "GREEN"),
    (300, 50, (255, 0, 0), "BLUE"),
    (400, 50, (0, 255, 255), "YELLOW"),
    (500, 50, (255, 0, 255), "PINK"),
]

DEFAULT_COLOR = (0, 0, 255)
DEFAULT_COLOR_NAME = "RED"
DEFAULT_BRUSH_SIZE = 5

# --- تنظیمات Canvas ---
MAX_CIRCLES = 1000
TRIM_TO = 500
MIN_BRUSH_SIZE = 1

# --- آستانه‌ها ---
ERASE_THRESHOLD = -10
BUTTON_RADIUS = 23
