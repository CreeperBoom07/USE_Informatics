def f(x, y, m):
    if x**2 + y**2 >= 169:
        return m%2 == 0
    if m == 0:
        return 0
    h = [f(x+3, y, m-1), f(x, y+3, m-1), f(x, y+4, m-1)]
    return any(h) if m%2 != 0 else all(h)

for s in range(1, 13):
    if not f(s, 2, 2) and f(s, 2, 4):
        print(s)
# 7
# 6 7
# 3
