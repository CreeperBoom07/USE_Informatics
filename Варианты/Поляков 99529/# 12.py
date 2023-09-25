s = 184*'5'
while any(x in s for x in ('333', '555')):
    if '555' in s:
        s = s.replace('555', '3', 1)
    else:
        s = s.replace('333', '5', 1)
print(s)
# 5335
    
