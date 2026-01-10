def fingers_up(lmList):
    """
    Detect which fingers are up
    Returns: [thumb, index, middle, ring, pinky]
    1 = finger up, 0 = finger down
    """
    tips = [4, 8, 12, 16, 20]  # Tip landmarks for each finger
    fingers = []

    # Thumb - check horizontal distance (x-axis) instead of vertical
    # Thumb is up if tip is to the right of the knuckle (for right hand)
    if lmList[tips[0]][1] < lmList[tips[0] - 1][1]:  # Comparing x coordinates
        fingers.append(1)
    else:
        fingers.append(0)
    
    # Other fingers - check if tip is above the middle joint (lower y = higher on screen)
    for tip in tips[1:]:
        if lmList[tip][2] < lmList[tip - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers
