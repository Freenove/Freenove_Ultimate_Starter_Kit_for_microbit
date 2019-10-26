from microbit import *
def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
while True:
    pin0.set_analog_period(20)
    for i in range(180):
        pin0.write_analog(map(i,0,180,25.6,128))
        sleep(5)
    for i in range(180,0,-1):
        pin0.write_analog(map(i,0,180,25.6,128))
        sleep(5)