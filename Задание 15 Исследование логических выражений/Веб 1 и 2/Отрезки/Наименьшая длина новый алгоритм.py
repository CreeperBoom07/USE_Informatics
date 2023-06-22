from itertools import *


def f(x):
    P = 25 <= x <= 50
    Q = 54 <= x <= 75
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))


# Перебираем числа от 24 до 76 с шагом 0.25
Ox = [i/4 for i in range(24*4, (76*4)+1)]
m = []

# Перебираем все возможные отрезки
# 2 - пары
for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        m.append(a2-a1)  # Добавляем длину подходящего списка

print(min(m))

# 21
