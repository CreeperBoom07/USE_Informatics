def f(a, b, m):
    if a >= 40 or b >= 40:
        return m%2 == 0
    if m == 0:
        return 0
    h = []
    if a > b:
        h += [f(a+x, b, m-1) for x in range(1, 4)]
        h += [f(a, b*2, m-1)]
    elif a < b:
        h += [f(a, b+x, m-1) for x in range(1, 4)]
        h += [f(a*2, b, m-1)]
    elif a == b:
        h += [f(a+x, b, m-1) for x in range(1, 4)]
        h += [f(a, b+x, m-1) for x in range(1, 4)]
    return any(h) if m%2 != 0 else all(h)


for s in range(1, 40):
    if not f(31, s, 2) and f(31, s, 4):
        print(s)

# 38
# 22 35
# 16
