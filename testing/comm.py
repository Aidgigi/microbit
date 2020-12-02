from microbit import *
import radio

radio.on()
radio.config(data_rate = radio.RATE_250KBIT, channel = 10)

count = 0

ls = True
while ls:
    if button_a.is_pressed(): ls = False

while True:
    new_count = 0
    message = radio.receive()
    if message != None:
        new_count = int(message)

        if new_count != count:
            count = new_count

    if button_a.is_pressed(): count -= 1
    if button_b.is_pressed(): count += 1

    if count > 9: count = 0
    if count < 0: count = 0

    if new_count != count:
        radio.send(str(count))
        display.show(count)
        sleep(200)

    display.show(count)
