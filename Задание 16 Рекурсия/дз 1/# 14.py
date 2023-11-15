def f(n):
    if n > 30:
        return n**2 + 5*n + 4
    if n % 2 == 0:
        return f(n+1) + 3*f(n+4)
    return 2*f(n+2) + f(n+5)
k = 0
for n in range(1, 1001):
    if sum(int(i) for i in str(f(n))) == 27:
        k += 1
print(k)
# 137
