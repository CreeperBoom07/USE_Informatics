from turtle import *


def sq(a):
    for i in range(4):
        color(colors[i])
        forward(a)  # Движение вперёд на 100 пикселей
        left(90)


colors = ['red', 'brown', 'green', 'blue']

# joe.color('red')
speed(10000)  # Скорость

dlina = 30
for i in range(60):
    #color(colors[i % 4])
    sq(dlina)
    # circle(dlina)
    right(10)
    dlina += 4
done()
