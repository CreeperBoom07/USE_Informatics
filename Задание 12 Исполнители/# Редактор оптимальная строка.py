s = '2525252525252525252525252222222'
print(s.count('2'))
while '25' in s:
    s = s.replace('25', '9', 1)
print(sum(int(x) for x in s))
# 19
