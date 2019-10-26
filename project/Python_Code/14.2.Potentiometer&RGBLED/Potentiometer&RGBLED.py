from microbit import *
display.off()
def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
def HSL_RGB(degree):
    degree=degree/360*255
    if degree < 85:
        red = 255 - degree * 3
        green = degree * 3
        blue = 0
    elif degree < 170:
        degree = degree - 85
        red = 0
        green = 255 - degree * 3
        blue = degree * 3
    else:
        degree = degree - 170
        red = degree * 3
        green = 0
        blue = 255 - degree * 3
    return red,green,blue
while True:
    value=map(pin3.read_analog(),0,1023,0,360)
    red,green,blue=HSL_RGB(value)
    red=map(red,0,255,1023,0)
    green=map(green,0,255,1023,0)
    blue=map(blue,0,255,1023,0)
    pin2.write_analog(red)
    pin1.write_analog(green)
    pin0.write_analog(blue)