def f(s1, s2, s3, c, m):
    if s1 + s2 + s3 >= 73:
        return c%2 == m%2
    if c == m:
        return 0
    h = []
    h += [f(s1+x, s2, s3, c+1, m) for x in (3, 13, 23)]
    h += [f(s1, s2+x, s3, c+1, m) for x in (3, 13, 23)]
    h += [f(s1, s2, s3+x, c+1, m) for x in (3, 13, 23)]

    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1, 24):
    for m in range(1, 5):
        if f(2, s, 2*s, 0, m):
            if m == 4: print(s)
            break
# 9
# 8 14
# 10 13
