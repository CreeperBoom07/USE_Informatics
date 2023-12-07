from functools import lru_cache

@lru_cache(None)
def f(x, y):
    if x == y:
        return 1
    if x > y or x == 100:
        return 0
    h = []
    if (x + x%10) != x:
        h += [f(x + x%10, y)]
    if (x + x%68) != x:
        h += [f(x + x%68, y)]
    if x**2 != x:
        h += [f(x**2, y)]
    return sum(h)

print(f(2, 68)*f(68, 680))
