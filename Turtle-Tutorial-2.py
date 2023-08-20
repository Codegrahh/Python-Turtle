#Turtle Graphics Tutorial Code Part 2
import turtle
t=turtle.Turtle()

#8 bgpic function
turtle.bgpic("back.png")

#1. Speed function
t.speed(5)

#9. shape function
t.shape("circle")
#setting position - don't know about this function check out previous video
t.penup()
t.right(90)
t.forward(150)
t.left(90)
t.pendown()

#6. fillcolor,begin_fill and end_fill
t.fillcolor("yellow")
t.begin_fill()
#3. Circle Function
t.circle(250)
t.end_fill()

t.penup()
t.left(130)
t.forward(200)
t.right(190)
t.pendown()

#3.5 pensize function
t.pensize(5)


t.circle(140,130)

t.penup()
t.left(30)
t.forward(180)
t.pendown()
#4. dot function
t.dot(80)

t.penup()
t.left(85)
t.forward(180)
t.pendown()

t.dot(80)

#5 pencolor
t.pencolor("red")

t.penup()
t.left(120)
t.forward(150)
t.pendown()
t.dot(30)

#7 bgcolor
turtle.bgcolor("blue")

t.hideturtle()

#2. Done function
turtle.done()             #Subscribe To CodeGrahHHHH.