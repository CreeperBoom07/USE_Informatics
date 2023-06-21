def f(num, osn):
    k = 0
    while num:
        k += 1
        num //= osn
    return k


s = 0
for n in range(2, 1000):
    if f(100, n) == 3:
        s += n
print(s)

# 45
