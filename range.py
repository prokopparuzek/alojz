from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=2, queue_len=5)
while True:
    print(sensor.distance*100)
    sleep(1)
