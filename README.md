# 🎨 AI Virtual Painter

A real-time virtual painting application built with **Python, OpenCV, and MediaPipe**.

AI Virtual Painter allows you to draw on your screen using hand gestures captured through a webcam. It uses MediaPipe to detect hand landmarks and OpenCV to process camera frames and render drawings in real time.

## ✨ Features

- **Real-Time Hand Detection:** Detects and tracks hand landmarks using MediaPipe.
- **Virtual Drawing:** Draw on the screen using your index finger.
- **Color Selection:** Select different brush colors using hand gestures.
- **Dynamic Brush Size:** Adjust the brush size by changing the distance between your fingers.
- **Clear Canvas:** Clear the entire drawing using a fist gesture.
- **Live Hand Tracking:** Visualizes detected hand landmarks and connections.
- **Webcam Integration:** Captures and processes live video frames using OpenCV.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| OpenCV | Image processing and webcam handling |
| MediaPipe | Hand landmark detection |
| Math | Distance calculations and gesture recognition |

## 📂 Project Structure

```text
AI-Virtual-Painter/
│
├── main.py
│
├── modules/
│   ├── __init__.py
│   ├── camera.py
│   ├── config.py
│   ├── drawing.py
│   ├── hand_detector.py
│   └── ui.py
│
├── assets/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AGCode7/AI-Virtual-Painter.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Virtual-Painter
```

### 3. Install Dependencies

```bash
pip install opencv-python mediapipe
```

### 4. Run the Application

```bash
python main.py
```

**Note:** Make sure your webcam is connected and accessible before running the application.

## 🖐️ Hand Gestures & Controls

| Gesture / Key | Action |
|---|---|
| Index Finger Extended | Display color selection buttons |
| Move Index Finger | Select a color |
| Change Finger Distance | Adjust brush size |
| Other Drawing Position | Draw on the canvas |
| Make a Fist | Clear the canvas |
| `C` | Clear the canvas |
| `Q` | Exit the application |

## 🎨 Available Colors

The application currently supports five brush colors:

- 🔴 Red
- 🟢 Green
- 🔵 Blue
- 🟡 Yellow
- 🩷 Pink

## 📋 Requirements

- Python 3.12
- A working webcam
- OpenCV
- MediaPipe

## 🚀 Future Improvements

Potential improvements for future versions:

- Multiple webcam selection and camera configuration.
- Modular gesture controller.
- Additional drawing tools and colors.
- Save and export drawings.
- Improved gesture recognition.

## 👨‍💻 Author

**AGCode7**

GitHub: [@AGCode7](https://github.com/AGCode7)

---

*Built with Python, OpenCV, and MediaPipe.*