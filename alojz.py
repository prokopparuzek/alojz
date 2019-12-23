#!/usr/bin/python3
from gpiozero import DistanceSensor
from os import system
import signal
import time
from time import sleep

def on():
    system("/home/pi/bin/on")
    sleep(10)

def off():
    system("/home/pi/bin/off")

def Wake(when, plus):
    '''vzbud mne'''
    s = time.asctime(time.localtime(time.time() + plus)).split(' ')
    s[3] = when
    stop = time.mktime(time.strptime(' '.join(s)))
    delta = stop-time.time()
    signal.alarm(int(delta))
    signal.pause()

def Run(signum, frame): #handler musí příjmat 2 argumenty (číslo signálu a frame (odkudse volá))
    '''switch dle casu'''
    t = time.asctime(time.localtime(time.time())).split(' ')[3]
    if t >= '22:00:00' or t < '07:00:00':
        off()
        sensor.when_in_range = None
        sensor.when_out_of_range = None
        Wake('07:00:00', 36000)
    elif t >= '07:00:00' and t <= '09:00:00':
        on()
        sensor.when_in_range = None
        sensor.when_out_of_range = None
        Wake('09:00:00', 0)
    else:
        off()
        sensor.when_in_range = on
        sensor.when_out_of_range =  off
        Wake('22:00:00', 0)

run = 0.7
sensor = DistanceSensor(echo=24, trigger=23, max_distance=2, threshold_distance=run, queue_len=5)
signal.signal(signal.SIGALRM, Run)
Run(14, None)
