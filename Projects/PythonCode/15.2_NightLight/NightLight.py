from microbit import *
while True:
   value = pin0.read_analog()
   if value>=400:
       pin1.write_digital(1)
   else:
       pin1.write_digital(0)