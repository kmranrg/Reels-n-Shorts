# importing the library
from turtle import *

# setting up the pen speed
speed(2)

# changing the screen color (background)
bgcolor("black")
penup()

# let's change the pen position
goto(-50,60)
pendown()
color("#00adef")
begin_fill()

# position change
goto(100,100)
goto(100,-100)
goto(-50,-60)
goto(-50,60)
end_fill()

# making the plus part
color("black")
goto(15,100)
color("black")
width(10)
goto(15,-100)
penup()
goto(100,0)
pendown()
goto(-100,0)
done()