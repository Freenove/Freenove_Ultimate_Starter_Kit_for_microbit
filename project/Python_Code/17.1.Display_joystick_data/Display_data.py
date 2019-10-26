from microbit import *
while True:
    xVal = pin2.read_analog()
    yVal = pin1.read_analog()
    zVal = pin0.read_digital()
    print(xVal,yVal,zVal)
    sleep(500)