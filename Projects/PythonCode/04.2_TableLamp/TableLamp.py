from microbit import *

status = 0

while True:
    if pin0.read_digital() == 0:
        sleep(10)
        if pin0.read_digital() == 0:
            if status == 0:
                status = 1
            else:
                status = 0
            pin1.write_digital(status)
            while pin0.read_digital() == 0:
                sleep(10)