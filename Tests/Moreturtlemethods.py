import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist=5
tess.up()
for _ in range(30):
    tess.stamp()
    tess.forward(dist)
    tess.right(24) 
    dist+=2
wn.exitonclick()