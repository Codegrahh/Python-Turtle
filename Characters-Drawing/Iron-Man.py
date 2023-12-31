#Draw Iron-Man In Python Turtle
from turtle import *
tracer(10)
# function for curve
def curve01(a,d):
    for i in range(d):
          right(a)
          forward(1)
def curve02(a,d):
    for i in range(d):
        left(a)
        forward(1)
penup()
backward(20)
pendown()
#Making Helmet  --------------------
fillcolor('red')
begin_fill()
pensize(7)
forward(70)
left(51)
forward(88)
left(35)
forward(185)
curve02(0.6,100)
curve02(0.5,100)
curve02(0.5,50)
curve02(0.7,80)
forward(190)
left(28)
forward(83)
end_fill()
#face
penup()
left(156)
forward(305)
right(75)
pensize(5)
pendown()
fillcolor('#b97d10')
begin_fill()
curve01(0.10,60)
right(97)
forward(70)
left(79)
forward(48)
left(80)
forward(65)
right(100)
curve01(0.10,60)
right(70)
forward(100)
left(15)
forward(45)
right(60)
pensize(3)
curve02(0.3,136)
right(83.5)
forward(56)
right(77)
curve02(0.25,137)
pensize(5)
right(55)
forward(40)
left(16)
forward(105)
end_fill()
penup()
right(172)
forward(270)
right(68)
pendown()
fillcolor('#b97d10')
begin_fill()
pensize(3)
forward(16)
right(85)
forward(25)
right(48)
curve02(0.51,105)
right(60)
forward(15)
right(124)
curve01(0.22,137)
end_fill()
penup()
right(160)
forward(118)
right(27)
pendown()
pensize(7)
forward(20)
penup()
right(140)
forward(175.01)
right(5)
pendown()
fillcolor('#b97d10')
begin_fill()
pensize(3)
forward(13)
left(95)
forward(20)
left(50)
curve01(0.5,112)
left(45)
forward(17)
left(134)
curve02(0.3,142)
end_fill()
penup()
left(155)
forward(120)
pensize(7)
pendown()
left(34)
forward(22)
penup()
pensize(3)
left(140)
forward(205)
right(170)
pendown()
forward(20)
right(60)
forward(51)
right(65)
forward(20)
backward(20)
left(145)
forward(20)
backward(20)
penup()
left(100)
forward(50)
right(80)
pendown()
forward(21)
penup()
left(33)
forward(44)
right(180)
pendown()
pensize(5)
penup()
forward(3)
pendown()
forward(17)
left(105)
pensize(4)
forward(15)
right(60)
forward(3)
pensize(10)
forward(67)
pensize(5)
forward(3)
right(54)
forward(13)
left(105)
pensize(4)
forward(16.5)
penup()
left(5)
forward(76)
pendown()
pensize(4)
#Making Ears
fillcolor("red")
begin_fill()
forward(14)
left(30)
forward(63)
left(40)
forward(14)
left(140)
forward(85)
end_fill()
penup()
right(83.5)
forward(188)
right(50)

#second ear
fillcolor('red')
begin_fill()
pendown()
forward(17)
right(35)
forward(64)
right(50)
forward(12)
right(130)
forward(84)
end_fill()
penup()
left(165)
forward(67)
right(100)
pendown()
curve02(0.18,80)
left(2)
curve02(0.35,92)
right(178)
penup()
forward(9.5)
pendown()
left(50)
pensize(7)

#first eye
fillcolor('white')
begin_fill()
forward(27)
right(68)
curve01(0.4,49)
right(75)
forward(11)
right(87)
pensize(4)
curve02(0.19,60)
end_fill()

#second eye
right(195.5)
penup()
forward(104)
left(80)
pensize(7)
pendown()
fillcolor('white')
begin_fill()
forward(15)
right(82)
curve01(0.4,48)
right(65)
forward(25.5)
right(70)
right(52)
pensize(5)
curve02(0.2,60)
end_fill()
penup()
right(108)
forward(140)
right(55)
pendown()
fillcolor('red')
begin_fill()
pensize(7)
forward(70)
left(27)
forward(100)
left(55)
forward(282)
left(17)
forward(180)
left(70)
forward(355)
left(90)
forward(52)
right(15.5)
forward(135)
left(17)
forward(289)
left(55)
forward(92)
left(25)
forward(75)
left(62)
forward(73)
right(50.5)
forward(68)
right(55.5)
forward(75)
end_fill()

#body
left(145)
forward(82)
left(56)
forward(65)
left(33)
forward(45)
left(38)
forward(65)
left(50)
forward(74)
penup()
right(82)
forward(10)
right(88)
pendown()
forward(70)
right(40)
curve01(0.3,115)   
left(65)
forward(35)
right(90)
forward(19)
right(90)
forward(30)
left(70)
curve01(0.3,115)
right(40)
forward(70)
#shoulders
penup()
left(119.5)
forward(158)
right(40)
pendown()
fillcolor('red')
begin_fill()
curve02(0.45,210)
left(4)
forward(57)
left(91)
forward(22)
left(72)
forward(35)
right(68)
forward(38)
right(90)
curve02(0.8,120)
forward(25)
left(87.5)
forward(200)
end_fill()
penup()
left(150)
forward(138)
pendown()
fillcolor('#b97d10')
begin_fill()
circle(30)
end_fill()
penup()
left(85)
forward(317)
pendown()
fillcolor('white')
begin_fill()
circle(70)
end_fill()
penup()
left(83.5)
forward(400)
pendown()
fillcolor('red')
begin_fill()
right(34)
curve01(0.4,270)
right(88)
forward(24)
right(60)
forward(30)
left(60.5)
forward(40)
left(90)
curve01(0.8,140)
right(66)
forward(190)
end_fill()
penup()
right(172)
forward(142)
pendown()
fillcolor('#b97d10')
begin_fill()
circle(25)
end_fill()
done()              #Subscribe To CodeGrahHHHH.