from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 4938:
        return n+6
    return n*f(n+5)
print(f(4928) - f(4935))
