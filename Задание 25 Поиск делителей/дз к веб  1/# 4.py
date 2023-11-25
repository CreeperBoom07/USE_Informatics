def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(150_000, 150_200):
    d = f(x)
    if not d:
        s = 0
    else:
        s = sum(d)
    if s % 13 == 10:
        print(x, s)
