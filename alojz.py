#!/usr/bin/python3
from gpiozero import DistanceSensor
from signal import pause
from os import system
from time import sleep

run = 0.7

def on():
    system("/home/pi/bin/on")
    sleep(10)
    if sensor.distance > run:
        system("/home/pi/bin/off")

def off():
    system("/home/pi/bin/off")


sensor = DistanceSensor(echo=24, trigger=23, max_distance=2, threshold_distance=run, queue_len=5)

sensor.when_in_range = on
sensor.when_out_of_range =  off

pause()
