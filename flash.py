import sys, os
try:
    from MicroBitTools import flash, flashF
except IOError:
    print("Please plug in your microbit!")
    sys.exit()

args = sys.argv

if len(args) != 3:
    print("Command Structure: \"python flash.py [mode (file/dir)] [input file]\"")
    sys.exit()

if not os.path.exists(input := args[2]):
    print("Your input file does not seem to exist!")
    sys.exit()

try:
    if args[1] == "file":
        flash(input)
    else:
        flashF(input)

    print("Your microbit was successfully flashed!")

except Exception as e:
    print("There was an error flashing your microbit, please try again!")


# path for my microbit seems to be /dev/ttyACM0
