def f(n):
    if n < 3:
        return n+1
    if n % 2 == 0:
        return f(n-2) + n - 2
    return f(n+2) + n + 2
k = 0
for n in range(10000):
    try:
        if 10000<= f(n) <=99999:
            k += 1
    except:
        ...
print(k)
# 216
