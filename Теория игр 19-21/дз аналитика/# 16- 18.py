def f(s, c, m):
    if s == 0:
        return c%2 == m%2
    if c == m:
        return 0
    h = [f(s-i, c+1, m) for i in range(1, s//2 + 1) if s-i >= 0]

    return any(h) if (c+1)%2 == m%2 else all(h)


for s in range(100, 1000):
    for m in range(1, 10):
        if f(s, 0, m):
            if m % 2 != 0: print(s, m)
            break

