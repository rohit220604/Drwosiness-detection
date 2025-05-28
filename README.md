# Drowsy Driver Detection System

This project is a real-time drowsiness detection system using computer vision and hardware feedback (buzzer and servo). It uses facial landmark analysis to monitor eye activity and detect when a person is drowsy or asleep, triggering visual and hardware alerts.

## Features

- Detects driver's eye status (Active, Drowsy, Sleeping)
- Uses dlib's 68-point facial landmark detection
- Provides visual feedback on screen
- Sends signals to Arduino to:
  - Play buzzer tones
  - Control a servo motor (can be used to trigger further actions like seat vibrations)

---

## Tech Stack

- **Python (OpenCV, Dlib, Imutils, cvzone)**
- **Arduino (Servo, Buzzer control)**
- **Hardware:** Arduino Uno, Servo Motor, Buzzer

---

## Setup Instructions

### 1. Python Environment

#### Install Dependencies:
```bash
pip install opencv-python dlib imutils numpy cvzone playsound
