import cv2
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

xp, yp = 0, 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            if abs(y2 - y1) > 40:
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                cv2.line(canvas, (xp, yp), (x1, y1), (255, 0, 255), 8)
                xp, yp = x1, y1
            else:
                xp, yp = 0, 0

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas)

    cv2.imshow("AI Air Canvas", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('c'):
        canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

cap.release()
cv2.destroyAllWindows()
