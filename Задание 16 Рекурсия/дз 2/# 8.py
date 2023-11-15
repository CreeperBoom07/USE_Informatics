from functools import *

@lru_cache(None)
def f(n):
    if n > 10_000:
        return n - 10_000
    if 1 <= n <= 10_000:
        return f(n+1) + f(n+2)
for i in range(10_000,10,-1):
    f(i)
print(f(12345) * (f(10) - f(12))/f(11) + f(10_101))
# 2446
