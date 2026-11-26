import math
import cv2
from modules.config import (
    COLORS,
    DEFAULT_COLOR,
    DEFAULT_COLOR_NAME,
    DEFAULT_BRUSH_SIZE,
    MAX_CIRCLES,
    TRIM_TO,
    MIN_BRUSH_SIZE,
    BUTTON_RADIUS,
)


class DrawingCanvas:
    def __init__(self):
        self.circles: list[list] = []
        self.color = DEFAULT_COLOR
        self.color_name = DEFAULT_COLOR_NAME
        self.brush_size = DEFAULT_BRUSH_SIZE

    # ---------- مدیریت نقاط ----------
    def add_point(self, x: int, y: int):
        """افزودن یک نقطه به canvas با محدود کردن اندازه لیست."""
        if len(self.circles) > MAX_CIRCLES:
            self.circles = self.circles[-TRIM_TO:]
        self.circles.append([x, y, self.brush_size, self.color])

    def clear(self):
        self.circles.clear()

    def render(self, img):
        """رسم همه نقاط روی تصویر."""
        for x, y, radius, color in self.circles:
            cv2.circle(img, (x, y), radius, color, cv2.FILLED)

    # ---------- انتخاب رنگ ----------
    def draw_color_buttons(self, img):
        """رسم دکمه‌های رنگ روی تصویر."""
        for x, y, col, _name in COLORS:
            cv2.circle(img, (x, y), BUTTON_RADIUS, col, cv2.FILLED)

    def handle_color_selection(self, finger_x: int, finger_y: int):
        """بررسی کلیک روی دکمه‌های رنگ با نوک انگشت اشاره."""
        for x, y, col, name in COLORS:
            if (
                x - BUTTON_RADIUS < finger_x < x + BUTTON_RADIUS
                and y - BUTTON_RADIUS < finger_y < y + BUTTON_RADIUS
            ):
                self.color = col
                self.color_name = name
                return True
        return False

    # ---------- اندازه قلم ----------
    def update_brush_size(self, thumb_pinky_dist: float, index_pinky_dist: float):
        """به‌روزرسانی اندازه قلم بر اساس فاصله انگشت شست و اشاره."""
        diff = abs(thumb_pinky_dist - index_pinky_dist)
        self.brush_size = max(MIN_BRUSH_SIZE, int(diff / 2))
