def f(x):
    d = set()
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    if x in d:
        d.remove(x)
    return sorted(d)
for x in range(81234, 134689+1):
    d = f(x)
    if len(d) == 3:
        print(x, min(d), max(d))
# 83521 17 4913
# 130321 19 6859
