from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=2)
while True:
    print(sensor.distance*100)
    sleep(1)
