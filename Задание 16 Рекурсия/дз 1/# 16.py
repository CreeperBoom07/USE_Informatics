from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return f(n/2) + 1
    return f(n-1) + n

for n in range(0, 1000):
    try:
        if f(n) == 19:
            print(n)
            break
    except:
        ...
# 448
