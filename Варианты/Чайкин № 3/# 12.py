s = 128 * '1'
c1 = 128
k = 0
while '333' in s or '11' in s:
    if '333' in s:
        s = s.replace('333', '1', 1)
    else:
        s = s.replace('11', '3', 1)
        k += 2
print(k)
c2 = s.count('1')
print(128-c2)
