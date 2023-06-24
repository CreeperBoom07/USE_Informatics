"""
В невыраженном треугольнике сумма углов 180 градусов.
"""


def polygon(a, b, c):
    return a + b + c == 180


def f(x):
    return polygon(37, a, x + 45) == polygon(a, x, 90) and not (a + 23 < 120)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 98
