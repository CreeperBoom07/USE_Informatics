def f(a, b, m):
    if a*b >= 123:
        return m%2 == 0
    if m == 0:
        return 0
    h = []
    h += [f(a+2, b, m-1), f(a*2, b, m-1)]
    h += [f(a, b+2, m-1), f(a, b*2, m-1)]
    return any(h) if m%2 != 0 else all(h)

for s in range(1, 41):
    if not f(3, s, 1) and f(3, s, 3):
        print(s)
# 38
# 17 18
# 16
