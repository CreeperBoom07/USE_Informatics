def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(300_001, 300_200):
    d = [i for i in f(x) if i % 3 == 0 and i != x]
    if len(d) == 5:
        print(x, d[-1])
