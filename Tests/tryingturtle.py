import turtle
wn=turtle.Screen()
t=turtle.Turtle()
t.speed(10)
t._delay(0)
dist=1
nbr_of_edges=360
angle=360

t._tracer(0,0)
for _ in range(5):
    for _ in range(100):

        for _ in range(360):

             t.forward(dist)
             t.left(angle/nbr_of_edges)

        t.left(10)
    dist+=0.25

t._update()


wn.exitonclick()