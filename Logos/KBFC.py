#Drawing Kerala Blasters Logo Using Python Turtle
from turtle import *
pencolor('#F4E84E')
bgcolor('black')
penup()
forward(267)
pendown()
left(90)
pensize(19)
fillcolor("#013CA6")
begin_fill()
forward(350)
left(90)
forward(535)
left(90)
forward(430)
left(15)
circle(390,58)
left(32)
circle(390,58)
left(17)
forward(100)
end_fill()
penup()
home()
back(5)
pendown()
left(90)
pensize(1)
pencolor("#092F87")
fillcolor('#092F87')
begin_fill()
forward(340)
left(90)
forward(252)
left(90)
forward(420)
left(15)
circle(377,57.5)
left(107.5)
forward(400)
left(32)
forward(250)
pencolor('white')
write("KERALA", font=("Verdana",
                                    45, "bold"))
end_fill()
penup()
left(97)
forward(145)
pendown()
pencolor('yellow')
write("BLASTERS", font=("Verdana",
                                    65, "bold"))              
penup()
home()
back(5)
right(90)
forward(100)
pendown()
screen = Screen()
screen.addshape("kd.gif")    
shape("kd.gif")
done()           #Subscribe To CodeGrahHHHH.