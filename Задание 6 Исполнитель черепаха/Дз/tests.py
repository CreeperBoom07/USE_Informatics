from turtle import *
tracer(0)
r = 25
lt(90)

fd(9*r)
rt(90)
for i in range(2):
    fd(3*r)
    rt(90)
    fd(3*r)
    rt(270)
for j in range(2):
    fd(3*r)
    rt(90)
fd(9*r)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*r, y*r)
        dot(3, 'blue')
update()
done()
