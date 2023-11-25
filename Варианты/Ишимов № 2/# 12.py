def f(s):
    while any(x in s for x in ['25', '355', '5555']):
        s = s.replace('25', '33', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('5555', '2', 1)
    return s
m = 0
for n in range(4, 2000):
    s = f('2' + n*'5')
    m = max(m, s.count('2'))
print(m)
# 286
