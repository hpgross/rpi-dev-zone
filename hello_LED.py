#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

led = LED(25)
count = 25

while count > 0:
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.8)
    count -= 1