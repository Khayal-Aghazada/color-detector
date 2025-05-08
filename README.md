# 🎨 ColorPeek – Real-Time Color Detector

**ColorPeek** is a simple yet powerful color detection tool that uses your webcam to detect the name of the color in the center of the screen, using a color database.

---

## ✨ Features

- 🎥 Real-time webcam color detection
- 🧠 Detects color by comparing average pixel values in a central box
- 🗂️ Matches RGB values to color names using a CSV database
- 💡 Automatically adjusts text color (white/black) for readability

---

## 🛠️ Tech Stack

- **Python 3**
- **OpenCV** — for webcam and image processing
- **pandas** — to load and search the color name database

---

## 📦 Installation

### 🔧 Dependencies

```bash
pip install opencv-python pandas

Make sure to place colors.csv in the same directory or update the path in the script:
