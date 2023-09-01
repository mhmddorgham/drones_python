import cvzone
import cv2


#  A library to help to load my model in the Pycharm
cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier("Resourcess/khalil_and_marwan.h5", "Resourcess/labels.txt")

while True:
    _, img = cap.read()
    predictions = myClassifier.getPrediction(img)
    # print(predictions)
    print(_)
    cv2.imshow("Khalil and marwan classification", img)
    cv2.waitKey(1)