from microbit import *
from I2C_LCD1602_Class import *
display.off()
group=[["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]
Pin_row = [pin9, pin6, pin10, pin4]
Pin_column = [pin3, pin2, pin1, pin0]
lcd = I2C_LCD1602(0x27)
lcd.clear()
for i in range(4):
       Pin_row[i].write_digital(0)
for i in range(4):
       Pin_column[i].write_digital(0)
while True:
    for i in range(4):
       Pin_row[i].write_digital(1)
       for j in range(4):
           if Pin_column[j].read_digital()==1:
               lcd.puts(group[i][j], 0, 0)
       Pin_row[i].write_digital(0)