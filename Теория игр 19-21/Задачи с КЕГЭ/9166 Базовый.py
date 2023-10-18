def f(a, b, m):
    if a >= 50 or b >= 50:
        return m%2 == 0
    if m == 0:
        return 0
    h = []
    h += [f(a+3, b, m-1), f(a*2, b, m-1)]
    h += [f(a, b+3, m-1), f(a, b*2, m-1)]
    return any(h) if m%2 != 0 else all(h)

for s in range(0, 28):
    if not f(22, s, 2) and f(22, s, 4):
        print(s)
# 22
# 11 21
# 18
