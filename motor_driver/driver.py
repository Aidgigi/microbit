from microbit import *

class Driver:
    def __init__(self, L_PINS, R_PINS, diam, duty = 1023):
        LF_str = "pin" + str(L_PINS[1])
        LB_str = "pin" + str(L_PINS[0])
        RF_str = "pin" + str(R_PINS[1])
        RB_str = "pin" + str(R_PINS[0])
        self.L_F = eval(LF_str)
        self.L_B = eval(LB_str)

        self.R_F = eval(RF_str)
        self.R_B = eval(RB_str)

        self.analog_max = duty
        self.circumference = 2 * 3.14 * (diam / 2)

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
    def forward(self, time = 0, distance = 0, speed = 100):
        if not time and not distance: pass
        if time and distance: pass

        if time:
            if speed == 100:
                self.L_F.write_digital(1)
                self.R_F.write_digital(1)
                sleep(time * 1000)
                self.L_F.write_digital(0)
                self.R_F.write_digital(0)

            else:
                self.L_F.write_analog(round((speed / 100) * self.analog_max))
                self.R_F.write_analog(round((speed / 100) * self.analog_max))
                sleep(time * 1000)
                self.L_F.write_analog(0)
                self.R_F.write_analog(0)

    # for diection, -1 is left, 1 is right. give angle in degrees
    def turn(self, direction = None, time = 1, speed = 100, angle = None):
        if direction != None and angle != None: pass

        if direction != None:
            if direction == -1:
                if speed == 100:
                    self.R_F.write_digital(1)
                    self.L_B.write_digital(1)
                    sleep(time * 1000)
                    self.R_F.write_digital(0)
                    self.L_B.write_digital(0)

                else:
                    self.R_F.write_analog(round((speed / 100) * self.analog_max))
                    self.L_B.write_analog(round((speed / 100) * self.analog_max))
                    sleep(time * 1000)
                    self.R_F.write_analog(0)
                    self.L_B.write_analog(0)

            if direction == 1:
                if speed == 100:
                    self.R_F.write_digital(1)
                    self.L_B.write_digital(1)
                    sleep(time * 1000)
                    self.R_F.write_digital(0)
                    self.L_B.write_digital(0)

                else:
                    self.R_B.write_analog(round((speed / 100) * self.analog_max))
                    self.L_F.write_analog(round((speed / 100) * self.analog_max))
                    sleep(time * 1000)
                    self.R_B.write_analog(0)
                    self.L_F.write_analog(0)

        if angle != None:
            pass

    def forward_toggle(self, mode, speed = 100):
        if mode == 1:
            if speed == 100:
                self.L_F.write_digital(1)
                self.R_F.write_digital(1)

            else:
                spe = round((speed / 100) * self.analog_max)
                self.L_F.write_analog(spe)
                self.R_F.write_analog(spe)

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

            else: pass

        if mode == 0:
            self.stop()

robot = Driver([13, 14], [16, 15], 10)
