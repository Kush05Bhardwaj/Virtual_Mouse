import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np

class HandTracker:
    def __init__(self, maxHands=1, detectionCon=0.7, trackCon=0.7):
        # Download the hand landmarker model
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=maxHands,
            min_hand_detection_confidence=detectionCon,
            min_hand_presence_confidence=trackCon,
            min_tracking_confidence=trackCon,
            running_mode=vision.RunningMode.VIDEO
        )
        self.landmarker = vision.HandLandmarker.create_from_options(options)
        self.results = None
        self.timestamp = 0

    def findHands(self, img, draw=True):
        # Convert BGR to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Create MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
        
        # Process the image
        self.timestamp += 1
        self.results = self.landmarker.detect_for_video(mp_image, self.timestamp)
        
        # Draw landmarks if requested
        if draw and self.results.hand_landmarks:
            h, w, _ = img.shape
            for hand_landmarks in self.results.hand_landmarks:
                # Draw landmarks
                for landmark in hand_landmarks:
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                
                # Draw connections
                connections = [
                    (0, 1), (1, 2), (2, 3), (3, 4),  # Thumb
                    (0, 5), (5, 6), (6, 7), (7, 8),  # Index
                    (0, 9), (9, 10), (10, 11), (11, 12),  # Middle
                    (0, 13), (13, 14), (14, 15), (15, 16),  # Ring
                    (0, 17), (17, 18), (18, 19), (19, 20),  # Pinky
                    (5, 9), (9, 13), (13, 17)  # Palm
                ]
                for connection in connections:
                    x1, y1 = int(hand_landmarks[connection[0]].x * w), int(hand_landmarks[connection[0]].y * h)
                    x2, y2 = int(hand_landmarks[connection[1]].x * w), int(hand_landmarks[connection[1]].y * h)
                    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        
        return img

    def findPosition(self, img):
        lmList = []
        if self.results and self.results.hand_landmarks:
            hand = self.results.hand_landmarks[0]
            h, w, _ = img.shape
            for id, lm in enumerate(hand):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
        return lmList
