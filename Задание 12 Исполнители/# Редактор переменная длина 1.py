def f(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)

    return s

for i in range(51, 1000):
    s = i*'1'
    if f(s) == '22':
        print(i)
        break
# 54
