from djitellopy import tello
import KeyboardCommands as kbc
from time import sleep
import keyboard

kbc.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kbc.getKey("LEFT"): lr = -speed
    elif kbc.getKey("RIGHT"): lr = speed

    if kbc.getKey("UP"): fb = speed
    elif kbc.getKey("DOWN"): fb = -speed

    if kbc.getKey("w"): ud = speed
    elif kbc.getKey("s"): ud = -speed

    if kbc.getKey("a"): yv = -speed
    elif kbc.getKey("d"): yv = speed

    return [lr, fb, ud, yv]

while True:
    print("waiting for commands...")

    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    if keyboard.is_pressed("q"):
        me.land()
        print("Program is stopped")
        break
    elif keyboard.is_pressed("e"):
        me.takeoff()
    else:
        pass