#!/usr/bin/python3
from gpiozero import DistanceSensor
from os import system
import os
import signal
import time
from time import sleep

def on():
    system("/home/pi/bin/on")
    sleep(10)

def off():
    system("/home/pi/bin/off")

def Run(signum, frame): #handler musí příjmat 2 argumenty (číslo signálu a frame (odkud se volá))
    '''switch dle casu'''
    t = time.asctime(time.localtime(time.time())).split(' ')
    try: # někdy je mezera navíc, 1.-9.
        t = t.remove('')
    except ValueError:
        pass
    t = t[3]
    if t >= '22:00:00' or t < '07:00:00':
        off()
        sensor.when_in_range = None
        sensor.when_out_of_range = None
    elif t >= '07:00:00' and t <= '09:00:00':
        on()
        sensor.when_in_range = None
        sensor.when_out_of_range = None
    else:
        off()
        sensor.when_in_range = on
        sensor.when_out_of_range =  off
    signal.pause()

with open("/tmp/alojz.pid", "w", encoding="UTF-8") as f:
    f.write(str(os.getpid()))
run = 0.6
sensor = DistanceSensor(echo=24, trigger=23, max_distance=2, threshold_distance=run, queue_len=5)
signal.signal(signal.SIGALRM, Run)
Run(14, None)
