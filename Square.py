from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

#send_rc_control(-left/right, forward/-bakeward *actually speed*, 0, rotate)

#move forward
me.takeoff()
me.rotate_clockwise(90)
me.move_forward(100)
me.rotate_clockwise(90)
me.move_forward(100)
me.rotate_clockwise(90)
me.move_forward(100)
me.rotate_clockwise(90)
me.move_forward(100)


me.send_rc_control(0, 0, 0, 0)
me.land()