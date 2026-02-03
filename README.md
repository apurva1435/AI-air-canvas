# 🎨 AI Air Canvas

AI Air Canvas is a computer vision–based drawing application that allows users to draw in the air using hand gestures captured through a webcam.

The system uses AI-powered hand tracking to convert finger movements into digital drawings in real time—without the need for a mouse, stylus, or touchscreen.

---

## 🔍 Features
- Real-time hand and finger tracking
- Air-based drawing using index finger
- No physical contact required
- Clear canvas with a single key press
- Lightweight and fast execution

---

## 🧠 Technologies Used
- Python 3.11
- OpenCV
- MediaPipe
- NumPy

---

## ⚙️ How It Works
1. Webcam captures live video frames.
2. MediaPipe detects hand landmarks.
3. Index finger tip coordinates are tracked.
4. Movement is mapped to a virtual canvas.
5. Lines are drawn dynamically as the finger moves.

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
py -3.11 air_canvas.py

or
```bash


cd AI-air-canvas
py -3.11 air_canvas.py





