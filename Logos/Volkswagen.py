#Drawing VOLKSWAGEN LOGO Using Python Turtle
from turtle import*
#function for curve
def curve01(a,d):
 for i in range(d):
  right(a)
  forward(1)
def curve02(a,d):
 for i in range(d):
  left(a)
  forward(1)
bgcolor("black")
pencolor("#6091c3")    
turtlesize(5)
pensize(40)
penup()
goto(20,-332)
pendown()
circle(326)
end_fill()
left(90)
penup()
pensize(1)
forward(67)
pendown()
right(90)
fillcolor("#6091c3")
begin_fill()
curve02(0.2,65)
left(98)
forward(190)
left(138)
forward(190)
left(98)
curve02(0.2,70)
end_fill()
penup()
curve02(0.2,128)
pendown()
fillcolor("#6091c3")  
begin_fill()
curve02(0.23,370)
left(137.4)
fd(338)
end_fill()
right(69.5)
penup()
forward(249)
pendown()
fillcolor("#6091c3")
begin_fill()
right(69)
forward(335)
left(140)
curve02(0.22,362)
end_fill()
left(102)
penup()
forward(112)
pendown()
fillcolor("#6091c3")
begin_fill()
right(3)
forward(110)
right(69)
forward(105)
right(69)
forward(110)
left(138)
forward(306)
left(65)
curve02(0.12,88)
left(105)
forward(225)
right(69.5)
forward(108)
right(70)
forward(225)
left(105)
curve02(0.12,95)
left(64.8)
forward(301)
end_fill()
penup()
left(132)
forward(212)
pendown()
left(6.5)
fillcolor("#6091c3")
begin_fill()
forward(192)
left(98)
curve02(0.18,132)
left(98)
forward(192)
end_fill()
hideturtle()
done()           #Subscribe To CodeGrahHHHH.