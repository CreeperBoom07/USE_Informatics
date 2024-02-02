def f(s, m):
    if s == 0:
        return m%2 == 0
    if m == 0:
        return 0
    h = [f(s//3, m-1)]
    if s >= 5:
        h += [f(s-5, m-1)]
    return any(h) if m%2 != 0 else all(h)

for s in range(1, 1000):
    if not f(s, 2) and f(s, 4):
        print(s)
# 7
# 8 23
# 28

