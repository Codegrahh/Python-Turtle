#Drawing Indian Logo In Python Turtle
from turtle import*
pencolor('white')
pensize(3)

bgcolor('#000080')

#allignments
penup()
forward(58)
left(90)
forward(75)
left(90)
pendown()

#function for curve
def curve01(a,d):
    for i in range(d):
        right(a)
        forward(1)

def curve02(a,d):
    for i in range(d):
        left(a)
        forward(1)

#ddddddddddddddd
begin_fill()
fillcolor('white')
forward(410)
curve01(2.5,75)
left(7.5)
forward(400)
left(90)
forward(18)
left(90)
forward(100)
curve01(2.9,65)
left(8)
forward(120)
curve01(3,30)
left(1.5)
forward(35)
left(89)
forward(265)
left(7.5)
curve01(2.5,75)
forward(265)
left(90)
forward(215)
curve01(3,30)
right(1)
forward(124)
curve01(3,30)
left(2.5)
forward(60)
curve01(0.29,100)
curve01(0.73,118)
left(115)
forward(20)
end_fill()


pencolor('#000080')
penup()
backward(50)
pendown()
right(1)
fillcolor('#000080')
begin_fill()
back(140)
left(90)
forward(83)
right(90)
forward(60)
curve01(0.6,70)
curve01(1,65)
end_fill()

pencolor('#FF9933')
penup()
right(165)
forward(400)
pendown()
fillcolor('#FF9933')
begin_fill()
right(90)
forward(10)
curve01(2.5,75)
left(9)
forward(175)
curve01(2.5,75)
left(7.5)
forward(171)
end_fill()



#iiiiiiiiiiiiiiiii
pencolor('#FF9933')
penup()
forward(100)
right(90)
forward(20)
pendown()
fillcolor('#FF9933')
begin_fill()
circle(25)
end_fill()



#nnnnnnnnnnnnnnnn
penup()
forward(57)
right(90)
forward(100)

pendown()
fillcolor("#FF9933")
begin_fill()
forward(175)
curve02(2.8,65)
right(1.5)
forward(158)
right(90)
curve01(0.55,40)
left(8)
curve01(0.6,50)
curve01(0.8,20)
curve01(2.7,15)
left(7)
forward(100)
curve02(0.5,50)
curve02(2,35)
right(12)
curve02(0.2,25)
curve02(2.72,70)
curve01(4,20)
curve01(2,15)
left(11)
forward(80)
curve02(0.5,190)
right(5)
curve02(0.2,48)
curve02(3,37)
end_fill()




#iiiiiiiiiiiiiiiii
pencolor('#138808')
penup()
left(65)
forward(387)
pendown()
fillcolor('#138808')
begin_fill()
right(92.5)
forward(183)
curve02(2.9,65)
right(8.5)
forward(183)
curve02(2.9,65)
end_fill()

penup()
back(120)
pendown()
right(15)
fillcolor('#138808')
begin_fill()
circle(25)
end_fill()

penup()
left(55)
forward(150)
pendown()





#AAAAAAAAAAAAAAAA
fillcolor('#138808')
begin_fill()
left(42)
forward(125)
curve01(5,18)
forward(200)
curve01(5,18)
curve01(0.23,80)
curve01(0.58,110)
curve01(0.1,112)
curve01(3,32)
left(10)
forward(98)
end_fill()
penup()
right(90)
forward(40)
pendown()
pencolor('#000080')
fillcolor("#000080")
begin_fill()
forward(145)
right(90)
curve01(0.7,140)
left(6)
forward(50)
right(88)
forward(80)
end_fill()
done()               #Subscribe To CodeGrahHHHH.