from microbit import *
import math
from micropython import const

class Driver:
    def __init__(self, L_PINS, R_PINS, duty_cycle = 1023):
        self.L_F = eval("pin" + str(L_PINS[1]))
        self.L_B = eval("pin" + str(L_PINS[0]))

        self.R_F = eval("pin" + str(R_PINS[1]))
        self.R_B = eval("pin" + str(R_PINS[0]))

        self.analog_max = const(duty_cycle)

    def stop(self):
        self.R_F.write_analog(0)
        self.R_F.write_digital(0)
        self.R_B.write_analog(0)
        self.R_B.write_digital(0)

        self.L_F.write_analog(0)
        self.L_F.write_digital(0)
        self.L_B.write_analog(0)
        self.L_B.write_digital(0)


    # provide a time in seconds or a distance cm for the robot to drive forward for
    # speeds are to be specified as a fraction of the maximum
    def forward(self, time = 0, speed = 100):
        if not time: pass

        if time:
            if speed == 100:
                self.L_F.write_digital(1)
                self.R_F.write_digital(1)
                sleep(time)
                self.stop()

            else:
                self.L_F.write_analog(round((speed / 100) * self.analog_max))
                self.R_F.write_analog(round((speed / 100) * self.analog_max))
                sleep(time)
                self.stop()

    def reverse(self, time = 0, speed = 100):
        if speed == 100:
            self.L_B.write_digital(1)
            self.R_B.write_digital(1)
            sleep(time)
            self.stop()

        else:
            self.L_B.write_analog(round((speed / 100) * self.analog_max))
            self.R_B.write_analog(round((speed / 100) * self.analog_max))
            sleep(time)
            self.stop()

    # for diection, -1 is left, 1 is right. give angle in degrees
    def turn(self, direction = None, time = 1, speed = 100):
        if direction != None:
            if direction == -1:
                if speed == 100:
                    self.R_F.write_digital(1)
                    self.L_B.write_digital(1)
                    sleep(time)
                    self.stop()

                else:
                    self.R_F.write_analog(round((speed / 100) * self.analog_max))
                    self.L_B.write_analog(round((speed / 100) * self.analog_max))
                    sleep(time)
                    self.stop()

            if direction == 1:
                if speed == 100:
                    self.R_F.write_digital(1)
                    self.L_B.write_digital(1)
                    sleep(time)
                    self.stop()

                else:
                    self.R_B.write_analog(round((speed / 100) * self.analog_max))
                    self.L_F.write_analog(round((speed / 100) * self.analog_max))
                    sleep(time)
                    self.stop()

    def forward_toggle(self, mode, direction = 1, speed = 100):
        if mode == 1:
            if direction == 1:
                if speed == 100:
                    self.L_F.write_digital(1)
                    self.R_F.write_digital(1)

                else:
                    spe = round((speed / 100) * self.analog_max)
                    self.L_F.write_analog(spe)
                    self.R_F.write_analog(spe)

            if direction == -1:
                if speed == 100:
                    self.L_B.write_digital(1)
                    self.R_B.write_digital(1)

                else:
                    spe = round((speed / 100) * self.analog_max)
                    self.L_B.write_analog(spe)
                    self.R_B.write_analog(spe)

        if mode == 0:
            self.stop()

    def turn_toggle(self, mode, direction, speed = 30):
        if mode == 1:
            if direction == 2:
                if speed == 100:
                    self.R_F.write_digital(1)
                    self.L_B.write_digital(1)

                else:
                    self.R_F.write_analog(round((speed / 100) * self.analog_max))
                    self.L_B.write_analog(round((speed / 100) * self.analog_max))

            if direction == 1:
                if speed == 100:
                    self.R_B.write_digital(1)
                    self.L_F.write_digital(1)

                else:
                    self.R_B.write_analog(round((speed / 100) * self.analog_max))
                    self.L_F.write_analog(round((speed / 100) * self.analog_max))

        if mode == 0:
            self.stop()

robot = Driver([13, 14], [16, 15])
