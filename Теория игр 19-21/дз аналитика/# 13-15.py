def f(s, c, m):
    if s < 10:
        return c%2 == m%2
    if c == m:
        return 0

    h = [f(s - i, c + 1, m) for i in range(1, 6)]
    if s % 2 == 0:
        h += [f(s//2, c+1, m)]

    return any(h) if (c+1)%2 == m%2 else all(h)


for s in range(10, 100):
    for m in range(1, 10):
        if f(s, 0, m):
            if m == 3: print(s, m)
            break
# 15
# 17 30
# 21