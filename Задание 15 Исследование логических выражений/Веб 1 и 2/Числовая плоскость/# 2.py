"""Целые положительные числа - [1; +беск.]
   Целые неотрицательные числа - [0; +беск.]"""


def f(a, x, y):
    return (y + 3*x < a) or (x > 20) or (y > 40)


def generator_loops():
    for x in range(1, 1000):
        for y in range(1, 1000):
            yield x, y


for a in range(1, 10000):
    for x, y in generator_loops():
        if not f(a, x, y):
            break
    else:
        print(a)
        break

# Вариант 2
for a in range(1, 1000):
    if all(f(a, x, y) for y in range(1, 100) for x in range(1, 100)):
        print(a)
        break

# 101
