#!/usr/bin/env python3

from gpiozero import LEDBoard, Button
from time import sleep
from random import choice
from sys import exit

#leds in order are blue, green, red, yellow, white
leds = LEDBoard(18,17,10,5,19)

blue = Button(3)
green = Button(27)
red = Button(9)
yellow = Button(6)
white = Button(26)

lights = []
inputs = []

def add_input(btn):
    inputs.append({
        blue:0,
        green:1,
        yellow:2,
        red:3,
        white:4,
    }[btn])

def lightshow():
    i = 0
    while i < 20:
        current_led = choice(list(range(1,5)))
        leds[current_led].on()
        sleep(0.1)
        leds[current_led].off()
        i += 1

print("Welcome to Simon!\n\nWatch the pattern of lights, then press the buttons in the order they lit up!")

num_lights = 1
while num_lights < 6:
    #section for lighting up the leds
    for past_light in lights:
        leds[past_light].on()
        sleep(1)
        leds[past_light].off()
        sleep(1)
    current_led = choice(list(range(5)))
    leds[current_led].on()
    sleep(1)
    leds[current_led].off()
    lights.append(current_led)

    #section for the button pressing for input
    while len(inputs) < len(lights):
        for button in (blue, green, red, yellow, white):
            button.when_pressed = add_input
    
    #checking for correct inputs
    if lights == inputs:
        num_lights += 1
        inputs = []
    else:
        print("You lose!")
        exit()

#section to check, then put on a light show if successful
if lights == inputs:
    lightshow()