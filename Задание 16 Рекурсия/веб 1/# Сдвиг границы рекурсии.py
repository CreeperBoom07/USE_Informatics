from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < -100_000:
        return 1
    if n > 10:
        return f(n-1) + 3*f(n-3) + 2
    return -f(n-1)
for i in range(-100000, 1):
    f(i)
print(f(20))
# 136 













