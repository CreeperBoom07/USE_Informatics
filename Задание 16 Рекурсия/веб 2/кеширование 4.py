from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return 2*f(n-1) + g(n-1) + 2*n

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    return f(n-1) + 2*g(n-1) - n

for i in range(1, 10000):
    f(i)
print(f(10_000) - g(10_000) + g(9_999) - f(9_999))
# 30000
