def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)))

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(55_000_000, 60_000_000):
    t = x
    while t % 2 == 0: # Избавляемся от множителя 2
        t //= 2
    if int(t**0.25)**4 == t and p(int(t**0.25)):
        print(x, t\)
