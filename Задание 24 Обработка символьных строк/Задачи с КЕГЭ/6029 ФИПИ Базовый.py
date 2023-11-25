s = open('files/24_6029.txt').readline().strip()
m = c = 1
for i in range(len(s)-1):
    if (s[i] == 'E' and s[i+1] == 'F') or (s[i] == 'F' and s[i+1] == 'E'):
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)



s = s.replace('D', ' ')
while 'EE' in s:
    s = s.replace('EE', 'E E')

while 'FF' in s:
    s = s.replace('FF', 'F F')
s = s.split()
print(max(len(x) for x in s))
# 11
