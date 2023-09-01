from djitellopy import tello
#import KeyboardCommands as kbc
import keyboard
import cv2
import time
from time import sleep
import threading
import numpy as np


me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamoff()
me.streamon()

def getKeyboardInput():
    while True:
        if keyboard.is_pressed("q"):
            me.land()
            print("Program is stopped")
            break
        if keyboard.is_pressed("l"):
            me.land()
        if keyboard.is_pressed("e"):
            me.takeoff()

        lr, fb, ud, yv = 0, 0, 0, 0
        speed = 50
        print("Helloo")

        if keyboard.is_pressed("LEFT"): lr = -speed
        if keyboard.is_pressed("RIGHT"): lr = speed

        if keyboard.is_pressed("UP"): fb = speed
        if keyboard.is_pressed("DOWN"): fb = -speed

        if keyboard.is_pressed("w"): ud = speed
        if keyboard.is_pressed("s"): ud = -speed

        if keyboard.is_pressed("a"): yv = -speed
        if keyboard.is_pressed("d"): yv = speed

        #return [lr, fb, ud, yv]
        me.send_rc_control(lr, fb, ud, yv)

def getcam(me):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("Surveillance Feed", img)
        cv2.waitKey(1)

        #for saving pictures
        if keyboard.is_pressed("p"):
            cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
            print("i saved an image!")
            sleep(0.5)

        #for saving videos
        if keyboard.is_pressed("v"):
            pass


# def recordVid(img):
#     # This will return video from the first webcam on your computer.
#     #cap = cv2.VideoCapture(0) #VideoCapture is a method for getting webcam feed
#
#
#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter(f'Resources/Videos/{time.time()}.avi', fourcc, 20.0, (640, 480))
#
#     # loop runs if capturing has been initialized.
#     while True:
#         # output the frame
#         out.write(img)
#
#         # The original input frame is shown in the window
#         # cv2.imshow('Original', img)
#
#         # The window showing the operated video stream
#         # cv2.imshow('frame', gray)
#
#         # Wait for 'a' key to stop the program
#         if keyboard.is_pressed('b'):
#             break
#
#     # Close the window / Release webcam
#     cap.release()



# while True:
#     vals = getKeyboardInput()
#     me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
#
#     print("while true")


# to run functions at the same time, we used threads!
# Create a new thread
Thread1 = threading.Thread(target=getcam, args=[me])
Thread2 = threading.Thread(target=getKeyboardInput)

# Start the thread
Thread1.start()
Thread2.start()

# Wait for the threads to finish
Thread1.join()
Thread2.join()