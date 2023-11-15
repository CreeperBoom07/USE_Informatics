from functools import *

@lru_cache(None)
def f(n):
    if n <= 2:
        return 1
    return n*f(n-2)
for i in range(5000):
    f(i)
print(f(5000)/f(4994))
# 124850040000
