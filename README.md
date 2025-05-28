# Drowsy Driver Detection System

A real-time driver drowsiness detection system using computer vision and Arduino-based hardware alerts. This system monitors eye movements through facial landmarks and gives real-time feedback based on user alertness.

## Features

- Detects user state: Active, Drowsy, or Sleeping
- Uses eye aspect ratio (EAR) from facial landmarks
- Sends real-time signals to Arduino for hardware alerts:
  - Servo motor movement
  - Buzzer activation
- Visual feedback via OpenCV overlay

## Tech Stack

**Python**
- OpenCV
- Dlib
- Imutils
- NumPy
- cvzone
- Playsound

**Arduino**
- Servo library
- Tone (buzzer)

## File Structure

```
.
├── drowsiness_detector.py
├── arduino_hardware.ino
├── shape_predictor_68_face_landmarks.dat  # Not included, download separately
└── README.md
```

## Setup Instructions

### Python

1. Install dependencies:
   ```bash
   pip install opencv-python dlib imutils numpy cvzone playsound
   ```

2. Download the facial landmarks model:

   https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

   Extract and place `shape_predictor_68_face_landmarks.dat` in the project directory.

3. Update video path in `drowsiness_detector.py`:
   ```python
   cap = cv2.VideoCapture(r"PATH_TO_YOUR_VIDEO.mp4")
   ```

4. Run:
   ```bash
   python drowsiness_detector.py
   ```

### Arduino

1. Connect:
   - Servo → Digital Pin 8
   - Buzzer → Digital Pin 9

2. Open `arduino.ino` in Arduino IDE.

3. Upload to board.

## Serial Protocol

| State     | Signal | Servo | Buzzer |
|-----------|--------|--------|--------|
| Active    | `'0'`  | 0°     | Off    |
| Drowsy    | `'2'`  | 45°    | On     |
| Sleeping  | `'1'`  | 90°    | On     |

