#Drawing Illusion Animation In Python Turtle
from turtle import *
tracer(10)
t=Turtle()
hideturtle()
speed(0)
pensize(2)
bgcolor("black")
for i in range(10000):
 for colours in ("white" , "black" , ) :
   color(colours)
   right(3)
   circle(i)
   right(30) 
   forward(0.5)
done()            #Subscribe To CodeGrahHHHH. 