import turtle
from turtle import done
pen = turtle.Turtle()
pen.speed(10)
pen.up()  # Поднятьь перо
pen.setposition(-30, -3)  # Сместить позицию
pen.down()  # Опустить перо
def rightMNOG(n, dlina):
    sum_angle = (n - 2) * 180
    if sum_angle % n == 0:
        angle = sum_angle // n
        for i in range(n):
            pen.forward(dlina)
            pen.left(180 - angle)


for i in range(3, 11):
    rightMNOG(i, 50)
done() # Не закрываем программу после выполнения