from djitellopy import Tello
import cv2
import numpy as np

tello = Tello()
tello.connect()
tello.streamon()
window_name = "Tello Yellow Object Tracking"
cv2.namedWindow(window_name)

# Define lower and upper boundaries for yellow color in HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])

while True:
    frame = tello.get_frame_read().frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding rectangles around yellow objects and track their centers
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.circle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

            cv2.circle(frame, (x + w // 2, y + h // 2), max(w, h) // 2, (0, 255, 0), 2)
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            fbRange = [1200, 1800]
            if area > fbRange[0] and area < fbRange[1]:
                fb = 0
            elif area > fbRange[1]:
                fb = -20
            elif area < fbRange[0] and area != 0:
                fb = 20
            if x == 0:
                fb = 0


    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
tello.streamoff()
tello.land()



