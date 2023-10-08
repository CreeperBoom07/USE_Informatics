def f(s, p1, p2, c, m):
    """p1 - ход предыдущего игрока
       p2 - наш предыдущий ход"""
    if s >= 21: return c%2 == m%2
    if c == m: return 0

    h = []
    if p2 != '+1':
        h += [f(s+1, '+1', p1, c+1, m)]
    if p2 != '+2':
        h += [f(s+2, '+2', p1, c+1, m)]
    if p2 != '*2':
        h += [f(s*2, '*2', p1, c+1, m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for s in range(1, 20):
    for m in range(1, 10):
        if f(s, '', '', 0, m):
            if m==5: print(s, m)
            break
# 8
# 6 7
# 5
