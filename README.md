# 🖱️ Virtual Mouse - Hand Gesture Control

Control your computer mouse using hand gestures! This project uses MediaPipe for hand tracking and PyAutoGUI for mouse control, allowing you to interact with your computer hands-free.

## ✨ Features

- **Headless Mode**: Run in background without any window (no minimize issues!)
- **Mouse Movement**: Control cursor with your index finger only
- **Left Click**: Thumb + Index finger gesture
- **Right Click**: Thumb + Middle finger gesture  
- **Scroll**: Index + Middle fingers (no thumb)
- **Smart Exit**: Hold fist for 1 second to exit (prevents accidental exits)
- **Smooth Movement**: Exponential smoothing with configurable sensitivity
- **Click Debouncing**: Prevents accidental multiple clicks

## 🎮 Hand Gesture Controls

| Gesture | Fingers Extended | Action |
|---------|-----------------|--------|
| ☝️ Index only | `[0,1,0,0,0]` | Move mouse cursor |
| 👆 Thumb + Index | `[1,1,0,0,0]` | Left click |
| 👉 Thumb + Middle | `[1,0,1,0,0]` | Right click |
| ✌️ Index + Middle | `[0,1,1,0,0]` | Scroll down |
| ✊ Fist (hold 1 sec) | `[0,0,0,0,0]` | Exit application |

**Note:** For mouse movement, ONLY the index finger should be up - all other fingers must be down for precise control.

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Webcam
- Windows/Linux/macOS

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd "Virtual Mouse"
```

2. **Create a virtual environment**
```bash
python -m venv .venv
```

3. **Activate the virtual environment**

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Download the hand tracking model**

The model file `hand_landmarker.task` should be downloaded automatically. If not, download it manually:
```powershell
Invoke-WebRequest -Uri "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task" -OutFile "hand_landmarker.task"
```

## 🎯 Usage

### Running in Headless Mode (Recommended)

**Default mode - runs in background without any window:**

1. **Activate your virtual environment**
```powershell
.\.venv\Scripts\Activate.ps1
```

2. **Run the application**
```bash
python main.py
```

The application will start with:
- ✅ No window to minimize or manage
- ✅ Works completely in background
- ✅ Natural cursor movement (move right → cursor goes right)
- ✅ Smooth tracking with exponential smoothing

3. **Use hand gestures** in front of your webcam:
   - Point with **index finger only** to move cursor (keep thumb DOWN!)
   - Extend **thumb + index** to left click
   - Extend **thumb + middle** to right-click
   - Extend **index + middle** (no thumb) to scroll
   - Make a **fist and hold for 1 second** to exit

4. **Exit** by holding a fist for 1 second or press **Ctrl+C** in terminal

### Running with Visual Feedback (Optional)

If you want to see the camera feed and hand tracking:

1. Edit `main.py` line 8:
```python
HEADLESS_MODE = False  # Change from True to False
```

2. Run the application - a window will show the camera feed with:
   - Hand landmarks visualization
   - Active gesture indicators
   - Boundary rectangle for tracking area

3. **Exit** with ESC, Q, or fist gesture

## 📁 Project Structure

```
Virtual Mouse/
├── main.py                  # Main application entry point
├── hand_tracker.py          # Hand tracking implementation using MediaPipe
├── utils.py                 # Helper functions (finger counting)
├── hand_landmarker.task     # MediaPipe hand tracking model
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
└── .gitignore             # Git ignore rules
```

## 🛠️ Technical Details

### Dependencies
- **OpenCV** (`opencv-python==4.10.0.84`): Camera capture and image processing
- **MediaPipe** (`mediapipe==0.10.31`): Hand landmark detection using tasks API
- **PyAutoGUI** (`pyautogui==0.9.54`): Mouse control automation
- **NumPy** (`numpy==1.26.4`): Numerical computations
- **PyScreeze** (`pyscreeze==0.1.30`): Screenshot functionality (pinned for compatibility)

### How It Works

1. **Camera Capture**: Captures 30 FPS video from webcam using OpenCV
2. **Hand Detection**: MediaPipe detects hand landmarks (21 key points) using new tasks API
3. **Gesture Recognition**: Analyzes finger positions to identify gestures
4. **Coordinate Mapping**: Maps camera coordinates to screen coordinates with boundary checking
5. **Smoothing**: Applies exponential smoothing for fluid cursor movement
6. **Mouse Control**: Translates gestures to mouse actions via PyAutoGUI with zero delay

### Configuration

**In `main.py`:**

```python
# Modes
HEADLESS_MODE = True    # True = no window (works in background)
DEBUG_MODE = False      # True = show finger detection status

