# importing the turtle library
import turtle as t

# declaring the background color
t.bgcolor('black')

# setting up the pen size 
t.pensize(2)

# setting up  the speed of the turtle variable
t.speed(10)

# defining the color palette
colors = ['red','magenta','blue',
        'cyan','green','white','yellow']

# logic
for i in range(6):
    for color in colors:
        t.color(color)
        t.circle(100)
        t.left(10)
    t.hideturtle()
