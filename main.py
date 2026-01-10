import cv2
import numpy as np
import pyautogui
from hand_tracker import HandTracker
from utils import fingers_up

wCam, hCam = 640, 480
frameR = 100
smoothening = 7

plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

tracker = HandTracker()
wScr, hScr = pyautogui.size()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = tracker.findHands(img)
    lmList = tracker.findPosition(img)

    if lmList:
        fingers = fingers_up(lmList)
        x1, y1 = lmList[8][1], lmList[8][2]

        # 🖱️ Move Mouse (Index Finger)
        if fingers == [0,1,0,0,0]:
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            pyautogui.moveTo(clocX, clocY)
            plocX, plocY = clocX, clocY

        # 👆 Left Click
        if fingers[1] and fingers[0]:
            pyautogui.click()

        # 👉 Right Click
        if fingers[2] and fingers[0]:
            pyautogui.rightClick()

        # ✌️ Scroll
        if fingers[1] and fingers[2]:
            pyautogui.scroll(40)

        # ❌ Exit (Fist)
        if fingers == [0,0,0,0,0]:
            break

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
