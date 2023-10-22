def f(s):
    while any(x in s for x in ('23', '5333', '33333')):
        s = s.replace('23', '3', 1)
        s = s.replace('5333', '32', 1)
        s = s.replace('33333', '55', 1)
    return s

lst = []
for n in range(4, 2000):
    s = f('3'*n + '5')
    lst += [sum(int(x) for x in s)]
print(min(lst))
# 10
