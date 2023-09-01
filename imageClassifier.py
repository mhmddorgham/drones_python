import cv2
from djitellopy import tello
import time
import numpy as np
from tensorflow.keras.models import load_model

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

me.takeoff()
me.send_rc_control(0, 0, 0, 0)
time.sleep(2.2)


# Define a function to classify the image
def classify_image(img):
    # Load the saved model
    model = load_model('Resourcess/cat_dog_classifier.h5')
    img = cv2.resize(img, (100, 100))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    # Use the model to make predictions
    y_pred = model.predict(img.reshape(1, 100, 100, 3))
    print(y_pred)
    y_pred = y_pred > 0.5
    print(y_pred)

    if (y_pred == 0):
        pred = 'dog'
    else:
        pred = 'cat'

    return pred


# Loop over frames from the camera
while True:
    frame = me.get_frame_read().frame
    frame = cv2.resize(frame, (360, 240))

    # Display the frame
    cv2.imshow('frame', frame)

    # Classify the frame
    result = classify_image(frame)

    # Print the classification result on the frame
    cv2.putText(frame, result, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame with the classification result
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        me.land()
        break
