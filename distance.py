import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigger = 22
echo = 27

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

while True:
    GPIO.output(trigger, True)
    time.sleep(0.0000005)
    GPIO.output(trigger, False)

    start = time.time()
    stop = time.time()

# save StartTime
    while GPIO.input(echo) == 0:
        start = time.time()

# save time of arrival
    try:
        while GPIO.input(echo) == 1:
            stop = time.time()

        cas = stop - start
        print(cas)
        distance = cas*343/2
        print(distance)
        time.sleep(1)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
