def dif(n, m):
    return n % m == 0

def f(x):
    B = x in range(120, 131)
    return (B <= 1-dif(x, 7)) or (a > 2*x)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000000)):
        print(a)
        break
# 253
