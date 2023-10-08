def f(s, p, c, m):
    if s >= 20:
        return c%2 == m%2
    if c == m:
        return 0
    h = [f(s*2, p, c+1, m), f(s+2, p, c+1, m)]
    if p == 0:
        h += [f(s, 1, c+1, m)]

    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1, 20):
    for m in range(1, 20):
        if f(s, 0, 0, m):
            if m % 2 == 0: print(s, m)
            break
# 5
# 8 9
# 1 7

