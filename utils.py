def fingers_up(lmList):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    fingers.append(lmList[4][1] > lmList[3][1])  # Thumb
    for tip in tips[1:]:
        fingers.append(lmList[tip][2] < lmList[tip - 2][2])

    return fingers
