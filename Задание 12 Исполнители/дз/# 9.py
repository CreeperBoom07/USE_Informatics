s = 33*'9992' + 15*'2' + '9' + 14*'1'
while '999' in s or '22' in s:
    if '999' in s:
        s = s.replace('999', '12', 1)
    else:
        s = s.replace('22', '1', 1)
print(s.count('1'))
# 87
