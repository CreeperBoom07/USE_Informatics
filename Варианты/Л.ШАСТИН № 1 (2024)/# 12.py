def f(s):
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    return s

d = {}
for i in range(51, 10000):
    s = f(i*'5')
    if s.count('5') not in d:
        d[s.count('5')] = i
print(d[max(d)])
# 58
