def f(n):
    s = 0
    while n:
        s += n % 6
        n //= 6
    return s == 61


for x in range(1, 100):
    n = 36**17 - 6**x + 71
    if f(n):
        print(x)
        break

# 24