# Camera
wCam, hCam = 640, 480   # Camera resolution
frameR = 100            # Frame reduction (boundary margin in pixels)

# Movement
smoothening = 5         # Mouse smoothness (3-7: lower = faster, higher = smoother)

# Debouncing
click_cooldown = 10     # Frames between clicks (prevent double-click)
fist_counter = 30       # Frames to hold fist for exit (~1 second)
```

**In `hand_tracker.py`:**
```python
detectionCon=0.8        # Detection confidence threshold (0.0-1.0)
trackCon=0.8           # Tracking confidence threshold (0.0-1.0)
maxHands=1             # Maximum hands to detect
```

### API Changes

This project uses **MediaPipe 0.10.31** with the new **tasks API**. Key differences from older versions:
- ✅ Uses `mediapipe.tasks.python.vision` instead of `mediapipe.solutions`
- ✅ Custom drawing with OpenCV instead of MediaPipe drawing utilities
- ✅ `HandLandmarker` instead of deprecated `Hands` class
- ✅ Video mode for continuous frame processing

## 🐛 Troubleshooting

### Mouse movement is inverted/reversed
✅ **Fixed!** The latest version has correct movement mapping.
- Move hand right → cursor moves right
- Move hand left → cursor moves left

### Can't move mouse with index finger
- Make sure **ONLY the index finger is up**
- Keep thumb, middle, ring, and pinky fingers **DOWN**
- Try adjusting detection confidence in `hand_tracker.py`

### Program exits immediately / unexpectedly
✅ **Fixed!** Updated to require holding fist for 1 full second.
- Fist counter resets when performing other gestures
- Won't exit if no hand is detected
- Only exits after 30 consecutive frames (~1 second) of fist

### Window minimizes and stops working
✅ **Fixed!** Use headless mode (default).
- Set `HEADLESS_MODE = True` in `main.py` (line 8)
- No window to minimize - works completely in background

### Camera not detected
- Ensure webcam is connected and not used by another application
- Try changing camera index in `main.py`: `cap = cv2.VideoCapture(1)` (or 2, 3, etc.)
- Check camera permissions in Windows Settings

### Hand not detected / tracking unstable
- Ensure **good lighting** - bright, even light works best
- Keep hand within camera frame and at arm's length
- Try lowering detection confidence: `detectionCon=0.7` in `hand_tracker.py`
- Avoid cluttered backgrounds

### Mouse movement too fast/slow
- Adjust `smoothening` in `main.py`:
  - Lower (3-4) = faster, more responsive
  - Higher (6-8) = slower, smoother
- Default is 5 (balanced)

### Import errors / MediaPipe AttributeError
✅ **Fixed!** Migrated to new MediaPipe API.
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- Uses MediaPipe 0.10.31 with tasks API

### PyScreeze version issues
✅ **Fixed!** Pinned to compatible version.
- Project uses `pyscreeze==0.1.30`
- If issues: `pip install --force-reinstall pyscreeze==0.1.30`

### Accidental clicks
- Click cooldown is set to 10 frames
- Make gestures deliberately and hold briefly
- Increase `click_cooldown` in `main.py` for more delay

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for powerful hand tracking
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for cross-platform mouse control

## 💡 Tips for Best Performance

1. **Lighting**: Use bright, even lighting for best hand detection
2. **Camera Position**: Place camera at eye level, arm's length away
3. **Background**: Plain, uncluttered background improves tracking
4. **Hand Position**: Keep hand flat and facing camera
5. **Gestures**: Make deliberate, clear gestures - hold briefly
6. **Headless Mode**: Use headless mode to avoid window management issues

## 🚀 Future Improvements

- [ ] Add double-click gesture
- [ ] Implement drag-and-drop functionality
- [ ] Add scroll speed control
- [ ] Support for two-handed gestures
- [ ] Add gesture customization config file
- [ ] System tray icon for easy control
- [ ] Voice command integration

## ⚠️ Disclaimer

This tool is for educational and accessibility purposes. Use responsibly and be aware of system requirements when automating mouse control.

---

**Made with ❤️ using Python, MediaPipe, and OpenCV**

**Author:** Kush05Bhardwaj  
**Repository:** [Virtual_Mouse](https://github.com/Kush05Bhardwaj/Virtual_Mouse)
