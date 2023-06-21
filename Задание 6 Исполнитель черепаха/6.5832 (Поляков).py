from turtle import *
color('black', 'red')
#tracer(False)
speed(1)
m = 100
begin_fill()
up()
for i in range(2):
    left(120)
    down()

    for j in range(10):
        right(30)
        forward(4*m)
        right(60)

    up()
    left(150)
    backward(2*m)
    left(90)
    backward(2*m)
end_fill()
canvas = getcanvas()
for x in range(-100*m, 100*m, m):
    for y in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)

#update()
done()