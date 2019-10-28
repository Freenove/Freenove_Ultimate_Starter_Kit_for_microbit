from microbit import *
from DHT11_RW import *
if __name__ == '__main__':
    sensor = DHT11(pin0)
    while True:
        try:
            temperature , humidity = sensor.read()
            print("temperature:"+str(temperature)+" C")
            print("humidity:"+str(humidity)+"%")
        except Exception as e:
            print("Error : " + str(e))
        time.sleep(1)