import cv2
import time
import numpy as np
import HandsTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import imutils

# Navigate to google.github.io/mediapipe/hands to get all hands numbers correspondingly
# Basically we need two for this to work

# Settings Parameters
wCam, hCam = 320, 240 # or 640, 480

# Checking WebCam
# cap = cv2.VideoCapture(0) # For webcam
# For video from file

cap = cv2.VideoCapture('test.mp4')

cap.set(3, 1280)
cap.set(4, 720)
pTime = 0

# Creating hand detector to detect hands from HTM Module
detector = htm.handDetector(detectionCon=0.7)

# Setting Audio
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.GetMute()
# volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()       # -65 to 0
minimum = volumeRange[0]
maximum = volumeRange[1]
vol = 0
volBar = 40
volPerc = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img) # Find hands in img being given and returning it back
    img = imutils.resize(img, width=320)
    LmList = detector.findPosition(img, draw=False) # Returning positions list of hands to use
    if len(LmList) != 0:
        # print(LmList[4], LmList[8])

        # Retrieving two fingers coordinates
        x1, y1 = LmList[4][1], LmList[4][2]
        x2, y2 = LmList[8][1], LmList[8][2]
        centerx, centery = (x1 + x2) // 2, (y1 + y2) // 2
        # Drawing on the thumb and the index
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (centerx, centery), 7, (255, 0, 0), cv2.FILLED)

        # Next we need to find the length of the line and change the volume with that
        length = math.hypot(x2-x1, y2-y1)
        print(length)   # we got a minimum=50 and max=300 which need normalization

        # Converting Ranges proportionally
        vol = np.interp(length, [50, 250], [minimum, maximum])
        volBar = np.interp(length, [50, 250], [400, 150])
        volPerc = np.interp(length, [50, 250], [0, 100])
        volume.SetMasterVolumeLevel(vol, None) # Setting volume

        if length < 50:
            cv2.circle(img, (centerx, centery), 7, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPerc)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # cv2.putText(img, f'Fps: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)