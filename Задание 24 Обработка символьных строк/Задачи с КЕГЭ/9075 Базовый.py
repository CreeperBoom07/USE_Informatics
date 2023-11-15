s = open('files/24_9075.txt').readline().strip()
for i in '0123456789':
    if int(i) % 2 == 0:
        s = s.replace(i, '0')
    else:
        s = s.replace(i, '1')
s = s.replace('01', '0 1')
s = s.replace('10', '1 0')
s = s.split()
print(max(len(x) for x in s))
# 263
