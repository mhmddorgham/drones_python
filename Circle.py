from djitellopy import tello
import time
me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()

t_end = time.time() + 20
while time.time() < t_end:
    me.send_rc_control(0, 10, 0, 30)

me.land()