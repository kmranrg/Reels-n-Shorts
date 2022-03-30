# importing the library
import turtle

# setting up the turtle screen title
turtle.title("Alien Planet Animation")

# intializing the Turtle graphics
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

# setting up the pen color
t.pencolor("green")

# logic
x = 0
y = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(x)
    t.right(y)
    x += 3
    y += 1
    if y == 210:
        break
    t.hideturtle()

turtle.done()