from turtle import *
left(90)
tracer(False)
forward(20*30)

setposition(0, 0)
right(90)
forward(20*30)
setposition(0, 0)
left(90)
for i in range(4):
    forward(8*30)
    right(150)
    forward(8*30)
    right(30)
up()

for x in range(-11, 11):
    for y in range(-11, 11):
        goto(x*30, y*30)  # Перемещает
        dot(5)
update()
done()