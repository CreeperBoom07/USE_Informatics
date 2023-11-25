def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(550_001, 550_101):
    d = [i for i in f(x) if i % 10 == 7 and i != x]
    if len(d) == 3:
        print(x, d[-1])
