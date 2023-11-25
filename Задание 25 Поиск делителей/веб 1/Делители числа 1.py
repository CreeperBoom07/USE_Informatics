def f(x):
    d = set()
    for i in range(1, int(x**.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(193136, 193223+1):
    d = f(x)
    if len(d) == 6:
        print(x, *d, sep=' ')
