# 🖱️ Virtual Mouse - Hand Gesture Control

Control your computer mouse using hand gestures! This project uses MediaPipe for hand tracking and PyAutoGUI for mouse control, allowing you to interact with your computer hands-free.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.31-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Hand Gesture Controls](#-hand-gesture-controls)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Technical Details](#-technical-details)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## ✨ Features

- **Headless Mode**: Run in background without any window (works when minimized!)
- **Mouse Movement**: Control cursor with your index finger only (thumb down for precision)
- **Left Click**: Thumb + Index finger gesture
- **Right Click**: Thumb + Middle finger gesture  
- **Scroll Down**: Index + Middle fingers (no thumb)
- **Scroll Up**: Middle + Ring fingers (no thumb)
- **🆕 Quick Launch**: Open hand gesture to launch multiple URLs, folders, and apps instantly!
- **Smart Exit**: Hold fist for 1 second to exit (prevents accidental exits)
- **Smooth Movement**: Exponential smoothing with configurable sensitivity
- **Click Debouncing**: Prevents accidental multiple clicks
- **High Performance**: 30 FPS camera capture with zero-delay mouse control
- **Debug Mode**: Optional visual feedback for gesture detection

## 🎮 Hand Gesture Controls

| Gesture | Fingers Extended | Action |
|---------|-----------------|--------|
| ☝️ Index only | `[0,1,0,0,0]` | Move mouse cursor |
| 👆 Thumb + Index | `[1,1,0,0,0]` | Left click |
| 👉 Thumb + Middle | `[1,0,1,0,0]` | Right click |
| ✌️ Index + Middle | `[0,1,1,0,0]` | Scroll DOWN |
| 🖖 Middle + Ring | `[0,0,1,1,0]` | Scroll UP |
| 🖐️ Open hand (all 5 fingers) | `[1,1,1,1,1]` | **Quick Launch** URLs, folders & apps |
| ✊ Fist (hold 1 sec) | `[0,0,0,0,0]` | Exit application |

**Note:** For mouse movement, ONLY the index finger should be up - all other fingers (including thumb) must be down for precise control.

### 🚀 Quick Launch Feature

The **open hand gesture** (all 5 fingers extended) allows you to instantly launch multiple URLs, folders, and applications with a single gesture!

**Default Configuration:**
- **5 URLs**: GitHub profile, ChatGPT, LinkedIn, YouTube, Gmail
- **1 Folder**: Your Projects folder (F:\)
- **2 Apps**: Task Manager, VS Code

**Customization:**

Edit the configuration in `main.py` (lines 15-29) to add your favorite items:

```python
# Open Hand Gesture Configuration
URLS = [
    "https://github.com/Kush05Bhardwaj",
    "https://chatgpt.com/",
    "https://www.linkedin.com/in/kush2012bhardwaj",
    "https://www.youtube.com",
    "https://mail.google.com/mail/u/0/#inbox"
]

FOLDERS = [
    r"F:\Projects",
    r"C:\Users\YourName\Documents",  # Add more folders
]

APPS = [
    "taskmgr",      # Task Manager
    "code",         # VS Code
    "notepad",      # Add more apps
    "calc",         # Calculator
]
```

**Features:**
- ✅ Opens all URLs in browser tabs simultaneously
- ✅ Opens folders in Windows Explorer
- ✅ Launches applications
- ✅ 2-second cooldown prevents accidental re-triggering
- ✅ Fully customizable - add as many items as you want!

## 🚀 Quick Start

```powershell
# Clone the repository
git clone https://github.com/Kush05Bhardwaj/Virtual_Mouse.git
cd Virtual_Mouse

# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

**That's it!** Now use hand gestures in front of your webcam to control your mouse. Hold a fist for 1 second to exit.

**Pro Tip:** Show an open hand (all 5 fingers) to instantly launch your configured URLs, folders, and apps! Edit the `URLS`, `FOLDERS`, and `APPS` lists in `main.py` to customize what opens.

## 🚀 Installation

### Prerequisites
- **Python**: 3.8 or higher
- **Webcam**: Built-in or external USB webcam
- **Operating System**: Windows 10/11, Linux (Ubuntu 20.04+), or macOS 10.15+
- **RAM**: Minimum 4GB (8GB recommended for smooth performance)
- **Processor**: Dual-core CPU (Quad-core recommended)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Kush05Bhardwaj/Virtual_Mouse.git
cd Virtual_Mouse
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
   - Extend **thumb + middle** to right click
   - Extend **index + middle** (no thumb) to scroll DOWN
   - Extend **middle + ring** (no thumb) to scroll UP
   - Show **open hand (all 5 fingers)** to launch your configured URLs, folders, and apps
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
   - Finger array format: `[Thumb, Index, Middle, Ring, Pinky]`
   - `1` = finger extended/up, `0` = finger folded/down
   - Example: `[0,1,0,0,0]` = Only index finger is up
4. **Coordinate Mapping**: Maps camera coordinates to screen coordinates with boundary checking
5. **Smoothing**: Applies exponential smoothing for fluid cursor movement
6. **Mouse Control**: Translates gestures to mouse actions via PyAutoGUI with zero delay

#### Finger Detection Logic

The system uses a 5-element array to represent finger states:
```
[Thumb, Index, Middle, Ring, Pinky]
   0      1      2       3      4
```

- **Position 0 (Thumb)**: `1` if thumb is extended, `0` if folded
- **Position 1 (Index)**: `1` if index finger is extended, `0` if folded
- **Position 2 (Middle)**: `1` if middle finger is extended, `0` if folded
- **Position 3 (Ring)**: `1` if ring finger is extended, `0` if folded
- **Position 4 (Pinky)**: `1` if pinky is extended, `0` if folded

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for powerful hand tracking
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for cross-platform mouse control

## 💡 Tips for Best Performance

1. **Lighting**: Use bright, even lighting for best hand detection
   - Natural daylight works best
   - Avoid backlighting (light behind you)
   - Face a light source if possible
2. **Camera Position**: Place camera at eye level, arm's length away
   - Keep hand within the camera frame
   - Maintain consistent distance from camera
3. **Background**: Plain, uncluttered background improves tracking
   - Avoid busy patterns or moving objects
   - Solid-colored walls work great
4. **Hand Position**: Keep hand flat and facing camera
   - Palm should face the camera
   - Fingers should be clearly visible and separated
5. **Gestures**: Make deliberate, clear gestures - hold briefly
   - Avoid rapid hand movements
   - Pause between gestures for better recognition
6. **Headless Mode**: Use headless mode (default) to avoid window management issues
   - No performance impact from rendering
   - Works seamlessly when switching applications
7. **System Resources**: Close unnecessary applications for better performance
   - Virtual Mouse uses ~5-10% CPU on modern systems
   - Ensure webcam drivers are up to date

## 🚀 Future Improvements

- [x] ~~Quick launch apps and URLs with hand gesture~~ ✅ **Implemented!**
- [ ] Add double-click gesture (e.g., quick tap motion)
- [ ] Implement drag-and-drop functionality (pinch and move)
- [ ] Add configurable scroll speed control
- [ ] Support for two-handed gestures (multi-hand operations)
- [ ] Add gesture customization via config file
- [ ] System tray icon for easy control and status
- [ ] Voice command integration
- [ ] Add volume control gestures
- [ ] Support for custom keybindings
- [ ] Add gesture recording and playback

## ⚠️ Disclaimer

This tool is for educational and accessibility purposes. Use responsibly and be aware of system requirements when automating mouse control.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Areas for Contribution

- Bug fixes and performance improvements
- New gesture recognition patterns
- Cross-platform compatibility improvements
- Documentation and tutorials
- UI/UX enhancements
- Test coverage

---

**Author:** Kush05Bhardwaj  
**Repository:** [Virtual_Mouse](https://github.com/Kush05Bhardwaj/Virtual_Mouse)
