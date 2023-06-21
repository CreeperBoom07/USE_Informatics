def f(n):
    c = 0
    nc = 0
    while n:
        if (n % 7) % 2 == 0:
            c += 1
        else:
            nc += 1
        n //= 7
    return c == nc


k = 0
for num in range(7**5, 7**6):
    if num % 7 >= 4 and f(num):
      k += 1
print(k)

# 12672
