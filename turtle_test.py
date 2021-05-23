#!/usr/bin/env python3

import turtle

pat = turtle.Turtle()

for i in range(6):
    for i in range(2):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
    pat.right(60)