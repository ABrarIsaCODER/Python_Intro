import turtle
t  = turtle.Turtle()
t.shape("classic")
import datetime

minute = 45
hour = 2
second = 35 

t.penup()
t.goto(0,-180)
t.pendown()
t.color("blue")
t.circle(180)

t.color("red")

t.penup()
t.goto(0,0)
t.setheading(90) # Point to the top - 12 o' clock
t.right(hour*360/12)
t.pendown()
t.forward(100)

t.penup()
t.goto(0,0)
t.setheading(90) # Point to the top - 0 minute
t.right(minute*360/60)
t.pendown()
t.forward(150)

t.color("green")
t.penup()
t.goto(0,0)
t.setheading(90) # Point to the top - 0 second
t.right(second*360/60)
t.pendown()
t.forward(150)

t.getscreen().update()

