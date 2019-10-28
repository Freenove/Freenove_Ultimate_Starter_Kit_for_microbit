from microbit import *
def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
red=255
green=255
blue=0
red=map(red,0,255,1023,0)
green=map(green,0,255,1023,0)
blue=map(blue,0,255,1023,0)
pin2.write_analog(red)
pin1.write_analog(green)
pin0.write_analog(blue)