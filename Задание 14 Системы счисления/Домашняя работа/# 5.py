def f(n):
    k = 0
    while n:
        if n % 5 == 4:
            k += 1
        n //= 5
    return k == 100


for x in range(1000):
    n = 125**200 - 5**x + 74
    if f(n):
        print(x)
        break

# 502
