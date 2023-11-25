def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(190201, 190260+1):
    d = [i for i in f(x) if i % 2 == 0]
    if len(d) == 4:
        print(d[-1], d[-2])
