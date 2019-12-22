from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=22, trigger=27)
while True:
    print(sensor.distance)
    sleep(1)