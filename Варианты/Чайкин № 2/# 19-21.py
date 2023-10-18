def f(a, b, c, m):
    if (a+b)/2 >= 144:
        return c%2 == m%2
    if c == m:
        return 0
    h = []
    h += [f(a+2, b, c+1, m), f(a+6, b, c+1, m), f(a*3, b, c+1, m)]
    h += [f(a, b+2, c+1, m), f(a, b+6, c+1, m), f(a, b*3, c+1, m)]

    return any(h) if (c+1)%2 == m%2 else all(h)
for s in range(1, 106):
    for m in range(1, 5):
        if f(12, s, 0, m):
            if m == 4: print(s)
            break
# 94
# 30 84
# 2

