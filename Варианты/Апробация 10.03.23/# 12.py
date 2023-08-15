s = 104*'7'
while any(x in s for x in ('33333', '777')):
    if '33333' in s:
        s = s.replace('33333', '7', 1)
    else:
        s = s.replace('777', '3', 1)
print(s)
