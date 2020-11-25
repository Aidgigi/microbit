from microbit import *
import radio

count = 0
radio.on()
radio.config(data_rate = radio.RATE_250KBIT, channel = 10)

while True:
    msg = radio.receive()
    if msg:
        display.show(int(msg))
