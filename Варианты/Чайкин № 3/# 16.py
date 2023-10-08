from functools import lru_cache

@lru_cache(None)
def f(x):
    if x <= 2:
        return 2**x
    if x > 2 and x % 2 == 0:
        return f(x/2)
    if x > 2 and x % 2 != 0:
        return f(x+1) + f(x-4)

for i in range(0, 1000):
    f(i)

print(f(4202))
