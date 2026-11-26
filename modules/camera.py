import cv2


class Camera:
    def __init__(self, index: int = 0):
        self.index = index
        self.cap = cv2.VideoCapture(index)
        if not self.cap.isOpened():
            raise RuntimeError("Error In Get Frame From Webcam.")

    def read(self):
        """خواندن یک فریم و برگرداندن آن به صورت آینه‌ای (flip)."""
        ret, frame = self.cap.read()
        if not ret:
            return None
        return cv2.flip(frame, 1)

    def release(self):
        self.cap.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
