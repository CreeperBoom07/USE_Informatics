def f(s):
    while any(x in s for x in ('12', '322', '222')):
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    return s
lst = []
for n in range(4, 1000):
    s = f('1' + n*'2')
    lst.append(len(s))
print(max(lst))
