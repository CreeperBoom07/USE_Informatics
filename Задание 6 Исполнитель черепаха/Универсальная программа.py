from turtle import *

color('black', 'red') # Цвет: black - контур, red - заливка
#tracer(False)  # Убирает анимацию
m = 100 # Масштаб. Увеличение фигуры в сто раз
speed(0) # Скорость движения

begin_fill() # Начало заливки. Первая фигура
right(90)
#up()
#setposition(100, 100)
#down()
for i in range(4): #
    forward(8*m)
    right(90)
end_fill()

begin_fill() # Вторая фигура
for i in range(3):
    forward(12*m)
    right(120)
end_fill()



canvas = getcanvas()
cnt = 0
for y in range(-100*m, 100*m, m): # Важно, чтобы диапазон перибора был больше чем размер  фигуры
    for x in range(-100*m, 100*m, m):
        item = canvas.find_overlapping(x, y, x, y) # Список пересечения прямоугольника с заданной фигурой
        # find_overlapping(аргумент 1,2 - левый нижний угол; аргумент 3, 4 - правый верхний угол)
        # Т.е строим прямоугольник в виде точки
        if len(item) == 1 and item[0] == 5: # Если есть одно пересечение и лежим на красной заливке (5)
            print(item)
            cnt += 1
print(cnt)
#update()
done()
exit()