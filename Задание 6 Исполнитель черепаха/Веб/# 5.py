from turtle import *
tracer(0)
r = 5
screensize(10000, 10000)
for i in range(10):
    for j in range(3):
        fd(10*r)
        rt(90)
        fd(10*r)
        rt(270)
    rt(90)

    
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'blue')
down()

update()
