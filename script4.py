from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
pensize(3)

h = 0

def color_random():
    global h
    color(hsv_to_rgb(h, 1, 1))
    h += 0.02

def linea(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# V
color_random()
linea(-300, 100, -280, -100)
linea(-260, 100, -280, -100)

# I
color_random()
linea(-240, 100, -240, -100)

# C
color_random()
linea(-200, 100, -160, 100)
linea(-200, 100, -200, -100)
linea(-200, -100, -160, -100)

# E
color_random()
linea(-140, 100, -140, -100)
linea(-140, 100, -100, 100)
linea(-140, 0, -110, 0)
linea(-140, -100, -100, -100)

# N
color_random()
linea(-80, -100, -80, 100)
linea(-80, 100, -40, -100)
linea(-40, -100, -40, 100)

# T
color_random()
linea(0, 100, 60, 100)
linea(30, 100, 30, -100)

# E
color_random()
linea(100, 100, 100, -100)
linea(100, 100, 140, 100)
linea(100, 0, 130, 0)
linea(100, -100, 140, -100)

hideturtle()
done()
