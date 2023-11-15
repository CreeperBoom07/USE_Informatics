from functools import lru_cache

@lru_cache(None)
def f(n):
    if n==1:
        return 1
    if n > 1 and n % 2 == 0:
        return n//2 + f(n-1)
    return n + f(n-2)

for i in range(1, 10000):
    f(i)

print(f(10000)-f(9993))
# 34991
