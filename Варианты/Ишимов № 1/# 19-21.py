def f(a, b, m):
    if a+b >= 464:
        return m%2 == 0
    if m == 0:
        return 0
    h = [f(a+2, b, m-1), f(a*3, b, m-1), f(a, b+2, m-1), f(a, b*3, m-1)]
    return any(h) if m%2 != 0 else all(h)

for s in range(1, 451):
    if not f(13, s, 2) and f(13, s, 4):
        print(s)
# 150
# 50 141
# 139
