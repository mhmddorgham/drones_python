from djitellopy import tello
import time
me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()

from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

#send_rc_control(-left/right, forward/-bakeward *actually speed*, 0, rotate)

me.takeoff()
me.send_rc_control(0, 50, 0, 0)



me.send_rc_control(0, 0, 0, 0)
me.land()