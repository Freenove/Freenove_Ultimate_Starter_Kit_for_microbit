from microbit import *
display.off()
Pin = [pin0, pin1, pin2, pin3]
while True:
    for i in Pin:
        for j in Pin:
            if i == j:
                j.write_digital(1)
            else:
                j.write_digital(0)
        sleep(10)