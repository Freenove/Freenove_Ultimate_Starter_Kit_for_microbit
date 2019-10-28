from microbit import *
from I2C_LCD1602_Class import *
display.off()
group=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Pin_row = [pin9, pin6, pin10, pin4]
Pin_column = [pin3, pin2, pin1, pin0]
lcd = I2C_LCD1602(0x27)
lcd.clear()
number=0
for i in range(4):
       Pin_row[i].write_digital(0)
for i in range(4):
       Pin_column[i].write_digital(0)
while True:
    for i in range(4):
       Pin_row[i].write_digital(1)
       for j in range(3):
           if Pin_column[j].read_digital()==1:
               sleep(100)
               if Pin_column[j].read_digital()==1:
                   if i==3 and j==0:     #Press the "*" button
                       number=0
                       lcd.clear()
                   elif i==3 and j==1:   #Press the "0" button
                        number=number*10
                   elif i==3 and j==2:   #Press the "#" button
                       while True:
                           lcd.clear()
                           lcd.puts(str(number), 0, 0)
                           number-=1
                           sleep(1000)
                           if pin3.read_digital()==1 or number==0:
                               number=0
                               lcd.clear()
                               break
                   else:                 #Press the number button
                       number=number*10+group[i][j]
                   lcd.puts(str(number), 0, 0)
       Pin_row[i].write_digital(0)