def f(s):
    while '111' in s:
        s = s.replace('111', '33', 1)
        s = s.replace('333', '1', 1)
    return s
k = 0
for i in range(1, 36):
    s = i*'1'
    if f(s) == '131':
        k += 1
print(k)
# 5
