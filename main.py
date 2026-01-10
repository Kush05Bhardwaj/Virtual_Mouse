import cv2
import numpy as np
import pyautogui
from hand_tracker import HandTracker
from utils import fingers_up
import sys

# Configuration
HEADLESS_MODE = True  # Set to True to run without showing the window (WORKS WHEN MINIMIZED!)
DEBUG_MODE = False  # Show finger detection status (only works with window)

# Camera settings
wCam, hCam = 640, 480
frameR = 100  # Frame reduction (border)

# Smoothing settings - higher = smoother but slower response
smoothening = 5  # Reduced for faster response (was 7)

# Previous and current locations
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# Click debouncing
click_cooldown = 0
right_click_cooldown = 0
fist_counter = 0  # Count frames with fist to avoid accidental exit

# PyAutoGUI settings for smoother movement
pyautogui.FAILSAFE = False  # Disable failsafe for smoother movement
pyautogui.PAUSE = 0  # Remove delay between PyAutoGUI calls

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cap.set(cv2.CAP_PROP_FPS, 30)  # Set FPS for smoother capture

tracker = HandTracker(detectionCon=0.8, trackCon=0.8)  # Higher confidence for stability
wScr, hScr = pyautogui.size()

# Create window only if not in headless mode
if not HEADLESS_MODE:
    cv2.namedWindow("Virtual Mouse", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Virtual Mouse", 640, 480)
    print("Virtual Mouse Started! Press ESC or Q to exit.")
else:
    print("Virtual Mouse Started in HEADLESS mode! Close terminal or make a fist to exit.")

print("Controls:")
print("  ☝️  Index finger only - Move cursor")
print("  👆 Thumb + Index - Left click")
print("  👉 Thumb + Middle - Right click")
print("  ✌️  Index + Middle - Scroll")
print("  ✊ Fist - Exit")

while True:
    success, img = cap.read()
    if not success:
        continue
        
    img = cv2.flip(img, 1)

    img = tracker.findHands(img)
    lmList = tracker.findPosition(img)

    # Draw boundary rectangle
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

    if lmList:
        fingers = fingers_up(lmList)
        x1, y1 = lmList[8][1], lmList[8][2]  # Index finger tip

        # Debug: Show finger status in console if headless
        if DEBUG_MODE and HEADLESS_MODE:
            print(f"Fingers: {fingers}", end='\r')

        # Debug: Show finger status on screen if window visible
        if DEBUG_MODE and not HEADLESS_MODE:
            finger_status = f"Fingers: {fingers}"
            cv2.putText(img, finger_status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

        # 🖱️ Move Mouse (Index Finger only - thumb must be down!)
        if fingers[1] == 1 and fingers[0] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            # Convert coordinates with boundary checking
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Exponential smoothing for better control
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move mouse with duration=0 for instant movement (no flip needed - already flipped in image)
            pyautogui.moveTo(clocX, clocY, duration=0)
            
            if not HEADLESS_MODE:
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                cv2.putText(img, "MOVING", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            
            plocX, plocY = clocX, clocY
            fist_counter = 0  # Reset fist counter when moving

        # 👆 Left Click (with debouncing)
        if fingers[1] and fingers[0] and click_cooldown == 0:
            pyautogui.click()
            click_cooldown = 10  # Cooldown frames
            if not HEADLESS_MODE:
                cv2.putText(img, "LEFT CLICK", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            fist_counter = 0  # Reset fist counter

        # 👉 Right Click (with debouncing)
        if fingers[2] and fingers[0] and not fingers[1] and right_click_cooldown == 0:
            pyautogui.rightClick()
            right_click_cooldown = 10  # Cooldown frames
            if not HEADLESS_MODE:
                cv2.putText(img, "RIGHT CLICK", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            fist_counter = 0  # Reset fist counter

        # ✌️ Scroll
        if fingers[1] and fingers[2] and not fingers[0]:
            pyautogui.scroll(40)
            if not HEADLESS_MODE:
                cv2.putText(img, "SCROLL", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            fist_counter = 0  # Reset fist counter

        # ❌ Exit (Fist) - must hold for 30 frames to avoid accidental exit (about 1 second)
        if fingers == [0,0,0,0,0]:
            fist_counter += 1
            if not HEADLESS_MODE:
                cv2.putText(img, f"EXITING... {fist_counter}/30", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                if fist_counter % 5 == 0:  # Print every 5 frames
                    print(f"\rHold FIST to exit: {fist_counter}/30", end='', flush=True)
            if fist_counter >= 30:
                print("\nExiting...")
                break
        else:
            fist_counter = 0  # Reset if not a fist
    else:
        # No hand detected - reset fist counter to prevent accidental exit
        fist_counter = 0

    # Decrease cooldown
    if click_cooldown > 0:
        click_cooldown -= 1
    if right_click_cooldown > 0:
        right_click_cooldown -= 1

    # Show mode indicator
    cv2.putText(img, "Virtual Mouse Active", (10, hCam - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Display the frame only if not in headless mode
    if not HEADLESS_MODE:
        cv2.imshow("Virtual Mouse", img)
        
        # Non-blocking key check - works even when minimized
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC to exit
            break
        elif key == ord('q'):  # Q to exit
            break
    else:
        # In headless mode, just add a small delay to prevent CPU overload
        cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
print("\nVirtual Mouse stopped. Goodbye!")
