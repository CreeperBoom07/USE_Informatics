def f(s, c, m):
    if s >= 82:
        return m%2 == c%2
    if m == c:
        return 0

    h = [f(s+2, c+1, m), f(s+4, c+1, m), f(s*3, c+1, m)]
    return any(h) if m%2 != c%2 else all(h)

for s in range(1, 82):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 4: print(s)
            break
# 10
# 9 22
# 21
