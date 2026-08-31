# 🎨 AI Virtual Painter

A simple real-time virtual painting application built with **Python, OpenCV, and MediaPipe**.

The application uses a webcam to detect hand landmarks and allows the user to interact with a virtual drawing canvas using hand gestures.

---

## ✨ Features

- 🖐️ Real-time hand tracking
- 🎨 Gesture-based color selection
- 🖌️ Draw using the index finger
- 📏 Dynamic brush size adjustment
- 🧹 Clear the drawing using a hand gesture
- 📷 Real-time webcam processing
- 🔄 Horizontal camera flip for a natural interaction experience
- ⌨️ Keyboard controls

---

## 🛠️ Technologies

- **Python**
- **OpenCV**
- **MediaPipe**

---

## 📂 Project Structure

```text
AI-Virtual-Painter/
│
├── Drawing.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## ⚙️ Requirements

Make sure you have **Python 3** installed on your system.

The project requires:

- `opencv-python`
- `mediapipe`

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/AGCode7/AI-Virtual-Painter.git
```

### 2. Enter the project directory

```bash
cd AI-Virtual-Painter
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the application with:

```bash
python Drawing.py
```

Make sure your webcam is connected and accessible.

---

## 🎮 Controls & Gestures

| Action               | Gesture / Key                       |
| -------------------- | ----------------------------------- |
| 🎨 Select Color      | Point at a color                    |
| 🖌️ Draw              | Use the index finger                |
| 📏 Change Brush Size | Adjust the distance between fingers |
| 🧹 Clear Canvas      | Close the fingers                   |
| 🗑️ Clear Canvas      | Press `C`                           |
| ❌ Exit              | Press `Q`                           |

---

## 🎨 Available Colors

The application currently provides the following colors:

- 🔴 Red
- 🟢 Green
- 🔵 Blue
- 🟡 Yellow
- 🩷 Pink

---

## 🧠 How It Works

The application captures video frames from the webcam using **OpenCV**.

Each frame is processed by **MediaPipe Hands**, which detects hand landmarks.

The detected landmarks are converted into pixel coordinates and used to calculate distances between specific points on the hand.

These measurements are then used to determine different interactions:

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hands
   ↓
Hand Landmarks
   ↓
Gesture Detection
   ↓
Drawing / Color Selection / Brush Size
```

The application then renders the drawing directly onto the webcam view.

---

## 🖐️ Hand Tracking

The project uses MediaPipe's hand landmark model to track the hand in real time.

The detected hand contains multiple landmarks that are used by the application to identify finger positions and calculate distances.

This allows the program to recognize different hand configurations without requiring a physical mouse or drawing tablet.

---

## 🎨 Color Selection

A color palette is displayed near the top of the webcam view.

The user can point toward one of the available colors with the index finger to change the active drawing color.

Available colors:

```text
RED
GREEN
BLUE
YELLOW
PINK
```

---

## 🖌️ Drawing

When the appropriate hand gesture is detected, the application uses the position of the index finger as the drawing point.

The drawing is represented by filled circles whose size depends on the current brush size.

This creates the effect of drawing directly in the air using the webcam.

---

## 📏 Brush Size

The application calculates distances between selected hand landmarks to dynamically change the brush size.

This allows the user to control the size of the virtual brush without using the keyboard or mouse.

---

## 🧹 Clearing the Canvas

The canvas can be cleared in two ways:

- Perform the configured hand gesture.
- Press `C` on the keyboard.

---

## ⌨️ Keyboard Shortcuts

```text
Q → Quit
C → Clear Canvas
```

---

## 🚀 Future Improvements

Possible improvements for future versions include:

- ✏️ Eraser mode
- ↩️ Undo / Redo
- 💾 Save drawings as image files
- 🖼️ Improved virtual canvas
- 🖐️ Multiple hand support
- 🎨 More colors
- 🖌️ More drawing tools
- 🧠 More robust gesture recognition
- 🖥️ Improved user interface

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you want to improve the project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Ali Gholami**

---

⭐ If you found this project useful, consider giving the repository a star!
