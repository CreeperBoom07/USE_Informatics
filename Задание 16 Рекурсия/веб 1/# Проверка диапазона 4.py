def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n//3) - 1
    return f(n-1) + 17
k = 0
for n in range(1, 100_001):
    if f(n) == 43:
        k += 1
print(k)
# 201
