def div(n, m):
    return n % m == 0

def f(x):
    B = x in range(70, 81)
    return div(x, 12) and B and not div(x, a)


k = 0
for a in range(1, 1000):
    if all(not f(x) for x in range(1,  10000)):
        k += 1

print(k)

# 12
