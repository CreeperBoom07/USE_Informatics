from functools import reduce



def f(x):
    d = set()
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(300_000_000, 300_011_900):
    d = f(x)
    if len(d) < 5:
        p = 0
    else:
        p = reduce(lambda x, y: x*y, d[:5])

    if p % 100 == 31 and p <= x:
        print(p, d[4])
## 26222031 199
## 2481831 53
## 303831 33
## 1274931 59
## 143483131 121
