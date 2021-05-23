#!/usr/bin/env python3

from gpiozero import Buzzer, Button
from time import sleep

buzzer = Buzzer(15)
button = Button(2)

while True:
    button.wait_for_press()
    buzzer.on()
    sleep(3)
    buzzer.off()