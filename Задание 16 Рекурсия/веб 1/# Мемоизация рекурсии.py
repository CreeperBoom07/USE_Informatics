from functools import lru_cache

def g(n):
    if n == 1:
        return 1
    return f(n-1) - 2*g(n-1)

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n-1) + 3*g(n-1)

s = str(f(50))
print(sum(int(i) for i in s))
# 103
