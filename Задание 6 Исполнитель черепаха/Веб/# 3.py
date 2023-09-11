from turtle import *

tracer(0)
r = 25  # масштаб 

for i in range(7):
     rt(90)
     fd(4*r)  # Всё, что связано с движением умножаем на масштаб
     for j in range(2):
         lt(90)
         fd(4*r)
# Рисуем сетку         
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*r, y*r) # Переместиться на эти координаты
        dot(3, 'blue') # Точка
update()
done()
