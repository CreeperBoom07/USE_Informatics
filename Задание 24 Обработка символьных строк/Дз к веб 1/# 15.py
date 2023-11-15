s = open('files/24_1146.txt').readline().strip()

for i in 'ABCEF':
    s = s.replace(i, ' ')
s = s.split()
print(min(len(x) for x in s))
# 5
