def f(num, osn, lenght):
    k = 0
    while num:
        k += 1
        num //= osn
    return k == lenght


for n in range(1, 101):
    if f(n, 7, 2) and f(n, 6, 3) and n % 13 == 3:
        print(n)
        break

# 42
