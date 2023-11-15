def f(n, m):
    if m == 0:
        d = 0
    else:
        d = n+f(n,m-1)
    return d
k = 0
for n in range(1, 1000):
    for m in range(1, 100):
        if f(n, m) == 30:
            k += 1
print(k)
# 8
 
