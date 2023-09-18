from turtle import *
tracer(0)
m = 25
screensize(10000, 10000)
lt(90)

up()
goto(xcor() + 5*m, ycor() + 5*m)
down()
for i in range(20):
    goto(xcor() - 5*m, ycor() - 5*m)
    goto(xcor() - 0*m, ycor() + 5*m)

goto(xcor() - 0*m, ycor() - 5*m)

for i in range(20):
    goto(xcor() + 5*m, ycor() - 0*m)
    
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'blue')
update()
done()
