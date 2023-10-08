def f(a, b, c, m):
    if a == 0 or b == 0:
        return c%2 == m%2
 

    h = []
    if a >= 3 and b >= 3:
        h += [f(a-3, b-3, c+1, m)]
    if a % 2 == 0:
        h += [f(a//2, a//2, c+1, m)]
    if b % 2 == 0:
        h += [f(b//2, b//2, c+1, m)]

    if len(h) == 0:
        return c%2 == m%2
    if c == m:
        return 0
    
    return any(h) if (c+1)%2 == m%2 else all(h)

for k in range(1, 60):
    for m in range(1, 5):
        if f(20, k, 0, m):
            if m==4: print(k, m)
            break
# 5
# 8 9 10 12 14
# 17
