from itertools import product as pd

# from pprint import pprint
"""
Пусть P - множество всех 8-битовых цепочек, начинающихся на 11,
Q - множество всех 8-битовых цепочек, оканчивающихся на 0, а A -
некоторое множество произвольных 8-битовых цепочек. Сколько элементов
содержит минимальное множество А, при котором для любой 8-битовой
цепочки х истинно выражение: (указанно в функции f)
"""
a = set()
# Тут лучше сразу сгенерировать все комбинации бит
bit = [''.join(i) for i in pd('01', repeat=8)]
p = {i for i in bit if i[0] == '1' and i[1] == '1'}
q = {i for i in bit if i[-1] == '0'}


def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not A) <= ((not P) and (not Q))


for x in bit:
    if not f(x):
        a.add(x)

# print(a)
print(len(a))

# 160
