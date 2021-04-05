import cv2
import mediapipe as mp
import time  # Frames

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()  # Keep empty to use defaults
mpDraw = mp.solutions.drawing_utils  # Drawing function

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    # Converting object to RGB to send to hands
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Processing the converted img
    results = hands.process(imgRGB)

    # print(results.multi_hand_landmarks)

    # Checking for multiHands
    if results.multi_hand_landmarks:
        # Extracting information of each hand
        for handsLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handsLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)

                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                # Drawing on the original image on a single hand in the loop
                mpDraw.draw_landmarks(img, handsLms, mpHands.HAND_CONNECTIONS)

    # Calculating Frames
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

