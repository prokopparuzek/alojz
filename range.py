from gpiozero import DistanceSensor, LED
from signal import pause

red = LED(14)
sensor = DistanceSensor(echo=24, trigger=23, max_distance=2, threshold_distance=0.6, queue_len=5)

sensor.when_in_range = red.on
sensor.when_out_of_range = red.off

pause()
