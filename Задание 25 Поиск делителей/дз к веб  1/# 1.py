def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
lst = []
for x in range(174457, 174505+1):
    d = f(x)
    if len(d) == 2:
        lst += [[d[0], d[1]]]
for i in sorted(lst, key=lambda x: x[0]*x[1]):
    print(*i)
