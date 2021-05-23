#!/usr/bin/env python3

from gpiozero import LED, Button
from time import sleep
import random

blue_led = LED(2)
blue_button = Button(3)
green_led = LED(17)
green_button = Button(27)
red_led = LED(10)
red_button = Button(9)
yellow_led = LED(5)
yellow_button = Button(6)
white_led = LED(19)
white_button = Button(26)

led_list = [2,17,10,5,19]
button_list = [3,27,9,6,26]

print("Welcome to Simon!\n\nWatch the pattern of lights, then press the buttons in the order they lit up!")

#section for lighting up the leds
current_led = random.choice(led_list)
LED(current_led).on()
sleep(1)
LED(current_led).off()

#section for the button pressing for input

#section to check, then put on a light show if successful