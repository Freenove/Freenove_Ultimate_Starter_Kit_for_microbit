from microbit import *
while True:
    ADC = pin0.read_analog()
    voltage = ADC/1023*3.3
    print("convertvalue: "+str(ADC)+" voltage: "+str(voltage))
    sleep(1000)
