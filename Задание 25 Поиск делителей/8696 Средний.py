def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(1_273_548, 1_275_000):
    m = sum(f(x))
    if p(m % 100_000):
        print(x, m)
#1273566 1637537
#1273570 1139869
#1273578 1287317
#1273582 651769
#1273590 2225609
