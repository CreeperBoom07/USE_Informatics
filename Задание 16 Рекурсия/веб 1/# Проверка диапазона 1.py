def f(n):
    if n > 25:
        return 2*n**3 + 1
    return f(n+2) + 2*f(n+3)

k = 0
for n in range(1, 1001):
    if f(n) % 11 == 0:
        k += 1
print(k)
# 91
