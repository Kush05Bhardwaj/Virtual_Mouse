# 🖱️ Virtual Mouse - Hand Gesture Control

Control your computer mouse using hand gestures! This project uses MediaPipe for hand tracking and PyAutoGUI for mouse control, allowing you to interact with your computer hands-free.

## ✨ Features

- **Mouse Movement**: Control cursor with your index finger
- **Left Click**: Thumb + Index finger gesture
- **Right Click**: Thumb + Middle finger gesture  
- **Scroll**: Peace sign (Index + Middle fingers)
- **Exit**: Make a fist or press ESC

## 🎮 Hand Gesture Controls

| Gesture | Fingers Extended | Action |
|---------|-----------------|--------|
| ☝️ Index only | `[0,1,0,0,0]` | Move mouse cursor |
| 👆 Thumb + Index | `[1,1,0,0,0]` | Left click |
| 👉 Thumb + Middle | `[1,0,1,0,0]` | Right click |
| ✌️ Index + Middle | `[0,1,1,0,0]` | Scroll down |
| ✊ Fist (all closed) | `[0,0,0,0,0]` | Exit application |

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

1. **Activate your virtual environment** (if not already activated)

2. **Run the application**
```bash
python main.py
```

3. **Position your hand** in front of the webcam with good lighting

4. **Use gestures** to control your mouse:
   - Point with index finger to move cursor
   - Extend thumb + index to click
   - Extend thumb + middle to right-click
   - Peace sign to scroll
   - Make a fist to exit

5. **Exit** by making a fist or pressing ESC

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
- **OpenCV** (`opencv-python`): Camera capture and image processing
- **MediaPipe** (`mediapipe`): Hand landmark detection
- **PyAutoGUI** (`pyautogui`): Mouse control automation
- **NumPy** (`numpy`): Numerical computations

### How It Works

1. **Camera Capture**: Captures video frames from webcam using OpenCV
2. **Hand Detection**: MediaPipe detects hand landmarks (21 key points)
3. **Gesture Recognition**: Analyzes finger positions to identify gestures
4. **Mouse Control**: Translates gestures to mouse actions via PyAutoGUI

### Configuration

You can adjust these parameters in `main.py`:

```python
wCam, hCam = 640, 480    # Camera resolution
frameR = 100             # Frame reduction (boundary margin)
smoothening = 7          # Mouse movement smoothness (higher = smoother)
```

In `hand_tracker.py`:
```python
maxHands=1              # Maximum hands to detect
detectionCon=0.7        # Detection confidence threshold
trackCon=0.7           # Tracking confidence threshold
```

## 🐛 Troubleshooting

### Camera not detected
- Ensure your webcam is connected and not being used by another application
- Try changing the camera index in `main.py`: `cap = cv2.VideoCapture(1)`

### Hand not detected
- Ensure good lighting
- Keep your hand within the camera frame
- Try adjusting detection confidence in `hand_tracker.py`

### Import errors
- Make sure you've activated the virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### PyScreeze version issues
- The project uses `pyscreeze==0.1.30` for compatibility
- If issues persist: `pip install --force-reinstall pyscreeze==0.1.30`

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking
- [OpenCV](https://opencv.org/) for computer vision
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for mouse control

## ⚠️ Disclaimer

This tool is for educational purposes. Use responsibly and be aware of accessibility requirements when automating mouse control.

---

**Made with ❤️ using Python, MediaPipe, and OpenCV**
