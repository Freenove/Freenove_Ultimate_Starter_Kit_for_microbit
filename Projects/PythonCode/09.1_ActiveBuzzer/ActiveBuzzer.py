from microbit import *
while True:
    for i in range(4):
        pin0.write_digital(1)
        sleep(100)
        pin0.write_digital(0)
        sleep(100)
    sleep(500)
