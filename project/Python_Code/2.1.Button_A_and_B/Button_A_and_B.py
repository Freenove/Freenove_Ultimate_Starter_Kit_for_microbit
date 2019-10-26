from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.YES)
    elif button_a.is_pressed():
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        display.show(Image.ARROW_E)
    else:
        display.show(Image.NO)