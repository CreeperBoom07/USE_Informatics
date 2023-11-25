def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(250_200, 251_000):
    d = f(x)
    if not d:
        continue
    if max(d) != min(d) and (max(d)+min(d)) % 123 == 17:
        print(x, min(d)+max(d))
