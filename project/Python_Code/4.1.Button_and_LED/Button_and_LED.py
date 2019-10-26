from microbit import *

while True:
    buttonState = pin0.read_digital()
    if buttonState == 0:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)