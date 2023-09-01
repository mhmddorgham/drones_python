import cv2
from djitellopy import tello
import cvzone
import sys
import keyboard

thres = 0.55
nmsThres = 0.2
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
print(classNames)
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamoff()
me.streamon()

# me.takeoff()
# me.move_up(80)


def getKeyboardInput():
    if keyboard.is_pressed("l"):
        me.land()
    if keyboard.is_pressed("e"):
        me.takeoff()

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    print("inside keyboard input")

    if keyboard.is_pressed("LEFT"): lr = -speed
    if keyboard.is_pressed("RIGHT"): lr = speed

    if keyboard.is_pressed("UP"): fb = speed
    if keyboard.is_pressed("DOWN"): fb = -speed

    if keyboard.is_pressed("w"): ud = speed
    if keyboard.is_pressed("s"): ud = -speed

    if keyboard.is_pressed("a"): yv = -speed
    if keyboard.is_pressed("d"): yv = speed

    return [lr, fb, ud, yv]

while True:
    # success, img = cap.read()
    img = me.get_frame_read().frame
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cvzone.cornerRect(img, box , rt=0)
            cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 255, 0), 2)
    except:
        pass
    print("Waiting for commands...")
    # STEP 1
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    me.send_rc_control(0, 0, 0, 0)

    if img.any():
        cv2.imshow("Image", img)
        cv2.waitKey(1)


    if keyboard.is_pressed("q"):
        me.land()
        cv2.destroyAllWindows
        sys.exit("Program is stopped.")
        break


