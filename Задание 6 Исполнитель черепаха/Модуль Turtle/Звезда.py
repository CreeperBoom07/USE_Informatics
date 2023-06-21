import turtle, time
from turtle import done

joe = turtle.Turtle()



def star_fill(n, dlina):
    joe.begin_fill()
    star(n, dlina)
    joe.end_fill()

def star(n, dlina):
    if n % 2:
        for i in range(n):
            joe.forward(dlina)
            angle = n // 2 * 360 / n
            joe.left(angle)


for i in range(5, 16, 2):
    joe.speed(100)
    star_fill(i, 150)
    time.sleep(2)
    joe.reset()
done()
