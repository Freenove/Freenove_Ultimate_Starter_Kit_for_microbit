from microbit import *
number =[0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90]
LSBFIRST=1
MSBFIRST=2
#define the pins connect to 74HC595
dataPin=pin0 #DS Pin of 74HC595(Pin14)
latchPin=pin1 #ST_CP Pin of 74HC595(Pin12)
clockPin=pin2 #SH_CP Pin of 74HC595(Pin11)
def shiftOut(value,dPin,cPin,order):
    for i in range (8):
        cPin.write_digital(0)
        if order==MSBFIRST:
            flag=value<<i & 0x80
            if flag==0x80:
                dPin.write_digital(1)
            else:
                dPin.write_digital(0)
        else:
            flag=value>>i & 0x01
            if flag==0x01:
                dPin.write_digital(1)
            else:
                dPin.write_digital(0)
        cPin.write_digital(1)
while True:
    for Num in number:
        latchPin.write_digital(0)
        shiftOut(Num,dataPin,clockPin,MSBFIRST)
        latchPin.write_digital(1)
        sleep(500)