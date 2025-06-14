import cv2
import numpy as np
import dlib
from imutils import face_utils
from cvzone.SerialModule import SerialObject
from playsound import playsound
from time import sleep

from cvzone.FaceDetectionModule import FaceDetector

arduino = SerialObject()

cap = cv2.VideoCapture(r"PATH_TO_YOUR_VIDEO")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cap.set(cv2.CAP_PROP_FPS, 15)  # Reduce the frame rate to 15 FPS or lower


detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

asleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)


def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)


def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > 0.25:
        return 2
    elif ratio > 0.21 and ratio <= 0.25:
        return 1
    else:
        return 0


while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38],
                             landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44],
                              landmarks[47], landmarks[46], landmarks[45])

        if left_blink == 0 or right_blink == 0:
            asleep += 1
            if asleep > 6 and status != "SLEEPING !!!":
                arduino.sendData([1])
                # sleep(2)
                # arduino.sendData([0])
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                # playsound(r"PATH_TO_YOUR_BUZZER_AUDIO")
        elif left_blink == 1 or right_blink == 1:
            drowsy += 1
            if drowsy > 6 and status != "Drowsy !":
                arduino.sendData([2])
                # sleep(2)
                # arduino.sendData([0])
                status = "Drowsy !"
                color = (0, 0, 255)
        else:
            active += 1
            if active > 6 and status != "Active :)":
                arduino.sendData([0])
                # sleep(0.1)
                # arduino.sendData([0])
                status = "Active :)"
                color = (0, 255, 0)

        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
        break  # Only process the first detected face

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
