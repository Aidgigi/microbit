from driver import robot
from microbit import *
import math

acc_xp, acc_yp, acc_zp = accelerometer.get_values()


# this is our main loop
def event_loop():
    driving = False
    sensitivity = 700

    started = False

    while True:
        while not started:
            if button_a.is_pressed(): started = True

        while started:
            # getting the current readings
            acc_x, acc_y, acc_z = accelerometer.get_values()

            # doing some math
            delta_x, delta_y, delta_z = acc_x - acc_xp, acc_y - acc_yp, acc_z - acc_zp

            # calculating magnitute of impact
            magnitute = math.sqrt((delta_x ** 2) + (delta_y ** 2) + (delta_z ** 2))

            if not driving:
                driving = True
                robot.forward_toggle(1, speed = 40)


            if magnitute >= sensitivity:
                robot.stop()
                sleep(1000)
                robot.reverse(time = 1000, speed = 30)
                robot.turn(-1, time = 200, speed = 20)
                sleep(1200)
                driving = False

            if button_b.is_pressed():
                robot.stop()
                started = False
                driving = False

event_loop()
