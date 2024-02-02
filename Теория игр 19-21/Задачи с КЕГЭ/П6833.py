def f(s, m):
    if s >= 37:
        return m%2 == 0
    if m == 0:
        return 0
    h = [f(s+1, m-1), f(s+2, m-1), f(s*3, m-1)]
    return any(h) if m%2 != 0 else all(h)

for s in range(1, 37):
    if not f(s, 2) and f(s, 4):
        print(s)
# 12
# 4 10
# 9
