#Draw Sharengan In Python Turtle
from turtle import *
begin_poly()
pencolor('red')
dot(750)
pencolor('black')
dot(500)
pencolor('red')
dot(475)
#Function For Curve01
def curve01(a,d):
 for i in range(d):
  right(a)
  forward(1)
def curve02(a,d):
 for i in range(d):
  left(a)
  forward(1)
pencolor('black')
#Function For Sharengan
def shr(n,p):
 right(n)
 penup()
 forward(230)
 pendown()
 right(p)
 fillcolor("black")
 begin_fill()
 curve02(1.3,200)
 right(125)
 curve01(1,60)
 left(160)
 curve02(0.85,180)
 end_fill()
#Calling Sharengan
shr(200,200)
penup()
home()
pendown()
#Calling Sharengan
shr(-15,200)
penup()
home()
pendown()
#Calling Sharengan
shr(90,200)
done()              #Subscribe To CodeGrahHHHH.