s = '3' + 100*'5' + '3'
while any(x in s for x in ('25', '355', '4555')):
    s = s.replace('25', '4', 1)
    s = s.replace('355', '2', 1)
    s = s.replace('4555', '3', 1)
print(s)
# 453
