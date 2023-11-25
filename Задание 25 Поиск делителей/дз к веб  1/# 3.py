def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(154026, 154043+1):
    d = f(x)
    if len(d) == 4:
        print(d[-2], d[-1])
