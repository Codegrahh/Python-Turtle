#Learn to Control Turtle Movements
import turtle
def func(x, y):
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.ondrag(func)
turtle.speed(10)
sc = turtle.Screen()
sc.setup(600, 600)
turtle.ondrag(func)
sc.mainloop()          #Subscribe To CodeGrahHHHH.