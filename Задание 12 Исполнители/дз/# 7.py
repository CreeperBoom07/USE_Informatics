def f(s):
    while any(x in s for x in ('01', '02', '03')):
        s = s.replace('01', '302', 1)
        s = s.replace('02', '3103', 1)
        s = s.replace('03', '20', 1)
    return s

def generator_loops():
    for i in range(1, 100):
        for j in range(1, 100):
            for o in range(1, 100):
                yield i, j, o
                
for i, j, o in generator_loops():
    s = f('0' + i*'1' + j*'2' + o*'3')
    if s.count('1') == 28 and s.count('2') == 34 and s.count('3') == 45:
        print(i)
        break
# 17
