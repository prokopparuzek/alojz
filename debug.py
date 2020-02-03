from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=2, queue_len=5)

while True:
    print(sensor.distance)
    sleep(1)
