from microbit import *
from I2C_LCD1602_Class import *
from time import sleep_us,ticks_us
def getdistance():
    distance=0
    pin1.write_digital(1)
    sleep_us(15)
    pin1.write_digital(0)
    while pin0.read_digital() == 0:
        pass
    if pin0.read_digital() == 1:
        ts = ticks_us()
        while pin0.read_digital() == 1:
            pass
        te = ticks_us()
        tc = te - ts
        print(te,ts)
        distance = (tc*170)*0.0001
    return distance

lcd = I2C_LCD1602(0x27)
while True:
  distance=round(getdistance())
  lcd.clear()
  lcd.puts("Distance is:",0,0)
  lcd.puts(str(distance),12,0)
  sleep(1000)