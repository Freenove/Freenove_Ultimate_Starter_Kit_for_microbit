from microbit import *
from I2C_LCD1602_Class import *
lcd = I2C_LCD1602(0x27)
while True:
    lcd.puts("temperature:"+str(temperature()), 0, 0)