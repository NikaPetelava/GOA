from turtle import *

speed(10)
width(5)
color("purple")

#draw a square
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#draw a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

#draw a roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 140)
pendown()

#draw a window
#left window
color("blue")
begin_fill()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(140, 140)
pendown()

#right window
begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()



exitonclick()

