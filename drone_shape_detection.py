import cv2
from djitellopy import tello
import time
import cvzone

# Connect to Tell drone
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

me.takeoff()
me.send_rc_control(0, 0, 0, 0)
time.sleep(2.2)


def face_recognition(img):
    myClassifier = cvzone.Classifier("Resourcess/face_recognition.h5",
                                     "Resourcess/face_recognition_labels.txt")
    predictions = myClassifier.getPrediction(img)

    return predictions

# Loop over frames from the camera
while True:
    frame = me.get_frame_read().frame
    frame = cv2.resize(frame, (360, 240))
    me.send_rc_control(0, 0, 0, 0)

    result = face_recognition(frame)
    cv2.imshow('Face Recognition', result)
    if cv2.waitKey(1) == ord('q'):
        me.land()
        break



