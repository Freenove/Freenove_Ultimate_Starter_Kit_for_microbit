from microbit import *
while True:
    potentiometer=pin0.read_analog()
    if potentiometer<=411:
        pin2.write_digital(0)
        pin1.write_analog((411-potentiometer)/411*1023)
        pin1.set_analog_period(20)
    elif potentiometer>=612:
        pin1.write_digital(0)
        pin2.write_analog((potentiometer-612)/411*1023)
        pin2.set_analog_period(20)
    else:
        pin1.write_digital(1)
        pin2.write_digital(1)