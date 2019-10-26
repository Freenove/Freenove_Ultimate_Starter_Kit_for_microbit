from microbit import *
display.off()
outPin = [pin0, pin1, pin2, pin3, pin4, pin10, pin6, pin7, pin9, pin8]
while True:
    for p in outPin:
        p.write_digital(1)
        sleep(100)
        p.write_digital(0)
        sleep(100)