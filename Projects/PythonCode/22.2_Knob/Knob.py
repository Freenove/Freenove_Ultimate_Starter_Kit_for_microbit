from microbit import *
def map(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
while True:
    value=pin0.read_analog()
    pin1.set_analog_period(20)
    pin1.write_analog(map(value,0,1023,25.6,128))