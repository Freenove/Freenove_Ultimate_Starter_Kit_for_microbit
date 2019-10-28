from microbit import *
compass.calibrate()
while True:
    azimuth = compass.heading()
    if azimuth<22.5 and azimuth<67.5:
        display.show(Image.ARROW_NW)
    elif azimuth<67.5 and azimuth<112.5:
        display.show(Image.ARROW_W)
    elif azimuth<112.5 and azimuth<157.5:
        display.show(Image.ARROW_SW)
    elif azimuth<157.5 and azimuth<202.5:
        display.show(Image.ARROW_S)
    elif azimuth<202.5 and azimuth<247.5:
        display.show(Image.ARROW_SE)
    elif azimuth<247.5 and azimuth<292.5:
        display.show(Image.ARROW_E)
    elif azimuth<292.5 and azimuth<337.5:
        display.show(Image.ARROW_NE)
    elif azimuth<22.5 or azimuth>337.5:
        display.show(Image.ARROW_N)