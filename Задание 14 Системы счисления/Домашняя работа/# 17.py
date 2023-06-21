def f(n):
    k = 0
    a = 68
    while a:
        k += 1
        a //= n
    return k == 4

for n in range(3, 11):
    if 68 % n == 2 and f(n):
        print(n)
        break

# 3
