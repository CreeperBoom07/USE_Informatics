def f(s):
    while any(x in s for x in ('01', '02', '03')):
        s = s.replace('01', '2302', 1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
    return s


def generator_loops():
    for i in range(1, 100):
        for j in range(1, 100):
            for o in range(1, 100):
                yield i, j, o

                
for i, j, o in generator_loops():
    s = f('0' + i*'1' + j*'2' + o*'3')
    if s.count('1') == 51 and s.count('2') == 29 and \
       s.count('3') == 23:
        print(o)
        break
# 6
