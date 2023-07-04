def f(s):
    while any(x in s for x in ('12', '322', '222')):
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    return s
max_sum = -1
for n in range(4, 10000):
    s = f('1' + '2'*n)
    temp_sum = sum(map(int, s))
    max_sum = max(max_sum, temp_sum)
print(max_sum)
