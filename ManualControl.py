# from djitellopy import tello
# #import KeyboardCommands as kbc
# import keyboard
# import cv2
# import time
# from time import sleep
# import threading
# import numpy as np
#
#
# me = tello.Tello()
# me.connect()
# print(me.get_battery())
#
# global img
# record = False
#
# me.streamoff()
# me.streamon()
#
#
# def getKeyboardInput():
#     if keyboard.is_pressed("l"):
#         me.land()
#     if keyboard.is_pressed("e"):
#         me.takeoff()
#
#     lr, fb, ud, yv = 0, 0, 0, 0
#     speed = 50
#     print("inside keyboard input")
#
#     if keyboard.is_pressed("LEFT"): lr = -speed
#     if keyboard.is_pressed("RIGHT"): lr = speed
#
#     if keyboard.is_pressed("UP"): fb = speed
#     if keyboard.is_pressed("DOWN"): fb = -speed
#
#     if keyboard.is_pressed("w"): ud = speed
#     if keyboard.is_pressed("s"): ud = -speed
#
#     if keyboard.is_pressed("a"): yv = -speed
#     if keyboard.is_pressed("d"): yv = speed
#
#     return [lr, fb, ud, yv]
#
#
# def getcam(me):
#     img = me.get_frame_read().frame
#     img = cv2.resize(img, (360, 240))
#
#     print("inside get camera")
#
#     if keyboard.is_pressed("p"):
#         cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
#         print("i saved an image!")
#         sleep(0.1)
#
#     return img
#
#
# # Define the codec and create VideoWriter object
# # specifies video format
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
#
# # saving specifications of the video file
# video = cv2.VideoWriter(f'Resources/Videos/{time.time()}.avi', fourcc, 20, (360, 240))
#
#
# def recordVid(img):
#     print("inside record")
#     # loop runs if capturing has been initialized.
#     video.write(img)
#     time.sleep(1/30)
#
#
# while True:
#     print("Waiting for commands...")
#     # STEP 1
#     vals = getKeyboardInput()
#     me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
#     # STEP 2
#     img = getcam(me)
#     print("while true")
#     cv2.imshow("Surveillance Feed", img)
#     cv2.waitKey(1)
#
#     # STEP 3 ???
#     if keyboard.is_pressed("q"):
#         me.land()
#         print("Program is stopped")
#         break
#     if keyboard.is_pressed("v"):
#         record = True
#         recordVid(img)
#     if keyboard.is_pressed('b'):
#         video.release
#         record = False