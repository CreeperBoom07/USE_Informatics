def f(n):
    if n <= 5:
        return n
    if n%4 == 0: return n + f(n//2 - 1)
    return n + f(n+2)

for n in range(1, 1000):
    try:
        f(n)
    except:
        continue
    else:
        print(n)
# 12
