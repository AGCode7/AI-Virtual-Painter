import math
import mediapipe as mp

from modules.config import (
    HANDS_MODEL_COMPLEXITY,
    MIN_DETECTION_CONFIDENCE,
    MIN_TRACKING_CONFIDENCE,
    LANDMARKS_HAND,
    LANDMARKS_TOP,
    LANDMARKS_DOWN,
    IDX_WRIST,
    IDX_INDEX_MCP,
    IDX_THUMB_TIP,
    IDX_INDEX_DIP,
    IDX_MIDDLE_MCP,
    IDX_PINKY_MCP,
)


def _distance(p1, p2) -> float:
    """فاصله اقلیدسی بین دو نقطه"""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            model_complexity=HANDS_MODEL_COMPLEXITY,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
        )

    def process(self, img):
        """پردازش تصویر و برگرداندن نتیجه MediaPipe."""
        return self.hands.process(img)

    @staticmethod
    def get_coordinates(hand_landmarks, width: int, height: int):
        """استخراج مختصات پیکسلی نقاط کلیدی انتخاب‌شده."""
        coords = []
        for idx in LANDMARKS_HAND:
            lm = hand_landmarks.landmark[idx]
            coords.append([int(lm.x * width), int(lm.y * height)])
        return coords

    @staticmethod
    def compute_finger_extension(hand_landmarks, coords, width: int, height: int):
        """محاسبه اختلاف فاصله نوک و مفصل هر انگشت از مچ (برای تشخیص حالت)."""
        wrist = coords[IDX_WRIST]
        result = []
        for top_idx, down_idx in zip(LANDMARKS_TOP, LANDMARKS_DOWN):
            top = hand_landmarks.landmark[top_idx]
            down = hand_landmarks.landmark[down_idx]
            top_xy = (int(top.x * width), int(top.y * height))
            down_xy = (int(down.x * width), int(down.y * height))
            result.append(_distance(top_xy, wrist) - _distance(down_xy, wrist))
        return result

    @staticmethod
    def compute_features(coords):
        """محاسبه فواصل کلیدی برای تشخیص حالت‌های برنامه."""
        return {
            "index_extended": _distance(coords[IDX_INDEX_DIP], coords[IDX_WRIST])
            < _distance(coords[IDX_MIDDLE_MCP], coords[IDX_WRIST]),
            "thumb_pinky": _distance(coords[IDX_THUMB_TIP], coords[IDX_PINKY_MCP]),
            "index_pinky": _distance(coords[IDX_INDEX_MCP], coords[IDX_PINKY_MCP]),
        }

    def draw(self, img, hand_landmarks):
        """رسم نقاط و اتصالات دست روی تصویر."""
        self.mp_draw.draw_landmarks(
            img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

    def close(self):
        self.hands.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
