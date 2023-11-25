def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**.5)+1))

def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(25317, 51237+1):
    d = [i for i in f(x) if p(i)]
    if len(d) >= 6:
        print(x, d[-1])

