from microbit import *

duty_cycle = 1023
speed = round((60 / 100) * duty_cycle)

pin14.write_analog(speed)
pin15.write_analog(speed)
sleep(10000)
pin14.write_analog(0)
pin15.write_analog(0)
