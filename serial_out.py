import MicroBitTools as mbt
mbs = mbt.SerialSystem()

mbs.readyMicroBit()


while True:
    print(mbs.read())
