s = open('files/24_9753.txt').readline().strip()
s = s.split('Y')
m = 0
for i in range(len(s)-150):
    c = 'Y'.join(s[i:i+151])
    m = max(len(c), m)
print(m)
# 244
