from functools import *

@lru_cache(None)
def f(n):
    if int((n**0.5))**2 == n:
        return n**0.5
    return f(n+1) + 1
print(f(4850) + f(5000))
# 232
