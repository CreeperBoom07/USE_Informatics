from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return 2*f(n-1)
for i in range(1, 2000):
    f(i)
print(f(1900)/2**1890)
# 1024
