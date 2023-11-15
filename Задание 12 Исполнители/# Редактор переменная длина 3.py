def f(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('2222', '1', 1)
    return s

d = {}
for i in range(81, 1000):
    s = f('1'*i)
    if s.count('1') in d:
        pass
    else:
        d[s.count('1')] = i
print(d[min(d)])
# 83
