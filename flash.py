import sys, os
try:
    from MicroBitTools import flash

except IOError:
    print("Please plug in your microbit!")
    sys.exit()

args = sys.argv

if len(args) != 2:
    print("Command Structure: \"python flash.py [input file]\"")
    sys.exit()

if not os.path.exists(input := args[1]):
    print("Your input file does not seem to exist!")
    sys.exit()

try:
    flash(input)
    print("Your microbit was successfully flashed!")

except Exception as e:
    print("There was an error flashing your microbit, please try again!")


# path for my micrbit seems to be /dev/ttyACM0
