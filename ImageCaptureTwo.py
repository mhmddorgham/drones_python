import cv2
from djitellopy import Tello

# Initialize Tello
tello = Tello()
tello.connect()
tello.streamon()

# Create a video capture object
cap = tello.get_frame_read()

# Main loop
while True:
    # Read frame from the video capture
    frame = cap.frame

    # Display the frame
    cv2.imshow("Tello Stream", frame)

    # Check for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Capture image when 'c' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Save the frame as an image
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured!")

# Release resources
cv2.destroyAllWindows()
tello.streamoff()
tello.end()
