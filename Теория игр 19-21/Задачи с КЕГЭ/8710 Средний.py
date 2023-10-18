def f(a, m):
    if a <= 1: return m%2 == 0
    if m == 0: return 0
    h = [f(a-1, m-1)]
    if a % 3 == 0:
        h += [f(a//3, m-1)] 
    if a >= 4:
        h += [f(a-4, m-1)]   
    return any(h) if m%2 != 0 else all(h)

for s in range(4, 101):
    if not f(s, 2) and f(s, 4):
        print(s)
# 6
# 7 10
# 8
