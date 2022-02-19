import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
from cv2 import QT_FONT_NORMAL
import numpy as np
import time
import PoseModule as pm
#Enter pushup/squats/curls to change video
cap = cv2.VideoCapture('squats.mp4')
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        #Comment and uncomment below based on the funcionality you don't want or want to use.
        # #Right Arm
        # angle = detector.findAngle(img, 12, 14, 16)
        # # Left Arm
        # angle = detector.findAngle(img, 11, 13, 15)
        # # Curls And PushUps
        # per = np.interp(angle, (210, 280), (0, 100))
        # bar = np.interp(angle, (210, 280), (650, 100))
        #Squats
         #Right Leg
        angle = detector.findAngle(img, 24,26,28)
        #Left Leg
        angle = detector.findAngle(img, 23,25,27)
        per = np.interp(angle, (185, 210), (0, 100))
        bar = np.interp(angle, (185, 210), (650, 100))
        # Counting algorithm
        color = (0, 0, 255)
        if per == 100:
            color = (255, 255, 255)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (255, 255, 255)
            if dir == 1:
                count += 0.5
                dir = 0
        #print(count)
        # Draw Bar
        cv2.rectangle(img, (1190, 100), (1240, 650), color, 2)
        cv2.rectangle(img, (1190, int(bar)), (1240, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (1190, 75), cv2.QT_FONT_NORMAL, 1,
                    color, 2)
        # Draw Curl Count
        cv2.rectangle(img, (0, 510), (200, 720), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, str(int(count)), (10, 670), cv2.QT_FONT_BLACK, 4,
                    (0, 0, 0), 7)
        cv2.putText(img, 'Reps', (50,555), cv2.QT_FONT_NORMAL, 1, (0,0,255), 2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (5,50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                (0, 255, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
