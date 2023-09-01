import cvzone
import cv2

cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier("my_models/object_detection_model.h5", "my_models/labels.txt")


while True:
    _, img = cap.read()
    predictions = myClassifier.getPrediction(img)

    cv2.imshow("image", img)

    cv2.waitKey(1)