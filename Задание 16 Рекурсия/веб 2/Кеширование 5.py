from functools import *
from math import factorial as fc

@lru_cache(None)
def f(n):
    if n >= 100:
        return fc(n)
    if n % 2 == 0:
        return f(n+1)*f(n+2)
    return (n+2)/f(n+2) 

for i in range(100, 10,-1):
    f(i)
print(f(10)/f(38))
