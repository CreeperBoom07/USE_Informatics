from functools import *

@lru_cache(None)
def f(n):
    if n >= 10_000:
        return n
    if n % 3 == 0:
        return n + f(n//3)
    return 2*n + f(n+3)

for i in range(10_000, 30,-1):
    if i % 3 != 0:
        f(i)

print(f(999) - f(46))
# 1683
