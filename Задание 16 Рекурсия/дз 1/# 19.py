from functools import *

@lru_cache(None)
def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + f(n//3)
    return n + f(n+3)

for n in range(100):
    try:
        if f(n) > 100:
            print(n)
            break
    except:
        ...
# 81
