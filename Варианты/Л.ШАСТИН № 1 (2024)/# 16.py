from functools import lru_cache

@lru_cache(None)
def g(n):
    if n < 3:
        return n
    if n > 2:
        return n - 1 + g(n-1)
for i in range(1, 4000):
    g(i)
print(g(4044))
