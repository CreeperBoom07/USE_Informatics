def f(s, m):
    if s >= 100:
      return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s+x, m-1) for x in range(1, 6)]
    h += [f(s*2, m-1)]
    return any(h) if m%2 != 0 else all(h)

for s in range(1, 100):
    if not f(s, 2) and f(s, 4):
        print(s)
# 49
# 44 48
# 43
