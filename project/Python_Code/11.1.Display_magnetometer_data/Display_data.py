from microbit import *
compass.calibrate()
while True:
    azimuth = compass.heading()
    uart.write(str(azimuth)+"\r\n")
    sleep(1000)