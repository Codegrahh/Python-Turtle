from turtle import *    #Subscribe To CodeGrahHHHH.
turtlesize(5)

#Function for right curve
def curve01(a,d):
    for i in range(d):
        right(a)
        forward(1)
#Function for left curve
def curve02(a,d):
    for i in range(d):
        left(a)
        forward(1)

penup()
forward(179)
pendown()
pensize(4)
left(87)
fillcolor("#DCB579")
begin_fill()
curve02(0.15,20)
right(5)
curve01(0.15,135)
left(45)
forward(84)
left(115 )
forward(35)
right(127)
forward(97)
left(53)
curve02(0.4,60)
curve02(0.8,40)
right(8)
curve02(0.2,43)
left(35)
forward(30)
right(130)
curve01(0.28,100)
left(95)
forward(40)
left(12)
curve02(0.2,84)
left(45)
curve02(0.2,160)
right(180)
curve01(0.2,65)
left(39)
forward(36)
left(110)
curve01(0.3,60)
left(40)
curve02(0.15,100)
curve02(0.1,80)
curve01(0.3,45)
curve02(0.5,100)
curve02(0.3,137)
right(6)
curve02(0.19,90)
curve02(0.41,120)
curve02(0.75,40)
end_fill()

#eyes
left(90)
penup()
forward(65)
pendown()
right(95)
#eye
fillcolor("black")
begin_fill()
curve02(1.2,60)
curve02(1.9,65)
curve02(1.2,55)
curve02(2,60)
end_fill()

pencolor('white')
left(36)
penup()
forward(36)
pendown()
dot(25)

penup()
left(27.5)
forward(184)
left(29)
pendown()
pencolor("black")

fillcolor("black")
begin_fill()
curve02(1.2,60)
curve02(1.9,65)
curve02(1.2,55)
curve02(2,60)
end_fill()

pencolor('white')
left(110)
penup()
forward(35)
pendown()
dot(25)

pencolor("black")
penup()
right(36)
forward(90)
pendown()
left(25)
circle(50,70)
hideturtle()
done()                 #Subscribe To CodeGrahHHHH.