def f(s, m):
    if s  == 42:
        return m%2 == 0
    if m == 0:
        return 0
    h = []
    if s > 42:
        h += [f(s-1, m-1), f(s-3, m-1), f(s-7, m-1)]
    elif s < 42:
        h += [f(s+1, m-1), f(s+3, m-1), f(s+7, m-1)]

    return any(h) if m%2 != 0 else all(h)

for s in range(1, 100):
    if f(s, 4) and not f(s, 2):
        print(s)
# 28
# 31 37
# 50
