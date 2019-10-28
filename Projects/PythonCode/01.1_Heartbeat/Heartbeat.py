from microbit import *
while True:
    display.show(Image.HEART)  # Display heartbeat pattern
    sleep(1000)                # Stop for 1 second
    display.show(Image.HEART_SMALL)
    sleep(1000)