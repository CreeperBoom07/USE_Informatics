from functools import lru_cache

from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n >= 2222:
        return n
    if n < 2222:
        return n**3 + f(n+2)


print(f(4) - f(10))
