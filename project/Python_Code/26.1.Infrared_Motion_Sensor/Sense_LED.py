from microbit import *
while True:
    if pin0.read_digital()==1:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)