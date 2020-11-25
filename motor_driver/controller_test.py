from microbit import *
import radio

radio.on()
radio.config(data_rate = radio.RATE_250KBIT, channel = 10, power = 7)
turning_left = False
turning_right = False
going_forward = False
message = 0

while True:
    if button_a.is_pressed() and not button_b.is_pressed():
        turning_left = True
        message = 3
        display.show(3)

    elif button_b.is_pressed() and not button_a.is_pressed():
        turning_right = True
        message = 5
        display.show(5)

    elif not button_a.is_pressed() or not button_b.is_pressed():
        if turning_left:
            turning_left = False
            message = 4
            display.show(4)

        if turning_right:
            turning_right = False
            message = 4
            display.show(4)

    elif button_a.is_pressed() and button_b.is_pressed():
        going_forward = True
        message = 1
        display.show(1)

    elif not button_a.is_pressed() and not button_b.is_pressed():
        if going_forward:
            going_forward = False
            message = 4
            display.show(4)

    radio.send(str(message))
    display.show(message)
