def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(0, 10**6):
    d = [n for n in f(x) if str(n)[0]=='4']
    if len(d) == 24:
        print(x, max(d))
##997920 498960
