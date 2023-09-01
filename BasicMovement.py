from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

#send_rc_control(-left/right, forward/-bakeward, 0, rotate)


#move forward
me.takeoff()
sleep(2)
me.send_rc_control(0, 50, 0, 0)
sleep(2)

#stopping completly, to not move forward while landing
me.send_rc_control(0, 0, 0, 0)
me.land()