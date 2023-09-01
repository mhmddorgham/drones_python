# from utils import *
# import numpy as np
#
# w, h = 360, 240
# pid = [0.5, 0.5, 0] #kp, kd, ki
# pError = 0
# startCounter = 1 ##for no flight put 1  -  for flight put 0
# myDrone = initializeTello()
#
# #find the faces in our image
# def findFace(img):
#     faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#     #find their coordinates and display it on the image
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         #first create empty lists in which we will add the Center
#         # points of the detected faces and their areas.
#         myFacesListC = []
#         myFaceListArea = []
#
#         #find the center point and the area of each face and add to list
#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             cx = x + w // 2
#             cy = y + h // 2
#             area = w * h
#             myFacesListC.append([cx, cy])
#             myFaceListArea.append(area)
#
#         #find the closest one and return its coordinates. If no faces are found we will return 0
#         if len(myFaceListArea) != 0:
#             i = myFaceListArea.index(max(myFaceListArea))
#             # index of closest face
#             return img, [myFacesListC[i], myFaceListArea[i]]
#         else:
#             return img, [[0, 0], 0]
#
# # create a function that will use the information of the face and try to follow it
# def trackFace(myDrone, info, w, pid, pError):
#     #print(info)
#
#     # PID (proportional–integral–derivative), to move smoothly
#     error = info[0][0] - w // 2
#     # Current Value - Target Value
#     speed = int(pid[0] * error + pid[1] * (error - pError))
#     speed = int(np.clip(speed, -100, 100))
#     print(speed)
#     # make sure that the face is detected
#     if info[0][0] != 0:
#         myDrone.yaw_velocity = speed
#     else:
#         myDrone.left_right_velocity = 0
#         myDrone.for_back_velocity = 0
#         myDrone.up_down_velocity = 0
#         myDrone.yaw_velocity = 0
#         error = 0
#
#     # SEND VELOCITY VALUES TO TELLO
#     if myDrone.send_rc_control:
#         myDrone.send_rc_control(myDrone.left_right_velocity,
#                                 myDrone.for_back_velocity,
#                                 myDrone.up_down_velocity,
#                                 myDrone.yaw_velocity)
#
#     # Now we will return the error since we will need it for
#     # the calculation of the Derivative part of the PID controller in the next frame.
#     return error
#
#
# # Lastly we will call this function in the main script
# ## STEP 3
# # pError = trackFace(myDrone,c,w,pid,pError)
#
#
# #----------
#
# #def start_faceFinding():
# while True: #we put this in a function
#     ##FLIGHT
#     if startCounter == 0:
#         myDrone.takeoff()
#         #myDrone.streamon()
#         startCounter = 1 #1 is the original
#
#     ## STEP 1
#     img = telloGetFrame(myDrone, w, h)
#     ## STEP 2
#     img, info = findFace(img)
#     print(info[0][0])
#     ## STEP 3
#     pError = trackFace(myDrone, info, w, pid, pError)
#     print(info[0][0])
#     cv2.imshow('Image', img)
#     # WAIT FOR THE 'Q' BUTTON TO STOP
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#     # replace the 'and' with '&amp;'
#         myDrone.land()
#         break
#
#
#
