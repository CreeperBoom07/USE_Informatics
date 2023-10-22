from functools import lru_cache

@lru_cache
def f(n):
    if n <= 6:
        return n
    if n > 6:
        return 2*n + 3 + f(n-1)

for i in range(6000):
    f(i)

print(f(6188) - f(6185))
# 37131
