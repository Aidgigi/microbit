from microbit import *
import math

sensitivity = 1000
acc_xp, acc_yp, acc_zp = accelerometer.get_values()

while True:
    acc_x, acc_y, acc_z = accelerometer.get_values()
    delta_x, delta_y, delta_z = acc_x - acc_xp, acc_y - acc_yp, acc_z - acc_zp
    acc_xp, acc_yp, acc_zp = acc_x, acc_y, acc_z

    magnitute = math.sqrt((delta_x ** 2) + (delta_y ** 2) + (delta_z ** 2))

    if magnitute >= sensitivity:
        print(magnitute)

    sleep(50)
