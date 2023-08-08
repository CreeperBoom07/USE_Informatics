def f(s):
    while any(x in s for x in ('18', '388', '888')):
        s = s.replace('18', '8', 1)
        s = s.replace('388', '81', 1)
        s = s.replace('888', '3', 1)
    return s



for n in range(4, 10000):
    s_temp = f('1' + '8'*n)
    if s_temp.count('1') == 3:
        print(n)
        
        break

