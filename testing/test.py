from microbit import *
import radio

count = 0
radio.on()
radio.config(data_rate = radio.RATE_250KBIT, channel = 10)

while True:
    if button_a.is_pressed():
        count -= 1

    if button_b.is_pressed():
        count += 1

    if count > 9: count = 0
    if count < 0: count = 0
    display.show(count)
    radio.send(str(count))
    sleep(200)
