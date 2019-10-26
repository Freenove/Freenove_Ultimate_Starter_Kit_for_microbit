from microbit import *
import utime
number=0
while True:
    uart.write('Counter: '+str(number)+"\r\n")
    sleep(1000)
    number=number+1