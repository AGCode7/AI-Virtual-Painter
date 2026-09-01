import mediapipe as mp
import cv2
import math

hand = mp.solutions.hands
Hand_D = hand.Hands(
    model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.8
)
draw = mp.solutions.drawing_utils
font = cv2.FONT_HERSHEY_SIMPLEX

list_land = [0, 2, 3, 4, 7, 8, 12, 17]
list_T = [8, 12, 16, 20]
list_D = [6, 10, 14, 18]
list_circle = []

color = (0, 0, 255)
distance = 5
name_c = "RED"

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error In Connect To WebCam")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error In Get Frame")
        break

    img = cv2.flip(frame, 1)
    result = Hand_D.process(img)
    h, w = img.shape[:2]

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        ln = []
        for i in list_land:
            cx = int(hand_landmarks.landmark[i].x * w)
            cy = int(hand_landmarks.landmark[i].y * h)
            ln.append([cx, cy])

        # محاسبه فواصل برای تشخیص حالت‌ها
        list_erase = []
        for i in range(4):
            landT_x = int(hand_landmarks.landmark[list_T[i]].x * w)
            landT_y = int(hand_landmarks.landmark[list_T[i]].y * h)
            landD_x = int(hand_landmarks.landmark[list_D[i]].x * w)
            landD_y = int(hand_landmarks.landmark[list_D[i]].y * h)

            sqrt_landT = math.sqrt(
                (landT_x - ln[0][0]) ** 2 + (landT_y - ln[0][1]) ** 2
            )
            sqrt_landD = math.sqrt(
                (landD_x - ln[0][0]) ** 2 + (landD_y - ln[0][1]) ** 2
            )

            list_erase.append(sqrt_landT - sqrt_landD)

        sqrt_7_0 = math.sqrt((ln[4][0] - ln[0][0]) ** 2 + (ln[4][1] - ln[0][1]) ** 2)
        sqrt_12_0 = math.sqrt((ln[6][0] - ln[0][0]) ** 2 + (ln[6][1] - ln[0][1]) ** 2)
        sqrt_4_17 = math.sqrt((ln[3][0] - ln[7][0]) ** 2 + (ln[3][1] - ln[7][1]) ** 2)
        sqrt_2_17 = math.sqrt((ln[1][0] - ln[7][0]) ** 2 + (ln[1][1] - ln[7][1]) ** 2)
        sqrt_12_4 = math.sqrt((ln[6][0] - ln[3][0]) ** 2 + (ln[6][1] - ln[3][1]) ** 2)
        sqrt_4_3 = math.sqrt((ln[3][0] - ln[2][0]) ** 2 + (ln[3][1] - ln[2][1]) ** 2)

        draw.draw_landmarks(img, hand_landmarks, hand.HAND_CONNECTIONS)

        # رسم دکمه‌های انتخاب رنگ
        if sqrt_7_0 < sqrt_12_0:
            # رسم دکمه‌های رنگ
            colors = [
                (100, 50, (0, 0, 255), "RED"),
                (200, 50, (0, 255, 0), "GREEN"),
                (300, 50, (255, 0, 0), "BLUE"),
                (400, 50, (0, 255, 255), "YELLOW"),
                (500, 50, (255, 0, 255), "PINK"),
            ]

            for x, y, col, name in colors:
                cv2.circle(img, (x, y), 23, col, cv2.FILLED)
                # تشخیص کلیک روی دکمه‌ها با نوک انگشت اشاره
                if x - 23 < ln[5][0] < x + 23 and y - 23 < ln[5][1] < y + 23:
                    color = col
                    name_c = name

        # تغییر اندازه قلم
        elif sqrt_4_17 > sqrt_2_17:
            distance = abs(
                sqrt_4_17 - sqrt_2_17
            )  # استفاده از abs برای جلوگیری از منفی شدن
            distance = max(1, int(distance / 2))  # حداقل شعاع 1

        # رسم نقطه
        else:
            # محدود کردن لیست برای جلوگیری از رشد بیش از حد
            if len(list_circle) > 1000:
                list_circle = list_circle[-500:]
            list_circle.append([ln[5][0], ln[5][1], distance, color])

        # پاک کردن صفحه با حرکت خاص (مثلاً بستن تمام انگشتان)
        if all(i < -10 for i in list_erase):  # آستانه دقیق‌تر
            list_circle = []

    # رسم تمام نقاط
    for i in list_circle:
        cv2.circle(img, (i[0], i[1]), i[2], i[3], cv2.FILLED)

    # نمایش اطلاعات
    cv2.putText(img, f"Size: {str(distance)}", (20, 120), font, 1, (0, 255, 0), 4)
    cv2.putText(img, f"Color : {name_c}", (20, 160), font, 1, color, 4)
    cv2.putText(img, "Press 'c' to clear", (20, 200), font, 0.7, (255, 255, 255), 2)
    cv2.putText(img, "Press 'q' to quit", (20, 230), font, 0.7, (255, 255, 255), 2)

    cv2.imshow("WedCam", img)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("c"):
        list_circle = []

# آزادسازی منابع
cap.release()
cv2.destroyAllWindows()
