#Drawing Fan Animation In Python Turtle
from turtle import*
pensize(10)
home()
begin_poly()
left(90)
fd(100)
end_poly()
p = get_poly()
register_shape("myFavouriteShape", p)
shape('myFavouriteShape')
pensize(20)
right(300000)
done()                 #Subscribe To CodeGrahHHHH. 