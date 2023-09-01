# Cat face detection using har cascade
import cv2
import numpy

face = cv2.CascadeClassifier("Resourcess/haarcascade_frontalcatface.xml")  # for detecting face

image = cv2.imread("Resourcess/dogcat.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert into gray so color not affect accuracy

# parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray, 1.1, 1)  # for  faces

for (x, y, w, h) in faces:
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 20), 3)
    cv2.putText(image, "Cat", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (127, 0, 20), 2)
image = cv2.resize(image, (800, 700))
cv2.imshow("Face Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()