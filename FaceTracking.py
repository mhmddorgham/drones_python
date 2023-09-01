from utils import *
import keyboard

w, h = 640, 360
pid = [0.5, 0.5, 0] #kp, kd, ki
pError = 0
startCounter = 1 #put as 1 if takeoff is not needed

myDrone = initializeTello()

while True:

    ## Flight
    if startCounter == 0:
        myDrone.takeoff()
        myDrone.move_up(70)
        startCounter = 1

    # STEP 1
    img = telloGetFrame(myDrone, w, h)
    # STEP 2
    img, info = findFace(img)
    #print("img", info[1])
    # STEP 3
    pError = trackFace(myDrone, info, w, pid, pError)
    #print(info[0][0]) #printing the coordinates of the tracked face
    # DISPLAY IMAGE
    cv2.imshow('Image', img)
    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) and 0xFF == ord('q'):
    # replace the 'and' with '&amp;'
        myDrone.land()
        break

    if keyboard.is_pressed("q"):
        cv2.destroyAllWindows
        print("Program is stopped")
        break
    else:
        pass