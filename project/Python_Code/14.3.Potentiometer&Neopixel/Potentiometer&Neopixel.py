from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0, 8)
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
    return int(red),int(green),int(blue)
while True:

    for i in range(0, 8):
        value=pin1.read_analog()/1023*360+i*45
        if value > 360 :
            value = value-360
        red,green,blue=HSL_RGB(value)
        np[i] = (red,green,blue)
    np.show()