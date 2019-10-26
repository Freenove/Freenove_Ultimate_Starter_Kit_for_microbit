from microbit import *
while True:
   uart.write(str(accelerometer.get_values())+"\r\n")
   sleep(1000)
