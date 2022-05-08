# importing the library
from turtle import *

# setting up the turtle graphics variables
t = Turtle()
s = Screen()

# defining the background color
s.bgcolor("black")

# defining the widht and the speed of turtle variable
t.width(3)
t.speed(0)

# making the color palette
colors = ['orange','white','green']

# logic
for i in range(300):
    t.pencolor(colors[i%3])
    t.forward(i*4)
    t.right(1201)
