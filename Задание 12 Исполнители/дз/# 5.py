def f(s):
    while '66' in s:
        s = s.replace('66', '1', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('22', '6', 1)
    return s

m = 0
for i in range(1, 51):
    s = f(i*'6')
    if s == '21':
        m = max(m, i)
print(m)
# 48
