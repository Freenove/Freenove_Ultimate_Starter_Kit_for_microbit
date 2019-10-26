from microbit import *
circle = Image("09900:"
               "90090:"
               "90090:"
               "90090:"
               "09900")
while True:
    xVal = pin2.read_analog()
    yVal = pin1.read_analog()
    zVal = pin0.read_digital()
    if zVal == 0:
        display.clear()
        display.show(circle)
    elif xVal <450  and yVal < 650 and yVal >450:
        display.clear()
        display.show(Image.ARROW_N)
    elif xVal >650  and yVal < 650 and yVal >450:
        display.clear()
        display.show(Image.ARROW_S)
    elif yVal >650  and xVal < 650 and xVal >450:
        display.clear()
        display.show(Image.ARROW_W)
    elif yVal < 450  and xVal < 650 and xVal >450:
        display.clear()
        display.show(Image.ARROW_E)
    elif xVal <450  and yVal > 650:
        display.clear()
        display.show(Image.ARROW_NW)
    elif xVal <450  and yVal < 450:
        display.clear()
        display.show(Image.ARROW_NE)
    elif xVal > 650  and yVal > 650:
        display.clear()
        display.show(Image.ARROW_SW)
    elif xVal > 650  and yVal < 450:
        display.clear()
        display.show(Image.ARROW_SE)
    else:
        display.clear()