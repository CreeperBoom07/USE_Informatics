def f(x):
    return (x % a == 0) or ((x in range(70, 81)) <= (x % 18 != 0))


k = 0
for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        k += 1

print(k)

# 12
