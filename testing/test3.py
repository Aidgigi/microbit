from microbit import *

pin_num = 13
pin_str = "pin" + str(pin_num)
pin_var = eval(pin_str)
pin_var.write_digital(1)
sleep(2000)
pin_var.write_digital(0)
