def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(550_001, 550_101):
    d = f(x)
    if not d:
        F = 0
    else:
        F = sum(d) // len(d)
    if F%31 == 13:
        print(x, F)
