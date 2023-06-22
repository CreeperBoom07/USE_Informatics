"""Задача с минимальным А"""
p: set = {1, 3, 5, 7, 9, 11}  # Первое множество
q: set = {3, 6, 9, 12}
a: set[int] = set()


def f(x: int) -> bool:
    return ((x in p) <= (x not in q)) or (x in a)


for x in range(1, 1000):
    if not f(x):  # Если функция ложна
        a.add(x)
print(a)

# {9, 3}
