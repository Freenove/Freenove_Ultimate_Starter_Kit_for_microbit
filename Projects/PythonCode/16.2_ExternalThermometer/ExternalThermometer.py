from microbit import *
import math
while True:
    adcValue = pin0.read_analog()
    V = adcValue*3.3/1023.0
    Rt = V/((3.3-V)/10)
    tempC = (1/(1/(273.15+25) + math.log(Rt/10)/3950))-273.15
    display.scroll(round(tempC))
