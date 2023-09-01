import cv2
import numpy as np
from djitellopy import Tello

drone = Tello()
drone.connect()
drone.streamon()

cv2.namedWindow("Color Detection", cv2.WINDOW_NORMAL)
lower_color = np.array([0, 0, 0])
upper_color = np.array([255, 255, 255])
gate_area_threshold = 1000

# Movement thresholds for drone control
area_big_threshold = 20000
area_small_threshold = 5000
center_x_threshold = 20
center_y_threshold = 20

# Main loop
while True:
    frame = drone.get_frame_read().frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > gate_area_threshold:
            moments = cv2.moments(contour)
            center_x = int(moments["m10"] / moments["m00"])
            center_y = int(moments["m01"] / moments["m00"])

            if area > area_big_threshold:
                drone.move_forward(20)  # Stop moving forward
            elif area < area_small_threshold:
                drone.move_forward(50)  # Move forward

            if center_x > center_x_threshold:
                drone.rotate_clockwise(20)  # Turn right
            elif center_x < -center_x_threshold:
                drone.rotate_counter_clockwise(20)  # Turn left

            if center_y > center_y_threshold:
                drone.move_up(20)  # Move up
            elif center_y < -center_y_threshold:
                drone.move_down(20)  # Move down

    cv2.imshow("Color Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.streamoff()
drone.disconnect()



#
# import cv2
# import numpy as np
# from djitellopy import Tello
#
# # Initialize Tello drone
# drone = Tello()
#
# # Connect to the drone
# drone.connect()
#
# # Set up the video stream
# drone.streamon()
#
# # Create a window to display the video feed
# cv2.namedWindow("Color Detection", cv2.WINDOW_NORMAL)
#
# # Color range for gate detection (adjust these values accordingly)
# lower_color = np.array([0, 0, 0])
# upper_color = np.array([255, 255, 255])
#
# # Gate detection parameters
# gate_area_threshold = 1000  # Adjust this value according to your needs
#
# # Movement thresholds for drone control
# area_big_threshold = 20000
# area_small_threshold = 5000
# center_x_threshold = 20
# center_y_threshold = 20
#
# # Main loop
# while True:
#     # Get the latest frame from the drone's video stream
#     frame = drone.get_frame_read().frame
#
#     # Convert the frame to the HSV color space
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # Apply color thresholding to detect the gate
#     mask = cv2.inRange(hsv_frame, lower_color, upper_color)
#
#     # Find contours of gate objects in the mask
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Process each contour
#     for contour in contours:
#         # Calculate the area of the contour
#         area = cv2.contourArea(contour)
#
#         if area > gate_area_threshold:
#             # Calculate the centroid of the contour
#             moments = cv2.moments(contour)
#             center_x = int(moments["m10"] / moments["m00"])
#             center_y = int(moments["m01"] / moments["m00"])
#
#             # Control drone movements based on the gate detection
#             if area > area_big_threshold:
#                 drone.move_forward(20)  # Stop moving forward
#             elif area < area_small_threshold:
#                 drone.move_forward(50)  # Move forward
#
#             if center_x > center_x_threshold:
#                 drone.rotate_clockwise(20)  # Turn right
#             elif center_x < -center_x_threshold:
#                 drone.rotate_counter_clockwise(20)  # Turn left
#
#             if center_y > center_y_threshold:
#                 drone.move_up(20)  # Move up
#             elif center_y < -center_y_threshold:
#                 drone.move_down(20)  # Move down
#
#     # Display the frame with gate detection
#     cv2.imshow("Color Detection", frame)
#
#     # Check for keyboard input and break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release resources
# cv2.destroyAllWindows()
# drone.streamoff()
# drone.disconnect()
