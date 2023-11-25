def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(500_001, 500_200):
    d = [i for i in f(x) if i % 10 == 8 and i != 8 and i != x]
    if len(d) > 0:
        print(x, d[0])
        
