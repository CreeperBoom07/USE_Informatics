"""
Всегда увеличивай диапазоны для x, y ..., чтобы проверить ответ
"""


def f(a, x, y, z):
    return (220 != y + 2*x + z) or (a < 6*x) or (a < y) or (a < 2*z)


for a in range(1000):
    if all(f(a, x, y, z) for z in range(150) for y in range(150) for x in range(150)):
        print(a)


# 145
