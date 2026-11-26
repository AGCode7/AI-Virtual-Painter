import mediapipe as mp
import cv2
import math

hands_solutions = mp.solutions.hands
hands_detect = hands_solutions.Hands(
    model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.8
)
draw_solutions = mp.solutions.drawing_utils
font = cv2.FONT_HERSHEY_SIMPLEX

landmarks_hand = [0, 2, 3, 4, 7, 8, 12, 17]
landmarks_top = [8, 12, 16, 20]
landmarks_down = [6, 10, 14, 18]
circles_list = []
colors = [
    (100, 50, (0, 0, 255), "RED"),
    (200, 50, (0, 255, 0), "GREEN"),
    (300, 50, (255, 0, 0), "BLUE"),
    (400, 50, (0, 255, 255), "YELLOW"),
    (500, 50, (255, 0, 255), "PINK"),
]
color = (0, 0, 255)
distance = 5
color_name = "RED"

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error In Connect To WebCam")
    exit()
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error In Get Frame")
            break

        img = cv2.flip(frame, 1)
        result = hands_detect.process(img)
        height, width = img.shape[:2]

        if result.multi_hand_landmarks:
            hand_landmarks = result.multi_hand_landmarks[0]
            coordinate_list = []
            for i in landmarks_hand:
                cx = int(hand_landmarks.landmark[i].x * width)
                cy = int(hand_landmarks.landmark[i].y * height)
                coordinate_list.append([cx, cy])

            # محاسبه فواصل برای تشخیص حالت‌ها
            erase_list = []
            for i in range(4):
                landmarkTop_x = int(hand_landmarks.landmark[landmarks_top[i]].x * width)
                landmarkTop_y = int(
                    hand_landmarks.landmark[landmarks_top[i]].y * height
                )
                landmarkDown_x = int(
                    hand_landmarks.landmark[landmarks_down[i]].x * width
                )
                landmarkDown_y = int(
                    hand_landmarks.landmark[landmarks_down[i]].y * height
                )

                sqrt_landTop = math.sqrt(
                    (landmarkTop_x - coordinate_list[0][0]) ** 2
                    + (landmarkTop_y - coordinate_list[0][1]) ** 2
                )
                sqrt_landDown = math.sqrt(
                    (landmarkDown_x - coordinate_list[0][0]) ** 2
                    + (landmarkDown_y - coordinate_list[0][1]) ** 2
                )

                erase_list.append(sqrt_landTop - sqrt_landDown)

            sqrtLandmak_7_0 = math.sqrt(
                (coordinate_list[4][0] - coordinate_list[0][0]) ** 2
                + (coordinate_list[4][1] - coordinate_list[0][1]) ** 2
            )
            sqrtLandmak_12_0 = math.sqrt(
                (coordinate_list[6][0] - coordinate_list[0][0]) ** 2
                + (coordinate_list[6][1] - coordinate_list[0][1]) ** 2
            )
            sqrtLandmak_4_17 = math.sqrt(
                (coordinate_list[3][0] - coordinate_list[7][0]) ** 2
                + (coordinate_list[3][1] - coordinate_list[7][1]) ** 2
            )
            sqrtLandmak_2_17 = math.sqrt(
                (coordinate_list[1][0] - coordinate_list[7][0]) ** 2
                + (coordinate_list[1][1] - coordinate_list[7][1]) ** 2
            )
            sqrtLandmak_12_4 = math.sqrt(
                (coordinate_list[6][0] - coordinate_list[3][0]) ** 2
                + (coordinate_list[6][1] - coordinate_list[3][1]) ** 2
            )
            sqrtLandmak_4_3 = math.sqrt(
                (coordinate_list[3][0] - coordinate_list[2][0]) ** 2
                + (coordinate_list[3][1] - coordinate_list[2][1]) ** 2
            )

            draw_solutions.draw_landmarks(
                img, hand_landmarks, hands_solutions.HAND_CONNECTIONS
            )

            # رسم دکمه‌های انتخاب رنگ
            if sqrtLandmak_7_0 < sqrtLandmak_12_0:
                # رسم دکمه‌های رنگ

                for x, y, col, name in colors:
                    cv2.circle(img, (x, y), 23, col, cv2.FILLED)
                    # تشخیص کلیک روی دکمه‌ها با نوک انگشت اشاره
                    if (
                        x - 23 < coordinate_list[5][0] < x + 23
                        and y - 23 < coordinate_list[5][1] < y + 23
                    ):
                        color = col
                        color_name = name

            # تغییر اندازه قلم
            elif sqrtLandmak_4_17 > sqrtLandmak_2_17:
                distance = abs(
                    sqrtLandmak_4_17 - sqrtLandmak_2_17
                )  # استفاده از abs برای جلوگیری از منفی شدن
                distance = max(1, int(distance / 2))  # حداقل شعاع 1

            # رسم نقطه
            else:
                # محدود کردن لیست برای جلوگیری از رشد بیش از حد
                if len(circles_list) > 1000:
                    circles_list = circles_list[-500:]
                circles_list.append(
                    [coordinate_list[5][0], coordinate_list[5][1], distance, color]
                )

            # پاک کردن صفحه با حرکت خاص (مثلاً بستن تمام انگشتان)
            if all(i < -10 for i in erase_list):  # آستانه دقیق‌تر
                circles_list = []

        # رسم تمام نقاط
        for i in circles_list:
            cv2.circle(img, (i[0], i[1]), i[2], i[3], cv2.FILLED)

        # نمایش اطلاعات
        cv2.putText(img, f"Size: {str(distance)}", (20, 120), font, 1, (0, 255, 0), 4)
        cv2.putText(img, f"Color : {color_name}", (20, 160), font, 1, color, 4)
        cv2.putText(img, "Press 'c' to clear", (20, 200), font, 0.7, (255, 255, 255), 2)
        cv2.putText(img, "Press 'q' to quit", (20, 230), font, 0.7, (255, 255, 255), 2)

        cv2.imshow("WedCam", img)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("c"):
            circles_list = []
finally:
    # آزادسازی منابع
    cap.release()
    cv2.destroyAllWindows()
