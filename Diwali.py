#Drawing Diwali Animation In Python Turtle
from turtle import *
import time
window=Screen()
carver=Turtle()
#function for curve
def curve01(a,d):
    for i in range(d):
        right(a)
        fd(1)
def curve02(a,d):
    for i in range(d):
        left(a)
        fd(1)
pensize(10)
penup()
setposition(-800,-327)
pendown()
forward(820)

#Making diya
left(150)
fillcolor("black")
begin_fill()
curve01(0.25,225)
right(124)
curve02(0.37,275)
right(142)
curve02(0.37,275)
right(125)
curve01(0.25,225)
left(150)
forward(520)
right(90)
forward(100)
right(90)
forward(1800)
right(90)
forward(90)
end_fill()

#function for drawing stars
def star(a):
 for i in range(12):
  forward(a)
  back(a)
  right(30)
penup()
home()
left(30)
forward(500)
pendown()

#Making Stars using star function
star(100)
penup()
right(90)
forward(200)
pendown()
star(50)
penup()
right(110)
forward(200)
pendown()
star(30)
penup()
forward(400)
pendown()
star(80)
right(90)
penup()
forward(250)
pendown()
star(60)
penup()
right(60)
forward(200)
pendown()
star(50)
penup()
left(160)
forward(750)
pendown()
pencolor("red")
write("HAPPY ",font=("Verdana",80, "normal"))
left(30)
penup()
forward(150)
pendown()
write("DIWALI",font=("Verdana",100, "bold"))
pencolor("yellow")
left(128)
penup()
forward(880)
pendown()
left(25)

#Function of color
def carve_pumpkin(colour,sd):
    carver.color(colour)
    bgcolor(sd)


# recording a fire flame
begin_poly()
curve02(0.4,200)
curve02(0.18,190)
left(90)
curve02(0.18,190)
curve02(0.4,200)
end_poly()
pairs = get_poly()
register_shape("new_shape", pairs)
carver.shape("new_shape")
carver.left(90)
carve_pumpkin("skyblue","blue")

#Loop For changing colors
start = time.time()
count = 0
colours = "yellow", "black"
bg="white","yellow"
while True:
   if time.time() - start > 1:
        carve_pumpkin(colours[count % 2],bg[count%2])
        window.update()
        count += 1
        start = time.time() 
done()              #Subscribe To CodeGrahHHHH. 