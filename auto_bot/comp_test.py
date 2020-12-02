from microbit import *
import math

sensitivity = 100000

while True:
    if compass.get_field_strength() >= sensitivity:
        display.show("M")

    else:
        display.clear()

    sleep(50)
