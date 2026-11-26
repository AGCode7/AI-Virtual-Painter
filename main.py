import cv2
from modules.config import (
    ERASE_THRESHOLD,
    IDX_INDEX_DIP,
    IDX_INDEX_TIP,
    IDX_WRIST,
    IDX_INDEX_MCP,
)
from modules.camera import Camera
from modules.drawing import DrawingCanvas
from modules.hand_detector import HandDetector
from modules.ui import draw_ui


def main():
    with Camera() as camera, HandDetector() as detector:
        canvas = DrawingCanvas()

        while True:
            img = camera.read()
            if img is None:
                print("Error In Get Frame From Webcam.")
                break

            result = detector.process(img)
            height, width = img.shape[:2]

            if result.multi_hand_landmarks:
                hand_landmarks = result.multi_hand_landmarks[0]
                coords = detector.get_coordinates(
                    hand_landmarks, width, height)
                detector.draw(img, hand_landmarks)

                finger_extension = detector.compute_finger_extension(
                    hand_landmarks, coords, width, height
                )
                features = detector.compute_features(coords)
                finger_x, finger_y = coords[IDX_INDEX_DIP]

                index_tip_y = coords[IDX_INDEX_TIP][1]
                wrist_y = coords[IDX_WRIST][1]
                middle_mcp_y = coords[IDX_INDEX_MCP][1]

                # --- حالت انتخاب رنگ ---
                if features["index_extended"]:
                    canvas.draw_color_buttons(img)
                    canvas.handle_color_selection(finger_x, finger_y)

                # --- حالت تغییر اندازه قلم ---
                elif features["thumb_pinky"] > features["index_pinky"]:
                    canvas.update_brush_size(
                        features["thumb_pinky"], features["index_pinky"]
                    )

                # --- حالت رسم ---
                else:
                    canvas.add_point(finger_x, finger_y)

                # --- پاک کردن با حالت مشت ---
                if all(v < ERASE_THRESHOLD for v in finger_extension):
                    canvas.clear()

            canvas.render(img)
            draw_ui(img, canvas.brush_size, canvas.color_name, canvas.color)

            cv2.imshow("WebCam", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            elif key == ord("c"):
                canvas.clear()


if __name__ == "__main__":
    main()
