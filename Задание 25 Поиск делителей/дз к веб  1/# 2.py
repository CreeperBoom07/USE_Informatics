def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(81234, 134689+1):
    d = f(x)
    if len(d) == 3:
        print(*d)
# 17 289 4913
# 19 361 6859
