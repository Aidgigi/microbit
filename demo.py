from microbit import *

while True:
    if button_a.is_pressed():
        
        pin14.write_digital(1)
        pin15.write_digital(1)
        sleep(5000)
        pin14.write_digital(0)
        pin15.write_digital(0)

        break
