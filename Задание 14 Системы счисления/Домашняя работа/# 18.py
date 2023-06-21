def f(num, osn, lenght=None):
    k = 0
    while num:
        k += 1
        num //= osn
    if not lenght is None:
        return k == lenght

for n in range(1, 100):
    if f(n, 6, 2) and f(n, 5, 3) and n % 11 == 1:
        print(n)
        break

# 34


