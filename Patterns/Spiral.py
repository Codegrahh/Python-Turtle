#Draw Spiral In Python Turtle
from turtle import *
import colorsys
tracer(7)
bgcolor('black')

colors = 360

for x in range(1000):
    hue = x / colors
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(r, g, b)
    width(x / 1 + 1)
    forward(x)
    left(59)

done()              #Subscribe To CodeGrahHHHH.